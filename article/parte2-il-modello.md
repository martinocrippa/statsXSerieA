# Cosa conta a metà stagione
### Parte 2 — Il modello

*Il campione d'inverno vince il 73% delle volte. Ma cosa distingue chi poi alza la coppa da chi si fa rimontare? L'abbiamo chiesto a una regressione, con prudenza.*

Nella prima parte era rimasta una domanda. Non tutti i primati di metà stagione valgono uguale: la Juventus converte quasi sempre, ogni tanto qualcuno viene rimontato. Allora qualcosa, già a gennaio, deve separare il campione d'inverno che vince da quello che no. La forza? Il margine? Proviamo a misurarlo.

## Non è una previsione

Prima un avvertimento, che è anche metodo. Le stagioni sono trentatré: pochissime. Con così pochi casi, allenare un modello a prevedere e vantarsi della sua precisione è fragile, perché il risultato cambia a ogni scelta. La domanda giusta non è "quanto prevedo bene", ma "c'è un legame, quanto è forte, quanto è incerto". Si legge il modello, non lo si fa scommettere.

## Conta solo il distacco

La regressione dà una risposta pulita: l'unica cosa che sposta davvero le probabilità è il distacco sul secondo a metà stagione. Ogni punto di margine in più aumenta di circa la metà le probabilità di chiudere primo. Non è un effetto enorme, con 33 stagioni niente lo è, ma è il solo segnale che regge.

> **Come si legge — l'odds ratio.** "Aumenta di circa la metà" vuol dire odds ratio 1,5: ogni punto di margine moltiplica per 1,5 le quote di vincere. Le quote, non la probabilità diretta.

E si vede a occhio. Chi all'andata ha un margine corto, due punti o meno, vince poi il 62% delle volte. Chi ne ha da tre a cinque, il 69%. Chi chiude con almeno sei punti, in trentatré anni ha sempre vinto: sette su sette. Un primo assaggio di quella "soglia" di cui parleremo.

![Conversione per ampiezza del distacco a fine andata][g-modello]

## Quello che non conta

La parte più istruttiva è ciò che non funziona. Abbiamo provato la forza assoluta, i punti per partita: niente, i campioni d'inverno sono tutti forti e si somigliano troppo. Abbiamo separato attacco e difesa, gol fatti e gol subiti: segnale quasi nullo. Abbiamo misurato quanto fosse affollata la corsa dietro al primo: ma quello è solo il distacco, visto da un altro lato.

| Cosa abbiamo provato | Aggiunge segnale? |
|---|---|
| Distacco sul secondo | Sì, l'unico |
| Differenza reti | Quasi nulla |
| Punti per partita | No |
| Attacco e difesa separati | No |
| Rivali vicini | È il distacco, da un altro lato |

Il messaggio è chiaro: conta di quanto sei primo, non quanto sei forte né come giochi.

![Cosa distingue chi converte: solo il distacco sul secondo si stacca da zero][g-regressori]

> **Come si legge — la differenza standardizzata.** Misura quanto chi converte e chi si fa rimontare differiscono su una caratteristica, in deviazioni standard. Zero vuol dire nessuna differenza; più la barra è lontana da zero, più quella caratteristica separa i due gruppi.

Nel grafico si vede subito: di tutte le caratteristiche del campione d'inverno, solo il distacco si stacca da zero. Attacco, difesa, forza, differenza reti restano indistinguibili dal caso. E con appena nove squadre rimontate, le bande di incertezza sono larghe.

Una cosa, però, prima di seppellire la difesa. Un conto è chiedersi chi converte tra i primi d'inverno, un altro chi diventa campione. E lì la difesa pesa: in trentatré stagioni il campione d'Italia ha avuto la miglior difesa nel 73% dei casi, il miglior attacco solo nel 39%[^calc]. "La difesa vince i campionati" nei numeri c'è. Ma la difesa serve a costruire il vantaggio; a dire se un vantaggio già costruito regge, no. Quello dipende da quanto è grande.

## La prova: l'Inter 2025/26

Una prova, per gioco e per onestà. Quest'anno il campione d'inverno è stato l'Inter, con tre punti di margine. Abbiamo addestrato il modello su tutte le altre stagioni, tenendo fuori questa, e gli abbiamo chiesto: che probabilità dai all'Inter? Ha risposto circa il 70%. L'Inter ha poi vinto.

> **Come si legge — la prova "out-of-sample".** Il modello impara senza la stagione da giudicare, poi prova a indovinarla. Così non bara: non ha già visto la risposta.

