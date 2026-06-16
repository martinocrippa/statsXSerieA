# statsXSerieA

> *"Hai tempo? Qual è la probabilità che una squadra di Serie A sia
> campione d'Italia, dato che è campione d'inverno?"*

Da una provocazione tra colleghi: uno senior, con un po' di strada da data
scientist alle spalle, lancia la domanda a uno più giovane che quella strada la
sta appena imboccando. Da una domanda nascono domande.

## La domanda

Il campione d'inverno è la squadra prima in classifica a fine girone di andata.
Quante di queste vincono poi lo scudetto? Sulle stagioni di Serie A dal 1993/94
al 2024/25 succede circa il 72% delle volte (23 su 32).

## Dati e perimetro

- Fonte: football-data.co.uk (codice `I1` = Serie A), risultati con date e gol.
- Copertura: 1993/94 → 2024/25, **32 stagioni**: è tutto ciò che la fonte offre.
- **Pochi dati.** 32 osservazioni sono poche, soprattutto per un modello
  predittivo. Per andarci oltre servono le stagioni storiche (pre-1993), che non
  esistono in CSV pronto e vanno recuperate da:
  - Wikipedia, pagine per stagione (risultati e classifiche dal 1929/30) — scraping;
  - RSSSF (rsssf.org), archivio storico in formato testuale.
- Non mescolare altri campionati per "fare numero": la Serie A è un caso a sé.
  Se proprio, usare dummy di lega o interazioni tra variabili.

## Occhio metodologico-statistico

Con n=32 il framing predittivo (train/test, accuracy/ROC) è fragile: il test set
è minuscolo e la metrica balla a ogni split. A questo numero la domanda è
**descrittiva/inferenziale** (c'è associazione? quanto forte? quanto incerta?),
non predittiva. Meglio uno sguardo statistico: la logistica letta sui parametri,
o tecniche più adatte al piccolo n.

## Next steps (indicazioni)

1. **Logistica in ottica statistica, con statsmodels.** Leggere l'output:
   coefficienti, errori standard, p-value, odds ratio (`exp` del coefficiente),
   pseudo-R². Si possono includere anche le feature già calcolate ma non usate
   (`WinRate`, `AvgGoalScored`, `AvgGoalConceded`) per mostrare con i p-value che
   **non sono significative** — tenendo presente che a n=32 troppi regressori
   rendono instabili le stime (~10 eventi per variabile → al massimo un paio).
   Meglio pochi regressori, normalizzati per giornata (18 vs 20 squadre = 17 vs
   19 partite all'inverno).

2. **Altre tecniche**, dalla più semplice da applicare alla più impegnativa:
   1. tavola di contingenza + test esatto di Fisher;
   2. Beta-Binomiale bayesiana (coniugata, forma chiusa): proporzione + intervallo di credibilità;
   3. bootstrap per gli intervalli (proporzione e coefficienti);
   4. logistica penalizzata (Firth), pensata per campioni piccoli;
   5. modello gerarchico bayesiano per squadra (la conversione varia molto tra squadre).

3. **Più dati.** Recuperare le stagioni storiche (Wikipedia / RSSSF, vedi sopra).

4. **Codice.**
   - via gli `iterrows` e i cicli espliciti: vettorializzare con pandas;
   - DRY: classifica e parser data (`parseDateSafe`) definiti in due punti → uno solo;
   - KISS: `colonneDaMappare` è una mappa identità → basta una lista;
   - PEP8: snake_case, niente `except:` nudo, niente `;`, import inutili, residui `[cite: 1]`;
   - percorsi relativi (non assoluti); le 2 stagioni non parsabili ripulite una volta sola;
   - `random_state` fissato negli split per riproducibilità;
   - verificare che il "campione d'inverno" (`min(partite) ≥ n−1`) coincida con
     la classifica ufficiale a fine andata: le partite rinviate possono spostarlo.

5. **Esplorativa** — rispondere a queste domande descrittive:
   - quante stagioni si osservano? quante squadre?
   - quante squadre sono state almeno una volta campione d'inverno e poi campione?
   - conteggi aggregati per squadra: scudetto dato campione d'inverno;
   - chi è stato campione d'Italia **senza** essere campione d'inverno?

## Chi ha fatto cosa

| | Contributo |
|---|---|
| Analisi originale | dati, calcolo della probabilità storica, modello |
| Review (`mc`) | README, dati e perimetro, note metodologico-statistiche, next steps |
