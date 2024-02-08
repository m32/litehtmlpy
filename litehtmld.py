#!/usr/bin/env vpython3
import gc
gc.enable()

import logme

from litehtmlpy import litehtml, litehtmlpy

class document_container(litehtml.document_container):
    pass

def main():
    #litehtml.litehtml.liblitehtmlpy.debuglog(1)
    html = open('demo.html', 'rt').read()
    cntr = document_container()
    doc = litehtmlpy.fromString(cntr, html, None, None)
    doc.render(cntr.size[0], litehtmlpy.render_all)
    clip = litehtmlpy.position(0, 0, doc.width(), doc.height())
    doc.draw(0, 0, 0, clip)
    del doc, cntr

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
