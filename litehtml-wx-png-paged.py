#!/usr/bin/env vpython3
import logme
import wx
from litehtmlpy import litehtmlwx, litehtmlpy

class document_container(litehtmlwx.document_container):
    pass

class Main:
    def __init__(self):
        self.wxapp = wx.App(False)

    def save(self, i, htmlstart, htmldata, htmlend):
        html = htmlstart+htmldata+htmlend
        if 0:
            fp = open('demo-{i:04d}.html'.format(i=i), 'wt')
            fp.write(html)
            fp.close()

        cntr = document_container()
        cntr.reset()

        doc = litehtmlpy.fromString(cntr, html, None, None)
        doc.render(cntr.size[0], litehtmlpy.render_all)

        cntr.size[1] = doc.height()
        cntr.reset()
        clip = litehtmlpy.position(0, 0, doc.width(), doc.height())
        doc.draw(0, 0, 0, clip)

        cntr.bmp.SaveFile('demo-{i:04d}.png'.format(i=i), wx.BITMAP_TYPE_PNG)

        del doc
        del cntr

    def main(self):
        html = open('demo.html', 'rt').read()
        split='<body>'
        start = html.find(split) + len(split)
        start = html.find('>', start) + 1
        i = end = start
        while True:
            i = html.find('</div>', i+1)
            if i == -1:
                break
            end = i
        htmlstart = html[0:start]
        htmldata = html[start:end]
        htmlend = html[end:]
        i = 0
        split = '<div class="lamstrone"/>'
        while True:
            istop = htmldata.find(split)
            if istop == -1:
                self.save(i, htmlstart, htmldata, htmlend)
                break
            self.save(i, htmlstart, htmldata[:istop], htmlend)
            htmldata = htmldata[istop+len(split):]
            i += 1

def main():
    cls = Main()
    cls.main()
main()
