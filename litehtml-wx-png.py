#!/usr/bin/env vpython3
import sys
import os
import io
import logging
import urllib.parse
import logme
import wx

from litehtmlpy import litehtmlwx, litehtmlpy

#litehtmlpy.debuglog(1)

logger = logging.getLogger(__name__)

class Input(litehtmlwx.litehtmlpy.html_tag):
    def __init__(self, parent, attributes, doc):
        super().__init__(doc)
        self.parent = parent
        self.attributes = attributes

    def destroy(self):
        pass

    def draw(self, hdc, x, y, clip, ri):
        super().draw(hdc, x, y, clip, ri)
        pos = ri.pos()
        css = self.css()
        nx = x + pos.x
        ny = y + pos.y
        w = pos.width
        h = pos.height
        self.parent.dc.SetPen(wx.Pen(wx.RED, 1))
        self.parent.dc.SetBrush(wx.NullBrush) 
        self.parent.dc.DrawRectangle(nx, ny, w, h)
        self.parent.dc.SetBrush(wx.NullBrush) 
        self.parent.dc.DrawText('A', nx, ny)

        fh = css.get_font_size()
        lh = css.get_line_height()
        ny = y + pos.y + h - lh
        h = lh
        print('h', h, 'ln_h', lh, 'fh', fh)
        self.parent.dc.SetPen(wx.Pen(wx.BLACK, 1))
        self.parent.dc.SetBrush(wx.NullBrush) 
        self.parent.dc.DrawRectangle(nx, ny, w, h)
        self.parent.dc.SetBrush(wx.NullBrush) 
        self.parent.dc.DrawText('B', nx, ny)

class document_container(litehtmlwx.document_container):
    handlers = []

    def create_element(self, tag_name, attributes=None, doc=None):
        if tag_name == 'input':
            t = attributes.get('type', '').lower()
            if t == 'text':
                tagh = Input(self, attributes, doc)
                self.handlers.append(tagh)
                return tagh

    def draw_text(self, hdc, text, hFont, color, pos):
        print('draw_text(%d, %s, %d, %s, %s)' %(hdc, text, hFont, color, (pos.x, pos.y, pos.width, pos.height)))
        super().draw_text(hdc, text, hFont, color, pos)

    def draw_image(self, hdc, layer, url, base_url):
        img = self.parent.HtmlGetImage(url, base_url)
        if img is None:
            return
        bpos = layer.border_box
        #cpos = layer.clip_box
        img = img.Scale(bpos.width, bpos.height, wx.IMAGE_QUALITY_HIGH)
        bmp = wx.Bitmap(img)
        #gc = wx.GraphicsContext.Create(dc)
        self.dc.DrawBitmap(bmp, wx.Point(bpos.x, bpos.y))

    def draw_solid_fill(self, hdc, layer, color):
        
        color = wx.Colour(color.red, color.green, color.blue)
        b = wx.Brush(color) 
        self.dc.SetBrush(b) 

        bpos = layer.clip_box
        self.dc.DrawRectangle(bpos.x, bpos.y, bpos.width, bpos.height)
        self.dc.SetBrush(wx.NullBrush) 

class App(wx.App):
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
