# E-Buch barrierefrei

[Deutsch](README.md) · **English**

Converts teaching material from PowerPoint, Word or PDF into accessible DOCX files following the German E-Buch standard — for learners who work with a screen reader or a braille display.

**Author:** [masterflai](https://github.com/masterflai)
**Version:** 0.2.3
**License:** MIT — free to use, including commercially, with attribution
**Target edition of the standard:** E-Buch standard, guidance in its updated 2025 edition (checked in September 2026)

## About the E-Buch standard

The E-Buch standard ("E-Buch" is German for e-book) is the format German media centres for blind and visually impaired students use to prepare textbooks and teaching material. It defines how a document is structured so that it can be read with a screen reader and converted to braille: a consistent heading hierarchy, page markers, tagged image descriptions and plain, navigable structure instead of visual layout.

**The documents this plugin produces are in German and follow German conventions**, because the standard is a German one. The plugin works best with German source material. You can use it from an English-language Claude session; the output stays a German E-Buch document.

## What the plugin does

It does not repair a presentation. It turns the content into a structured Word document:

- a continuous heading hierarchy across all slides, navigable with a screen reader
- detailed image descriptions inside `<Bild>` tags, written only after each image has actually been looked at
- slide markers such as `((Folie 17))`, so a class can refer to the same spot
- real Word tables with header rows instead of pictures of tables
- graphically arranged content (mind maps, tile grids) converted into lists
- an automatic table of contents, the list styles "Liste" and "Liste 2", document language German

## Installation

In a Claude session, in one step:

```
/plugin install ebuch-barrierefrei --marketplace masterflai/claude-plugins
```

Or in two steps — add the collection first, then install the plugin:

```
/plugin marketplace add masterflai/claude-plugins
/plugin install ebuch-barrierefrei@masterflai-plugins
```

`/plugin update ebuch-barrierefrei@masterflai-plugins` fetches new versions. To get them automatically, turn on automatic updates for this collection.

Without a command line: zip the plugin folder and upload it in the Claude app as a custom plugin file. Updates are not applied automatically that way.

## Usage

Attach a file and say something like *"Make this readable for a blind student."* The skill picks this up automatically. To call it explicitly, use `/ebuch`.

Three things are settled first: detailed or brief image descriptions, whether to embed the images, and whether the file goes to a media centre.

## Contents

| Part | Purpose |
|---|---|
| `skills/ebuch/SKILL.md` | Conversion workflow |
| `skills/ebuch/references/ebuch-konventionen.md` | Markers, notations, do's and don'ts |
| `skills/ebuch/references/docx-fallstricke.md` | Word XML details, loaded only when needed |
| `skills/ebuch/scripts/extrahieren.py` | Extracts content and images |
| `skills/ebuch/scripts/ebuch_docx.py` | DOCX library for the E-Buch standard |
| `skills/ebuch/scripts/pruefen.py` | Checks completeness, hierarchy and metadata |

The scripts need `python-docx` and `python-pptx`, and `pymupdf` for PDF.

## No tool traces in the output

The generated documents contain no reference to this plugin, to the tool used or to AI — neither in the text nor in the metadata. `docProps/app.xml` is neutralised and `lastModifiedBy` is cleared.

Title, author and language **are** set: the E-Buch standard requires filled-in document properties, and the screen reader reads out the title. The author is the creator of the original material.

`pruefen.py` checks this and reports any tool trace it finds.

## Origin of the standard

The E-Buch standard was developed in 2007 by a working group on behalf of the media centres' working group (Arbeitskreis Medienzentren) of the German federal commission reviewing teaching and learning materials for blind students. It was revised in 2016; the guidance was updated in 2025. It is published in the Augenbit wiki (in German):

- https://www.augenbit.de/wiki/index.php?title=E-Buch-Standard
- https://www.augenbit.de/wiki/index.php?title=Einstellungen_in_Word

**This plugin is not an official implementation of the standard** and is not affiliated with augenbit.de, the Arbeitskreis Medienzentren or the publishing bodies. It is an independent working aid. Whether a file produced with it meets a media centre's requirements is for that media centre to decide.

The guidance on augenbit.de is always the binding version. When a new edition appears there, this plugin should be reviewed.

## Privacy

Full text: [Datenschutzhinweise / Privacy](PRIVACY.md)

Processing takes place in Anthropic's cloud: the source file is uploaded and read there.

For general teaching material this is unproblematic. As soon as the source contains personal data — graded work, exams, reports, material with learners' names — this is processing on behalf of a controller under the GDPR. Before such use, check whether your institution allows it and whether a data processing agreement is in place.

When in doubt, remove personal data from the source file before converting it.

## Limitations

- Image descriptions need a subject-matter check. Where conclusions about subject content are drawn from an image, they can be wrong.
- Mathematical and chemical formulas, music notation and tactile graphics are not covered. There are dedicated methods for these (LaTeX, swell paper, 3D printing); the Augenbit wiki lists points of contact.
- For very long assignments the standard recommends a separate document. This is not automated.

## License

MIT License, see [`LICENSE.md`](LICENSE.md).

You may use, modify, share and include the plugin in your own projects — commercially too. The only condition: the copyright notice and license text stay intact.

The E-Buch standard itself is not covered by this license.

## Contributing

Feedback from practice is very welcome — especially from teachers, media centres and people who learn with a screen reader or braille display. Please report bugs, suggestions and deviations from the standard as an issue in the repository.
