# LLMCodeBench – Anleitung für MJ

## Setup

1. Virtuelle Umgebung erstellen:
   ```bash
   python -m venv venv
   ```

2. Virtuelle Umgebung aktivieren:
   ```bash
   source venv/bin/activate
   ```

3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

4. In den data_setup-Ordner wechseln:
   ```bash
   cd ./data_setup
   ```

5. .env-Datei vorbereiten:  
   Die Datei `.example.env` muss in `.env` umbenannt werden. Für diesen Arbeitsschritt wird ausschließlich `OLLAMA_MODEL="devstral:24b"` verwendet. Alle anderen Werte können leer bleiben.

6. LLM-Generierung starten:
   ```bash
   python main.py --ollama
   ```
