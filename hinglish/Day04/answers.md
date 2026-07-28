# Day 04 — Jawab

Ye tab padho jab aap apne jawab likh chuke ho.

---

### A1. Kya galat hoga

**Reading and writing text files** — classic failure ye hai:

> Badi file par `fh.read().split('\n')`, jo sab RAM me laa kar mar jaata hai.

Ye isliye aam hai kyunki code phir bhi chalta rehta hai. Kuch crash nahi hota; bas numbers
chupchap wo matlab dena band kar dete hain jo aap samajh rahe the.

---

### A2. Output predict karo

**CSV files with the csv module** wali file `examples/03_csv_files_with_the_csv_module.py` hai.
Use chalao aur apne likhe hue se milao.

Baat number ki nahi hai. Baat ye hai ki code ke baare me aapka mental model machine
ke asli behaviour se milta hai ya nahi. Jahan wo alag hain, wahan aapka model galat hai —
guess nahi, model theek karo.

Khud ko jis idea par jaanchna hai: Merge se pehle aur baad me `df.shape` zaroor check karo — chupke se rows badhna matlab duplicate keys.

---

### A3. Ye rule kyun

Rule: Slashes wali string joduai ke bajaye `Path` division (`root / 'data' / 'x.csv'`) use karo.

Ye isliye hai kyunki theek uske neeche wali failure hai: API key commit karna, phir baad ke commit me 'hata dena' jabki wo history me abhi bhi zinda hai.

Is course ke saare rules ek hi shakl ke hain — har ek kisi asli bug ka nishaan hai.
Bug samajh lo aur rule arbitrary ke bajaye obvious lagne lagega.

---

### A4. Design faisla

**Working with large files line by line** ek line me: `with open(...)` file band kar deta hai chahe body me exception aa jaaye — context manager isi ke liye hai.

Ise tab use karo jab iski assumptions sach hon aur cost jaayaz ho. Jab na hon to kuch
simple uthao — jo baseline aap samajhte ho wo us fancy method se behtar hai jise aap raat
2 baje debug nahi kar sakte. Sahi jawab *assumption* ka naam leta hai, tool ka nahi.

Dhyaan rakho: Badi file par `fh.read().split('\n')`, jo sab RAM me laa kar mar jaata hai.

---

### A5. Debug karo

**A tiny dataset downloader script** ke liye is kram me check karo:

1. **Data.** Shapes, dtypes, null counts, value ranges. Zyadatar 'model bugs' data bugs hote hain.
2. **Split.** Train/test split se pehle nikaali gayi koi bhi cheez leak kar sakti hai — result accha dikhega aur galat hoga.
3. **Is concept ka khaas jaal:** API key commit karna, phir baad ke commit me 'hata dena' jabki wo history me abhi bhi zinda hai.

In teeno ke baad hi algorithm par shak karo.

---

### Build task

Iska koi ek sahi jawab nahi hai. Achhe submission me:

- saaf interpreter par bina error chalta hai,
- dono concepts kisi aisi wajah se use hote hain jo aap ek line me bata sako,
- kuch aisa print hota hai jo logic tootne par badal jaaye,
- aur koi line aisi nahi jise aap samjha na sako.
