#!/usr/bin/env vpython3
import wxversion
wxversion.select('3.0-ansi')
import wx
from optparse import OptionParser
import litehtml27

def main():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", default="pit-11-29.html",
                     help="html file to parse", metavar="FILE")
    parser.add_option("-v", "--verbose",
                     action="store_true", dest="verbose", default=False)
    parser.add_option("-r", "--resize",
                     action="store_true", dest="resize", default=False)

    (options, args) = parser.parse_args()

    wxapp = wx.App(False)
    v = 3.96 * 96 / 72
    w = int(210 * v)
    h = int(297 * v)
    cls = litehtml27.LiteHtml(w, h)
    cls.render(options.filename, options.resize)
    cls.close()

if __name__ == '__main__':
    main()
