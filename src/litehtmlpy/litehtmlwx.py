#!/usr/bin/env vpython3
import logging
import wx
from . import litehtmlpy

logger = logging.getLogger(__name__)

class document_container(litehtmlpy.document_container):
    def __init__(self, parent=None):
        #super().__init__()
        litehtmlpy.document_container.__init__(self)
        self.parent = parent
        self.hfont = 0
        self.fonts = {}
        v = 3.96 * 96 / 72
        self.size = [int(210 * v), int(297 * v)]

    def size0(self):
        v = 3.96 * 96 / 72
        self.size = [int(210 * v), int(297 * v)]

    def reset(self):
        self.bmp = wx.Bitmap(self.size[0], self.size[1], 32)
        self.dc = wx.MemoryDC()
        self.dc.SelectObject(self.bmp)
        self.dc.SetBackground(wx.Brush(wx.WHITE))
        self.dc.Clear()
        self.ppi = self.dc.GetPPI()

    def create_font(self, face, size, weight, italic, decoration):
        #logger.debug('create_font(%s, %s, %d, %d, %d)', face, size, weight, italic, decoration)
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
        font = wx.Font(size, wx.FONTFAMILY_DEFAULT, style, weight, underline, face)
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
        #logger.debug('delete_font(%d)', hFont)
        del self.fonts[hFont]

    def text_width(self, text, hFont):
        #logger.debug('text_width(%s, %s)', text, hFont)
        font = self.fonts[hFont]
        width = self.dc.GetFullTextExtent(text, font)[0]
        return width

    def draw_text(self, hdc, text, hFont, color, pos):
        #logger.debug('draw_text(%d, %s, %d, %s, %s)', hdc, text, hFont, color, pos)
        font = self.fonts[hFont]
        color = wx.Colour(color.red, color.green, color.blue, color.alpha)
        self.dc.SetFont(font)
        self.dc.SetTextForeground(color)
        self.dc.DrawText(text, pos.x, pos.y)

    def pt_to_px(self, pt):
        #logger.debug('pt_to_px(%d)', pt)
        pt = int(pt * self.ppi[1] / 72)
        return pt

    def get_default_font_size(self):
        #logger.debug('get_default_font_size()')
        return 12

    def get_default_font_name(self):
        #logger.debug('get_default_font_name()')
        return 'Times New Roman'

    def draw_list_marker(self, hdc, marker):
        #logger.debug('draw_list_marker(%d, %s)', hdc, marker)
        pass

    def load_image(self, src, baseurl, redraw_on_ready):
        #logger.debug('load_image(%s, %s, %s)', src, baseurl, redraw_on_ready)
        if self.parent is not None:
            self.parent.HtmlLoadImage(src, baseurl, redraw_on_ready)

    def get_image_size(self, src, baseurl, size):
        #logger.debug('get_image_size(%s, %s)', src, baseurl)
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

    def draw_background(self, hdc, bgs):
        bg = bgs[-1]
		#image, baseurl, attachment, repeat, color, clip_box, origin_box, border_box, border_radius, image_size, position_x, position_y, is_root
        #logger.debug('draw_background(%d, %s)', hdc, bgs)
        x, y, w, h = bg.clip_box.x, bg.clip_box.y, bg.clip_box.width, bg.clip_box.height
        self.dc.SetClippingRegion(x, y, w, h)
        color = wx.Colour(bg.color.red, bg.color.green, bg.color.blue, bg.color.alpha)
        self.dc.SetBrush(wx.Brush(color, style=wx.BRUSHSTYLE_SOLID))
        x, y, w, h = bg.border_box.x, bg.border_box.y, bg.border_box.width, bg.border_box.height
        pt = [
            (x, y), (x+w, y), (x+w, y+h), (x, y+h), (x, y)
        ]
        self.dc.DrawPolygon(pt)
        self.dc.SetBrush(wx.NullBrush)
        self.dc.DestroyClippingRegion()
        for i in range(len(bgs)-1, -1, -1):
            bg = bgs[i]
            if bg.image_size.width == 0 or bg.image_size.height == 0:
                continue
            x, y, w, h = bg.clip_box.x, bg.clip_box.y, bg.clip_box.width, bg.clip_box.height
            self.dc.SetClippingRegion(x, y, w, h)
            img = self.parent.HtmlGetImage(bg.image, bg.baseurl)
            if img is not None:
                if bg.image_size.width != w or bg.image_size.height != h:
                    img = img.Rescale(w, h)
                bmp = wx.Bitmap(img)
                # TODO: repeat image inside box
                self.dc.DrawBitmap(bmp, bg.position_x, bg.position_y)
            self.dc.DestroyClippingRegion()

    def draw_borders(self, hdc, borders, draw_pos, root):
        #logger.debug('draw_borders(%d, %s, %s, %s)', hdc, borders, draw_pos, root)
        left = draw_pos.x
        top = draw_pos.y
        right = left + draw_pos.width
        bottom = top + draw_pos.height

        b = borders.left
        colorLeft = wx.Colour(b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthLeft = b.width

        b = borders.top
        colorTop = wx.Colour(b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthTop = b.width

        b = borders.right
        colorRight = wx.Colour(b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthRight = b.width

        b = borders.bottom
        colorBottom = wx.Colour(b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthBottom = b.width

        self.dc.SetPen(wx.Pen(colorLeft, widthLeft))
        self.dc.DrawLine(left, top, left, bottom)
        self.dc.SetPen(wx.Pen(colorTop, widthTop))
        self.dc.DrawLine(left, top, right, top)
        self.dc.SetPen(wx.Pen(colorRight, widthRight))
        self.dc.DrawLine(right, top, right, bottom)
        self.dc.SetPen(wx.Pen(colorBottom, widthBottom))
        self.dc.DrawLine(left, bottom, right, bottom)

    def set_caption(self, caption):
        #logger.debug('set_caption(%s)', caption)
        pass

    def set_base_url(self, url):
        #logger.debug('set_base_url(%s)', url)
        pass

    #void    link(const std::shared_ptr<document>& doc, const element::ptr& el) override 

    #void    on_anchor_click(const char* url, const element::ptr& el) override 

    def set_cursor(self, cursor):
        #logger.debug('set_cursor(%s)', cursor)
        pass

    def transform_text(self, text, tt):
        #logger.debug('transform_text(%s, %d)', text, tt)
        pass

    def import_css(self, text, url, base_url):
        #logger.debug('import_css(%s, %s, %s)', text, url, base_url)
        pass

    def set_clip(self, pos, radius):
        #logger.debug('set_clip(%s, %s, %d, %d)', pos, radius)
        pass

    def del_clip(self):
        #logger.debug('del_clip()')
        pass

    def get_client_rect(self, client):
        #logger.debug('get_client_rect(%s)'%client)
        client.clear()
        client.width = self.size[0]
        client.height = self.size[1]

    #element::ptr create_element( const char* tag_name, const string_map& attributes, const std::shared_ptr<document>& doc) override 

    def get_media_features(self):
        #logger.debug('get_media_features()')
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
        #logger.debug('get_language()')
        return ('en', '')
