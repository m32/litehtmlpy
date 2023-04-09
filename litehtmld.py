#!/usr/bin/env vpython3
import gc
gc.enable()

import sys
sys.path.insert(1, 'build/lib.linux-x86_64-3.8')

import litehtml.litehtml

class LiteHtml(litehtml.litehtml.LiteHtml):
    pass

def main():
    #litehtml.litehtml.liblitehtmlpy.debuglog(1)
    html = open('demo.html', 'rt').read()
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
