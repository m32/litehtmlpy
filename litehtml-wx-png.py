#!/usr/bin/env vpython3
import logme
import wx
from litehtmlpy import litehtmlwx, litehtmlpy

class document_container(litehtmlwx.document_container):
    pass

class Main:
    def demo(self):
        wxapp = wx.App(False)
        html = open('demo.html', 'rt').read()


        cntr = document_container()
        cntr.reset()
        print('max size=', cntr.size)

        doc = litehtmlpy.fromString(cntr, html, None, None)
        doc.render(cntr.size[0], litehtmlpy.render_all)
        print('doc: width:', doc.width(), 'height:', doc.height())

        cntr.size[1] = doc.height()
        cntr.reset()

        print('*'*10, 'draw')
        clip = litehtmlpy.position(0, 0, doc.width(), doc.height())
        doc.draw(0, 0, 0, clip)

        cntr.bmp.SaveFile('demo.png', wx.BITMAP_TYPE_PNG)

        del doc
        del cntr

def main():
    app = Main()
    app.demo()

main()
