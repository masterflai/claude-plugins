# Wartungshandbuch

Wie dieses Repository gepflegt wird: Releases, das Verzeichnis von Anthropic, Updates bei einer neuen Fassung des E-Buch-Standards und die Erfahrungen aus der ersten Veröffentlichung.

Für das Plugin selbst siehe [`ebuch-barrierefrei/README.md`](ebuch-barrierefrei/README.md), für die Versionsgeschichte [`ebuch-barrierefrei/CHANGELOG.md`](ebuch-barrierefrei/CHANGELOG.md).

## Aufbau

| Pfad | Inhalt |
|---|---|
| `.claude-plugin/marketplace.json` | Katalog der Sammlung `masterflai-plugins` |
| `LICENSE` | MIT-Lizenz für das gesamte Repository |
| `ebuch-barrierefrei/` | das Plugin |
| `ebuch-barrierefrei/.claude-plugin/plugin.json` | Manifest mit Version, Autor, Links |
| `ebuch-barrierefrei/.claude-plugin/icon.png` | Icon, 1024 × 1024 px |
| `ebuch-barrierefrei/skills/ebuch/SKILL.md` | Ablauf der Übertragung |
| `ebuch-barrierefrei/skills/ebuch/references/` | E-Buch-Konventionen und Word-XML-Fallstricke |
| `ebuch-barrierefrei/skills/ebuch/scripts/` | `extrahieren.py`, `ebuch_docx.py`, `pruefen.py` |
| `ebuch-barrierefrei/PRIVACY.md` | Datenschutzhinweise, im Manifest als `privacyPolicyUrl` verlinkt |

## Ein Release veröffentlichen

1. Änderungen im Plugin-Ordner vornehmen.
2. Version anheben, **an beiden Stellen gleich**:
   - `ebuch-barrierefrei/.claude-plugin/plugin.json` → `version`
   - `.claude-plugin/marketplace.json` → `plugins[0].version`
   - zusätzlich die Zeile „Version" oben in `ebuch-barrierefrei/README.md` **und** `ebuch-barrierefrei/README.en.md`
3. Eintrag in `ebuch-barrierefrei/CHANGELOG.md`.
   Geänderte Texte in beiden Sprachen nachziehen: Jede README gibt es als `README.md` (Deutsch) und `README.en.md` (Englisch); die Beschreibungen in `plugin.json` und `marketplace.json` sind zweisprachig.
4. Prüfen:
   ```
   claude plugin validate --strict ./ebuch-barrierefrei
   claude plugin validate .
   ```
5. Committen und nach `main` pushen.
6. Im Entwicklerportal die neue Version veröffentlichen (siehe unten).

Ohne Versionssprung erreicht ein Commit die Nutzer der eigenen Sammlung nicht.

## Das Verzeichnis von Anthropic

