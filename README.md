# statsXSerieA

> *"Festa in ufficio per il nuovo campione d'inverno della serie A, ma qual è la probabilità che una squadra di Serie A sia
> campione d'Italia, dato che è campione d'inverno?"*

Da una provocazione tra colleghi: uno senior, con un po' di strada da data
scientist alle spalle, la lancia a uno più giovane che quella strada la sta
appena imboccando. Da una domanda nascono domande.

In concreto:
1. qual è la probabilità che il campione d'inverno (primo a fine girone di andata) vinca lo scudetto?
2. e l'Inter 2025/26, da campione d'inverno, che probabilità aveva?

## Dati e perimetro

- Fonte: football-data.co.uk (codice `I1` = Serie A), risultati con date e gol.
- Copertura: 1993/94 → 2025/26, **33 stagioni** — è quanto offre la fonte.
- **Pochi dati.** 33 osservazioni sono poche, soprattutto per un modello
  predittivo. Per andare oltre servono le stagioni storiche (pre-1993), che non
  esistono in CSV pronto: andrebbero recuperate via scraping da Wikipedia
  (pagine per stagione dal 1929/30) o dall'archivio RSSSF (rsssf.org).
- Non mescolare altri campionati per "fare numero": la Serie A è un caso a sé.
  Se mai, con dummy di lega o interazioni tra variabili.

## Il risultato

Sulle 33 stagioni il campione d'inverno vince poi lo scudetto **24 volte su 33,
circa il 73%** (intervallo di Wilson 95%: 0.56–0.85).

![Risultati](docs/risultati.png)

La media però nasconde molto:
- per squadra la conversione va da Juventus 12/13 (92%) a Fiorentina 0/1, con Inter 86%, Milan 60%, Napoli 50%, Roma 33%;
- 9 volte lo scudetto è andato a chi non era campione d'inverno (Juventus 4, Milan 3, Inter 1, Lazio 1);
- confronto netto: P(scudetto | campione d'inverno) = 72.7% contro P(scudetto | non) = 1.5% (Fisher esatto, p ≈ 6e-29);
- nella logistica letta sui parametri, a metà stagione conta il distacco sul secondo (odds ×1.5 per punto), non la differenza reti.

L'Inter 2025/26 (campione d'inverno) ha poi vinto: un modello addestrato sulle
altre 32 stagioni le dava ~70% — dalla parte giusta, ma quasi pari al tasso
storico (con un distacco piccolo il modello tende verso la media).

33 stagioni restano poche: è una tendenza forte, non una legge. Dettagli, tavole e test nel notebook.

## Com'è fatto

Dati e analisi sono separati. I dati passano per un piccolo magazzino in stile **medallion** (raw -> bronze -> silver); il notebook fa solo l'analisi e legge l'ultimo strato.

```
                football-data.co.uk
                        |
                        v   ingestion.py
            +------------------------+
            |  data/raw/             |   CSV grezzi, come scaricati
            +------------------------+
                        |
                        v   bronze.py      (schema fatto rispettare)
            +------------------------+
            |  data/bronze/          |   CSV validi e leggibili
            +------------------------+
                        |
                        v   silver.py      (solo colonne utili)
            +------------------------+
            |  data/silver/          |   l'input dell'analisi
            +------------------------+
                        |
                        v
            analisi/probScudetto...ipynb   (le due domande)
```

- **raw**: quello che arriva da football-data.co.uk, intatto.
- **bronze**: stessi dati resi leggibili. Alcune stagioni (2003/04, 2004/05) hanno un numero variabile di colonne vuote in coda e pandas non le parsa. Qui si tiene solo lo schema dichiarato dall'intestazione e si scartano le colonne vuote. Una volta sola, non a ogni lettura.
- **silver**: solo le colonne che servono all'analisi (Date, HomeTeam, AwayTeam, FTHG, FTAG), una stagione per file.

## Struttura

```
statsXSerieA/
├── pipeline/        gli script dati
│   ├── config.py
│   ├── ingestion.py
│   ├── bronze.py
│   ├── silver.py
│   └── run_pipeline.py
├── data/
│   ├── raw/
│   ├── bronze/
│   └── silver/
├── analisi/
│   └── probScudettoSeCampioneInverno.ipynb
├── environment.yml
├── requirements.txt
└── README.md
```

## Ambiente

Con conda:

```
conda env create -f environment.yml
conda activate statsxseriea
```

Oppure con pip:

```
pip install -r requirements.txt
```

## Come si usa

I dati sono già nel repo, quindi puoi aprire direttamente il notebook e fare Run All:

```
jupyter notebook analisi/probScudettoSeCampioneInverno.ipynb
```

Per rigenerare o aggiornare il magazzino dati (scarica e prepara tutto):

```
python -m pipeline.run_pipeline
```

## Occhio metodologico-statistico

Con n=33 il framing predittivo (train/test, accuracy/ROC) è fragile: il test set
è minuscolo e la metrica balla a ogni split. A questo numero la domanda è
**descrittiva/inferenziale** (c'è associazione? quanto forte? quanto incerta?),
non predittiva. Meglio leggere la logistica sui parametri (coefficienti, p-value,
odds ratio), o usare tecniche più adatte al piccolo n — vedi i next step.

## Next steps (discussi, non ancora sviluppati)

- **Altre tecniche** — oltre alla contingenza + Fisher e all'IC di Wilson già presenti:
  - Beta-Binomiale bayesiana (proporzione + intervallo di credibilità);
  - bootstrap per gli intervalli (proporzione e coefficienti);
  - logistica penalizzata (Firth), pensata per campioni piccoli;
  - modello gerarchico per squadra (la conversione varia molto tra squadre).
- **Più dati** — stagioni storiche pre-1993 via scraping (Wikipedia / RSSSF).
- **Verifica del dato** — controllare che il campione d'inverno (`min partite ≥ n−1`)
  coincida con la classifica ufficiale a fine andata: le partite rinviate possono spostarlo.

## Cosa è cambiato rispetto all'originale

- Dati e analisi separati: pipeline negli script, analisi nel notebook.
- Introdotto il magazzino medallion (raw/bronze/silver).
- La pulizia delle stagioni "rotte" non è più un cerotto a ogni lettura: si fa una volta, in bronze, facendo rispettare lo schema.
- Tolti i percorsi assoluti: tutto relativo al repo.
- Analisi ampliata: parte esplorativa, tavola di contingenza (con test) e lettura statistica della logistica (statsmodels).
- Codice rivisto: classifica vettorializzata (niente `iterrows`), niente duplicazioni, snake_case/PEP8, `random_state` fissato. Risultati invariati.
- Aggiunti README, requirements.txt, environment.yml.

## Crediti

- Dati: football-data.co.uk
- Idea e analisi originale: il collega (questo repo è un fork).
