# Second Brain — mappa

Leggi questo file a inizio sessione. È una mappa: punta ai file giusti, non contiene know-how.

## Chi sono
- Tommaso: marketer in proprio, anche programmatore software.
- Lavoro solo su progetti miei (store e prodotti digitali), niente clienti.
- Dettagli (offerta, tono di voce, obiettivi, strumenti): `10-me/_index.md`.

## Regole fisse
1. Cerca a strati e fermati appena hai la risposta: questa mappa → `_index.md` della cartella → `summary` delle note → corpo della nota. Non leggere cartelle intere.
2. Per cercare in tutto il brain senza aprire file: `grep -rn "^summary:" 20-knowledge/` (vale per ogni cartella).
3. Non leggere `00-inbox/` né `90-archivio/` se non te lo chiedo (eccezione: aprire una fonte citata in `fonte:` per verificarla).
4. Usa solo fatti presenti nel brain o detti da me. Se l'informazione manca, rispondi "non presente nel brain". Cita il file da cui prendi ogni informazione.
5. Ogni progetto è isolato: lavorando su un progetto non usare materiali di un altro progetto, salvo mia richiesta. Il know-how in `20-knowledge/` vale per tutti.
6. Prima di creare una nota controlla nell'indice che non esista già: se esiste, aggiornala invece di duplicarla.
7. Non modificare a mano i file `_index.md`: li genera `tools/brain.py`.

## Stanze
| Cartella | Contiene | Quando entrarci |
|---|---|---|
| `00-inbox/` | materiale grezzo da smistare (transcript, PDF, appunti) | solo quando ti chiedo di smistare |
| `10-me/` | chi sono, offerta, tono di voce, obiettivi, stack | serve il mio contesto o il mio tono |
| `20-knowledge/` | biblioteca: note atomiche di know-how, per area | crei o valuti qualcosa di marketing |
| `30-playbooks/` | procedure passo passo ("come faccio X") | un'attività che si ripete |
| `40-progetti/` | un'ala per progetto/store | lavori su un progetto specifico |
| `50-esempi/` | landing di riferimento, template, asset di brand | ti serve un modello concreto |
| `90-archivio/` | materiale chiuso o superato; `fonti/` = materiale grezzo già smistato | solo su richiesta |
| `tools/` | script di manutenzione e template di nota | manutenzione |

Aree di `20-knowledge/`: `landing-page`, `copywriting`, `meta-ads`, `email`, `social`, `funnel`, `offerta` (prezzo, posizionamento, bundle, brand), `unit-economics` (conto economico, margini, CAC, cassa).

## Formato delle note
- Una nota = una idea. Massimo 150 righe. Nome file descrittivo in kebab-case (`hero-section-che-converte.md`).
- In cima, intestazione YAML (modello: `tools/template-nota.md`):
  - `summary:` una frase che dica cosa contiene e quando serve (è ciò che leggi per decidere se aprirla). Sempre tra virgolette doppie: senza virgolette un ": " nel testo rompe lo YAML
  - `tags:` area + tipo (`regola`, `esempio`, `dato`, `decisione`, `definizione`)
  - `related:` almeno un wikilink a note collegate, su una riga: `["[[nota-a]]", "[[nota-b]]"]`
  - `fonte:` da dove viene l'informazione (di norma un file in `90-archivio/fonti/`) · `aggiornato:` data AAAA-MM-GG
- Nel testo collega i concetti con `[[nome-nota]]`.
- La fonte si cita solo nel campo `fonte:`, mai nel testo della nota.
- Niente note di definizioni standard di marketing (CPC, CTR, CAC, LTV, ROAS…): un'AI le conosce già. Si scrivono solo dati, soglie e regole propri della fonte; una sigla si spiega in una riga dentro la nota che la usa.

## Skill
Procedure ripetibili in `.claude/skills/<nome>/SKILL.md`. Se il tuo agente non carica le skill da solo, apri il file e seguilo.
- `smista-inbox` — trasforma un file di `00-inbox/` in note atomiche e lo archivia in `90-archivio/fonti/`. Usala ogni volta che si smista l'inbox.

Video, audio, PDF e zip in inbox e fonti restano fuori da Git (vedi `.gitignore`).

## Progetti
- Ogni progetto vive in `40-progetti/<nome>/` con: `AGENTS.md` (scheda del progetto), `memory.md`, `note/` (ricerche, dati, decisioni), `output/` (landing, copy, creatività).
- Nuovo progetto: copia `40-progetti/_template/`, compila la scheda e aggiungilo qui sotto.
- Lavorando su un progetto leggi prima la sua `AGENTS.md` e la sua `memory.md`.

Progetti attivi:
- (nessuno ancora)

## Memoria
- `memory.md` qui nella radice: filoni trasversali (il brain stesso, l'attività in generale). Ogni progetto ha la sua `memory.md`.
- Formato: una voce per filone, telegrafica, massimo 10 righe, tre campi fissi: **Stato** / **Deciso** / **Prossimo passo**. Niente cronaca.
- A fine sessione aggiorna solo la voce del filone che hai toccato.

## Manutenzione
- Dopo aver creato, spostato o modificato note: `python tools/brain.py` (rigenera gli indici e segnala errori). Correggi gli errori prima di chiudere.
- Git: non fare commit se non te lo chiedo. A fine lavoro metti in staging i file del brain (non `.obsidian/`). Prima di una ristrutturazione grossa proponimi un commit di checkpoint.
- Se aggiungi una cartella o un'area, aggiorna questa mappa nella stessa sessione.
