#!/usr/bin/env vpython3
import os
import sys
import wx
import array
from ctypes import *

tFont = c_ulonglong

class CreateFont(Structure):
    _fields_ = (
        ('face', c_char_p),
        ('size', c_int),
        ('weight', c_int),
        ('italic', c_int),
        ('decor', c_uint),
        # out
        ('ascent', c_int),
        ('descent', c_int),
        ('height', c_int),
        ('xheight', c_int),
        ('font', tFont),
    )

class DeleteFont(Structure):
    _fields_ = (
        ('font', tFont),
    )

class TextWidth(Structure):
    _fields_ = (
        ('text', c_char_p),
        ('font', tFont),
        # out
        ('width', c_int),
    )

class DrawText(Structure):
    _fields_ = (
        ('dc', c_int),
        ('text', c_char_p),
        ('font', tFont),
        ('color', c_uint),
        ('x', c_int),
        ('y', c_int),
    )

class DrawBackground(Structure):
    _fields_ = (
        ('dc', c_int),
        ('x', c_int),
        ('y', c_int),
        ('w', c_int),
        ('h', c_int),
        ('color', c_uint),
    )

class DrawBorders(Structure):
    _fields_ = (
        ('dc', c_int),
        ('left', c_int),
        ('right', c_int),
        ('top', c_int),
        ('bottom', c_int),
        ('colorLeft', c_uint),
        ('colorRight', c_uint),
        ('colorTop', c_uint),
        ('colorBottom', c_uint),
        ('widthLeft', c_uint),
        ('widthRight', c_uint),
        ('widthTop', c_uint),
        ('widthBottom', c_uint),
    )

class DrawMarker(Structure):
    _fields_ = (
        ('dc', c_int),
        ('x', c_int),
        ('y', c_int),
        ('w', c_int),
        ('h', c_int),
        ('mt', c_int),
        ('color', c_uint),
    )

class ClientRect(Structure):
    _fields_ = (
        ('x', c_int),
        ('y', c_int),
        ('width', c_int),
        ('height', c_int),
    )

class DocumentRender(Structure):
    _fields_ = (
        ('width', c_int),
        ('height', c_int),
    )

class PT2PX(Structure):
    _fields_ = (
        ('pt', c_int),
    )

