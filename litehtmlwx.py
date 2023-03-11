#!/usr/bin/env vpython3
import sys
sys.path.insert(1, 'build/lib.linux-x86_64-3.8')

import wx
from litehtml import litehtmlwx

class LiteHtml(litehtmlwx.LiteHtml):
    pass

class Main:
    def demo(self):
        wxapp = wx.App(False)
        html = open('demo.html', 'rt').read()


        cls = LiteHtml()

        print('*'*10, 'fromString')
        cls.reset()
        cls.fromString(html)

        print('*'*10, 'render')
        cls.render(cls.size[0])
        cls.size[1] = cls.height()
        cls.reset()

        print('*'*10, 'draw')
        cls.draw(
            0, 0,
            0, 0, cls.size[0], cls.size[1])
        #cls.close()
        cls.bmp.SaveFile('demo.png', wx.BITMAP_TYPE_PNG)

def main():
    app = Main()
    app.demo()

main()
