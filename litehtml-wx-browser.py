#!/usr/bin/env vpython3
import os
import io
import logme
import requests
import urllib.parse
import wx
from litehtmlpy import litehtmlwx

class Button(litehtmlwx.litehtmlpy.html_tag):
    def __init__(self, parent, attributes, doc):
        super().__init__(doc)
        self.parent = parent
        self.attributes = attributes

    def destroy(self):
        pass

    def draw(self, hdc, x, y, clip, ri):
        super().draw(hdc, x, y, clip, ri)
        pos = ri.pos()
        x += pos.x
        y += pos.y
        w = pos.width
        h = pos.height
        print('Button.draw', x, y, w, h, self.attributes)

    def on_mouse_over(self):
        return False

    def on_mouse_leave(self):
        return False

    def on_lbutton_down(self):
        print('Button.on_lbutton_down')
        return False

    def on_lbutton_up(self):
        print('Button.on_lbutton_up')
        return False

    def on_click(self):
        print('Button.on_click')
        self.parent.HtmlClick(self)

class Input(litehtmlwx.litehtmlpy.html_tag):
    def __init__(self, parent, attributes, doc):
        super().__init__(doc)
        self.parent = parent
        self.attributes = attributes
        self.ctrl = wx.TextCtrl(parent, -1)

    def destroy(self):
        self.ctrl.Destroy()
        self.ctrl = None

    def draw(self, hdc, x, y, clip, ri):
        super().draw(hdc, x, y, clip, ri)
        pos = ri.pos()
        #print('input.draw', ri.left(), ri.top(), ri.right(), ri.bottom())
        x += pos.x
        y += pos.y
        w = pos.width
        h = pos.height
        css = self.css()
        fh = css.get_font_size()
        lh = css.get_line_height()
        y = y + (h - lh) // 2
        h = pos.height
        self.ctrl.SetSize(x, y, w, h)

    def on_mouse_over(self):
        return False

    def on_mouse_leave(self):
        return False

    def on_lbutton_down(self):
        print('input.on_lbutton_down')
        return False

    def on_lbutton_up(self):
        print('input.on_lbutton_up')
        return False

    def on_click(self):
        print('input.on_click')
        self.parent.HtmlClick(self)

class document_container(litehtmlwx.document_container):
    handlers = []

    def destroy(self):
        super().reset()
        for h in self.handlers:
            h.destroy()
        self.handlers = []

    def on_anchor_click(self, url, el):
        self.parent.HtmlClickHRef(url, el)

    def create_element(self, tag_name, attributes=None, doc=None):
        if tag_name == 'button':
            print('create_element', tag_name, attributes, doc)
            tagh = Button(self.parent, attributes, doc)
            self.handlers.append(tagh)
            return tagh
        if tag_name == 'input':
            t = attributes.get('type', '').lower()
            if t == 'text':
                tagh = Input(self.parent, attributes, doc)
                self.handlers.append(tagh)
                return tagh
            elif t == 'submit':
                tagh = Button(self.parent, attributes, doc)
                self.handlers.append(tagh)
                return tagh
        return None

    def draw_image(self, hdc, layer, url, base_url):
        self.parent.DrawImage(layer, url, base_url)

    def draw_solid_fill(self, hdc, layer, color):
        self.parent.DrawSolidFill(layer, color)

