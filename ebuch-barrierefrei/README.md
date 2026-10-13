# E-Buch barrierefrei

Überträgt Unterrichtsmaterial aus PowerPoint, Word oder PDF in barrierefreie DOCX-Dateien nach E-Buch-Standard — für Lernende, die mit Screenreader oder Braillezeile arbeiten.

**Autor:** [masterflai](https://github.com/masterflai)
**Version:** 0.2.2
**Lizenz:** MIT — frei nutzbar, auch kommerziell, bei Nennung des Autors
**Zielfassung des Standards:** E-Buch-Standard, Handreichung in der aktualisierten Fassung 2025 (geprüft im September 2026)

## Was das Plugin tut

Es repariert keine Präsentation, sondern überführt ihren Inhalt in ein strukturiertes Word-Dokument:

- durchgehende Überschriftenhierarchie über alle Folien hinweg, navigierbar per Screenreader
- ausführliche Bildbeschreibungen in `<Bild>`-Tags, geschrieben nachdem jedes Bild tatsächlich angesehen wurde
- Folienmarken `((Folie 17))`, damit im Unterricht auf dieselbe Stelle Bezug genommen werden kann
- echte Word-Tabellen mit Kopfzeile statt Bildern von Tabellen
- grafisch angeordnete Inhalte (Mindmaps, Kachelraster) in Listen überführt
- automatisches Inhaltsverzeichnis, Formatvorlagen Liste und Liste 2, Sprache Deutsch

## Installation

In einer Claude-Sitzung, in einem Schritt:

```
/plugin install ebuch-barrierefrei --marketplace masterflai/claude-plugins
```

Oder in zwei Schritten — erst die Sammlung hinzufügen, dann das Plugin installieren:

```
/plugin marketplace add masterflai/claude-plugins
/plugin install ebuch-barrierefrei@masterflai-plugins
```

Neue Versionen holt `/plugin update ebuch-barrierefrei@masterflai-plugins`. Wer das automatisch möchte, schaltet für diese Sammlung die automatische Aktualisierung ein.

Ohne Kommandozeile: den Plugin-Ordner als ZIP-Datei packen und in der Claude-App bei den Plugins als eigene Plugin-Datei hochladen. Aktualisierungen gibt es dabei nicht automatisch.

## Benutzung

Datei anhängen und sinngemäß sagen: *„Mach das für eine blinde Person lesbar."* Die Fähigkeit greift automatisch. Wer sie ausdrücklich aufrufen will, nutzt `/ebuch`.

Vorab werden drei Dinge geklärt: ausführliche oder knappe Bildbeschreibungen, Bilder einbetten oder nicht, und ob die Datei an ein Medienzentrum geht.

## Inhalt

| Bestandteil | Zweck |
|---|---|
| `skills/ebuch/SKILL.md` | Ablauf der Übertragung |
| `skills/ebuch/references/ebuch-konventionen.md` | Marken, Notationen, Do's und Don'ts |
| `skills/ebuch/references/docx-fallstricke.md` | Word-XML-Details, nur bei Bedarf |
| `skills/ebuch/scripts/extrahieren.py` | Inhalt und Bilder auslesen |
| `skills/ebuch/scripts/ebuch_docx.py` | DOCX-Bibliothek nach E-Buch-Standard |
| `skills/ebuch/scripts/pruefen.py` | Vollständigkeit, Hierarchie, Metadaten prüfen |

Die Skripte brauchen `python-docx` und `python-pptx`, für PDF zusätzlich `pymupdf`.

## Keine Markierung in den Ausgabedateien

In den erzeugten Dokumenten steht nirgends ein Hinweis auf dieses Plugin, auf das verwendete Werkzeug oder auf KI — weder im Text noch in den Metadaten. `docProps/app.xml` wird neutralisiert, `lastModifiedBy` geleert.

Titel, Autor und Sprache **werden** gesetzt: Der E-Buch-Standard verlangt gefüllte Dokumenteigenschaften, und der Screenreader liest den Titel vor. Als Autor gilt der Urheber des Originalmaterials.

`pruefen.py` kontrolliert das und meldet jede gefundene Werkzeugspur.

## Herkunft des Standards

Der E-Buch-Standard wurde 2007 von einer Arbeitsgruppe im Auftrag des Arbeitskreises Medienzentren der Bundesfachkommission für die Überprüfung von Lehr- und Lernmitteln für blinde Schülerinnen und Schüler erarbeitet, 2016 überarbeitet; die Handreichung wurde 2025 aktualisiert. Veröffentlicht wird sie im Augenbit-Wiki:

- https://www.augenbit.de/wiki/index.php?title=E-Buch-Standard
- https://www.augenbit.de/wiki/index.php?title=Einstellungen_in_Word

**Dieses Plugin ist keine offizielle Umsetzung des Standards** und steht in keiner Verbindung zu augenbit.de, zum Arbeitskreis Medienzentren oder zu den herausgebenden Stellen. Es ist eine unabhängige Arbeitshilfe. Ob eine damit erzeugte Datei den Anforderungen eines Medienzentrums genügt, entscheidet dieses Medienzentrum.

Die verbindliche Fassung ist immer die Handreichung auf augenbit.de. Erscheint dort eine neue Fassung, gehört dieses Plugin überprüft.

## Datenschutz

Ausführlich: [Datenschutzhinweise / Privacy](PRIVACY.md)

Die Verarbeitung findet in Anthropics Cloud statt: Die Quelldatei wird dorthin übertragen und dort gelesen.

Bei allgemeinem Lehrmaterial ist das unkritisch. Sobald die Quelle personenbezogene Daten enthält — Leistungsnachweise, Prüfungen, Gutachten, Material mit Namen von Lernenden — ist das eine Auftragsverarbeitung im Sinne der DSGVO. Vor einem solchen Einsatz ist zu klären, ob die Einrichtung das zulässt und ob ein Auftragsverarbeitungsvertrag besteht.

Im Zweifel: personenbezogene Angaben vor der Übertragung aus der Quelldatei entfernen.

## Grenzen

- Bildbeschreibungen brauchen fachliche Gegenkontrolle. Wo aus einem Bild auf Fachinhalte geschlossen wird, kann das falsch sein.
- Mathematische und chemische Formeln, Notenschrift und taktile Grafiken deckt das Plugin nicht ab. Dafür gibt es eigene Verfahren (LaTeX, Schwellkopien, 3-D-Druck); Anlaufstellen nennt das Augenbit-Wiki.
- Bei sehr langen Arbeitsaufträgen empfiehlt der Standard ein eigenes Dokument. Das ist nicht automatisiert.

## Lizenz

MIT-Lizenz, siehe [`LICENSE.md`](LICENSE.md).

Sie dürfen das Plugin frei nutzen, verändern, weitergeben und in eigene Projekte übernehmen — auch kommerziell. Einzige Bedingung: Der Copyright-Vermerk und der Lizenztext bleiben erhalten.

Der E-Buch-Standard selbst ist nicht Gegenstand dieser Lizenz.

## Mitwirken

Rückmeldungen aus der Praxis sind ausdrücklich willkommen — besonders von Lehrkräften, Medienzentren und von Menschen, die mit Screenreader oder Braillezeile lernen. Fehler, Verbesserungsvorschläge und Hinweise auf Abweichungen vom Standard gerne als Issue im Repository.
