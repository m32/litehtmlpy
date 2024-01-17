#!/usr/bin/env vpython3
import sys
sys.path.insert(1, 'src')

import wx
from litehtml import litehtmlwx

class LiteHtml(litehtmlwx.LiteHtml):
    pass

class LiteWindow(wx.Window):
    def __init__(self, parent, ID):
        wx.Window.__init__(self, parent, ID, style=wx.NO_FULL_REPAINT_ON_RESIZE)
        self.SetBackgroundColour("WHITE")
        self.InitBuffer()
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.url = None
        self.cls = LiteHtml()

    def InitBuffer(self):
        """Initialize the bitmap used for buffering the display."""
        size = self.GetClientSize()
        self.buffer = wx.Bitmap(max(1,size.width), max(1,size.height))
        dc = wx.BufferedDC(None, self.buffer)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        self.reInitBuffer = False

    def OnSize(self, event):
        self.reInitBuffer = True

    def OnIdle(self, event):
        if self.reInitBuffer:
            self.InitBuffer()
            self.Refresh(False)

    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self, self.buffer)

    def LoadURL(self, url):
        print('loadURL({})'.format(url))
        html = open(url, 'rt').read()

        self.cls.reset()
        self.cls.fromString(html)
        size = self.GetClientSize()
        self.cls.size = (size.width, size.height)
        self.cls.render(size.width)
        self.cls.reset()
        self.cls.draw(0, 0, 0, 0, self.width, self.height)

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
        self.location.AppendItems(['http://wxPython.org',
                                   'http://wxwidgets.org',
                                   'http://google.com'])

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

    def OnPrevPageButton(self, event):
        self.wv.GoBack()

    def OnCheckCanGoBack(self, event):
        event.Enable(self.historyno > 0)

    def OnNextPageButton(self, event):
        #for i in self.wv.GetForwardHistory():
        #    print("%s %s" % (i.Url, i.Title))
        self.wv.GoForward()

    def OnCheckCanGoForward(self, event):
        event.Enable(self.historyno < len(self.history))

    def OnStopButton(self, event):
        pass

    def OnRefreshPageButton(self, event):
        pass

    def OnLocationSelect(self, event):
        url = self.location.GetStringSelection()
        self.wv.LoadURL(url)

    def OnLocationEnter(self, event):
        url = self.location.GetValue()
        self.history.append(url)
        self.wv.LoadURL(url)

class SampleFrame(wx.Frame):
    def __init__(self, parent, url=None):
        super().__init__(parent, title="litehtml", size=(800,900))
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
        pnl = LiteHtmlPanel(self, url)

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
