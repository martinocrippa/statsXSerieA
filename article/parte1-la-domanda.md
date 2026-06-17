# Campione d'inverno, poi campione d'Italia?
### Parte 1 — La domanda

*In 33 stagioni di Serie A il campione d'inverno ha poi vinto lo scudetto quasi tre volte su quattro. Quanto conta davvero quel primato di metà stagione?*

In Serie A c'è un titolo che non esiste: il campione d'inverno, la squadra prima in classifica a fine girone di andata. Non si alza al cielo e non vale un punto, ma ogni gennaio i giornali lo assegnano lo stesso. La domanda, sotto, è semplice: conta qualcosa?

Il collega alle spalle provoca con il titolo del giornale e spera. È nata una curiosità tra colleghi. Uno con un po' di strada da data scientist alle spalle e uno più giovane: «Qual è la probabilità che una squadra vinca lo scudetto, sapendo che è campione d'inverno? è matematico come si dice? è sempre stato così?». Sembra una domanda da bar, ed è invece un buon punto di partenza: da lì ne nascono altre.

L'ipotesi di base da verificare è quella popolare: campione d'inverno uguale campione d'Italia. Vediamo se i numeri le danno ragione.

> **Come definiamo — il campione d'inverno.** È il primo in classifica quando tutte le squadre hanno completato il girone di andata[^def], a meno di eccezioni. Coincide con le fonti ufficiali nelle ultime 10 stagioni.

## La risposta

Dal 1993/94 a oggi[^dati], 33 stagioni, il campione d'inverno ha poi vinto lo scudetto 24 volte su 33: il 73%. Tra le squadre prime a metà stagione poco meno di tre su quattro hanno poi chiuso davanti a tutte. Quindi è molto probabile che da primi in inverno si finisce primi a fine stagione.

Da solo il numero dice poco, serve un ulteriore confronto per capire meglio la potenzialità di chi non è campione d'inverno e il fine stagione. Chi a metà stagione non è primo vince lo scudetto nell’1,5% dei casi.

L'1,5% riguarda tutte le altre: ogni anno c'è una sola capolista e dietro una folla di inseguitrici, e in 33 stagioni le rimonte sono state appena nove. Una squadra presa a caso tra chi non era in testa vince lo scudetto circa una volta e mezza su cento. Essere primi al giro di boa non garantisce nulla, ma sposta le probabilità da un mondo all'altro.

Immaginiamo di fermare il campionato a metà. Da una parte mettiamo la squadra prima in classifica. Dall’altra mettiamo tutte le altre.

In sintesi osservando la fotografia compete delle ultime stagioni: la squadra che era prima a metà stagione ha poi vinto lo scudetto quasi tre volte su quattro. Le altre, prese una per una, lo hanno vinto molto raramente.

Il senso è questo: essere campione d’inverno non significa aver già vinto, ma significa partire da una posizione molto più forte. Non è una certezza. È un vantaggio.

Restano due cose da dire. Con così poche stagioni il 73% è una stima incerta e media. Una media, e una media tiene insieme storie molto diverse. Sfruttando uno strumento in più possiamo calcolare un intervallo. La probabilità di vincere il campionato da primo in classifica a Natale sta in una forbice tra il 56% e l'85%. Cosa nascondono questi valori, allora? Perchè 56% è vicino alla probabilità che esca testa e croce lanciando una moneta. Il passato quindi ha un andamento da approfondire perchè intervallo 56% a 85% nasconde che in passato non era scontato vincere il campionato da capolista invernale.[^tab]

> **Come si legge — l'intervallo.** Il 73% è quello che è successo finora, non una legge fissa. Con sole 33 stagioni il conto è ballerino: basterebbero un paio di rimonte in più o in meno per spostarlo parecchio. L'intervallo è il modo onesto di dirlo: invece di un numero secco, dà una forbice — qui dal 56 all'85% — dentro cui, con ragionevole sicurezza (il 95%), sta il valore "vero", quello che vedremmo con tantissime stagioni. È un po' come stimare l'altezza media di una città intervistando poche persone: dici «tra tot e tot», non un numero al millimetro. Più dati si accumulano, più la forbice si stringe; con così pochi anni resta larga. La forbice si calcola con il metodo di Wilson, adatto quando i casi sono pochi.
>
> E c'è un secondo motivo, diverso dall'incertezza: la variabilità. Anche avendo mille stagioni, quel 73% non sarebbe un numero buono per tutti. Cambia da squadra a squadra — la Juventus non è il Napoli — e da epoca a epoca. Una cosa è non essere sicuri della media perché i dati sono pochi; un'altra è che dietro la media ci sono situazioni davvero diverse, e una percentuale sola le appiattisce. È quello che andiamo a spacchettare nei prossimi capitoli.

