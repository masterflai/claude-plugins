# Technische Fallstricke beim DOCX-Bau

Diese Datei nur laden, wenn `scripts/ebuch_docx.py` erweitert oder ein Fehler gesucht wird. Im Normalfall kapselt die Bibliothek alles Folgende.

## Formatvorlagen für deutsches Word

`python-docx` nutzt englische styleIds: `Heading 1`–`Heading 9`, `List`, `List 2`, `List Number`, `Title`, `Table Grid`. Deutsches Word zeigt sie lokalisiert als „Überschrift 1", „Liste", „Liste 2", „Listennummer", „Titel", „Tabellenraster". Das ist genau die vom E-Buch-Standard geforderte Auszeichnung — **nichts umbenennen**, sonst entstehen benutzerdefinierte Formatvorlagen, die Word nicht als Überschriften erkennt.

Gegenprobe an einer echten E-Buch-Datei: dort steht `<w:style w:styleId="Liste"><w:name w:val="List"/>`. Der `w:name` ist der kanonische englische Name; die styleId ist lokalisiert. Beides ist zulässig.

## Aufzählungszeichen an die Liste-Formatvorlagen hängen

`List` und `List 2` haben von Haus aus nur einen Einzug, kein Aufzählungszeichen. Eigene `abstractNum`-Definitionen in `numbering.xml` anlegen und per `numPr` an die Formatvorlage hängen. Das entspricht dem, was Word tut, wenn man die Formatvorlage im Dialog mit einer Aufzählung verknüpft.

## Nummerierte Listen starten sonst nicht neu

Alle Absätze mit `List Number` teilen sich eine Nummerierungsinstanz und zählen dokumentweit hoch — die dritte nummerierte Liste beginnt dann bei 12. Pro Liste eine eigene `w:num`-Instanz mit `startOverride` anlegen und dem Absatz direkt zuweisen:

```xml
<w:num w:numId="N">
  <w:abstractNumId w:val="A"/>
  <w:lvlOverride w:ilvl="0"><w:startOverride w:val="1"/></w:lvlOverride>
</w:num>
```

Alternative, falls die Nummerierung Probleme macht: Zahl, Tabulator, Text in der Formatvorlage Liste. Der Standard nennt dieses Vorgehen ausdrücklich für Zeilennummerierung; für Braille ist es sogar robuster.

## Elementreihenfolge im OOXML-Schema ist verbindlich

Manuell angehängte Elemente landen an der falschen Stelle und machen die Datei ungültig. Word bietet dann beim Öffnen „Reparieren" an — für eine Datei, die ein blinder Mensch benutzen soll, ein echtes Problem.

Vor dem Speichern `w:pPr`, `w:rPr` und `w:settings` sortieren:

- **pPr**: pStyle, keepNext, keepLines, pageBreakBefore, framePr, widowControl, **numPr**, suppressLineNumbers, pBdr, shd, tabs, suppressAutoHyphens, kinsoku, wordWrap, overflowPunct, topLinePunct, autoSpaceDE, autoSpaceDN, bidi, adjustRightInd, snapToGrid, **spacing**, **ind**, contextualSpacing, mirrorIndents, suppressOverlap, jc, textDirection, textAlignment, textboxTightWrap, outlineLvl, divId, cnfStyle, rPr, sectPr, pPrChange
- **rPr**: rStyle, rFonts, b, bCs, i, iCs, caps, smallCaps, strike, dstrike, outline, shadow, emboss, imprint, noProof, snapToGrid, vanish, webHidden, **color**, spacing, w, kern, position, **sz**, szCs, highlight, u, effect, bdr, shd, fitText, vertAlign, rtl, cs, em, lang, eastAsianLayout, specVanish, oMath
- **settings**: … documentProtection, autoFormatOverride, styleLockTheme, styleLockQFSet, defaultTabStop, **autoHyphenation**, consecutiveHyphenLimit, hyphenationZone, doNotHyphenateCaps, … alwaysMergeEmptyNamespace, **updateFields**, hdrShapeDefaults, footnotePr, endnotePr, compat, docVars, rsids, mathPr, …

Elemente aus fremden Namensräumen (`w14:docId`, `w14:defaultImageDpi`, `m:mathPr`) beim Sortieren ans Ende stellen, nicht abbrechen — sonst bleibt die Sortierung wirkungslos.

Die Vorlage von `python-docx` enthält außerdem ein `<w:zoom>` ohne `w:percent`. Attribut ergänzen, sonst schlägt die Schema-Prüfung fehl.

## Kursiv und Themenfarbe sind hartnäckig

`Heading 4` ist in der Standardvorlage kursiv, `Title` themenblau mit Unterlinie. Zwei Fallen:

1. Ein zweites `w:color` anhängen wirkt nicht — vorhandene `w:color`-Elemente erst **entfernen**.
2. Die verknüpfte Zeichenformatvorlage (`Heading 4 Char`, `Title Char`) trägt dieselben Eigenschaften und muss mitbehandelt werden.

`w:i` und `w:iCs` explizit auf `0` setzen, nicht nur entfernen.

## Tabellen

- `tcW` pro Zelle **und** `tblGrid` über `table.columns[i].width` setzen, sonst bleiben die Spalten gleich breit
- Kopfzeile wiederholen: `<w:tblHeader w:val="true"/>` in die `trPr` der ersten Zeile
- Schattierung nur mit `ShadingType.CLEAR`, nie `SOLID`
- Keine verbundenen Zellen, keine Verschachtelung

## Inhaltsverzeichnis

Feld `TOC \o "1-4" \h \z \u` einfügen und `<w:updateFields w:val="true"/>` in den Einstellungen setzen, damit Word es beim Öffnen füllt. Als sichtbaren Platzhaltertext einen Hinweis auf F9 hinterlegen, damit die Stelle nicht leer wirkt, falls die Aktualisierung unterbleibt.

## Sprache

`w:lang` mit `w:val="de-DE"` in `docDefaults/rPrDefault/rPr`. Ohne das liest der Screenreader deutschen Text mit englischer Aussprachetabelle.

## Keine Werkzeugspur

Nach dem Speichern das Zip neu schreiben:

- `docProps/app.xml` neutralisieren — die Vorlage von `python-docx` trägt dort `Application`, `Company` und `Template` ein. Elemente leeren, nicht entfernen; Word berechnet die Statistikwerte beim nächsten Speichern neu.
- `dc:creator` auf den Urheber des Originalmaterials setzen, `cp:lastModifiedBy` leeren.
- `dc:title`, `dc:language` und `dc:description` füllen — das verlangt der Standard und der Screenreader liest es vor.

Nirgends ein Hinweis auf Werkzeug, Plugin oder KI, weder in Metadaten noch im Text.

## Prüfwerkzeuge

- Schema: `validate.py` aus der docx-Skill, falls vorhanden
- Sichtprüfung: `soffice --headless --convert-to pdf`, dann `pdftoppm -jpeg -r 80` und die Seiten ansehen
- LibreOffice ersetzt fehlende Schriften und stellt Formatvorlagen teils abweichend dar. Bei Zweifeln die XML prüfen, nicht das Rendering.
