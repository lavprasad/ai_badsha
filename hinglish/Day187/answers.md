# Day 187 — Jawab

Ye tab padho jab aap apne jawab likh chuke ho.

---

### A1. Kya galat hoga

**Harms taxonomy for your product** — classic failure ye hai:

> Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Ye isliye aam hai kyunki code phir bhi chalta rehta hai. Kuch crash nahi hota; bas numbers
chupchap wo matlab dena band kar dete hain jo aap samajh rahe the.

---

### A2. Output predict karo

**Fairness definitions and their conflicts** wali file `examples/03_fairness_definitions_and_their_conflicts.py` hai.
Use chalao aur apne likhe hue se milao.

Baat number ki nahi hai. Baat ye hai ki code ke baare me aapka mental model machine
ke asli behaviour se milta hai ya nahi. Jahan wo alag hain, wahan aapka model galat hai —
guess nahi, model theek karo.

Khud ko jis idea par jaanchna hai: Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

---

### A3. Ye rule kyun

Rule: Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

Ye isliye hai kyunki theek uske neeche wali failure hai: Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Is course ke saare rules ek hi shakl ke hain — har ek kisi asli bug ka nishaan hai.
Bug samajh lo aur rule arbitrary ke bajaye obvious lagne lagega.

---

### A4. Design faisla

**Contestability and appeals** ek line me: Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain.

Ise tab use karo jab iski assumptions sach hon aur cost jaayaz ho. Jab na hon to kuch
simple uthao — jo baseline aap samajhte ho wo us fancy method se behtar hai jise aap raat
2 baje debug nahi kar sakte. Sahi jawab *assumption* ka naam leta hai, tool ka nahi.

Dhyaan rakho: Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

---

### A5. Debug karo

**Saying no to a bad use case** ke liye is kram me check karo:

1. **Data.** Shapes, dtypes, null counts, value ranges. Zyadatar 'model bugs' data bugs hote hain.
2. **Split.** Train/test split se pehle nikaali gayi koi bhi cheez leak kar sakti hai — result accha dikhega aur galat hoga.
3. **Is concept ka khaas jaal:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

In teeno ke baad hi algorithm par shak karo.

---

### Build task

Iska koi ek sahi jawab nahi hai. Achhe submission me:

- saaf interpreter par bina error chalta hai,
- dono concepts kisi aisi wajah se use hote hain jo aap ek line me bata sako,
- kuch aisa print hota hai jo logic tootne par badal jaaye,
- aur koi line aisi nahi jise aap samjha na sako.