![Campione d'inverno e scudetto][g-risultati]

## Dietro la media

Prima ancora di spacchettare, un dato dà la misura: in 33 stagioni sono passate per la Serie A 53 squadre diverse, ma a guidare a metà strada sono state solo sei, e a vincere lo scudetto sempre sei. Il giro di chi conta, davanti, è strettissimo.

Il 73% è una media, e spacchettata per squadra racconta storie diverse. La Juventus è stata campione d'inverno tredici volte e ha poi vinto dodici scudetti: il 92%. L'Inter converte sei volte su sette, il Milan tre su cinque, il Napoli una su due, la Roma una su tre. La Fiorentina, l'unica volta che ha guidato a metà strada, ha chiuso a mani vuote.

Poi ci sono le rimonte: nove volte in 33 anni lo scudetto è andato a chi a metà stagione inseguiva. Quattro portano la firma della Juventus, tre del Milan, una a testa di Inter e Lazio.

E dal lato dei delusi: a farsi rimontare almeno una volta sono finite tutte e sei le squadre arrivate prime all'inverno. La Fiorentina è l'unica mai riuscita a convertire, ma su un solo tentativo; Roma, Milan e Napoli hanno fallito due volte ciascuna. Il Napoli ha guidato a metà strada nel 2015/16 e nel 2017/18 e in entrambi i casi ha visto la Juventus passargli davanti; persino chi di solito non sbaglia ha steccato, la Juventus una volta (1999/00, scudetto alla Lazio) e l'Inter una (2021/22, rimontata dal Milan). Il vantaggio dell'inverno è reale, ma non basta da solo[^squadre].

## L'epoca conta

Negli anni come è cambiata la probabilità di vincere il campionato da capolista invernale? 

![Campione d'inverno e campione d'Italia, stagione per stagione; in rosso le stagioni in cui chi guidava all'inverno è stato poi rimontato][g-timeline]

Un momento storico del campionato di serie A cambia parecchio la storia: il numero di squadre. Dal 2004/05 la Serie A è passata da diciotto a venti squadre[^riforma], e quel taglio separa due ere — un cambio nato per ragioni istituzionali, non per equilibrare il campionato.

Nell'era a diciotto squadre, fino al 2003/04, il campione d'inverno ha poi vinto solo il 55% delle volte, sei su undici. Nell'era a venti, dal 2004/05, si sale all'82%, diciotto su ventidue. Con così pochi casi gli intervalli sono larghi e in parte si sovrappongono (dal 28 al 79% la prima era, dal 61 al 93% la seconda): la differenza è chiara come tendenza, incerta come numero.

![Conversione per era][g-era]

Su tutta la storia della Serie A, 93 campionati a girone unico, la media è del 67,7%[^lega]; le testate, guardando solo gli ultimi anni, parlano di circa il 79%[^sm], in linea col nostro 82%. Il primato d'inverno non è una costante: pesa molto di più nella Serie A moderna. A seconda di quali anni si guardano, la risposta cambia.

Si vede bene seguendo la stima mentre si accumulano le stagioni. All'inizio degli anni Novanta il campione d'inverno vinceva sempre, e la percentuale partiva dal 100%, ma su pochissimi casi e con un'incertezza enorme. La lunga era a diciotto squadre l'ha fatta scendere fino al 55% dei primi anni Duemila; con l'era moderna è risalita e si è assestata intorno al 73%, mentre la banda d'incertezza si stringeva.

![Come si assesta la stima, stagione dopo stagione, con la banda d'incertezza di Wilson][g-cumulata]

Quale fenomeno spiega un campionato moderno più orientata a una squadra dominante, intesa come campione invernale con alta probabilità di vincere la serie a, mentre periodi precedenti dove la predominanza sembra fosse più debole? possiamo misurare impatto tramite i punti della competitività del campionato e divario tra campione invernale e inseguitori?

> **Una nota — Calciopoli e i dati.** I nostri campioni nascono dai risultati sul campo, non dai verdetti della giustizia sportiva. Due scudetti della Juventus furono revocati: il 2004/05 (non riassegnato) e il 2005/06 (assegnato all'Inter). Nei nostri dati restano alla Juventus, che in entrambe le stagioni era anche campione d'inverno. Con i titoli ufficiali il 2005/06 diventerebbe una rimonta e il 2004/05 uscirebbe dal conteggio: la conversione dell'era moderna calerebbe di qualche punto, ma il divario con l'era a diciotto squadre resterebbe.

## Quanti punti servono come campione d'inverno e d'italia

Un campione d'inverno chiude l'andata con 44 punti, e qui media e mediana coincidono (43,8 e 44): i primati d'inverno si somigliano tutti. A fine stagione il campione d'Italia arriva in media a 83 punti, mediana 84. Allegri, in conferenza, fissa di solito la quota-scudetto un po' più in alto, sugli 86-88 punti[^cds]: per vincere serve qualcosa in più della media, e nell'era a venti squadre i totali si sono alzati.

C'è un terzo numero, che racconta il girone di ritorno: dall'inverno al traguardo il futuro campione aggiunge in media una quarantina di punti, più o meno quanti ne aveva al giro di boa. Il campionato si vince due volte, prima e dopo l'inverno. A metà strada il primo viaggia a 2,34 punti a partita, contro i 2,26 con cui in media si chiude da campioni: la testa all'inverno è il meglio del primo tempo, poi qualcuno rallenta.

![Quota di stagioni per intervallo di 5 punti: campione d'inverno, campione d'Italia, e punti aggiunti dopo l'inverno][g-distribuzioni]

> **Come si legge — l'istogramma.** Ogni barra è la quota di stagioni in cui il campione ha chiuso in quell'intervallo di 5 punti. Cinque punti perché con 33 stagioni intervalli più stretti avrebbero uno o zero casi ciascuno: troppo rumore.

I conti più tecnici (in appendice) dicono la stessa cosa con altre parole. I totali in gioco sono i tre di prima: i punti del campione d'inverno a metà stagione (in media 44), quelli del campione d'Italia a fine anno (83) e quelli aggiunti nel girone di ritorno (40). Nessuno dei tre balla molto: le stagioni restano quasi tutte vicine alla media, senza annate fuori scala da una parte o dall'altra.

Quello che manca è un valore «tipico» che torni più spesso degli altri. Prendiamo i punti del campione d'Italia: non è che l'83 si ripeta di continuo e gli altri risultati siano rari. Le stagioni si spalmano in modo abbastanza uniforme su una fascia larga una quindicina di punti, più o meno dai 75 ai 90 — un anno il campione chiude a 78, un altro a 91, un altro ancora a 84, senza che una cifra precisa domini sulle altre. È come tirare un dado invece di lanciare tante monete: i risultati non si ammucchiano al centro, si distribuiscono piatti su tutta la fascia.

L'unica eccezione sono i punti del ritorno: di solito una quarantina, ma ogni tanto un campione accelera e ne aggiunge parecchi di più, e quei pochi casi allungano la distribuzione verso l'alto.

Ciò non basta ed è necessario indagare il distacco tra prima-seconda e compattezza degli inseguitori.

## La forma della classifica al giro di boa

Perché nell'era moderna il primato d'inverno pesa di più? L'ipotesi è che a cambiare non sia chi guida, ma come è fatta la classifica intorno a lui: un tempo il gruppo di testa era folto e ravvicinato, oggi la capolista tende a isolarsi.

Indagheremo quanto la capolista è distante da chi insegue, e quanto sono compatti gli inseguitori tra loro. Guardiamo le mediane, separate per le due ere.

| a metà stagione (mediane) | conversione | distacco sulla 2ª | distacco sulla 4ª | gruppo dalla 2ª alla 5ª | squadre entro 10 pt |
|---|---|---|---|---|---|
| era a 18 squadre (≤ 2003/04) | 55% | 3,0 | 6,0 | 5,0 | 6 |
| era a 20 squadre (2004/05+) | 82% | 3,5 | 11,5 | 9,0 | 3 |

![La forma della classifica al giro di boa, mediane per era: il distacco sulla seconda resta quasi uguale tra le due ere, mentre l'isolamento dal gruppo di testa cresce e le squadre in corsa calano][g-forma]

Il distacco sulla seconda non spiega niente: è quasi lo stesso nelle due ere, tre punti allora come oggi. Sul suo rivale diretto, il campione d'inverno moderno non ha più margine di una volta.

A cambiare è l'isolamento dal resto del gruppo di testa. Il distacco sulla quarta è raddoppiato, da sei a undici punti e mezzo, e le squadre racchiuse entro dieci punti dalla capolista si sono dimezzate, da sei a tre. Anche gli inseguitori si sfilacciano: il blocco dalla seconda alla quinta, che un tempo stava in cinque punti, oggi ne occupa nove. Dietro la testa, insomma, c'è meno gente e più distanziata.

In una frase: nella Serie A moderna il campione d'inverno converte di più non perché stacca la seconda, ma perché capita molto più spesso che si stacchi dal grosso del gruppo di testa. A gennaio non è uno tra tanti con un piccolo margine: è solo, davanti, con il vuoto alle spalle.

## La domanda che resta

Torniamo all'ipotesi di partenza, campione d'inverno uguale campione d'Italia. I dati le danno ragione a metà: come tendenza è forte, quasi tre volte su quattro e quattro su cinque negli ultimi vent'anni; come uguaglianza no. La Juventus converte nel 92% dei casi, la Roma in una su tre, e nove volte in 33 anni il pronostico è saltato. Non tutti i primati di metà stagione valgono uguale.

Qualche indizio l'abbiamo già raccolto: più del distacco sulla seconda, a separare un primato solido da uno fragile sembra contare l'isolamento dal grosso del gruppo di testa. Ma «sembra» non basta. Allora la domanda si sposta: cosa distingue davvero, già a gennaio, il campione d'inverno che vince da quello che verrà raggiunto — la forza, l'ampiezza del vantaggio, il modo in cui ci è arrivato — e quanto pesa ciascuna cosa?

Per rispondere non basta contare, serve un modello. È la seconda parte.

Da ultimo cosa permette a una squadra di dominare così tanto? in questo caso è necessario indagare e mettere a paragone dati di gioco, valore della squadra, etc..

---

## Appendice — la tavola di contingenza

Le frequenze su cui poggia tutta la prima parte, contando le coppie squadra-stagione (638 in tutto: 33 campioni d'inverno, uno per stagione, e 605 no):

| | scudetto | no scudetto |
|---|---|---|
| campione d'inverno | 24 | 9 |
| non campione d'inverno | 9 | 596 |

Lette per riga, come P(esito | riga):

| | scudetto | no scudetto |
|---|---|---|
| campione d'inverno | 72,7% | 27,3% |
| non campione d'inverno | 1,5% | 98,5% |

- P(scudetto | campione d'inverno) = 0,727, IC95% Wilson [0,56–0,85]
- P(scudetto | non campione d'inverno) = 0,015
- Fisher esatto: odds ratio = 176,6, p ≈ 6·10⁻²⁹
- Chi-quadro: 309,4 (1 grado di libertà), p ≈ 3·10⁻⁶⁹
- Frequenza attesa minima = 1,7: sotto 5, quindi il test affidabile è quello esatto di Fisher.

## Appendice — squadra per squadra

In 33 stagioni si sono viste 53 squadre diverse, ma solo sei hanno guidato all'inverno e solo sei hanno vinto lo scudetto. Quante volte chi era primo a metà stagione ha poi convertito:

| squadra | da campione d'inverno | poi campione | fallite | quota |
|---|---|---|---|---|
| Juventus | 13 | 12 | 1 | 92% |
| Inter | 7 | 6 | 1 | 86% |
| Milan | 5 | 3 | 2 | 60% |
| Napoli | 4 | 2 | 2 | 50% |
| Roma | 3 | 1 | 2 | 33% |
| Fiorentina | 1 | 0 | 1 | 0% |

La colonna "fallite" somma a nove, le nove rimonte qui sotto. La Fiorentina è l'unica mai riuscita a convertire il primato d'inverno; tutte le altre ce l'hanno fatta almeno una volta.

Le nove stagioni in cui lo scudetto è andato a chi inseguiva al giro di boa:

| stagione | campione d'inverno | campione d'Italia |
|---|---|---|
| 1998/99 | Fiorentina | Milan |
| 1999/00 | Juventus | Lazio |
| 2001/02 | Roma | Juventus |
| 2002/03 | Milan | Juventus |
| 2003/04 | Roma | Milan |
| 2015/16 | Napoli | Juventus |
| 2017/18 | Napoli | Juventus |
| 2020/21 | Milan | Inter |
| 2021/22 | Inter | Milan |

## Appendice — gli indici di dispersione

| Distribuzione | media | mediana | dev. std | CV | asimmetria | curtosi |
|---|---|---|---|---|---|---|
| Punti del campione d'inverno | 43,8 | 44 | 5,8 | 13% | -0,22 | -1,02 |
| Punti del campione d'Italia | 83,1 | 84 | 9,1 | 11% | -0,16 | -0,70 |
| Punti aggiunti dopo l'inverno | 40,1 | 40 | 4,8 | 12% | +0,64 | -0,05 |

Curtosi in eccesso (0 = normale). Con 33 stagioni, asimmetria e curtosi vanno prese con le pinze.

[^def]: In pratica fissiamo il giro di boa quando ogni squadra ha giocato almeno n−1 partite (n = numero di squadre). La soglia ammette una gara da recuperare, e così seguiamo la convenzione dei giornali: nel 2025/26, per esempio, consideriamo campione d'inverno il Napoli, come hanno fatto le testate, anche se l'Inter aveva una partita in meno e, recuperandola, sarebbe stata matematicamente lei la prima.
[^tab]: I valori — 24 scudetti su 33 da campione d'inverno (72,7%, IC95% Wilson 56–85%), 9 su 605 da non campione d'inverno (1,5%) — vengono dalla tavola di contingenza in appendice, dove ci sono anche i test (Fisher: odds ratio 176,6, p ≈ 6·10⁻²⁹).
[^squadre]: Il dettaglio per squadra (quante volte campione d'inverno e quante poi campione) e l'elenco delle nove rimonte, stagione per stagione, sono in appendice. In 33 stagioni sono passate 53 squadre, ma solo sei hanno guidato all'inverno e solo sei hanno vinto lo scudetto.
[^riforma]: Il passaggio a venti squadre nasce dalla riforma dei campionati FIGC del settembre 2003, dopo il «caso Catania» e i ricorsi sugli organici della Serie B: una riorganizzazione istituzionale, non una scelta pensata per rendere il campionato più equilibrato. Un lotto di venti squadre non si vedeva dal 1951/52. Fonte: [Serie A 2004-2005, Wikipedia](https://it.wikipedia.org/wiki/Serie_A_2004-2005).
[^dati]: Perimetro: Serie A dal 1993/94 (prima stagione disponibile nella fonte) al 2025/26, 33 stagioni. Provider: [football-data.co.uk](https://www.football-data.co.uk/italym.php). Numeri nostri: percentuali, intervalli e distribuzioni vengono dal notebook del progetto, dove ci sono codice e test.
[^lega]: [Lega Serie A](https://www.legaseriea.it/serie-a/news/inter-col-lecce-per-diventare-campione-d-inverno) — il campione d'inverno nella storia (63 su 93, 67,7%).
[^sm]: [SportMediaset](https://www.sportmediaset.mediaset.it/calcio/inter/inter-campione-inverno-statistica-scudetto_107743377-202602k.shtml) — la statistica scudetto nell'era recente (~79%).
[^cds]: [Corriere dello Sport](https://www.corrieredellosport.it/news/calcio/serie-a/milan/2026/01/07-145696785/il_calcolo_preciso_di_allegri_su_scudetto_e_champions_ecco_quanti_punti_servono) — Allegri sulla quota-punti da scudetto (86-88).

[g-risultati]: risultati.png
[g-era]: era.png
[g-cumulata]: cumulata.png
[g-timeline]: timeline.png
[g-forma]: forma.png
[g-distribuzioni]: distribuzioni.png
