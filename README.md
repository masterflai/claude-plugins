# Claude Plugins von masterflai

**Deutsch** · [English](README.en.md)

Plugins für Claude, frei nutzbar unter MIT-Lizenz.

## Enthaltene Plugins

| Plugin | Zweck |
|---|---|
| [`ebuch-barrierefrei`](ebuch-barrierefrei/) | Unterrichtsmaterial aus PowerPoint, Word oder PDF in barrierefreie DOCX-Dateien nach E-Buch-Standard übertragen — für Lernende mit Screenreader oder Braillezeile |

## Installation

In einer Claude-Sitzung, in einem Schritt:

```
/plugin install ebuch-barrierefrei --marketplace masterflai/claude-plugins
```

Oder die Sammlung einmal hinzufügen und dann beliebige Plugins daraus installieren:

```
/plugin marketplace add masterflai/claude-plugins
/plugin install ebuch-barrierefrei@masterflai-plugins
```

Aktualisieren mit `/plugin update <plugin>@masterflai-plugins`, oder für diese Sammlung die automatische Aktualisierung einschalten.

## Lizenz

Alle Plugins in diesem Repository stehen unter der MIT-Lizenz, sofern im jeweiligen Plugin-Ordner nichts anderes angegeben ist. Nutzung, Veränderung und Weitergabe sind frei — auch kommerziell —, solange Copyright-Vermerk und Lizenztext erhalten bleiben.

## Mitwirken

Fehler, Verbesserungsvorschläge und Erfahrungen aus der Praxis gerne als Issue.

## Für den Betreuer: neue Version veröffentlichen

1. Änderungen im Plugin-Ordner vornehmen
2. Version in `<plugin>/.claude-plugin/plugin.json` **und** in `.claude-plugin/marketplace.json` anheben — beide müssen übereinstimmen
3. `CHANGELOG.md` des Plugins ergänzen
4. `claude plugin validate --strict ./<plugin>` ausführen
5. Committen und pushen

Ohne Versionssprung erreicht ein Commit installierte Kopien nicht.
