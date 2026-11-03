# Sintesi Esecutiva: 4ª Live Luca Petrosino — Margini, Profit & Loss ed E-commerce Unit Economics

## Riassunto della live

- **Relatore:** Luca Petrosino
- **Titolo:** Margini, Profit & Loss ed E-commerce Unit Economics (4ª live)
- **Corso:** corso Skool di Riccardo Ruggeri, live di Luca Petrosino
- **Formato:** live registrata
- **Link:** non indicato (contenuto riservato agli iscritti al corso)
- **Durata:** non indicata
- **Fonte del riassunto:** registrazione della live. Gli esempi e i risultati riportati sono quelli dichiarati dal relatore.

---

## 1. Visione Aziendale e Struttura del Conto Economico per E-commerce

La gestione di uno store e-commerce — sia esso basato su prodotti fisici, prodotti digitali o modelli di rivendita — deve essere impostata con il medesimo rigore analitico e la stessa pianificazione finanziaria di un'azienda tradizionale. L'esistenza di bilanci, budget preventivi, consuntivi e conti economici previsionali rappresenta il prerequisito fondamentale per garantire la sostenibilità e la crescita del business nel tempo.

Sebbene la natura del prodotto influenzi la composizione percentuale delle singole voci di costo, la struttura logica del conto economico rimane la medesima.

### Confronto Strutturale: Prodotti Fisici vs. Prodotti Digitali

| Voce di Costo / Parametro | E-commerce di Prodotti Fisici | E-commerce di Prodotti Digitali |
| :--- | :--- | :--- |
| **Costo del Prodotto (COGS)** | Ricorrente per ciascuna unità venduta (acquisto stock / produzione). | Sostenuto una tantum in fase di sviluppo/creazione iniziale. |
| **Logistica e Spedizione** | Presente e proporzionale al volume degli ordini evasi. | Assente (erogazione o download automatizzato). |
| **Commissioni di Pagamento (Gateway)** | Presente (dal 2% al 4% in base al metodo: carte, PayPal, Klarna). | Presente (incidenza analoga sui gateway di pagamento). |
| **Spesa Pubblicitaria (Adv / CAC)** | Incidenza rilevante per l'acquisizione di traffico qualificato. | Incidenza primaria per la generazione di traffico e conversioni. |
| **Rischio di Magazzino / Inserimento** | Elevato (gestione scorte, stoccaggio, resi e obsolescenza). | Nullo (infinita scalabilità senza vincoli di magazzino). |

---

## 2. Architettura delle Metriche: Voci di Costo e KPI di Performance

Per analizzare la salute finanziaria e la redditività di un e-commerce è necessario distinguere nettamente le **voci di costo** (variabili e fisse) dalle **metriche di performance** operative.

### Voci di Costo Fondamentali

1. **COGS (Cost of Goods Sold)**: Costi variabili direttamente legati all'incremento delle vendite. Includono il costo unitario del prodotto, il packaging, la spedizione, l'eventuale gestione della logistica di terzi e le commissioni dei gateway di incasso (es. dal 2% al 4%, oltre a eventuali costi di cambio valuta).
2. **Margine di Contribuzione Lordo**: Calcolato come `Vendite Totali - COGS`. Rappresenta la somma disponibile per coprire i costi pubblicitari di acquisizione e generare profitto.
3. **CAC (Cost of Acquisition Customer)**: Il costo sostenuto per acquisire un singolo cliente. È dato dal totale della spesa pubblicitaria (Meta Ads, Google Ads, sponsorizzazioni con influencer) diviso per il numero di ordini generati:
   $$\text{CAC} = \frac{\text{Spesa Pubblicitaria Totale}}{\text{Numero di Ordini}}$$
4. **Costi Fissi (OPEX)**: Canoni di piattaforme (Shopify), abbonamenti software, costi di struttura e consulenze. Non variano in modo direttamente proporportional al numero di unità vendute e non rientrano nel margine di contribuzione unitario.

### KPI di Performance Operative

* **Conversion Rate (CR)**: Percentuale di visitatori del sito che completa un acquisto.
  $$\text{CR} = \left( \frac{\text{Numero di Ordini}}{\text{Numero di Visitatori}} \right) \times 100$$
* **Average Order Value (AOV / Ticket Medio)**: Valore medio della spesa sostenuta da un utente per singolo ordine, determinato dal prezzo medio delle referenze e dal numero di pezzi acquistati.
* **Lifetime Value (LTV)**: Il valore economico totale generato da un cliente nell'arco dell'intera relazione commerciale con il brand (somma di tutti i riacquisti nel tempo).
* **ROAS (Return on Ad Spend) e MER (Marketing Efficiency Ratio)**:
  * **ROAS**: Valuta l'efficienza del singolo canale pubblicitario ($\text{ROAS} = \frac{\text{Fatturato Canale}}{\text{Spesa Adv Canale}}$).
  * **MER**: Misura l'efficienza complessiva dell'ecosistema di marketing ($\text{MER} = \frac{\text{Fatturato Totale E-commerce}}{\text{Spesa Adv Complessiva}}$).

