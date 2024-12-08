#!/usr/bin/env vpython3
import wx
from litehtmlpy import litehtmlwx, litehtmlpy

class document_container(litehtmlwx.document_container):
    pass

class Main:
    def __init__(self):
        self.wxapp = wx.App(False)

    def save(self, i, htmlstart, htmlend, htmldata):
        html = htmlstart+htmldata+htmlend

        dc = wx.MemoryDC()

        cntr = document_container(dc)
        doc = litehtmlpy.fromString(cntr, html, None, None)
        doc.render(cntr.size[0], litehtmlpy.render_all)

        cntr.size[1] = doc.height()

        bmp = wx.Bitmap(cntr.size[0], cntr.size[1], 32)
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush(wx.WHITE))
        dc.Clear()

        clip = litehtmlpy.position(0, 0, doc.width(), doc.height())
        doc.draw(0, 0, 0, clip)

        bmp.SaveFile('demo-{i:04d}.png'.format(i=i), wx.BITMAP_TYPE_PNG)

        del doc
        del cntr

    def main(self):
        html = open('pit-11-29.html', 'rt').read()
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
            print(i, htmlpages[i][0], htmlpages[i][1])
            self.save(i, htmlstart, htmlend, html[htmlpages[i][0]:htmlpages[i][1]])
def main():
    cls = Main()
    cls.main()
main()