class LiteWindow(wx.ScrolledWindow):
    def __init__(self, parent, ID):
        #super().__init__( parent, ID, style=wx.NO_FULL_REPAINT_ON_RESIZE)
        wx.ScrolledWindow.__init__(self, parent, ID, style=wx.NO_FULL_REPAINT_ON_RESIZE)
        self.SetScrollbar(wx.VERTICAL, 0, 0, 0, True)
        self.SetBackgroundColour("WHITE")
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SCROLLWIN, self.OnScroll)
        self.url = None
        self.images = {}
        self.cntr = document_container(self)
        self.cntr.reset()
        self.doc = None

    def Cleanup(self):
        print('Cleanup')
        self.cntr.destroy()
        self.url = None
        self.doc = None
        self.cntr = None

    def OnMouseDown(self, evt):
        if self.doc is not None:
            cx = self.GetScrollPos(wx.HORIZONTAL)
            cy = self.GetScrollPos(wx.VERTICAL)
            self.doc.on_lbutton_down(evt.x, evt.y, cx, cy, [])
        evt.Skip()

    def OnMouseUp(self, evt):
        if self.doc is not None:
            cx = self.GetScrollPos(wx.HORIZONTAL)
            cy = self.GetScrollPos(wx.VERTICAL)
            self.doc.on_lbutton_up(evt.x, evt.y, cx, cy, [])
        evt.Skip()

    def OnMouseMove(self, evt):
        if self.doc is not None:
            cx = self.GetScrollPos(wx.HORIZONTAL)
            cy = self.GetScrollPos(wx.VERTICAL)
            self.doc.on_mouse_over(evt.x, evt.y, cx, cy, [])
        evt.Skip()

    def OnSize(self, event):
        if self.url is not None:
            self.HtmlRender()
            self.HtmlPaint()
        event.Skip()

    def OnPaint(self, event):
        if self.url is not None:
            dc = wx.PaintDC(self)
            dc.DrawBitmap(self.cntr.bmp, wx.Point(0, 0))
        event.Skip()

    def OnScroll(self, event):
        if self.url is not None:
            self.HtmlPaint()
        event.Skip()

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
                if r.headers['Content-Type'].find('text/html') != -1:
                    data = r.text
            else:
                if r.headers['Content-Type'] == 'image/png':
                    data = r.content
        if data is None:
            print('unknown url', url)
            return None
        return data

    def LoadURL(self, url):
        self.doc = None
        self.cntr.destroy()
        self.cntr.reset()
        self.url = None
        self.images = {}
        html = self.GetUrlData(url, True)
        if html is None:
            return
        self.url = url

        self.doc = litehtmlwx.litehtmlpy.fromString(self.cntr, html, None, None)
        self.HtmlRender()
        self.HtmlPaint()
        self.Refresh(True)

    def HtmlRender(self):
        size = self.GetClientSize()
        self.doc.render(size[0], litehtmlwx.litehtmlpy.render_all)
        self.cntr.size = size

        h = self.doc.height() + 20 # + statusline.height
        if h < 0:
            h = 0
        self.SetScrollbar(wx.VERTICAL, 0, size.Height, h, True)

    def HtmlPaint(self):
        self.cntr.reset()
        size = self.GetClientSize()
        y = self.GetScrollPos(wx.VERTICAL)
        print('*'*20, 'HtmlPaint')
        try:
            clip = litehtmlwx.litehtmlpy.position(0, 0, size.Width, size.Height)
            self.doc.draw(0, 0, -y, clip)
        finally:
            print('*'*20, '/HtmlPaint')

    def HtmlClickHRef(self, url, element):
        url = urllib.parse.urljoin(self.url, url)
        print('HtmlClickHref', url)
        self.GetParent().OnLocationOpen(url)

    def HtmlClick(self, element):
        print('HtmlClick', element.attributes)

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
            return img
        return None

    def HtmlGetImage(self, src, baseurl):
        if baseurl is not None:
            url = urllib.parse.urljoin(baseurl, src)
        else:
            url = urllib.parse.urljoin(self.url, src)
        #print('HtmlGetImage', src, baseurl)
        return self.images.get(url, None)

    def DrawImage(self, layer, url, base_url):
        img = self.HtmlGetImage(url, base_url)
        if img is None:
            return
        bpos = layer.border_box
        #cpos = layer.clip_box
        #print('DrawImage', url, (bpos.x, bpos.y, bpos.width, bpos.height))
        img = img.Scale(bpos.width, bpos.height, wx.IMAGE_QUALITY_HIGH)
        bmp = wx.Bitmap(img)
        #gc = wx.GraphicsContext.Create(dc)
        self.cntr.dc.DrawBitmap(bmp, wx.Point(bpos.x, bpos.y))

    def DrawSolidFill(self, layer, color):
        
        color = wx.Colour(color.red, color.green, color.blue)
        b = wx.Brush(color) 
        self.cntr.dc.SetBrush(b) 

        bpos = layer.clip_box
        self.cntr.dc.DrawRectangle(bpos.x, bpos.y, bpos.width, bpos.height)
        self.cntr.dc.SetBrush(wx.NullBrush) 

