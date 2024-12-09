#!/usr/bin/env vpython3
import sys
import wx

import logme
from litehtmlpy import litehtmlwx, litehtmlpy

class document_container(litehtmlwx.document_container):
    def pt_to_px(self, pt):
        return pt

class HTMLPrinterPrintout(wx.Printout):
    def __init__(self, htmlstart, htmlend, html, htmlpages):
        wx.Printout.__init__(self)
        self.npages = len(htmlpages)
        self.htmlstart = htmlstart
        self.htmlend = htmlend
        self.html = html
        self.htmlpages = htmlpages
        self.pageinfo = (1, self.npages, 1, self.npages)

    def OnBeginDocument(self, start, end):
        return self.GetDC().StartDoc('DEMO')

    def HasPage(self, page):
        return page <= self.npages

    def GetPageInfo(self):
        return self.pageinfo

    def OnPreparePrinting(self):
        pass

    def OnPrintPage(self, page):
        dc = self.GetDC()
        self.MakePage(dc, page)
        return True

    def MakePage(self, dc, page):
        page -= 1
        print('page:', page, self.htmlpages[page])
        dc.Clear()
        dc.SetMapMode(wx.MM_TEXT)
        dc.SetBackground(wx.Brush(wx.WHITE))

        (w, h) = dc.GetSize()
        print('DC:', 'w=', w, 'h=', h, 'ppi=', dc.GetPPI())

        html = self.html[self.htmlpages[page][0]:self.htmlpages[page][1]]
        html = self.htmlstart + html + self.htmlend

        cntr = document_container()
        cntr.SetDC(dc)
        doc = litehtmlpy.fromString(cntr, html, None, None)
        try:
            doc.render(cntr.size[0], litehtmlpy.render_all)
            cntr.size[1] = doc.height()

            if 1:
                print('DOC:', 'w=', doc.width(), 'h=', doc.height())
                maxX = doc.width() + (2*50) # marginesy 50 device units
                maxY = doc.height() + (2*50) # marginesy 50 device units
                (w, h) = dc.GetSize()
                scaleX = float(w) / maxX
                scaleY = float(h) / maxY
                actualScale = min(scaleX, scaleY)
                print('SCALE:', 'x=', scaleX, 'y=', scaleY, 'act=', actualScale)
                dc.SetUserScale(actualScale, actualScale)
                #dc.SetDeviceOrigin(int(posX), int(posY))

            #bmp = wx.Bitmap(cntr.size[0], cntr.size[1], 32)
            clip = litehtmlpy.position(0, 0, doc.width(), doc.height())
            doc.draw(0, 0, 0, clip)
        finally:
            cntr.SetDC(None)
            del doc
            del cntr

class HTMLPrintDokument:
    def __init__(self, fname):
        self.fname = fname

    def Run(self):
        html = open(self.fname, 'rt').read()
        split='<body>'
        start = html.find(split) + len(split)
        end = html.find('</body>')
        htmlstart = html[0:start]
        htmlend = html[end:]
        html = html[start:end]
        htmlpages = []
        split = '<div class="lamstrone"/>'
        start = 0
        while True:
            stop = html.find(split, start)
            if stop == -1:
                htmlpages.append((start, len(html)))
                break
            htmlpages.append((start, stop))
            start = stop+len(split)
        npages = len(htmlpages)

        pdd = wx.PrintDialogData()
        pdd.SetMaxPage(npages)
        pdd.SetToPage(npages)
        printer = wx.Printer(pdd)
        printout = HTMLPrinterPrintout(htmlstart, htmlend, html, htmlpages)
        if not printer.Print(None, printout, 1):
            rc = wx.Printer_GetLastError()
        else:
            rc = wx.PRINTER_NO_ERROR
        printout.Destroy()
        print('rc=', rc)

class Main:
    def demo(self):
        wxapp = wx.App(False)

        if len(sys.argv) > 1:
            fname = sys.argv[1]
        else:
            fname = 'demo.html'
        cls = HTMLPrintDokument(fname)
        cls.Run()

def main():
    app = Main()
    app.demo()

main()
