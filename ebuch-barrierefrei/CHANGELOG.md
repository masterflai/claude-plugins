# Änderungsverlauf

Das Format folgt [Keep a Changelog](https://keepachangelog.com/de/1.1.0/),
die Versionierung [Semantic Versioning](https://semver.org/lang/de/).

## [0.2.3] – 2026-10-15

### Hinzugefügt

- Englische Fassung der Beschreibung (README.en.md) mit Sprachumschalter, englischer Lizenzhinweis zum E-Buch-Standard
- Zweisprachige Beschreibung im Manifest und im Katalog, englische Schlagwörter
- Englische Auslöser für die Fähigkeit `ebuch`

### Geändert

- Rückfragen und Ergebnisbericht in der Sprache des Nutzers; das erzeugte Dokument bleibt deutsch nach E-Buch-Standard. Bei nicht deutschem Quellmaterial gibt es vorab einen Hinweis.

## [0.2.2] – 2026-10-13

### Hinzugefügt

- Datenschutzhinweise (PRIVACY.md), im Manifest als Datenschutzerklärung verlinkt

## [0.2.1] – 2026-10-13

### Hinzugefügt

- Icon ergänzt: Dokument mit dem Wort „ebuch“ in Braille-Punktschrift

## [0.2.0] – 2026-10-13

Erste öffentliche Fassung.

### Geändert

- Lizenz von „nur interne Nutzung" auf MIT umgestellt
- Autorenangabe auf `masterflai`
- Beispiel im Docstring von `ebuch_docx.py` neutralisiert
- Installationsanleitung für das öffentliche Repository
- Manifest um `displayName` und `homepage` ergänzt

## [0.1.0] – 2026-09-22

Erste Fassung.

### Hinzugefügt

- Fähigkeit `ebuch`: Übertragung von PowerPoint, Word und PDF in barrierefreie
  DOCX nach E-Buch-Standard, aufrufbar als `/ebuch`
- Referenz `ebuch-konventionen.md`: Marken, Notationen, Do's und Don'ts
- Referenz `docx-fallstricke.md`: Word-XML-Details
- `extrahieren.py`: Inhalt, Lesereihenfolge und Bilder auslesen
- `ebuch_docx.py`: DOCX-Bibliothek mit Formatvorlagen, Marken, Bild- und
  Tabellen-Tags, Inhaltsverzeichnis und Entfernen der Werkzeugspuren
- `pruefen.py`: Vollständigkeit, Überschriftenhierarchie, Tags und Metadaten

### Bekannte Grenzen

- Formeln, Notenschrift und taktile Grafiken werden nicht abgedeckt
- Auslagerung langer Arbeitsaufträge in ein eigenes Dokument ist nicht automatisiert

---

## Wenn augenbit.de eine neue Fassung veröffentlicht

1. Handreichung auf https://www.augenbit.de/wiki/index.php?title=E-Buch-Standard
   mit `references/ebuch-konventionen.md` abgleichen
2. Geänderte Konventionen in der Referenz nachziehen
3. Zielfassung in `README.md` und in `SKILL.md` (Abschnitt „Vorab klären") anpassen
4. Version anheben und hier eintragen
