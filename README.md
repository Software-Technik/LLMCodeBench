# LLMCodeBench


## Projekt komponenten

- **Evaluations daten**  
  Alle soltuions zu den rätseln angepasst für die pipeline

- **pipeline**  
  Automatisierte Testpipeline zur Ausführung und Analyse der Code-Performance vor und nach der Optimierung.

- **llm_controller**  
  Modul zur Steuerung des LLMs für die Generierung von optimiertem Quellcode.

- **advent-of-code-crawler**  
  Web-Crawler zur Sammlung von den inputs für die rätsel

- **solution_committer**  
  Komponente um die lösungen zu validieren und abzuspeichern

# GitHub-Regelwerk für dieses Projekt

## 1. Arbeiten mit Feature-Branches

- Jede*r arbeitet **in einem eigenen Branch**, z. B.:
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
