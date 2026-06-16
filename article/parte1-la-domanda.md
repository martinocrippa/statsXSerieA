# Campione d'inverno, poi campione d'Italia?
### Parte 1 — La domanda

*In 33 stagioni di Serie A il campione d'inverno ha poi vinto lo scudetto quasi tre volte su quattro. Quanto conta davvero quel primato di metà stagione?*

In Serie A c'è un titolo che non esiste: il campione d'inverno, la squadra prima in classifica a fine girone di andata. Non si alza al cielo e non vale un punto, ma ogni gennaio i giornali lo assegnano lo stesso. La domanda, sotto, è semplice: conta qualcosa?

È nata da una provocazione tra colleghi. Uno con un po' di strada da data scientist alle spalle la gira a uno più giovane: «Qual è la probabilità che una squadra vinca lo scudetto, sapendo che è campione d'inverno?». Sembra una domanda da bar, ed è invece un buon punto di partenza: da lì ne nascono altre.

L'ipotesi da verificare è quella popolare: campione d'inverno uguale campione d'Italia. Vediamo se i numeri le danno ragione.

> **Come lo definiamo — il campione d'inverno.** È il primo in classifica quando tutte le squadre hanno completato il girone di andata (in pratica: partite giocate ≥ n−1). Coincide con le fonti ufficiali nelle ultime 10 stagioni.

## La risposta

Dal 1993/94 a oggi, 33 stagioni: il campione d'inverno ha poi vinto lo scudetto 24 volte, il 73%[^calc] (con così pochi anni l'intervallo di confidenza va dal 56 all'85%). Da solo il numero dice poco, serve un confronto. Chi a metà stagione non è primo vince lo scudetto nell'1,5% dei casi; chi è primo, nel 73%. Essere in testa al giro di boa cambia tutto.

> **Come si legge — l'intervallo.** Con pochi dati una percentuale è incerta. L'intervallo di Wilson dà la forbice entro cui sta il valore vero, con il 95% di confidenza: più stagioni, forbice più stretta. Qui è ampia (56–85%) proprio perché 33 stagioni sono poche.

