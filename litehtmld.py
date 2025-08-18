#!/usr/bin/env vpython3
import sys
import gc
gc.enable()

import logme

from litehtmlpy import litehtml, litehtmlpy

class document_container(litehtml.document_container):
    pass

def main():
    #litehtml.litehtml.liblitehtmlpy.debuglog(1)
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        fname = 'demo.html'
    html = open(fname, 'rt').read()
    cntr = document_container()
    try:
        doc = litehtmlpy.fromString(cntr, html, None, None)
        try:
            doc.render(cntr.size[0], litehtmlpy.render_all)
            clip = litehtmlpy.position(0, 0, int(doc.width()), int(doc.height()))
            doc.draw(0, 0, 0, clip)
            del clip
            print('done')
        finally:
            print('del doc')
            del doc
    finally:
        print('del cntr')
        del cntr

showobjs = False
print('gc.collect', gc.collect())
print('gc.get_count=', gc.get_count())
print('gc.get_stats=', gc.get_stats())
if showobjs:
    print('gc.get_objects=', gc.get_objects())
main()
print('gc.collect', gc.collect())
print('gc.get_count=', gc.get_count())
print('gc.get_stats=', gc.get_stats())
if showobjs:
    print('gc.get_objects=', gc.get_objects())
