#!/usr/bin/env vpython3
import sys
import logme
from litehtmlpy import litehtml, litehtmlpy

#litehtmlpy.debuglog(1)

class document_container(litehtml.document_container):
    pass

class Main:
    def main(self):
        if len(sys.argv) > 1:
            fname = sys.argv[1]
        else:
            fname = 'demo.html'
        html = open(fname, 'rt').read()

        cntr = document_container()
        try:
            self.demo(cntr)
        finally:
            del cntr

    def demo(self, cntr):
        wc00 = litehtmlpy.web_color()
        print(wc00)
        wcff = litehtmlpy.web_color(0xff, 0xff, 0xff)
        print(wcff)
        print(wc00==wcff)
        print(wc00!=wcff)
        print('black', litehtmlpy.web_color.black)
        print('white', litehtmlpy.web_color.white)
        print('transparent', litehtmlpy.web_color.transparent)
        print('current', litehtmlpy.web_color.current_color)
        wcffd = wcff.darken(0.5)
        print(wcffd)

def main():
    app = Main()
    app.main()

main()
