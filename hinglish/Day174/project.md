# Day 174 PROJECT — production RAG assistant

Project bada exercise nahi hota. Ye wo hissa hai jahan koi aapko jawab ki shakl nahi batata.
Pehle sabse patla end-to-end version banao, phir use mota karo.

## Milestones

1. **Goal: grounded answers over your own documents**
2. **Ingestion and chunking pipeline**
3. **Embedding and index construction**
4. **Hybrid retrieval with reranking**
5. **Grounded generation with citations**
6. **Abstention when retrieval is weak**
7. **Evaluation set and scoring harness**
8. **Cost and latency measurement**
9. **Prompt injection hardening**
10. **Deploying it behind an API**

## Kab kaha jaayega ki ho gaya

- [ ] Saaf checkout par ek hi command se end to end chalta hai.
- [ ] README hai jisme problem, metric aur result likha hai.
- [ ] Ek batayi gayi baseline ko haraata hai — aur baseline ka number likha hua hai.
- [ ] Har random source seeded hai; dobara chalane par wahi number aata hai.
- [ ] Kam se kam ek test jo core logic tootne par fail ho.
- [ ] Limitations section jo imaandaari se batata hai ki ye kya nahi kar sakta.

## Aam jaal se kaise bacho

Aam jaal ye hai ki pehla hafta infrastructure me chala jaata hai aur chauthe hafte pata
chalta hai ki data se sawaal ka jawab mil hi nahi sakta. Ise ulta karo: pehle din sabse
bewakoof version end to end chalao — hard-coded paths, ek file, ghatiya accuracy. Wahi
version batata hai ki project mumkin bhi hai ya nahi. Uske baad ka sab sudhaar hai, aur
sudhaar schedule karna aasan hai.

## Stretch goals

- Ise HTTP endpoint ke peeche serve karo.
- Ek monitoring script jodo jo ise chupchap kharab hote hue pakad le.
- Ise aisi post ki tarah likho jise aapki team ke bahar ka koi follow kar sake.
