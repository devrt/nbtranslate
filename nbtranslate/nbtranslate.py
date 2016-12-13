#!/usr/bin/env python
# -*- coding: utf-8 -*-

# nbstranslate
# Translate jupyter notebook using gettext
#
# Written by Yosuke Matsusaka (MID Academic Promotions Inc.)

import sys
import argparse
import nbformat
import polib
from datetime import datetime

def extract_cells(cells, po):
    for c in cells:
        if c.cell_type != 'code':
            codeblock = False
            for l in c.source.split('\n'):
                if l.find('```') == 0:
                    codeblock = not codeblock
                elif not codeblock and len(l) > 0:
                    entry = polib.POEntry(
                        msgid=l
                    )
                    po.append(entry)

def extract_translation(nbfile, potfile):
    po = polib.POFile()
    po.metadata = {
        'POT-Creation-Date': datetime.utcnow().isoformat(),
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Transfer-Encoding': '8bit',
    }
    d = nbformat.read(nbfile, nbformat.NO_CONVERT)
    try:
        for w in d.worksheets:
            extract_cells(w.cells, po)
    except AttributeError:
        extract_cells(d.cells, po)
    po.save(potfile)
    return 0


def apply_translation(nbfile, pofile, outfile):
    d = nbformat.read(nbfile, nbformat.NO_CONVERT)
    po = polib.pofile(pofile)
    _ = {}
    for e in po.translated_entries():
        _[e.msgid] = e.msgstr
    for w in d.worksheets:
        for c in w.cells:
            if c.cell_type != 'code':
                lines = []
                for l in c.source.split('\n'):
                    try:
                        lines.append(_[l])
                    except:
                        lines.append(l)
                c.source = '\n'.join(lines)
    nbformat.write(d, outfile)
    return 0


def main():
    parser = argparse.ArgumentParser(description='Translate jupyter notebook using gettext.')
    parser.add_argument('infile', nargs=1, type=argparse.FileType('r'),
                        help='File to translate.')
    parser.add_argument('--pot', dest='potfile',
                        help='Extract translation text to pot file.')
    parser.add_argument('--po', dest='pofile',
                        help='Specify translated po file.')
    parser.add_argument('--out', dest='outfile', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Specify output file name (default: STDOUT).')
    args = parser.parse_args()
    
    if args.potfile:
        return extract_translation(args.infile[0], args.potfile)
    elif args.pofile:
        return apply_translation(args.infile[0], args.pofile, args.outfile)
    else:
        parser.print_help()
        return 1

if __name__ == '__main__':
    sys.exit(main())
