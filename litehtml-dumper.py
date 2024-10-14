#!/usr/bin/env vpython3
import sys
import logging

import logme
from litehtmlpy import litehtml, litehtmlpy

litehtmlpy.debuglog(0)

logger = logging.getLogger(__name__)

class document_container(litehtml.document_container):
    pass

class dumper(litehtmlpy.dumper):
    def __init__(self):
        super().__init__()

    def begin_node(self, descr):
        print('begin_node', descr)

    def end_node(self):
        print('end_node')

    def begin_attrs_group(self, descr):
        print('begin_attrs_group', descr)

    def end_attrs_group(self):
        print('end_attrs_group')

    def add_attr(self, name, value):
        print('add_attr', name, value)

class Main:
    def demo(self):
        if len(sys.argv) > 1:
            fname = sys.argv[1]
        else:
            fname = 'demo.html'
            fname = 'litehtmlt.html'
        html = open(fname, 'rt').read()

        cntr = document_container()
        print('max size=', cntr.size)

        doc = litehtmlpy.fromString(cntr, html, None, None)
        #doc.render(cntr.size[0], litehtmlpy.render_all)
        print('doc: width:', doc.width(), 'height:', doc.height())

        dump = dumper()
        doc.dump(dump)

        del doc
        del cntr

def main():
    app = Main()
    app.demo()

main()
