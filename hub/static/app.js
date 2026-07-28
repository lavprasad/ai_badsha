/* AI Badsha hub client — static files + in-browser Python (Pyodide) */
(() => {
  const STORAGE_KEY = "ai_badsha_progress_v1";
  const LAST_KEY = "ai_badsha_last_day";
  const LANG_KEY = "ai_badsha_lang";
  const PYODIDE_URL = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js";

  /** Base path for project Pages (e.g. /ai_badsha/) or ./ for local static. */
  function detectBase() {
    const scripts = document.getElementsByTagName("script");
    for (const s of scripts) {
      const src = s.getAttribute("src") || "";
      if (src.includes("app.js")) {
        const abs = new URL(src, location.href);
        // .../hub/static/app.js -> repo root is two levels up
        if (abs.pathname.includes("/hub/static/")) {
          return abs.href.replace(/hub\/static\/app\.js.*$/, "");
        }
        // served as /app.js from local hub server
        return abs.href.replace(/app\.js.*$/, "");
      }
    }
    const p = location.pathname;
    if (p.endsWith("/")) return location.origin + p;
    if (p.endsWith("index.html")) return location.origin + p.slice(0, -10);
    return location.origin + p.replace(/\/[^/]*$/, "/");
  }

  const BASE = detectBase();
  const state = {
    days: [],
    current: null,
    dayData: null,
    answersShown: false,
    help: {},
    searchDocs: null,
    pyodide: null,
    pyodideLoading: null,
    lang: localStorage.getItem(LANG_KEY) === "hi" ? "hi" : "en",
  };

  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => [...document.querySelectorAll(sel)];

  function joinUrl(...parts) {
    return parts
      .map((p, i) => {
        if (i === 0) return p.replace(/\/+$/, "");
        return String(p).replace(/^\/+/, "");
      })
      .filter((p, i) => p || i === 0)
      .join("/");
  }

  function loadProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
    } catch {
      return {};
    }
  }

  function saveProgress(p) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(p));
  }

  function markDone(n) {
    const p = loadProgress();
    p[n] = true;
    saveProgress(p);
    localStorage.setItem(LAST_KEY, String(n));
    renderDayList($("#dayFilter").value);
  }

  function lastDay() {
    const v = Number(localStorage.getItem(LAST_KEY) || "1");
    return Number.isFinite(v) && v > 0 ? v : 1;
  }

  function mdToHtml(src) {
    if (!src) return "<p><em>No content.</em></p>";
    const lines = src.replace(/\r\n/g, "\n").split("\n");
    const out = [];
    let inCode = false;
    let codeLang = "";
    let codeBuf = [];
    let inUl = false;
    let inOl = false;
    let inTable = false;
    let tableBuf = [];

    const closeLists = () => {
      if (inUl) {
        out.push("</ul>");
        inUl = false;
      }
      if (inOl) {
        out.push("</ol>");
        inOl = false;
      }
    };
    const flushTable = () => {
      if (!inTable) return;
      const rows = tableBuf.filter((r) => !/^\s*\|?\s*-+/.test(r));
      out.push("<table>");
      rows.forEach((row, i) => {
        const cells = row
          .replace(/^\|/, "")
          .replace(/\|$/, "")
          .split("|")
          .map((c) => c.trim());
        const tag = i === 0 ? "th" : "td";
        out.push(
          "<tr>" +
            cells.map((c) => `<${tag}>${inline(c)}</${tag}>`).join("") +
            "</tr>"
        );
      });
      out.push("</table>");
      tableBuf = [];
      inTable = false;
    };

    const inline = (t) =>
      escapeHtml(t)
        .replace(/`([^`]+)`/g, "<code>$1</code>")
        .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
        .replace(/\*([^*]+)\*/g, "<em>$1</em>");

    for (const line of lines) {
      const fence = line.match(/^```(\w*)/);
      if (fence) {
        if (!inCode) {
          closeLists();
          flushTable();
          inCode = true;
          codeLang = fence[1] || "";
          codeBuf = [];
        } else {
          out.push(
            `<pre><code class="lang-${codeLang}">${escapeHtml(
              codeBuf.join("\n")
            )}</code></pre>`
          );
          inCode = false;
        }
        continue;
      }
      if (inCode) {
        codeBuf.push(line);
        continue;
      }
      if (line.trim().startsWith("|")) {
        closeLists();
        inTable = true;
        tableBuf.push(line);
        continue;
      } else {
        flushTable();
      }

      if (/^\s*[-*]\s+/.test(line)) {
        if (inOl) {
          out.push("</ol>");
          inOl = false;
        }
        if (!inUl) {
          out.push("<ul>");
          inUl = true;
        }
        out.push(`<li>${inline(line.replace(/^\s*[-*]\s+/, ""))}</li>`);
        continue;
      }
      if (/^\s*\d+\.\s+/.test(line)) {
        if (inUl) {
          out.push("</ul>");
          inUl = false;
        }
        if (!inOl) {
          out.push("<ol>");
          inOl = true;
        }
        out.push(`<li>${inline(line.replace(/^\s*\d+\.\s+/, ""))}</li>`);
        continue;
      }
      closeLists();

      if (!line.trim()) {
        out.push("");
        continue;
      }
      if (line.startsWith("### ")) out.push(`<h3>${inline(line.slice(4))}</h3>`);
      else if (line.startsWith("## ")) out.push(`<h2>${inline(line.slice(3))}</h2>`);
      else if (line.startsWith("# ")) out.push(`<h1>${inline(line.slice(2))}</h1>`);
      else if (line.startsWith("> "))
        out.push(`<blockquote><p>${inline(line.slice(2))}</p></blockquote>`);
      else if (/^---+$/.test(line.trim())) out.push("<hr />");
      else out.push(`<p>${inline(line)}</p>`);
    }
    closeLists();
    flushTable();
    if (inCode) {
      out.push(`<pre><code>${escapeHtml(codeBuf.join("\n"))}</code></pre>`);
    }
    return out.join("\n");
  }

  function escapeHtml(s) {
    return s
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  async function fetchText(url) {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status} for ${url}`);
    return res.text();
  }

  async function fetchJson(url) {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status} for ${url}`);
    return res.json();
  }

  function dayFolder(n) {
    return `Day${String(n).padStart(2, "0")}`;
  }

  async function loadDayStatic(n) {
    const id = dayFolder(n);
    const meta = state.days.find((d) => d.n === n) || { theme: id, examples: [] };
    // Hinglish mirror lives in hinglish/DayNN/*.md; fall back to English if absent.
    const doc = (file) =>
      state.lang === "hi"
        ? fetchText(joinUrl(BASE, "hinglish", id, file)).catch(() =>
            fetchText(joinUrl(BASE, id, file)).catch(() => "")
          )
        : fetchText(joinUrl(BASE, id, file)).catch(() => "");
    const [notes, questions, answers, project] = await Promise.all([
      doc("notes.md"),
      doc("questions.md"),
      doc("answers.md"),
      meta.project ? doc("project.md") : Promise.resolve(""),
    ]);
    const examples = [];
    for (const name of meta.examples || []) {
      try {
        const source = await fetchText(joinUrl(BASE, id, "examples", name));
        examples.push({ name, source });
      } catch {
        /* skip missing */
      }
    }
    return {
      n,
      id,
      theme: meta.theme,
      notes: project ? notes + "\n\n---\n\n" + project : notes,
      questions,
      answers,
      examples,
    };
  }

  function searchStatic(q) {
    const terms = q
      .trim()
      .toLowerCase()
      .split(/\s+/)
      .filter(Boolean);
    if (!terms.length || !state.searchDocs) return [];
    const hits = [];
    for (const doc of state.searchDocs) {
      const low = doc.text.toLowerCase();
      if (!terms.every((t) => low.includes(t))) continue;
      const idx = low.indexOf(terms[0]);
      const start = Math.max(0, idx - 60);
      const end = Math.min(doc.text.length, idx + 140);
      let snippet = doc.text.slice(start, end).replace(/\n/g, " ");
      if (start > 0) snippet = "…" + snippet;
      if (end < doc.text.length) snippet += "…";
      hits.push({
        day: doc.day,
        file: doc.file,
        theme: doc.theme,
        snippet,
      });
      if (hits.length >= 40) break;
    }
    return hits;
  }

  function helpStatic(topic) {
    const t = topic.trim().toLowerCase();
    const glossary = state.help || {};
    if (!t) {
      return {
        title: "Help topics",
        body:
          "Try: " +
          Object.keys(glossary).join(", ") +
          ". The Run button executes Python in your browser (Pyodide) — numpy, pandas, scikit-learn and matplotlib load on demand.",
        matches: Object.keys(glossary),
      };
    }
    if (glossary[t]) {
      return { title: glossary[t].title, body: glossary[t].body, matches: [t] };
    }
    const matches = Object.keys(glossary).filter(
      (k) => t.includes(k) || glossary[k].title.toLowerCase().includes(t)
    );
    if (matches.length === 1) {
      const item = glossary[matches[0]];
      return { title: item.title, body: item.body, matches };
    }
    if (matches.length) {
      return {
        title: "Several topics matched",
        body: "Pick one: " + matches.join(", "),
        matches,
      };
    }
    return {
      title: `No glossary entry for '${topic}'`,
      body: "Use Search for course notes, or try: pointer, move, raii, virtual, ub.",
      matches: [],
      search_hits: searchStatic(t),
    };
  }

  /** Load Pyodide once, lazily — it is ~10MB, so never on page load. */
  function loadPyodide(onProgress) {
    if (state.pyodide) return Promise.resolve(state.pyodide);
    if (state.pyodideLoading) return state.pyodideLoading;

    state.pyodideLoading = (async () => {
      onProgress("Loading Python runtime (first run only, ~10MB)…");
      await new Promise((resolve, reject) => {
        const s = document.createElement("script");
        s.src = PYODIDE_URL;
        s.onload = resolve;
        s.onerror = () => reject(new Error("Could not load Pyodide from the CDN."));
        document.head.appendChild(s);
      });
      const py = await window.loadPyodide();
      onProgress("Loading numpy and pandas…");
      await py.loadPackage(["numpy", "pandas"]);
      state.pyodide = py;
      return py;
    })();
    return state.pyodideLoading;
  }

  /** Packages Pyodide can fetch on demand, keyed by the import name in the source. */
  const PY_PACKAGES = {
    numpy: "numpy",
    pandas: "pandas",
    sklearn: "scikit-learn",
    matplotlib: "matplotlib",
    scipy: "scipy",
  };

  async function runPython(source, onProgress) {
    const py = await loadPyodide(onProgress);

    const needed = Object.keys(PY_PACKAGES).filter((mod) =>
      new RegExp(`(^|\\n)\\s*(import|from)\\s+${mod}\\b`).test(source)
    );
    if (needed.length) {
      onProgress(`Loading ${needed.join(", ")}…`);
      try {
        await py.loadPackage(needed.map((m) => PY_PACKAGES[m]));
      } catch (e) {
        /* fall through — the import error below will be clearer */
      }
    }

    py.runPython(`
import sys, io
_stdout, _stderr = io.StringIO(), io.StringIO()
sys.stdout, sys.stderr = _stdout, _stderr
`);
    let ok = true;
    let error = "";
    try {
      await py.runPythonAsync(source);
    } catch (e) {
      ok = false;
      error = String(e.message || e);
    }
    const stdout = py.runPython("_stdout.getvalue()");
    const stderr = py.runPython("_stderr.getvalue()");
    py.runPython("sys.stdout, sys.stderr = sys.__stdout__, sys.__stderr__");

    return { ok, stdout, stderr: [stderr, error].filter(Boolean).join("\n"), exit_code: ok ? 0 : 1 };
  }

  function showWorkspace(show) {
    $("#hero").hidden = show;
    $("#workspace").hidden = !show;
  }

  function setTab(name) {
    $$(".tab").forEach((t) => t.classList.toggle("active", t.dataset.tab === name));
    $$(".tab-panel").forEach((p) =>
      p.classList.toggle("active", p.dataset.panel === name)
    );
  }

  function renderDayList(filter = "") {
    const progress = loadProgress();
    const q = filter.trim().toLowerCase();
    const nav = $("#dayList");
    nav.innerHTML = "";
    state.days
      .filter(
        (d) =>
          !q ||
          String(d.n).includes(q) ||
          d.theme.toLowerCase().includes(q)
      )
      .forEach((d) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "day-btn";
        if (state.current === d.n) btn.classList.add("active");
        if (progress[d.n]) btn.classList.add("done");
        btn.innerHTML = `<span class="n">Day ${String(d.n).padStart(
          2,
          "0"
        )}</span><span class="t">${escapeHtml(d.theme)}</span>`;
        btn.addEventListener("click", () => openDay(d.n));
        nav.appendChild(btn);
      });
  }

  async function openDay(n) {
    showWorkspace(true);
    state.current = n;
    state.answersShown = false;
    localStorage.setItem(LAST_KEY, String(n));
    $("#answersView").classList.remove("show");
    $("#btnReveal").textContent = "Reveal answers";
    renderDayList($("#dayFilter").value);
    $("#dayKicker").textContent = `Day ${String(n).padStart(2, "0")}`;
    $("#dayTitle").textContent = "Loading…";
    $("#notesView").innerHTML = "<p>Loading notes…</p>";

    const data = await loadDayStatic(n);
    state.dayData = data;
    $("#dayTitle").textContent = data.theme;
    $("#notesView").innerHTML = mdToHtml(data.notes);
    $("#questionsView").innerHTML = mdToHtml(data.questions);
    $("#answersView").innerHTML = mdToHtml(data.answers);

    const sel = $("#exampleSelect");
    sel.innerHTML = "";
    (data.examples || []).forEach((ex, i) => {
      const opt = document.createElement("option");
      opt.value = String(i);
      opt.textContent = ex.name;
      sel.appendChild(opt);
    });
    if (data.examples && data.examples.length) {
      $("#editor").value = data.examples[0].source;
    } else {
      $("#editor").value = `print("Day ${n}")\n`;
    }
    setTab("learn");
  }

  async function runCode() {
    const out = $("#output");
    out.classList.remove("err");
    const progress = (msg) => {
      out.textContent = msg;
    };
    progress("Running…");
    $("#btnRun").disabled = true;
    try {
      const result = await runPython($("#editor").value, progress);
      const parts = [];
      if (result.stderr) parts.push(result.stderr.trimEnd());
      if (result.stdout) parts.push(result.stdout.trimEnd());
      if (!parts.length) parts.push(`(no output) exit=${result.exit_code}`);
      else parts.push(`\n[exit ${result.exit_code}]`);
      out.textContent = parts.join("\n");
      if (!result.ok) out.classList.add("err");
    } catch (e) {
      out.textContent = String(e);
      out.classList.add("err");
    } finally {
      $("#btnRun").disabled = false;
    }
  }

  async function doSearch(q) {
    setTab("help");
    showWorkspace(true);
    const hits = searchStatic(q);
    const box = $("#searchResults");
    if (!hits.length) {
      box.innerHTML = `<p class="help-card">No hits for “${escapeHtml(q)}”.</p>`;
      return;
    }
    box.innerHTML = hits
      .map(
        (h) =>
          `<button type="button" class="hit" data-day="${h.day}"><strong>Day ${String(
            h.day
          ).padStart(2, "0")} — ${escapeHtml(h.theme)}</strong><span>${escapeHtml(
            h.file
          )} · ${escapeHtml(h.snippet)}</span></button>`
      )
      .join("");
    box.querySelectorAll(".hit").forEach((el) => {
      el.addEventListener("click", () => openDay(Number(el.dataset.day)));
    });
  }

  async function doHelp(topic) {
    setTab("help");
    showWorkspace(true);
    const data = helpStatic(topic);
    $("#helpCard").innerHTML = `<h3>${escapeHtml(data.title)}</h3><p>${escapeHtml(
      data.body
    )}</p>`;
    if (data.search_hits && data.search_hits.length) {
      $("#searchResults").innerHTML = data.search_hits
        .map(
          (h) =>
            `<button type="button" class="hit" data-day="${h.day}"><strong>Day ${
              h.day
            } — ${escapeHtml(h.theme)}</strong><span>${escapeHtml(
              h.snippet
            )}</span></button>`
        )
        .join("");
      $("#searchResults").querySelectorAll(".hit").forEach((el) => {
        el.addEventListener("click", () => openDay(Number(el.dataset.day)));
      });
    }
  }

  function setLang(lang) {
    state.lang = lang;
    localStorage.setItem(LANG_KEY, lang);
    $("#btnLang").textContent = lang === "hi" ? "हिं Hinglish" : "EN English";
    if (state.current) openDay(state.current);
  }

  function wire() {
    $("#btnLang").addEventListener("click", () =>
      setLang(state.lang === "hi" ? "en" : "hi")
    );
    $("#btnLang").textContent =
      state.lang === "hi" ? "हिं Hinglish" : "EN English";
    $("#brandHome").addEventListener("click", (e) => {
      e.preventDefault();
      showWorkspace(false);
    });
    $("#btnStart").addEventListener("click", () => openDay(1));
    $("#btnContinue").addEventListener("click", () => openDay(lastDay()));
    $("#btnHelpHero").addEventListener("click", () => doHelp(""));
    $("#dayFilter").addEventListener("input", (e) => renderDayList(e.target.value));
    $("#btnPrev").addEventListener("click", () => {
      if (state.current > 1) openDay(state.current - 1);
    });
    $("#btnNext").addEventListener("click", () => {
      const max = state.days.length ? state.days[state.days.length - 1].n : 1;
      if (state.current < max) openDay(state.current + 1);
    });
    $("#btnDone").addEventListener("click", () => {
      if (state.current) markDone(state.current);
    });
    $$(".tab").forEach((t) =>
      t.addEventListener("click", () => setTab(t.dataset.tab))
    );
    $("#exampleSelect").addEventListener("change", (e) => {
      const i = Number(e.target.value);
      if (state.dayData && state.dayData.examples[i]) {
        $("#editor").value = state.dayData.examples[i].source;
      }
    });
    $("#btnRun").addEventListener("click", runCode);
    $("#btnReveal").addEventListener("click", () => {
      state.answersShown = !state.answersShown;
      $("#answersView").classList.toggle("show", state.answersShown);
      $("#btnReveal").textContent = state.answersShown
        ? "Hide answers"
        : "Reveal answers";
    });
    $("#searchForm").addEventListener("submit", (e) => {
      e.preventDefault();
      doSearch($("#searchInput").value);
    });
    $("#helpForm").addEventListener("submit", (e) => {
      e.preventDefault();
      doHelp($("#helpInput").value);
    });
    $$("[data-help]").forEach((b) =>
      b.addEventListener("click", () => doHelp(b.dataset.help))
    );
  }

  async function fetchJsonFirst(urls) {
    let lastErr;
    for (const url of urls) {
      try {
        return await fetchJson(url);
      } catch (e) {
        lastErr = e;
      }
    }
    throw lastErr || new Error("fetch failed");
  }

  async function bootStatic() {
    const catalog = await fetchJsonFirst([
      joinUrl(BASE, "hub/data/catalog.json"),
      joinUrl(BASE, "data/catalog.json"),
    ]);
    state.days = catalog.days || [];
    try {
      state.help = await fetchJsonFirst([
        joinUrl(BASE, "hub/data/help.json"),
        joinUrl(BASE, "data/help.json"),
      ]);
    } catch {
      state.help = {};
    }
    try {
      const idx = await fetchJsonFirst([
        joinUrl(BASE, "hub/data/search_index.json"),
        joinUrl(BASE, "data/search_index.json"),
      ]);
      state.searchDocs = idx.docs || [];
    } catch {
      state.searchDocs = [];
    }
    const status = $("#gppStatus");
    status.textContent = `${state.days.length} days · python in browser`;
    status.classList.add("ok");
    renderDayList();
  }

  async function boot() {
    wire();
    try {
      await bootStatic();
    } catch (e) {
      $("#gppStatus").textContent = "hub error";
      $("#gppStatus").classList.add("bad");
      console.error(e);
      $("#hero .lede").textContent =
        "Could not load the course catalog. On GitHub Pages, ensure hub/data/catalog.json is published.";
    }
  }

  boot();
})();
