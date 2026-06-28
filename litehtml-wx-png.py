#!/usr/bin/env vpython3
import sys
import wx

import logme
from litehtmlpy import litehtmlwx, litehtmlpy
#litehtmlpy.debuglog(1)

class document_container(litehtmlwx.document_container):
    def pt_to_px(self, pt):
        return litehtmlpy.pixel_float_t(pt)

class Main:
    def __init__(self):
        self.wxapp = wx.App(False)

    def save(self, i, htmlstart, htmlend, htmldata):
        html = htmlstart+htmldata+htmlend

        dc = wx.MemoryDC()

        cntr = document_container()
        cntr.SetDC(dc)
        doc = litehtmlpy.fromString(cntr, html, None, None)
        doc.render(cntr.size.width, litehtmlpy.render_all)

        cntr.size.height.value = int(doc.height().value)

        bmp = wx.Bitmap(int(cntr.size.width.value), int(cntr.size.height.value), 32)
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush(wx.WHITE))
        dc.Clear()

        clip = litehtmlpy.position(0, 0, int(doc.width().value), int(doc.height().value))
        doc.draw(0, litehtmlpy.pixel_float_t(0), litehtmlpy.pixel_float_t(0), clip)

        bmp.SaveFile(f'demo-{i:04d}.png', wx.BITMAP_TYPE_PNG)

        cntr.SetDC(None)
        del doc
        del cntr

    def main(self):
        if len(sys.argv) > 1:
            fname = sys.argv[1]
        else:
            fname = 'demo.html'
        html = open(fname, 'rt').read()
        self.save(0, '', '', html)
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
        for i in range(len(htmlpages)):
            print(f'loop: {i} start={htmlpages[i][0]}, len={htmlpages[i][1]}')
            self.save(i+1, htmlstart, htmlend, html[htmlpages[i][0]:htmlpages[i][1]])
def main():
    cls = Main()
    cls.main()
main()
