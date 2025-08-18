#!/usr/bin/env vpython3
import logging
import wx
from . import litehtmlpy

#logger = logging.getLogger(__name__)
logger = None

class document_container(litehtmlpy.document_container):
    def __init__(self, parent=None):
        #super().__init__()
        litehtmlpy.document_container.__init__(self)
        self.parent = parent
        self.hfont = 0
        self.fonts = {}
        v = 3.96 * 96 / 72
        self.size = [int(210 * v), int(297 * v)]
        self.clips = []
        self.dc = None

    def SetDC(self, dc):
        self.dc = dc

    def reset(self):
        self.bmp = wx.Bitmap(self.size[0], self.size[1], 32)
        self.dc = wx.MemoryDC()
        self.dc.SelectObject(self.bmp)
        self.dc.SetBackground(wx.Brush(wx.WHITE))
        self.dc.Clear()
        self.ppi = self.dc.GetPPI()

    def create_font(self, descr):
        face = descr.family
        size = descr.size
        weight = descr.weight
        italic = descr.style == litehtmlpy.font_style_italic
        #decoration = descr.decoration_style
        decoration = 0
        #logger.debug('create_font(%s)', face, size, weight, italic, decoration)
        if not face:
            face = 'Times New Roman'
        else:
            face = face.split(',')[0].strip()
            if face[0] == '"':
                face = face.split('"')[1]
            elif face[0] == "'":
                face = face.split("'")[1]
        if italic:
            style = wx.FONTSTYLE_ITALIC
        else:
            style = wx.FONTSTYLE_NORMAL
        try:
            wx.FONTWEIGHT_THIN
            weigths = {
                100:wx.FONTWEIGHT_THIN,
                200:wx.FONTWEIGHT_EXTRALIGHT,
                300:wx.FONTWEIGHT_LIGHT,
                400:wx.FONTWEIGHT_NORMAL,
                500:wx.FONTWEIGHT_MEDIUM,
                600:wx.FONTWEIGHT_SEMIBOLD,
                700:wx.FONTWEIGHT_BOLD,
                800:wx.FONTWEIGHT_EXTRABOLD,
                900:wx.FONTWEIGHT_HEAVY,
                1000:wx.FONTWEIGHT_EXTRAHEAVY,
            }
            weight = weigths.get(weight, wx.FONTWEIGHT_NORMAL)
        except AttributeError:
            if weight < 400:
                wight = wx.FONTWEIGHT_LIGHT
            elif weight > 500:
                weight = wx.FONTWEIGHT_BOLD
            else:
                weight = wx.FONTWEIGHT_NORMAL
            
        underline = decoration != 0
        font = wx.Font(int(size), wx.FONTFAMILY_DEFAULT, style, weight, underline, face)
        self.hfont += 1
        self.fonts[self.hfont] = font
        self.dc.SetFont(font)
        fm = self.dc.GetFontMetrics()
        return [
            self.hfont,
            fm.ascent,
            fm.descent,
            fm.height,
            fm.height,
        ]

    def delete_font(self, hFont):
        if logger:
            logger.debug('delete_font(%d)', hFont)
        del self.fonts[hFont]

    def text_width(self, text, hFont):
        if logger:
            logger.debug('text_width(%s, %s)', text, hFont)
        font = self.fonts[hFont]
        width = self.dc.GetFullTextExtent(text, font)[0]
        return width

    def draw_text(self, hdc, text, hFont, color, pos):
        if logger:
            logger.debug('draw_text(%d, %s, %d, %s, %s)', hdc, text, hFont, color, (pos.x, pos.y, pos.width, pos.height))
        font = self.fonts[hFont]
        color = wx.Colour(color.red, color.green, color.blue, color.alpha)
        #self.dc.SetTextForeground(color)
        self.dc.SetTextBackground(color)
        self.dc.SetFont(font)
        self.dc.DrawText(text, int(pos.x), int(pos.y))

    def pt_to_px(self, pt):
        if logger:
            logger.debug('pt_to_px(%s)', pt)
        pt = int(pt * self.ppi[1] / 72.0)
        return pt

    def get_default_font_size(self):
        if logger:
            logger.debug('get_default_font_size()')
        return 12

    def get_default_font_name(self):
        if logger:
            logger.debug('get_default_font_name()')
        return 'Times New Roman'

    def draw_list_marker(self, hdc, marker):
        if logger:
            logger.debug('draw_list_marker(%d, %s)', hdc, marker)

    def load_image(self, src, baseurl, redraw_on_ready):
        if logger:
            logger.debug('load_image(%s, %s, %s)', src, baseurl, redraw_on_ready)
        if self.parent is not None:
            self.parent.HtmlLoadImage(src, baseurl, redraw_on_ready)

    def get_image_size(self, src, baseurl, size):
        if logger:
            logger.debug('get_image_size(%s, %s)', src, baseurl)
        if self.parent is None:
            size.width = 0
            size.height = 0
        else:
            img = self.parent.HtmlGetImage(src, baseurl)
            if img is None:
                size.width = 0
                size.height = 0
            else:
                sz = img.GetSize()
                size.width = sz[0]
                size.height = sz[1]

    def draw_image(self, hdc, layer, url, base_url):
        if logger:
            logger.debug('draw_image(%d, %s, %s, %s)', hdc, layer, url, base_url)

    def draw_solid_fill(self, hdc, layer, color):
        if logger:
            logger.debug('draw_solid_fill(%d, %s, %s)', hdc, layer, color)

    def draw_linear_gradient(self, hdc, layer, gradient):
        if logger:
            logger.debug('draw_linear_gradient(%d, %s, %s)', hdc, layer, gradient)

    def draw_radial_gradient(self, hdc, layer, gradient):
        if logger:
            logger.debug('draw_radial_gradient(%d, %s, %s)', hdc, layer, gradient)

    def draw_conic_gradient(self, hdc, layer, gradient):
        if logger:
            logger.debug('draw_conic_gradient(%d, %s, %s)', hdc, layer, gradient)

    def draw_borders(self, hdc, borders, draw_pos, root):
        if logger:
            logger.debug('draw_borders(%d, %s, %s, %s)', hdc, borders, draw_pos, root)
        left = int(draw_pos.x)
        top = int(draw_pos.y)
        right = int(left + draw_pos.width)
        bottom = int(top + draw_pos.height)

        b = borders.left
        colorLeft = wx.Colour(b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthLeft = int(b.width)

        b = borders.top
        colorTop = wx.Colour(b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthTop = int(b.width)

        b = borders.right
        colorRight = wx.Colour(b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthRight = int(b.width)

        b = borders.bottom
        colorBottom = wx.Colour(b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthBottom = int(b.width)

        self.dc.SetPen(wx.Pen(colorLeft, widthLeft))
        self.dc.DrawLine(left, top, left, bottom)
        self.dc.SetPen(wx.Pen(colorTop, widthTop))
        self.dc.DrawLine(left, top, right, top)
        self.dc.SetPen(wx.Pen(colorRight, widthRight))
        self.dc.DrawLine(right, top, right, bottom)
        self.dc.SetPen(wx.Pen(colorBottom, widthBottom))
        self.dc.DrawLine(left, bottom, right, bottom)

    def set_caption(self, caption):
        if logger:
            logger.debug('set_caption(%s)', caption)

    def set_base_url(self, url):
        if logger:
            logger.debug('set_base_url(%s)', url)

    #void    link(const std::shared_ptr<document>& doc, const element::ptr& el) override 

    #void    on_anchor_click(const char* url, const element::ptr& el) override 
    def on_mouse_event(self, el, event):
        if logger:
            logger.debug('on_mouse_event(%s, %s)', el, event)

    def set_cursor(self, cursor):
        if logger:
            logger.debug('set_cursor(%s)', cursor)

    def transform_text(self, text, tt):
        if logger:
            logger.debug('transform_text(%s, %d)', text, tt)

    def import_css(self, text, url, base_url):
        if logger:
            logger.debug('import_css(%s, %s, %s)', text, url, base_url)

    def set_clip(self, pos, radius):
        if logger:
            logger.debug('set_clip(%s, %s)', pos, radius)
        self.clips.append((pos, radius))

    def del_clip(self):
        if logger:
            logger.debug('del_clip()')
        if self.clips:
            self.clips.pop()

    def get_viewport(self, viewport):
        if logger:
            logger.debug('get_viewport()')
        viewport.clear()
        viewport.width = int(self.size[0])
        viewport.height = int(self.size[1])

    #element::ptr create_element( const char* tag_name, const string_map& attributes, const std::shared_ptr<document>& doc) override 

    def get_media_features(self):
        if logger:
            logger.debug('get_media_features()')
        return (
            2, # media_type_screen
            self.size[0],
            self.size[1],
            1024, # device width (screen width)
            800, # device height (screen height)
            8, # color
            0, # monochrome
            256, # color index
            96, # resolution
        )

    def get_language(self):
        if logger:
            logger.debug('get_language()')
        return ('en', '')
