#!/usr/bin/env vpython3
import gc
import sys
import os
import io
import logging
import requests
import urllib.parse
from PIL import Image
import wx
import logme
from litehtmlpy import litehtmlwx, litehtmlpy

#litehtmlpy.debuglog(1)

logger = logging.getLogger(__name__)

class document_container(litehtmlwx.document_container):
    def pt_to_px(self, pt):
        return pt

    def import_css(self, text, url, base_url):
        url = urllib.parse.urljoin(base_url, url)
        if os.path.exists(url):
            with open(url, 'rt') as fp:
                data = fp.read()
        elif url.split(':')[0] in ('http', 'https'):
            r = requests.get(url)
            if r.headers['Content-Type'] == 'text/css':
                data = r.text
        if data is None:
            print('unknown import_css', url)
            return
        return data

class App:
    images = {}
    url = ''
    def GetUrlData(self, url, html=True):
        data = None
        if os.path.exists(url):
            with open(url, 'rb') as fp:
                data = fp.read()
        elif url.split(':')[0] in ('http', 'https'):
            r = requests.get(url)
            print(r.headers)
            if html:
                if r.headers['Content-Type'] == 'text/html':
                    data = r.text
            else:
                if r.headers['Content-Type'] == 'image/png':
                    data = r.content
        if data is None:
            return None
        return data

    def HtmlLoadImage(self, cntr, src, baseurl, redraw_on_ready):
        if baseurl is not None:
            url = urllib.parse.urljoin(baseurl, src)
        else:
            url = urllib.parse.urljoin(self.url, src)
        data = self.GetUrlData(url, False)
        print('HtmlLoadImage({}, {})'.format(url, data is not None))
        if data is None:
            return
        try:
            im = Image.open(io.BytesIO(data))
        except:
            print('bang')
            return
        if 'A' not in im.getbands():
            alpha = 1.0
            im.putalpha(int(alpha * 256.))
        try:
            arr = bytearray(im.tobytes('raw', 'BGRa'))
        except ValueError:
            return
        cntr.put_image(url, arr, im.width, im.height)


class Main:
    def __init__(self):
        self.wxapp = wx.App(False)

    def demo(self):
        app = App()
        if len(sys.argv) > 1:
            fname = sys.argv[1]
        else:
            fname = 'demo.html'
        html = open(fname, 'rt').read()

        dc = wx.MemoryDC()

        cntr = document_container()
        cntr.SetDC(dc)
        print('max size=', cntr.size)

        doc = litehtmlpy.fromString(cntr, html, None, None)
        doc.render(cntr.size[0], litehtmlpy.render_all)
        print('doc: width:', doc.width(), 'height:', doc.height())

        i = 0
        height = 1500
        y = 0
        while y < doc.height():
            bmp = wx.Bitmap(doc.width(), height, 32)
            dc.SelectObject(bmp)
            dc.SetBackground(wx.Brush(wx.WHITE))
            dc.Clear()

            print('*'*10, 'draw')
            clip = litehtmlpy.position(0, 0, doc.width(), height)
            doc.draw(0, 0, -y, clip)

            bmp.SaveFile('demo-{i:04d}.png'.format(i=i), wx.BITMAP_TYPE_PNG)

            y += height
            i += 1

        cntr.SetDC(None)
        del doc
        del cntr

def main():
    app = Main()
    app.demo()

main()
gc.collect()
