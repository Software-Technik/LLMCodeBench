# LLMCodeBench 

## ⚙️ Pre-Start Setup

Bevor du das Projekt nutzen kannst, führe bitte folgende Schritte durch:

### 1. Virtuelle Umgebung erstellen

```bash
python -m venv .venv
source .venv/bin/activate  # Auf Windows: .venv\Scripts\activate
```

### 2. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 3. .env variablen setzen

Erstelle eine `.env`-Datei im Ordner `data_setup/` mit folgendem Inhalt:

```env
# Für OpenAI
OPENAI_API_KEY=dein_openai_api_key

# Für DeepSeek
DEEPSEEK_API_KEY=dein_deepseek_api_key

# Für Advent of Code – Session Cookie (aus dem Browser kopieren)
AOC_SESSION_COOKIE=dein_session_token

# Das Ollama model angeben welches mit geteset werden soll in unserem fall devstral:24b
OLLAMA_MODEL="devstral:24b"
```

> Du benötigst ein **Advent of Code Benutzerkonto** und musst eingeloggt sein, um dein Session-Token aus dem Browser zu extrahieren.  
---

## Part 1 – Datengenerierung

Hier werden Eingabedateien und Referenzlösungen zu allen Advent-of-Code-Tagen erstellt:

```bash
python data_setup/main.py --init
```

Dies erzeugt:
- Aufgaben-Eingaben (Input-Files)
- Menschliche Referenzlösungen zur Validierung
---

## Part 2 – Codegenerierung durch LLMs

Du kannst die folgenden Flags einzeln oder kombiniert verwenden:

```bash
python data_setup/main.py --openai
python data_setup/main.py --deepseek
python data_setup/main.py --ollama

# Oder kombiniert:
python data_setup/main.py --openai --deepseek
```
---

## Phase 3 – Evaluation

In der Evaluationsphase werden alle Lösungen (human + LLM) getestet und analysiert:

```bash
python evaluation/main.py
```

---


## Projektkomponenten

1. **Virtuelle Umgebung erstellen**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Auf Windows: .venv\Scripts\activate

### Data setup

- **input_crawler**
  Crawlt alle AoC Inputs und legt diese in die jeweiligen Ordner ab

- **solution_generator**  
  Generiert mit Hilfe der Inputs und human.py das entsprechende Solutionfile

- **solution_comitter**  
  Überprüft die erzeugten Solutions automatisiert auf ihre Korrektheit über AoC Webseite

- **llm_controller**  
  Erzeugt die KI Lösungen für die human.py Files

- **code_syntax_checker**
  Testet die KI Lösungen auf Syntax und Runtime Fehler und loggt diese

- **llm_error_fixer**  
  Liest geloggte Syntaxerror ein und wiederholt die KI Generierung

### Evaluation

- **code-evaluation**
  Testet sämtliche Codes in der project_root auf ihre Laufzeit und ihren RAM-Speicher und loggt die Ergebnisse

- **result-evaluation**
  Generiert automatisierte Analysen auf den erzeugten Evaluationsdaten

# GitHub-Regelwerk für dieses Projekt

## 1. Arbeiten mit Feature-Branches

- Jede\*r arbeitet **in einem eigenen Branch**, z. B.:
  - `feature/web-crawler` (Kevin)
  - `feature/pipeline` (Silas)
- Der `main`- oder `master`-Branch bleibt **stabil und sauber** – dort liegt nur getesteter und abgesprochener Code.

## 2. Kein Direkt-Push in `main` oder `master`

**Direktes Pushen in `main`/`master` ist nicht erlaubt**, außer:

- 1. Der Code ist **100 % funktionsfähig**.
- 2. Die Änderung wurde **im Team abgesprochen**.
- 3. Es wurde ein **Code-Review durchgeführt**.

> **Pull Requests (PRs)** nutzen, um Änderungen in `main` zu bringen.

## 3. Code aktuell halten

- Holt euch regelmäßig die **aktuellsten Änderungen aus `main`** in euren Feature-Branch (`git pull origin main` oder Rebase).
- So vermeidet ihr Merge-Konflikte und bleibt synchron mit dem Projekt.

## 4. Commit-Konventionen

- Schreibt **aussagekräftige Commit-Nachrichten**, z. B.:

  ```bash
  feat: add sitemap parser to crawler
  fix: handle API timeout in pipeline
  ```

- Keine generischen Nachrichten wie `update`, `last try lol`, `fix bug`.

## 5. Pull Requests

- Keine eigenen PRs mergen – **mindestens ein Teammitglied muss reviewen**.

## 6. GitHub-Hygiene & Best Practices

- **Alte Branches löschen**, sobald sie gemerged sind.
- `.gitignore` aktuell halten – keine sensiblen oder unnötigen Dateien committen.
- **Keine Secrets** (API-Keys, Passwörter) ins Repository pushen.
  - Diese gehören in `.env`-Dateien und bleiben lokal.
- Dokumentation wie `README.md` oder `/docs` immer aktuell halten.

## 7. Kommunikation

- Bei Unklarheiten lieber **kurz im Team abstimmen**, bevor ihr pusht.

---

**Ziel:** Sauberer Code, saubere Branches, klare Kommunikation – damit macht das Arbeiten mehr Spaß und das Projekt bleibt wartbar!
