#!/usr/bin/env vpython3
import logme
import wx
from litehtmlpy import litehtmlwx

class LiteHtml(litehtmlwx.LiteHtml):
    pass

class Main:
    def __init__(self):
        self.wxapp = wx.App(False)

    def save(self, i, htmlstart, htmldata, htmlend):
        with open(f'demo-{i:04d}.html', 'wt') as fp:
            fp.write(htmlstart+htmldata+htmlend)
        cls = LiteHtml()
        cls.reset()
        cls.fromString(htmlstart+htmldata+htmlend)
        cls.render(cls.size[0])
        cls.size[1] = cls.height()
        cls.reset()

        cls.draw(
            0, 0,
            0, 0, cls.size[0], cls.size[1])
        cls.bmp.SaveFile(f'demo-{i:04d}.png', wx.BITMAP_TYPE_PNG)

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
