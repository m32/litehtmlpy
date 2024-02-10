#!/usr/bin/env vpython3
import os
import io
import logme
import requests
import urllib.parse
import wx
from litehtmlpy import litehtmlwx

class Button(litehtmlwx.litehtmlpy.html_tag):
    def __init__(self, attributes, doc):
        super().__init__(doc)
        print('i`m the button', attributes)
        self.attributes = attributes
        self.wnd = None

    def update_position(self, wnd):
        pos = self.get_placement()
        print('button.pos: {},{},{},{}'.format(pos.x, pos.y, pos.width, pos.height))
        self.wnd = wnd

    def draw(self, hdc, x, y, clip, ri):
        super().draw(hdc, x, y, clip, ri)
        p = ri.pos()
        print('Button.draw', x, y, ri.left(), ri.top(), ri.right(), ri.bottom())

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
        self.wnd.HtmlClick(self)

class document_container(litehtmlwx.document_container):
    handlers = []

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def on_anchor_click(self, url, el):
        self.parent.HtmlClickHRef(url, el)

    def update_positions(self):
        for h in self.handlers:
            h.update_position(self.parent)

    def create_element(self, tag_name, attributes=None, doc=None):
        if tag_name == 'button':
            if doc is not None:
                tagh = Button(attributes, doc)
                self.handlers.append(tagh)
                return tagh
            return True

    def load_image(self, src, baseurl, redraw_on_ready):
        self.parent.HtmlLoadImage(src, baseurl, redraw_on_ready)

    def get_image_size(self, src, baseurl, size):
        sz = self.parent.HtmlGetImageSize(src, baseurl)
        size.width = sz[0]
        size.height = sz[1]

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
        del self.doc
        del self.cntr

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
                if r.headers['Content-Type'] == 'text/html':
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

        h = self.doc.height() - size[0] + 20 # + statusline.height
        if h < 0:
            h = 0
        self.SetScrollbar(wx.VERTICAL, 0, 16, h, True)

    def HtmlPaint(self):
        self.cntr.reset()
        size = self.GetClientSize()
        y = self.GetScrollPos(wx.VERTICAL)
        clip = litehtmlwx.litehtmlpy.position(0, 0, size[0], size[1])
        self.doc.draw(0, 0, -y, clip)
        self.cntr.update_positions()

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

    def HtmlGetImageSize(self, src, baseurl):
        if baseurl is not None:
            url = urllib.parse.urljoin(baseurl, src)
        else:
            url = urllib.parse.urljoin(self.url, src)
        img = self.images.get(url, None)
        if img is not None:
            return img.GetSize()
        return [0, 0]

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
            'wxpython.org.html',
            'http://wxPython.org',
            'http://wxwidgets.org',
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
            self.wv.LoadURL(url)

    def OnNextPageButton(self, event):
        n = self.historyno+1
        if n >=0 and n < len(self.history):
            self.historyno = n
            url = self.history[n]
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