Das Plugin ist über das Entwicklerportal unter [claude.ai/directory/manage](https://claude.ai/directory/manage) eingereicht. Das frühere Formular in der Claude Console wird nicht mehr unterstützt.

**Einstellungen der Einreichung**

| Einstellung | Wert | Warum |
|---|---|---|
| Repository / Pfad / Branch | `masterflai/claude-plugins` / `ebuch-barrierefrei` / `main` | Das Plugin liegt in einem Unterordner |
| Auto-Publish | aus | Jede neue Version wird bewusst per „Publish" freigegeben, solange direkt auf `main` gearbeitet wird |
| Neue Versionen | Scheduled check only | Das Verzeichnis prüft etwa alle 6 Stunden; ein Webhook ist nicht eingerichtet |

**Angaben zur Datenverarbeitung** — müssen zu `PRIVACY.md` passen:

| Frage | Antwort |
|---|---|
| Liest oder speichert personenbezogene Daten? | Reads only — übergebene Dokumente können Namen enthalten |
| Sendet Daten an Dienste außerhalb der Connectors? | Nein |
| Aufbewahrung beim eigenen Dienst | Not retained — es gibt keinen eigenen Dienst |
| Für Nutzer unter 18 gedacht? | Nein — Zielgruppe sind Lehrkräfte und Medienzentren |

Ändert sich am Plugin etwas, das diese Antworten berührt (Netzwerkzugriffe, Speicherung, MCP-Server), müssen `PRIVACY.md` **und** die Angaben im Portal angepasst werden.

**Neue Version freigeben:** Nach dem Push erkennt das Verzeichnis den Commit spätestens nach etwa 6 Stunden, sofort mit „Check for new commits" auf der Plugin-Seite im Portal. Besteht die Version die Prüfung, mit „Publish" freigeben.

## Wenn eine neue Fassung des E-Buch-Standards erscheint

Die verbindliche Fassung steht im Augenbit-Wiki: https://www.augenbit.de/wiki/index.php?title=E-Buch-Standard — die Versionsgeschichte unter `&action=history` zeigt, wann sich die Seite geändert hat.

Aktuelle Zielfassung des Plugins: **Handreichung, aktualisierte Version 2025** (Wiki-Seite zuletzt bearbeitet am 31.03.2025).

Bei einer neuen Fassung:

1. Handreichung mit `ebuch-barrierefrei/skills/ebuch/references/ebuch-konventionen.md` abgleichen und Änderungen nachziehen.
2. Zielfassung anpassen in:
   - `ebuch-barrierefrei/README.md` und `ebuch-barrierefrei/README.en.md` (Kopf)
   - `ebuch-barrierefrei/skills/ebuch/SKILL.md` (Abschnitt „Vorab klären")
   - `ebuch-barrierefrei/skills/ebuch/scripts/ebuch_docx.py` (Standardwert `fassung` in `vorbemerkung()`)
   - diese Datei (Abschnitt oben)
3. Prüfen, ob `ebuch_docx.py` neue Marken oder Notationen braucht.
4. Release wie oben, Changelog-Eintrag mit Verweis auf die neue Fassung.

## Entscheidungen

- **Autor:** `masterflai`. Commits laufen unter `masterflai` mit der noreply-Adresse von GitHub (repository-lokal per `git config` gesetzt). Klarnamen und private E-Mail-Adressen gehören nicht ins Repository.
- **Historie:** vor der Veröffentlichung neu begonnen. Ältere, nicht öffentliche Stände sind bewusst nicht enthalten.
- **Commits** enthalten keine Co-Autoren-Zeilen.
- **Lizenz:** MIT im Wurzelverzeichnis (`LICENSE`, damit GitHub sie erkennt) und im Plugin-Ordner (`LICENSE.md`, mit Hinweis, dass der E-Buch-Standard selbst nicht darunter fällt).
- **Keine Werkzeugspur** in den erzeugten DOCX-Dateien: kein Hinweis auf Plugin, Claude oder KI, weder im Text noch in den Metadaten. Titel, Autor des Originals und Sprache werden gesetzt, weil der Standard das verlangt. `pruefen.py` kontrolliert das.

## Fallstricke und Erfahrungen

**Verzeichnis**

- Das **Icon** wird nur beim allerersten Speichern oder Einreichen im Portal übernommen. Spätere Änderungen an `icon.png` ändern den Eintrag nicht.
- Ein **Dateipfad zu einem Bild** in einer Textdatei (z. B. im Changelog) löst einen „Policy hold" aus, weil die Prüfung ihn für ausführbaren Code hält. Bilddateien im Text nur beschreiben, nicht mit Pfad nennen.
- `privacyPolicyUrl` in `plugin.json` erzeugt im Portal eine Warnung „Unrecognized field". Das ist erwartet: Das Verzeichnis liest das Feld, nur Claude Code ignoriert es. `claude plugin validate --strict` akzeptiert es.
- Eine Validierung gilt für genau einen Commit. Nach jedem Push im Portal neu validieren.
- Für die Einreichung muss GitHub **in derselben Claude-Organisation** verbunden sein, aus der eingereicht wird. Repository-Zugriff der Claude-App auf `claude-plugins` beschränken.

**Augenbit-Wiki**

- Direkte Abrufe (WebFetch, curl) werden mit HTTP 403 abgewiesen. Lesen funktioniert nur über einen echten Browser.

**Prüfen nach Änderungen an GitHub**

- Abrufdienste wie WebFetch speichern Seiten bis zu 15 Minuten zwischen. Ob eine Änderung auf GitHub angekommen ist, live im Browser prüfen, nicht über einen zwischengespeicherten Abruf.
- Ein per Force-Push ersetzter Commit bleibt über seine Kennung abrufbar. Wirklich entfernt ist er erst, wenn das Repository gelöscht und neu angelegt wird oder der GitHub-Support ihn bereinigt.

**Word-Dokumente**

- Details zur Schema-Reihenfolge, zu Listen, Nummerierung und Formatvorlagen stehen in `ebuch-barrierefrei/skills/ebuch/references/docx-fallstricke.md`.
- LibreOffice stellt Formatvorlagen beim Rendern teils abweichend dar, etwa Kursivschrift trotz `w:i="0"`. Im Zweifel die XML prüfen, nicht das Rendering.
