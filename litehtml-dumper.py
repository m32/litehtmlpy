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
        self.indent = 0

    def printi(self, *args):
        s = '   '*self.indent if self.indent else ''
        print(s, *args)

    def begin_node(self, descr):
        self.printi('begin_node', descr)
        self.indent += 1

    def end_node(self):
        self.indent -= 1
        self.printi('end_node')

    def begin_attrs_group(self, descr):
        self.printi('begin_attrs_group', descr)
        self.indent += 1

    def end_attrs_group(self):
        self.indent -= 1
        self.printi('end_attrs_group')

    def add_attr(self, name, value):
        self.printi('add_attr', name, value)

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
        doc.render(cntr.size[0], litehtmlpy.render_all)
        print('doc: width:', doc.width(), 'height:', doc.height())

        dump = dumper()
        doc.dump(dump)

        del doc
        del cntr

def main():
    app = Main()
    app.demo()

main()