![Campione d'inverno e scudetto][g-risultati]

## Dietro la media

Il 73% è una media, e spacchettata per squadra racconta storie diverse. La Juventus è stata campione d'inverno tredici volte e ha poi vinto dodici scudetti: il 92%. L'Inter converte sei volte su sette, il Milan tre su cinque, il Napoli una su due, la Roma una su tre. La Fiorentina, l'unica volta che ha guidato a metà strada, ha chiuso a mani vuote.

Poi ci sono le rimonte: nove volte in 33 anni lo scudetto è andato a chi a metà stagione inseguiva. Quattro portano la firma della Juventus, tre del Milan, una a testa di Inter e Lazio. E dal lato opposto, a farsi rimontare almeno una volta sono finite tutte e sei le squadre arrivate prime all'inverno, con Roma, Milan e Napoli due volte ciascuna. Il vantaggio dell'inverno è reale, ma non basta da solo.

## L'epoca conta

Un taglio cambia parecchio la storia: il numero di squadre. Nell'era a diciotto squadre, fino al 2003/04, il campione d'inverno ha poi vinto solo il 55% delle volte, sei su undici. Nell'era a venti, dal 2004/05, si sale all'82%, diciotto su ventidue. Con così pochi casi gli intervalli sono larghi e in parte si sovrappongono (dal 28 al 79% la prima era, dal 61 al 93% la seconda): la differenza è chiara come tendenza, incerta come numero.

![Conversione per era][g-era]

Su tutta la storia della Serie A, 93 campionati a girone unico, la media è del 67,7%[^lega]; le testate, guardando solo gli ultimi anni, parlano di circa il 79%[^sm], in linea col nostro 82%. Il primato d'inverno non è una costante: pesa molto di più nella Serie A moderna. A seconda di quali anni si guardano, la risposta cambia.

Si vede bene seguendo la stima mentre si accumulano le stagioni. All'inizio degli anni Novanta il campione d'inverno vinceva sempre, e la percentuale partiva dal 100%, ma su pochissimi casi e con un'incertezza enorme. La lunga era a diciotto squadre l'ha fatta scendere fino al 55% dei primi anni Duemila; con l'era moderna è risalita e si è assestata intorno al 73%, mentre la banda d'incertezza si stringeva.

![Come si assesta la stima, stagione dopo stagione, con la banda d'incertezza di Wilson][g-cumulata]

## Quanti punti servono

Un campione d'inverno chiude l'andata con 44 punti, e qui media e mediana coincidono (43,8 e 44): i primati d'inverno si somigliano tutti. A fine stagione il campione d'Italia arriva in media a 83 punti, mediana 84. Allegri, in conferenza, fissa di solito la quota-scudetto un po' più in alto, sugli 86-88 punti[^cds]: per vincere serve qualcosa in più della media, e nell'era a venti squadre i totali si sono alzati.

C'è un terzo numero, che racconta il girone di ritorno: dall'inverno al traguardo il futuro campione aggiunge in media una quarantina di punti, più o meno quanti ne aveva al giro di boa. Il campionato si vince due volte, prima e dopo l'inverno. A metà strada il primo viaggia a 2,34 punti a partita, contro i 2,26 con cui in media si chiude da campioni: la testa all'inverno è il meglio del primo tempo, poi qualcuno rallenta.

![Quota di stagioni per intervallo di 5 punti: campione d'inverno, campione d'Italia, e punti aggiunti dopo l'inverno][g-distribuzioni]

> **Come si legge — l'istogramma.** Ogni barra è la quota di stagioni in cui il campione ha chiuso in quell'intervallo di 5 punti. Cinque punti perché con 33 stagioni intervalli più stretti avrebbero uno o zero casi ciascuno: troppo rumore.

Gli indici di dispersione (in appendice) confermano l'impressione: distribuzioni quasi simmetriche e poco disperse, con un coefficiente di variazione attorno al 12%. Sono però piatte: la curtosi negativa dice che non c'è un valore tipico, i punti si spalmano su una fascia ampia. Fa eccezione il delta del ritorno, un po' sbilanciato verso l'alto: ogni tanto un campione, dopo l'inverno, accelera.

## La domanda che resta

Torniamo all'ipotesi di partenza, campione d'inverno uguale campione d'Italia. I dati le danno ragione a metà: come tendenza è forte, quasi tre volte su quattro e quattro su cinque negli ultimi vent'anni; come uguaglianza no. La Juventus converte nel 92% dei casi, la Roma in una su tre, e nove volte in 33 anni il pronostico è saltato. Non tutti i primati di metà stagione valgono uguale.

Allora la domanda si sposta: cosa distingue, già a gennaio, il campione d'inverno che vince da quello che verrà raggiunto? La forza? L'ampiezza del vantaggio? Il modo in cui ci è arrivato? Per rispondere non basta contare, serve un modello. È la seconda parte.

---

*Dati: football-data.co.uk (Serie A, 1993/94–2025/26).*

## Appendice — gli indici di dispersione

| Distribuzione | media | mediana | dev. std | CV | asimmetria | curtosi |
|---|---|---|---|---|---|---|
| Punti del campione d'inverno | 43,8 | 44 | 5,8 | 13% | -0,22 | -1,02 |
| Punti del campione d'Italia | 83,1 | 84 | 9,1 | 11% | -0,16 | -0,70 |
| Punti aggiunti dopo l'inverno | 40,1 | 40 | 4,8 | 12% | +0,64 | -0,05 |

Curtosi in eccesso (0 = normale). Con 33 stagioni, asimmetria e curtosi vanno prese con le pinze.

[^calc]: Numeri nostri su 33 stagioni (1993/94–2025/26), dati football-data.co.uk: percentuali, intervalli e distribuzioni vengono dal notebook del progetto, dove ci sono codice e test.
[^lega]: [Lega Serie A](https://www.legaseriea.it/serie-a/news/inter-col-lecce-per-diventare-campione-d-inverno) — il campione d'inverno nella storia (63 su 93, 67,7%).
[^sm]: [SportMediaset](https://www.sportmediaset.mediaset.it/calcio/inter/inter-campione-inverno-statistica-scudetto_107743377-202602k.shtml) — la statistica scudetto nell'era recente (~79%).
[^cds]: [Corriere dello Sport](https://www.corrieredellosport.it/news/calcio/serie-a/milan/2026/01/07-145696785/il_calcolo_preciso_di_allegri_su_scudetto_e_champions_ecco_quanti_punti_servono) — Allegri sulla quota-punti da scudetto (86-88).

[g-risultati]: ../docs/risultati.png
[g-era]: ../docs/era.png
[g-cumulata]: ../docs/cumulata.png
[g-distribuzioni]: ../docs/distribuzioni.png