Modello promosso? Calma. Quel 70% è quasi uguale al tasso storico: con un margine piccolo, il modello dice solo "di solito sì". Non ci ha azzeccato per bravura, ma perché la base di partenza è alta. E un 70% lascia comunque tre possibilità su dieci che vada storto. Una stagione sola non promuove e non boccia nessuno.

## Le domande aperte

Eravamo partiti da una provocazione tra colleghi, e finiamo con più domande di prima. Quelle che restano:

- vale solo per la Serie A, o per tutto il calcio? Servirebbe guardare gli altri campionati, senza mescolarli: ognuno è un caso a sé.
- esiste una soglia oltre cui il titolo è quasi certo? Un margine, o un monte-punti, dopo cui non si torna indietro.
- la difesa fa il campione più dell'attacco (73% contro 39%): è sempre stato così, in tutte le epoche? E con dati più ricchi, come tiri, possesso ed expected goals, cos'altro conta?
- le neopromosse dalla Serie B partono forte e si spengono? Una curva di rendimento per blocchi di giornate lo direbbe.
- il pronostico salta per coppe, mercato di gennaio, infortuni: Immobile, da dentro, insiste sul peso del doppio impegno[^imm]. Si possono provare come variabili?
- e se invece di "vince o non vince" guardassimo di quanto si vince?

Ci sono poi i passi tecnici, che il piccolo numero di stagioni richiede: una stima bayesiana con il suo intervallo, intervalli da bootstrap, una logistica adatta ai campioni piccoli (Firth), un modello che tratti ogni squadra per sé. E soprattutto più dati: le stagioni prima del 1993, che non esistono già pronte e andrebbero ricostruite.

C'è anche un modo più onesto di leggere il legame. Il campione d'inverno non vince perché è campione d'inverno. Lo diventa perché ha già mostrato, in mezza stagione, le qualità che servono per vincere: continuità, solidità, una rosa profonda. Il primato di gennaio non è una causa, è una spia. Per questo gli allenatori lo ridimensionano ("non conta niente, conta arrivare a maggio in testa", ha tagliato corto Chivu da campione d'inverno in carica[^chivu]), mentre i numeri un po' contano. Le due cose non si escludono: il titolo non garantisce niente, ma chi se lo prende, di solito, è la squadra giusta.

Resta il punto di partenza, che il modello conferma. Il campione d'inverno parte nettamente favorito, e a gennaio fa la differenza quanto è chiaramente in testa. Trentatré stagioni sono poche per chiamarla legge: è una tendenza forte. E quel 27% di primi traditi dalla primavera è la parte più bella, la prova che una rimonta è sempre possibile.

---

## Nota metodologica

- **Campione d'inverno**: primo quando ogni squadra ha completato l'andata (partite giocate ≥ n−1). Verificato contro le fonti nelle ultime 10 stagioni. Resta una piccola imprecisione sui punti assoluti del primo, per i rinvii, non sul distacco.
- **Test**: proporzione storica con intervallo di Wilson; tavola di contingenza su tutte le coppie squadra-stagione con test esatto di Fisher, più adatto del chi-quadro quando le frequenze attese sono basse.
- **Modello**: regressione logistica letta sui parametri, non sull'accuratezza. Regressori del campione d'inverno a fine andata. Valutazione Leave-One-Out e prova out-of-sample sull'Inter 2025/26. Con 33 stagioni si leggono direzioni e ordini di grandezza, non certezze.

Regressori provati:

| Regressore | pseudo-R² | p-value |
|---|---|---|
| distacco sul secondo | 0,14 | 0,07 |
| + differenza reti | — | 0,71 |
| punti per partita | 0,02 | 0,40 |
| gol fatti + subiti per partita | 0,00 | ≈ 0,9 |
| rivali entro 5 punti | 0,10 | 0,07 (legato al distacco) |

I numeri vengono dal notebook del progetto, dove ci sono codice, tabelle e test.

[^calc]: Numeri nostri su 33 stagioni (1993/94–2025/26), dati football-data.co.uk; calcolati nel notebook del progetto.
[^chivu]: [Sportal](https://www.sportal.it/calcio/serie-a/inter-lecce-cristian-chivu-il-titolo-d-inverno-non-conta-eusebio-di-francesco-si-tiene-la-prestazione.html) — Chivu: «il titolo d'inverno non conta».
[^imm]: [FCInter1908](https://www.fcinter1908.it/news/interviste/immobile-intervista-scudetto-inter-inzaghi/) — Immobile sul peso del doppio impegno e delle tante partite.

[g-modello]: ../docs/modello.png
[g-regressori]: ../docs/regressori.png
