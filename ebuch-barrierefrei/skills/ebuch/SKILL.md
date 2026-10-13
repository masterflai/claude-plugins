---
name: ebuch
description: Überträgt Unterrichtsmaterial aus PowerPoint, Word oder PDF in eine barrierefreie DOCX nach E-Buch-Standard für blinde und sehbehinderte Lernende. Auslösen bei "barrierefrei machen", "für eine blinde Person lesbar", "E-Buch-Standard", "Screenreader-tauglich", "in Braille ausgeben", "Folien als Text für Sehbehinderte", oder wenn eine Präsentation oder ein Skript für einen blinden Lernenden aufbereitet werden soll.
---

# Barrierefreie Übertragung nach E-Buch-Standard

Ziel ist **nicht**, eine Präsentation barrierefrei zu reparieren, sondern ihren Inhalt in ein strukturiertes Word-Dokument zu überführen, das ein blinder Mensch mit Screenreader und Braillezeile zum Lernen benutzen kann.

PowerPoint ist ein Vortrags-, kein Lesemedium: keine durchgehende Dokumentstruktur, keine Überschriftenhierarchie über Folien hinweg, keine Navigation per Überschriftenliste, schlechte Braille-Ausgabe. DOCX ist Vorgabe des E-Buch-Standards; darauf setzen auch das E-Buch-Menü (Word-Add-in) und die Braille-Konvertierung (RTFC) auf.

Wenn jemand fragt, ob eine barrierefreie PPTX nicht genüge: technisch ja (Folientitel, Lesereihenfolge, Alternativtexte, Kontraste erfüllen BITV/EN 301 549), zum Lernen nein. Diese Unterscheidung aktiv benennen.

## Vorab klären

Nicht erreichbar? Standard nehmen und die Annahme im Ergebnis benennen.

1. **Bildbeschreibungen fachlich-ausführlich oder knapp-funktional?** Standard: ausführlich bei Lernmaterial.
2. **Bilder einbetten?** Standard: nein — reine Textfassung, wie E-Buch „ohne Bilder". Mit Bildern nur, wenn Sehende dieselbe Datei nutzen.
3. **Abgabe an ein Medienzentrum?** Dann vorher die aktuelle Handreichung auf augenbit.de prüfen. Die Wiki-Seite nennt die gültige Fassung. Dieses Plugin zielt auf die **Fassung 2025** (Seite zuletzt am 31.03.2025 bearbeitet, Stand der Prüfung: September 2026).

Bei Prüfungen oder Leistungsnachweisen mit Namen von Lernenden: auf die Cloud-Verarbeitung hinweisen, bevor die Datei gelesen wird.

## Ablauf

### 1. Inhalt extrahieren

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/ebuch/scripts/extrahieren.py <quelldatei> --out <arbeitsordner>
```

Schreibt `inhalt.json` und `bilder/`, gibt eine **indizierte Liste** aller Absätze je Folie aus und meldet Auffälligkeiten (Folien ohne Titel, Bilder ohne brauchbaren Alternativtext, freie Textfelder).

Die Lesereihenfolge wird aus `top`/`left` rekonstruiert, nicht aus der XML-Reihenfolge — die ist die Z-Order.

### 2. Bilder ansehen

Jedes inhaltstragende Bild aus `bilder/` mit dem Read-Tool **öffnen**. Nicht aus Dateiname, Alternativtext oder Kontext raten.

Mehrfach verwendete Grafiken (das Skript meldet sie) sind fast immer dekorativ: Logos, Designelemente, Symbole auf Kacheln. Automatisch erzeugte Alternativtexte („Ein Bild, das … enthält. Beschreibung automatisch generiert.") zählen als kein Alternativtext.

### 3. Beschreibungen schreiben

Zwei Teile je Bild:

1. Was sachlich zu sehen ist — Aufbau, Anordnung, Farben, **alle Beschriftungen vollständig**. Diagrammtexte gehören komplett in die Beschreibung.
2. Wozu das Bild im Zusammenhang der Folie steht.

Regeln:

- Keine Diagnosen, Wertungen oder Fachschlüsse aus einem Bild ableiten, die die Folie nicht hergibt. Nennt die Folie den Fachbegriff, darf die Beschreibung ihn benutzen.
- Personen sachlich beschreiben, ohne Rückschluss auf Erkrankungen oder Behinderungen.
- Dekoratives **nicht** beschreiben, sondern in der Vorbemerkung benennen.
- Deutsche Rechtschreibung mit Umlauten, keine ae/oe/ue-Umschrift.

### 4. Strukturplan aufstellen

Eine Liste von Operationen, die auf die Absatz-**Indizes** der jeweiligen Folie verweist. Text niemals abtippen — das erzeugt Übertragungsfehler und kostet unnötig Kontext.

```python
("folie", 17)                      # erzeugt ((Folie 17))
("h1"|"h2"|"h3"|"h4", idx_oder_text)
("p", idx_oder_text)
("ul", [idx, ...])   ("ul2", [...])   ("ol", [...])
("bild", "<beschreibung>")
("anmerkung", text)
("tabelle", kopf, zeilen, breiten)
```

Hierarchie bilden:

- Agenda- und Überblicksfolien markieren die Hauptteile → Überschrift 1
- Wiederholte Folientitel zu **einem** Abschnitt zusammenfassen, nicht fünfzehnmal als eigene Überschrift
- Wiederkehrende Signalwörter des Originals („Hier sind sie gefragt") in der Überschrift erhalten, nicht durch eigene Begriffe ersetzen
- Keine Ebenensprünge
- Grafisch angeordnete Folien (Mindmap, Kacheln) in Listen überführen; Zuordnung über die `left`/`top`-Werte rekonstruieren, mit `#Anmerkung#`
- Über mehrere Folien laufende Aufzählungen als eine Liste führen, nur durch die Folienmarke getrennt

