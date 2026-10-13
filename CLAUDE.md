# Hinweise für Claude

Dieses Repository enthält die Plugin-Sammlung `masterflai-plugins` mit dem Plugin `ebuch-barrierefrei`.

Vor jeder Änderung [`MAINTAINING.md`](MAINTAINING.md) lesen. Dort stehen der Release-Ablauf, die Einstellungen im Verzeichnis von Anthropic, das Vorgehen bei einer neuen Fassung des E-Buch-Standards und bekannte Fallstricke.

Feste Regeln:

- Das Repository ist öffentlich. Keine Klarnamen, keine privaten E-Mail-Adressen, keine lokalen Pfade, keine Namen von Schulen oder Personen aus Quellmaterial, keine Musterdokumente.
- Autor ist `masterflai`. Commits ohne Co-Autoren-Zeilen.
- Version bei jedem Release in `ebuch-barrierefrei/.claude-plugin/plugin.json` **und** `.claude-plugin/marketplace.json` gleich anheben, Changelog ergänzen, `claude plugin validate --strict ./ebuch-barrierefrei` ausführen.
- Erzeugte DOCX-Dateien enthalten keinen Hinweis auf Plugin, Claude oder KI.
- Nichts nach `main` pushen, was nicht als Release gedacht ist — das Verzeichnis liest `main`.