---

## 3. Simulazioni Finanziarie e Unit Economics

L'analisi della redditività richiede di comprendere come il **Margine di Contribuzione** rappresenti il **CAC Massimo** teorico a cui l'azienda lavora a Break-Even (pareggio di bilancio sul primo ordine).

### Definizione del CAC Massimo e Punto di Pareggio

Se un prodotto viene venduto a un prezzo netto di 30 € e presenta un COGS unitario di 10 €, il margine di contribuzione è pari a 20 €.
* Se il CAC è di **5 €**, il profitto netto unitario è di **15 €**.
* Se il CAC sale a **10 €**, il profitto netto unitario scende a **10 €**.
* Se il CAC raggiunge i **20 €**, il profitto netto sul primo ordine è pari a **0 €** (Break-Even).

### Impatto della Variazione delle Metriche sulle Performance Economiche

Il modello economico dell'e-commerce è estremamente sensibile alle variazioni delle singole KPI. A parità di traffico e di spesa pubblicitaria, il miglioramento anche marginale di una metrica produce un effetto moltiplicativo sul fatturato e sul margine netto.

| Scenario ipotetico (100 Visitatori, Spesa Adv = 10 €, CPC = 0,10 €) | Tasso di Conversione (CR) | Ordini Generati | Ticket Medio (AOV) | Fatturato Generato | CAC Medio | Profitto Netto (COGS = 10 €/ord) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Scenario Base (In perdita)** | 1,0% | 1 ordine | 25 € | 25 € | 10,00 € | **-5,00 €** |
| **Ottimizzazione CR (On-Site)** | 2,0% | 2 ordini | 25 € | 50 € | 5,00 € | **+10,00 €** |
| **Ottimizzazione AOV (Upsell/Offer)**| 1,0% | 1 ordine | 40 € | 40 € | 10,00 € | **+20,00 €** |
| **Ottimizzazione Ad (CPC ridotto)** | 2,0% (su 200 vis.)| 2 ordini | 25 € | 50 € | 5,00 € | **+10,00 €** |

---

## 4. Strategia di Frontend vs. Backend e Pianificazione della Cassa

### L'Equilibrio tra Acquisizione e Riacquisto

Quando un progetto parte da zero e non dispone di uno storico di dati, la pianificazione finanziaria deve necessariamente focalizzarsi sul raggiungere il pareggio o un margine positivo fin dal primo ordine (**Frontend**). 

Tuttavia, per gli e-commerce che dispongono di prodotti consumabili, ricorrenti o di un catalogo strutturato, la profittabilità reale si sposta sul **Backend**:

* **Acquisizione a Margine Zero o in Controllata Perdita**: Sapendo che un cliente genera riacquisti entro 30–90 giorni, è possibile accettare un CAC di primo ordine pari o leggermente superiore al margine di contribuzione di Frontend.
* **Profittabilità di Backend**: Nei riacquisti successivi, l'azienda sostiene unicamente il COGS, poiché il cliente è già stato acquisito e viene ricontattato tramite canali di proprietà (Email Marketing, SMS, automazioni).

### Gestione dei Flussi Finanziari (Cash Flow)

Spingere sull'acquisizione clienti sfruttando il Lifetime Value richiede disponibilità di cassa. L'azienda deve essere in grado di sostenere l'esborso finanziario immediato per l'advertising, sapendo che il rientro dell'investimento e la generazione del margine netto avverranno in differita nei mesi successivi.

---

## 5. Leve Operative per il Miglioramento della Marginalità

Per ottimizzare la profittabilità e superare le criticità del funnel, l'intervento deve avvenire su quattro leve fondamentali:

### 1. Tasso di Conversione (CR) — Ottimizzazione On-Site
* Interventi sulla user experience, velocità di caricamento e struttura della landing page o scheda prodotto.
* Riduzione delle frizioni durante la fase di checkout.

### 2. Average Order Value (AOV) — Struttura dell'Offerta
* Introduzione di bundle di prodotto, soglie per la spedizione gratuita e pacchetti promozionali.
* Applicazione di tecniche di Upsell e Cross-Sell sia prima che dopo il pagamento.

### 3. Click-Through Rate (CTR) e Riduzione del CPC — Creatività Advertising
* Sviluppo di asset visuali e video ad alto impatto visivo capaci di interrompere lo scroll nel feed.
* Un incremento del CTR riduce direttamente il costo per click (CPC), raddoppiando il traffico veicolato allo store a parità di budget pubblicitario.

### 4. Frequenza di Riacquisto — Modelli di Ricorrenza e Backend
* Creazione di prodotti ad abbonamento mensile o servizi a ricorrenza (es. piani nutrizionali, consumabili, planner periodici).
* Strategie di e-mail marketing post-acquisto e cura del customer care per massimizzare la fidelizzazione.