class LiteHtmlPanel(wx.Panel):
    def __init__(self, parent, url):
        wx.Panel.__init__(self, parent)

        self.current = url
        self.history = []
        self.historyno = 0
        self.frame = parent

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        btn = wx.Button(self, -1, "Open", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.OnOpenButton, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

        btn = wx.Button(self, -1, "◀︎", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.OnPrevPageButton, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)
        self.Bind(wx.EVT_UPDATE_UI, self.OnCheckCanGoBack, btn)

        btn = wx.Button(self, -1, "▶︎", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.OnNextPageButton, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)
        self.Bind(wx.EVT_UPDATE_UI, self.OnCheckCanGoForward, btn)

        btn = wx.Button(self, -1, "Stop", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.OnStopButton, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

        btn = wx.Button(self, -1, "Refresh", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.OnRefreshPageButton, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

        txt = wx.StaticText(self, -1, "URL:")
        btnSizer.Add(txt, 0, wx.CENTER|wx.ALL, 2)

        self.location = wx.ComboBox(self, -1, "", style=wx.CB_DROPDOWN|wx.TE_PROCESS_ENTER)
        self.location.AppendItems([
            'demo.html',
            'litehtmlt.html',
            'http://wxPython.org',
            'http://google.com'
        ])

        self.Bind(wx.EVT_COMBOBOX, self.OnLocationSelect, self.location)
        self.location.Bind(wx.EVT_TEXT_ENTER, self.OnLocationEnter)
        btnSizer.Add(self.location, 1, wx.EXPAND|wx.ALL, 2)


        self.wv = LiteWindow(self, -1)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(btnSizer, 0, wx.EXPAND)
        sizer.Add(self.wv, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self.frame.SetStatusText("Loaded")


    def OnOpenButton(self, event):
        dlg = wx.TextEntryDialog(self, "Open Location",
                                "Enter a full URL or local path",
                                self.current, wx.OK|wx.CANCEL)
        dlg.CentreOnParent()

        if dlg.ShowModal() == wx.ID_OK:
            self.current = dlg.GetValue()
            self.wv.LoadURL(self.current)

        dlg.Destroy()

    def OnCheckCanGoBack(self, event):
        event.Enable(self.historyno > 0)

    def OnCheckCanGoForward(self, event):
        event.Enable(self.historyno < len(self.history))

    def OnPrevPageButton(self, event):
        n = self.historyno-1
        if n >=0 and n < len(self.history):
            self.historyno = n
            url = self.history[n]
            self.location.SetValue(url)
            self.wv.LoadURL(url)

    def OnNextPageButton(self, event):
        n = self.historyno+1
        if n >=0 and n < len(self.history):
            self.historyno = n
            url = self.history[n]
            self.location.SetValue(url)
            self.wv.LoadURL(url)

    def OnStopButton(self, event):
        pass

    def OnRefreshPageButton(self, event):
        pass

    def OnLocationSelect(self, event):
        url = self.location.GetStringSelection()
        self.history.append(url)
        self.historyno = len(self.history)-1
        self.wv.LoadURL(url)

    def OnLocationEnter(self, event):
        url = self.location.GetValue()
        self.history.append(url)
        self.historyno = len(self.history)-1
        self.wv.LoadURL(url)

    def OnLocationOpen(self, url):
        self.location.SetValue(url)
        self.history.append(url)
        self.historyno = len(self.history)-1
        self.wv.LoadURL(url)


class SampleFrame(wx.Frame):
    def __init__(self, parent, url=None):
        #super().__init__(parent, title="litehtml", size=(800,900))
        wx.Frame.__init__(self, parent, title="litehtml", size=(800,900))
        # add a statusbar
        self.CreateStatusBar()

        # Add a menubar with just a quit item
        mb = wx.MenuBar()
        menu = wx.Menu()
        menu.Append(wx.ID_EXIT, '&Quit')
        mb.Append(menu, "File")
        self.SetMenuBar(mb)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=wx.ID_EXIT)

        # Create the main panel
        self.pnl = LiteHtmlPanel(self, url)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, event):
        print('Close')
        self.pnl.wv.Cleanup()
        event.Skip()

    # Menu event handler to close the frame
    def OnQuit(self, evt):
        self.Close(force=True)

def main():
    app = wx.App(False)
    frm = SampleFrame(None, "")
    frm.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
