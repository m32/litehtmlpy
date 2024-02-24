#!/usr/bin/env vpython3
import sys
import os
import io
import urllib.parse
import logme
import wx
from litehtmlpy import litehtmlwx, litehtmlpy

#litehtmlpy.debuglog(1)

class document_container(litehtmlwx.document_container):
    pass

class App(wx.App):
    images = {}
    url = ''

    def GetUrlData(self, url, html=True):
        data = None
        print('GetUrlData', url)
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
            print('unknown url', url)
            return None
        return data

    def HtmlLoadImage(self, src, baseurl, redraw_on_ready):
        if baseurl is not None:
            url = urllib.parse.urljoin(baseurl, src)
        else:
            url = urllib.parse.urljoin(self.url, src)
        data = self.GetUrlData(url, False)
        if data is None:
            return
        img = wx.Image(io.BytesIO(data), type=wx.BITMAP_TYPE_ANY, index=-1)
        if img.IsOk():
            self.images[url] = img

    def HtmlGetImage(self, src, baseurl):
        if baseurl is not None:
            url = urllib.parse.urljoin(baseurl, src)
        else:
            url = urllib.parse.urljoin(self.url, src)
        return self.images.get(url, None)


class Main:
    def demo(self):
        wxapp = App(False)
        if len(sys.argv) > 1:
            fname = sys.argv[1]
        else:
            fname = 'demo.html'
            fname = 'litehtmlt.html'
        html = open(fname, 'rt').read()

        cntr = document_container(wxapp)
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
