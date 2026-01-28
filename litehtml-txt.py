#!/usr/bin/env vpython3
import sys
import wx

import logme
from litehtmlpy import litehtmltxt, litehtmlpy

class Dokument(litehtmltxt.document_container):
    def __init__(self, fname):
        super().__init__()
        self.fname = fname

    def pt_to_px(self, pt):
        return 1
        return pt

    def Run(self):
        with open(self.fname, 'rt') as fp:
            html = fp.read()

        doc = litehtmlpy.fromString(self, html, None, None)
        try:
            doc.render(self.size[0], litehtmlpy.render_all)
            self.size[1] = doc.height()
            self.reset()

            print('DOC:', 'w=', doc.width(), 'h=', doc.height())
            clip = litehtmlpy.position(0, 0, int(doc.width()), int(doc.height()))
            doc.draw(0, 0, 0, clip)
            for y in self.dc.lines():
                line = self.dc.line(y)
                print(line)
            for line in sorted(self.dc._lines.keys())[:5]:
                print(self.dc._lines[line])

        finally:
            self.SetDC(None)
            del doc

class Main:
    def demo(self):
        if len(sys.argv) > 1:
            fname = sys.argv[1]
        else:
            fname = 'demo.html'
        cls = Dokument(fname)
        cls.Run()

def main():
    app = Main()
    app.demo()

main()
