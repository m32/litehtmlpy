#!/usr/bin/env vpython3
import sys
from weasyprint import HTML

def main():
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        fname = 'demo.html'
        #fname = 'litehtmlt.html'
    HTML(fname).write_pdf('demo.pdf')
main()
