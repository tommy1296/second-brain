---
name: smista-inbox
description: Trasforma il materiale grezzo di 00-inbox/ (transcript, riassunti, appunti) in note atomiche del second brain e archivia la fonte. Usala quando Tommaso chiede di smistare l'inbox o di trasformare un file dell'inbox in note.
---

# Smista inbox

Trasforma un file di `00-inbox/` in note atomiche, poi archivia la fonte. Le regole generali (formato note, stanze, aree) sono in `AGENTS.md`: qui c'è solo la procedura.

## 0. Scegli il file
- Elenca i file in `00-inbox/` (ignora `.gitkeep`).
- Se te ne ho indicato uno, usa quello. Se sono più di uno e non ho specificato, elencameli e lavora **un file alla volta**, nell'ordine che scelgo io (o in ordine alfabetico se ti dico di procedere).
- Se il file è un binario (PDF, audio, video), estrai prima il testo; se non ci riesci, dimmelo e fermati.

## 1. Leggi
- Leggi il file per intero.
- Leggi `20-knowledge/_index.md` e gli `_index.md` delle aree toccate dal contenuto. Apri solo le note esistenti che sembrano sovrapporsi alla fonte (decidi dal `summary`).

## 2. Proponi un piano e fermati
Mostrami:
1. **Note nuove:** tabella con nome file (kebab-case), area, summary in una riga.
2. **Note esistenti da aggiornare:** quale nota e cosa aggiungeresti. Aggiornare è sempre meglio che duplicare.
3. **Conflitti:** dove la fonte contraddice note esistenti.
4. **Cosa lasci fuori:** parti promozionali (call to action del video, offerte, inviti a iscriversi) e contenuti non riutilizzabili.

**Non scrivere nulla finché non ti do l'ok.** Se correggo il piano, riproponilo solo se le modifiche sono sostanziali.

## 3. Scrivi le note (dopo l'ok)
Parti da `tools/template-nota.md`. Per ogni nota:
- **Una idea per nota**, testo autonomo, massimo 150 righe (puntare a 20–50).
- **Solo fatti presenti nella fonte.** Niente aggiunte tue, niente esempi inventati. Esempi e numeri vanno presentati come esempi o casi riportati, non come verità generali.
- **Niente definizioni standard.** Non creare note che definiscono termini noti del marketing (CPC, CTR, CAC, LTV, ROAS…). Se la fonte dà soglie, dati o regole su quel termine, mettili nella nota della regola o in una nota di dati.
- **Niente numeri incoerenti.** Se un esempio della fonte ha numeri che non tornano, non riportarlo e segnalalo nel piano.
- **Frontmatter:**
  - `summary:` sempre tra virgolette doppie; deve dire cosa contiene la nota e quando serve.
  - `tags:` area + tipo (`regola`, `esempio`, `dato`, `decisione`, `definizione`).
  - `related:` su una riga, formato `["[[nota-a]]", "[[nota-b]]"]`, almeno un link.
  - `fonte:` il percorso in `90-archivio/fonti/<nome-file>`. Se una nota esistente riceve informazioni da una seconda fonte: `fonte: ["90-archivio/fonti/a.md", "90-archivio/fonti/b.md"]`.
  - `aggiornato:` data di oggi (anche sulle note esistenti che modifichi).
- **La fonte si cita solo nel campo `fonte:`.** Nel testo niente autore, niente link al video, niente minuti.
- Collega le note tra loro con `[[nome-nota]]`. Se l'argomento ha già una nota hub (es. `anatomia-landing-page`), aggiungi lì i link alle note nuove.
- Se c'è un conflitto con una nota esistente, scrivi nel testo che le indicazioni divergono e riporta entrambe, senza scegliere tu.

## 4. Archivia la fonte
- Sposta il file in `90-archivio/fonti/` con lo stesso nome (`git mv` se è già tracciato, altrimenti `mv`).
- Nel file archiviato togli i riferimenti ai minuti/timestamp (righe o link tipo `[4:50–10:10](...&t=290s)`). Tieni il link principale e l'intestazione (autore, titolo, durata).
- L'inbox deve contenere solo `.gitkeep` e gli eventuali file non ancora smistati.

## 5. Controlla
- Lancia `python tools/brain.py` (rigenera gli indici). Correggi gli errori e rilancialo finché non dà `OK`.
- Verifica che nelle note nuove non ci siano link a YouTube o riferimenti alla fonte nel testo: `grep -rn "youtube" 20-knowledge/`.

## 6. Chiudi
- Aggiorna la voce "Second brain" di `memory.md` (Stato / Deciso / Prossimo passo, telegrafico).
- Metti in staging i file toccati (`git add` dei file del brain, non di `.obsidian/`).
- **Non fare commit.** Lo faccio io, o te lo chiedo esplicitamente.
- Riepilogo finale in poche righe: note create, note aggiornate, esito dello script.
