#!/usr/bin/env vpython3
import gc
gc.enable()

import logme

from litehtmlpy import litehtml

class LiteHtml(litehtml.LiteHtml):
    pass

def main():
    #litehtml.litehtml.liblitehtmlpy.debuglog(1)
    html = open('wxpython.org.html', 'rt').read()
    cls = LiteHtml()
    cls.fromString(html)
    cls.draw(
        0, 0,
        0, 0, cls.size[0], cls.size[1])

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