### 5. Dokument bauen

`ebuch_docx.py` importieren — die Bibliothek kapselt alle Fallstricke aus `references/docx-fallstricke.md`.

```python
import sys; sys.path.insert(0, "<CLAUDE_PLUGIN_ROOT>/skills/ebuch/scripts")
from ebuch_docx import EBuchDokument

d = EBuchDokument(titel="…", autor="…")   # autor = Urheber des Originalmaterials
d.ueberschrift("…", 1); d.absatz("…"); d.liste([...]); d.bild("…")
d.speichern(pfad)
```

Aufbau: Titel → „Hinweise zu dieser Übertragung" → Inhaltsverzeichnis → Inhalt → Quellen.

Die Vorbemerkung erklärt Aufbau, alle verwendeten Marken, das Vorgehen bei Bildern und **jede Abweichung vom Original**. `EBuchDokument.vorbemerkung()` erzeugt den Standardtext; Abweichungen werden als Liste übergeben.

**Keine Werkzeugspur.** In der erzeugten Datei steht nirgends ein Hinweis auf dieses Plugin, auf Claude oder auf KI — weder im Text noch in den Metadaten. `speichern()` neutralisiert `docProps/app.xml` und `lastModifiedBy` automatisch. Titel, Autor und Sprache werden gesetzt, weil der E-Buch-Standard das verlangt; als Autor gilt der Urheber des Originalmaterials, nicht das Werkzeug.

### 6. Prüfen

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/ebuch/scripts/pruefen.py <arbeitsordner>/inhalt.json <ergebnis.docx>
```

Meldet Absätze ohne Entsprechung, Sprünge in der Überschriftenhierarchie, Zahl der Marken und Tags. **Jeden gemeldeten Absatz einzeln begründen** (als Überschrift verwendet, zusammengefasst, Dublette) oder nachtragen — nie pauschal abhaken.

Danach: Schema-Prüfung und Sichtprüfung.

```bash
soffice --headless --convert-to pdf <ergebnis.docx>
pdftoppm -jpeg -r 80 <ergebnis.pdf> seite
```

Die gerenderten Seiten mit dem Read-Tool ansehen: Tabellen, Listen, Nummerierung, Überschriftenabstände.

## Referenzen

- `references/ebuch-konventionen.md` — Marken, Notationen, Do's und Don'ts des Standards. Laden, bevor der Strukturplan entsteht.
- `references/docx-fallstricke.md` — technische Details zu Word-XML. Nur laden, wenn `ebuch_docx.py` erweitert oder ein Fehler gesucht wird.

## Ergebnis melden

Kurz und konkret: Seitenzahl, Zahl der Überschriften, wie viele Bilder beschrieben und welche als dekorativ weggelassen wurden, jede strukturelle Abweichung.

Explizit benennen, welche Stellen **fachlich** gegengelesen werden sollten — typischerweise Bildbeschreibungen, bei denen aus dem Bild auf Fachinhalte geschlossen wurde.