class LiteHtml:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fonts = {}
        if os.name == "posix":
            pylib = CDLL("./liblitehtmlpy.so")
        elif os.name == "nt":
            pylib = WinDLL(os.path.join(os.getcwd(), "liblitehtmlpy.dll"))
        else:
            raise ValueError("unsuported os")
        self.pylib = pylib

        self.pylib.container_create.argtypes = (c_void_p, )
        self.pylib.container_create.restype = c_void_p
        self.pylib.container_delete.argtypes = (c_void_p, )
        self.pylib.document_create.argtypes = (c_void_p, c_void_p)
        self.pylib.document_render.argtypes = (c_void_p, c_int, c_void_p)
        self.pylib.document_draw.argtypes = (c_void_p, c_int, c_int, c_int, c_int, c_int, c_int)

        self.pycb = CFUNCTYPE(None, c_char_p, POINTER(None))(self.cbproc)
        self.pyclass = self.pylib.container_create(self.pycb)
        #print('self.pyclass    =%016X'%self.pyclass)

    def reset(self):
        bpp = 3
        bytes = array.array('B', [255] * self.width*self.height*bpp)

        self.bmp = wx.BitmapFromBuffer(self.width, self.height, bytes)
        self.dc = wx.MemoryDC()
        self.dc.SelectObject(self.bmp)
        self.ppi = self.dc.GetPPI()

    def close(self):
        self.pylib.container_delete(self.pyclass)
        assert len(self.fonts) == 0

    def GetColourFromRGBA(self, rgba):
        a = rgba & 0xff; rgba >>= 8
        b = rgba & 0xff; rgba >>= 8
        g = rgba & 0xff; rgba >>= 8
        r = rgba & 0xff; rgba >>= 8
        return wx.Colour(r, g, b, a)

    def cbproc(self, name, argp):
        #print("cbproc", name, argp)
        name = name.decode('utf8')
        getattr(self, name)(argp)

    def createFont(self, argp):
        pfi = cast(argp, POINTER(CreateFont))
        fi = pfi.contents
        face = fi.face
        if not face:
            face = 'Times New Roman'
        else:
            face = face.split(b',')[0].strip()
            if face[0] == b'"':
                face = face.split(b'"')[1]
            elif face[0] == b"'":
                face = face.split(b"'")[1]
            face = face.decode('utf8')
        if fi.italic:
            style = wx.FONTSTYLE_ITALIC
        else:
            style = wx.FONTSTYLE_NORMAL
        weigths = {
            #100:wx.FONTWEIGHT_THIN,
            #200:wx.FONTWEIGHT_EXTRALIGHT,
            300:wx.FONTWEIGHT_LIGHT,
            400:wx.FONTWEIGHT_NORMAL,
            #500:wx.FONTWEIGHT_MEDIUM,
            #600:wx.FONTWEIGHT_SEMIBOLD,
            700:wx.FONTWEIGHT_BOLD,
            #800:wx.FONTWEIGHT_EXTRABOLD,
            #900:wx.FONTWEIGHT_HEAVY,
            #1000:wx.FONTWEIGHT_EXTRAHEAVY,
        }
        weight = weigths.get(fi.weight, wx.FONTWEIGHT_NORMAL)
        underline = fi.decor != 0
        font = wx.Font(fi.size, wx.FONTFAMILY_DEFAULT, style, weight, underline, face)
        nfont = id(font)
        self.fonts[nfont] = font
        if 0:
            w, h, d, e = self.dc.GetFullTextExtent('H', font)
            xw, xh, xd, xe = self.dc.GetFullTextExtent('x', font)
            a = 0
        else:
            self.dc.SetFont(font)
            fm = self.dc.GetFontMetrics()
            a = fm.ascent
            d = fm.descent
            h = fm.height
            xh = h
        fi.ascent = a
        fi.descent = d
        fi.height = h
        fi.xheight = xh
        fi.font = nfont

    def deleteFont(self, argp):
        pfi = cast(argp, POINTER(DeleteFont))
        fi = pfi.contents
        del self.fonts[fi.font]

    def textWidth(self, argp):
        pfi = cast(argp, POINTER(TextWidth))
        fi = pfi.contents

        font = self.fonts[fi.font]
        text = fi.text.decode('utf8').encode('cp1250')
        w, h, d, e = self.dc.GetFullTextExtent(text, font)
        fi.width = w

    def drawText(self, argp):
        pfi = cast(argp, POINTER(DrawText))
        fi = pfi.contents

        font = self.fonts[fi.font]
        text = fi.text.decode('utf8')
        color = self.GetColourFromRGBA(fi.color)
        x = fi.x
        y = fi.y

        self.dc.SetFont(font)
        self.dc.SetTextForeground(color)
        self.dc.DrawText(text, x, y)

    def drawBackground(self, argp):
        pfi = cast(argp, POINTER(DrawBackground))
        fi = pfi.contents

        x = fi.x
        y = fi.y
        w = fi.w
        h = fi.h
        color = self.GetColourFromRGBA(fi.color)
        pt = [
            (x, y), (x+w, y), (x+w, y+h), (x, y+h), (x, y)
        ]
        self.dc.SetBrush(wx.Brush(color))
        self.dc.DrawPolygon(pt)
        self.dc.SetBrush(wx.NullBrush)

    def drawMarker(self, argp):
        pfi = cast(argp, POINTER(DrawMarker))
        fi = pfi.contents

        x = fi.x
        y = fi.y
        w = fi.w
        h = fi.h
        mt = fi.mt
        color = self.GetColourFromRGBA(fi.color)
        print('drawMarker', x, y, w, h)

    def pt2px(self, argp):
        pfi = cast(argp, POINTER(PT2PX))
        fi = pfi.contents

        pt = fi.pt
        fi.pt = int(pt * self.ppi[1] / 72)

    def drawBorders(self, argp):
        pfi = cast(argp, POINTER(DrawBorders))
        fi = pfi.contents

        left = fi.left
        right = fi.right
        top = fi.top
        bottom = fi.bottom
        colorLeft = self.GetColourFromRGBA(fi.colorLeft)
        colorRight = self.GetColourFromRGBA(fi.colorRight)
        colorTop = self.GetColourFromRGBA(fi.colorTop)
        colorBottom = self.GetColourFromRGBA(fi.colorBottom)
        widthLeft = fi.widthLeft
        widthRight = fi.widthRight
        widthTop = fi.widthTop
        widthBottom = fi.widthBottom

        self.dc.SetPen(wx.Pen(colorLeft, widthLeft))
        self.dc.DrawLine(left, top, left, bottom)
        self.dc.SetPen(wx.Pen(colorTop, widthTop))
        self.dc.DrawLine(left, top, right, top)
        self.dc.SetPen(wx.Pen(colorRight, widthRight))
        self.dc.DrawLine(right, top, right, bottom)
        self.dc.SetPen(wx.Pen(colorBottom, widthBottom))
        self.dc.DrawLine(left, bottom, right, bottom)

    def clientRect(self, argp):
        pfi = cast(argp, POINTER(ClientRect))
        fi = pfi.contents
        fi.x = 0
        fi.y = 0
        fi.width = self.width
        fi.height = self.height

    def render(self, fname, resize=False):
        self.reset()
        html = open(fname, 'rb').read()
        self.pylib.document_create(self.pyclass, html)
        fi = DocumentRender()
        self.pylib.document_render(self.pyclass, self.width, byref(fi))
        if resize and fi.height > self.height:
            #print('render:', fi.width, fi.height)
            self.height = fi.height
            self.reset()
            self.pylib.document_render(self.pyclass, self.width, byref(fi))
        self.pylib.document_draw(self.pyclass, 0, 0, 0, 0, self.width, self.height)
        #bmp = self.dc.GetSelectedBitmap()
        self.bmp.SaveFile(fname+'.png', wx.BITMAP_TYPE_PNG)
