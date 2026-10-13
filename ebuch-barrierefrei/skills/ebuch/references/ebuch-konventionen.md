# E-Buch-Konventionen

Zusammenfassung der Auszeichnungen und Regeln des E-Buch-Standards, wie sie für die Übertragung gebraucht werden. Die verbindliche Fassung ist die Handreichung auf augenbit.de.

## Marken und Notationen

| Element | Schreibweise |
|---|---|
| Seitenmarke | `((12))` für Seite 12 |
| Folienmarke (Abweichung, siehe unten) | `((Folie 12))` |
| Bild | `<Bild>` Beschreibung `</Bild>` |
| Tabelle | `<Tabelle> Sp. 4, Zei. 2` … `</Tabelle>` um eine echte Word-Tabelle |
| Anmerkung der Übertragung | `#…#` |
| Lücke zum Ausfüllen | `_..._` |
| Ankreuzkästchen | `[ ]` |
| Hervorhebung | `*…*` oder `_…_` |
| Kurze Fußnote | in runden Klammern direkt im Text |
| Lange Fußnote | `^Ziffer` im Text, Text verlinkt am Ende |
| Zeilennummerierung | Liste, je Zeile: Zahl, Tabulator, Text |

**Folienmarke statt Seitenmarke:** Der Standard kennt nur Seitenzahlen. Bei Präsentationen ist die Foliennummer die sinnvollere Bezugsgröße, weil im Unterricht darüber gesprochen wird. Diese Abweichung gehört in die Vorbemerkung. Verlangt das Medienzentrum die reine Zahl, `((12))` verwenden.

## Formatvorlagen

Überschriften ausschließlich über die Formatvorlagen Überschrift 1 bis Überschrift 6 — nie durch Fettung oder Schriftgröße, und nie innerhalb von Tabellen.

Aufzählungen über die Formatvorlagen Liste, Liste 2, Liste 3 (englische styleIds `List`, `List 2`, `List 3`; deutsches Word zeigt sie als Liste, Liste 2, Liste 3).

Vorteile, die daran hängen: optisch unterscheidbare Ebenen, Navigation über Gliederungsansicht und Überschriftenliste des Screenreaders, automatisches Inhaltsverzeichnis, übersichtlicher Braille-Ausdruck.

## Do's

- Text linksbündig
- Textblöcke und Abbildungen untereinander statt nebeneinander
- Neue Zeile im Absatz mit Umschalt+Eingabe, neuer Absatz mit Eingabe
- Manueller Seitenwechsel mit Strg+Eingabe
- Einzüge nur über Funktionen der Textverarbeitung
- Listen und Nummerierungen über die Registerkarte Start
- Automatische Silbentrennung einschalten, bei Bedarf bedingter Bindestrich (Strg+Minus)
- Alternativtexte für Grafiken, sofern Grafiken eingebettet werden
- Dokumenteigenschaften füllen (Autor, Titel, Sprache)
- Barrierefreiheitsprüfung in Word laufen lassen
- Bei langen Texten Aufgaben in ein eigenes Dokument auslagern
- Korrekturen zwischen Rauten setzen
- In Word unter Datei → Optionen → Dokumentprüfung → AutoKorrektur-Optionen abschalten: automatische Nummerierung, automatische Aufzählung, Silbentrennung, Autoerkennung der Sprache. Sprache korrekt einstellen.
- Export nach PDF über Speichern unter mit den Optionen „Textmarken erstellen mithilfe von Überschriften", „Strukturtags für Barrierefreiheit" und „Dokumenteigenschaften"

## Don'ts

- Eingabetaste am Ende jeder Zeile
- Einzüge durch mehrere Leerzeichen
- Silbentrennung durch fest eingefügte Trennstriche
- Mehrere aufeinanderfolgende Leerzeilen am Seitenende
- Verschachtelte Tabellen, häufig wechselnde Spaltenanzahl, verbundene oder geteilte Zellen
- Für das Verständnis wichtige Informationen in Kopf- oder Fußzeile
- Positionsrahmen und Textfelder — sie zerstören die Lesereihenfolge
- Word-Dokumente mit Formularobjekten nach PDF exportieren

## Typische Umbauten aus Präsentationen

**Wiederholte Folientitel.** Fünfzehn Folien mit demselben Titel werden ein Abschnitt mit Unterüberschriften, nicht fünfzehn gleichlautende Überschriften.

**Grafisch angeordnete Begriffe.** Mindmaps, Kreise um einen Mittelpunkt, Kachelraster: in Listen überführen. Die Zuordnung der Beschriftungen zu Gruppen oder Nummern lässt sich aus den `left`/`top`-Koordinaten der Formen rekonstruieren. Anmerkung setzen, dass die Anordnung im Original grafisch ist.

**Nebeneinanderliegende Textfelder.** Untereinander in Lesereihenfolge, sortiert nach `top`, dann `left`.

**Tabellenköpfe als separate Textfelder.** Häufig liegt in der Folie eine Tabelle mit leerer Kopfzeile, über die Textfelder gelegt sind. Die Kopfzeile aus diesen Textfeldern rekonstruieren.

**Umbrüche mitten im Satz.** Auflösen. Der Wortlaut bleibt unverändert.

**Leere Platzhalter.** Steht auf der Folie „Beispiel:" ohne Inhalt, ist das eine im Unterricht zu füllende Lücke: `_..._` setzen und in einer Anmerkung erklären.

## Quellen

- E-Buch-Standard, Handreichung in der aktualisierten Fassung 2025, herausgegeben über das Augenbit-Wiki: https://www.augenbit.de/wiki/index.php?title=E-Buch-Standard
- Erarbeitet 2007 von einer Arbeitsgruppe im Auftrag des Arbeitskreises Medienzentren der Bundesfachkommission für die Überprüfung von Lehr- und Lernmitteln für blinde Schülerinnen und Schüler, überarbeitet 2016, Handreichung aktualisiert 2025.
- Weiterführend: Einstellungen in Word — https://www.augenbit.de/wiki/index.php?title=Einstellungen_in_Word
