---
summary: "Come trovare il punto del funnel e-commerce (prodotto → carrello → checkout → acquisto) dove si perdono più utenti: distinguere il problema off-site (annunci) da quello on-site (sito) e le cause tipiche di ogni passaggio."
tags: [funnel, meta-ads, regola]
related: ["[[decisioni-con-dati-statisticamente-rilevanti]]", "[[ctr]]", "[[cpc]]", "[[cpm]]", "[[dati-al-pixel-cpm-ed-evento-di-conversione]]", "[[microsoft-clarity-mappe-e-registrazioni]]", "[[rassicurazioni-vicino-al-pulsante-acquisto]]", "[[campagna-che-non-converte-controlla-la-landing]]"]
fonte: 90-archivio/fonti/riassunto-live-luca-petrosino-analisi-dati.md
aggiornato: 2026-11-03
---

# Trovare il collo di bottiglia del funnel e-commerce

Quando un e-commerce non vende o non è profittevole, si analizzano due livelli: il traffico pubblicitario (**off-site**) e la conversione dentro il sito (**on-site**). Il collo di bottiglia è il punto in cui si perde la quota maggiore di utenti. Prima di leggere i dati, serve un campione sufficiente → [[decisioni-con-dati-statisticamente-rilevanti]].

## La sequenza
Traffico pubblicitario → **pagina prodotto** → **carrello** → **checkout** → **acquisto**

| Passaggio | Causa tipica dell'abbandono |
|---|---|
| Pagina prodotto | incoerenza con l'annuncio, bug |
| Carrello | sfiducia, costi |
| Checkout | mancano i metodi di pagamento |

## Problema off-site: gli annunci
Il sintomo è un afflusso di visitatori insufficiente rispetto al budget investito. Le metriche da guardare sono:
- [[ctr]]: sotto lo 0,5% creatività e copy sono poco pertinenti;
- [[cpc]]: in Italia, sopra 1€ il costo è eccessivo;
- [[cpm]]: si può abbassare dando più dati al Pixel → [[dati-al-pixel-cpm-ed-evento-di-conversione]].

## Problema on-site: il sito
Il sintomo è che gli annunci portano traffico adeguato ma le conversioni restano nulle o marginali.
1. **Da pagina prodotto a carrello:** poche aggiunte al carrello dipendono spesso dall'incoerenza tra la promessa dell'inserzione e la scheda prodotto, oppure da problemi di usabilità.
2. **Da carrello a checkout:** gli abbandoni nascono spesso da promozioni promesse e non applicate (es. un bundle 3x2 non calcolato nel carrello) o da dubbi sulla sicurezza dei pagamenti.
3. **Fiducia:** loghi dei circuiti di pagamento e certificati SSL riducono l'incertezza → [[rassicurazioni-vicino-al-pulsante-acquisto]].

Per vedere dove si bloccano gli utenti sulla pagina: [[microsoft-clarity-mappe-e-registrazioni]]. Quando il problema è la landing: [[campagna-che-non-converte-controlla-la-landing]].
