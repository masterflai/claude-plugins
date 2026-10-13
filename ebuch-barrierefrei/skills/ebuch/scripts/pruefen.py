#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prüft eine E-Buch-Übertragung gegen das Original.

    python pruefen.py <arbeitsordner>/inhalt.json <ergebnis.docx>

Meldet:
  * Absätze des Originals ohne Entsprechung im Ergebnis
  * Sprünge in der Überschriftenhierarchie
  * Zahl der Marken, Bild- und Tabellen-Tags, unpaarige Tags
  * Verteilung der Formatvorlagen
  * Reste von Werkzeugspuren in den Metadaten

Jeder gemeldete Absatz ist einzeln zu begründen oder nachzutragen.
"""
import argparse
import json
import re
import sys
import zipfile


def norm(s):
    s = s.replace(" ", " ").replace("​", "").lower()
    return re.sub(r"[^a-zäöüß0-9]+", " ", s).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inhalt_json")
    ap.add_argument("ergebnis_docx")
    args = ap.parse_args()

    try:
        from docx import Document
    except ImportError:
        sys.exit("python-docx fehlt: pip install python-docx --break-system-packages")

    dok = Document(args.ergebnis_docx)
    teile = [p.text for p in dok.paragraphs]
    for t in dok.tables:
        for r in t.rows:
            for z in r.cells:
                teile.append(z.text)
    voll = " ".join(teile)
    gesucht = " " + norm(voll) + " "

    with open(args.inhalt_json, encoding="utf-8") as f:
        daten = json.load(f)

    fehlend = []
    for e in daten["einheiten"]:
        for form in e["formen"]:
            for a in form.get("absaetze", []):
                n = norm(a["text"])
                if not n:
                    continue
                w = n.split()
                vorn = " ".join(w[:8]) if len(w) >= 8 else n
                hinten = " ".join(w[-8:]) if len(w) >= 8 else n
                if vorn in gesucht or hinten in gesucht:
                    continue
                fehlend.append((e["nr"], a["text"][:80]))

    print(f"Absätze ohne Entsprechung: {len(fehlend)}")
    for nr, t in fehlend:
        print(f"   F{nr}: {t}")
    if fehlend:
        print("   -> jeden Punkt einzeln begründen (als Überschrift verwendet, "
              "zusammengefasst, Dublette) oder nachtragen")

    ueber = [(int(p.style.name[-1]), p.text) for p in dok.paragraphs
             if re.fullmatch(r"Heading [1-9]", p.style.name or "")]
    spruenge, vorher = [], 1
    for stufe, text in ueber:
        if stufe > vorher + 1:
            spruenge.append((stufe, text))
        vorher = stufe
    print(f"\nÜberschriften: {len(ueber)} | Hierarchiesprünge: {len(spruenge)}")
    for stufe, text in spruenge:
        print(f"   Ebene {stufe} nach Ebene {vorher}: {text[:60]}")

    marken = len(re.findall(r"\(\([^)]+\)\)", voll))
    auf, zu = voll.count("<Bild>"), voll.count("</Bild>")
    tauf, tzu = voll.count("<Tabelle>"), voll.count("</Tabelle>")
    print(f"\nMarken: {marken}")
    print(f"Bild-Tags: {auf} offen / {zu} geschlossen" + ("  FEHLER" if auf != zu else ""))
    print(f"Tabellen-Tags: {tauf} / {tzu}" + ("  FEHLER" if tauf != tzu else ""))
    print(f"Tabellen im Dokument: {len(dok.tables)}")

    from collections import Counter
    print("\nFormatvorlagen:")
    for name, n in Counter(p.style.name for p in dok.paragraphs).most_common():
        print(f"   {name}: {n}")

    print("\nMetadaten:")
    with zipfile.ZipFile(args.ergebnis_docx) as z:
        app = z.read("docProps/app.xml").decode("utf-8", "replace")
        core = z.read("docProps/core.xml").decode("utf-8", "replace")
    verdacht = [w for w in ("python-docx", "Claude", "KI ", "Anthropic", "Microsoft Office",
                            "LibreOffice", "ebuch-barrierefrei")
                if w.lower() in (app + core + voll).lower()]
    if verdacht:
        print(f"   WERKZEUGSPUR GEFUNDEN: {verdacht}")
    else:
        print("   keine Werkzeugspur gefunden")
    for feld, muster in (("Titel", r"<dc:title>(.*?)</dc:title>"),
                         ("Autor", r"<dc:creator>(.*?)</dc:creator>"),
                         ("Sprache", r"<dc:language>(.*?)</dc:language>")):
        m = re.search(muster, core, re.S)
        wert = (m.group(1) if m else "").strip()
        print(f"   {feld}: {wert!r}" + ("   LEER" if not wert else ""))


if __name__ == "__main__":
    main()
