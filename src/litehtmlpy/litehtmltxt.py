#!/usr/bin/env vpython3
import logging
from . import litehtmlpy

#logger = logging.getLogger(__name__)
logger = None

class Font:
    def __init__(self, face, size, weight, style):
        self.face = face
        self.size = size
        self.weight = weight
        self.style = style

class DC:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = None
        self.colour = None
        self._lines = {}

    def lines(self):
        return sorted(self._lines.keys())

    def line(self, ly):
        try:
            rec = self._lines[ly]
        except KeyError:
            return ''
        rec = sorted(rec)
        line = [' ']*rec[-1][0][0]
        line.extend([' ']*len(rec[-1][1]))
        for (x, y), txt in rec:
            for i in range(len(txt)):
                line[x+i] = txt[i]
        return ''.join(line)

    def SetFont(self, font):
        self.font = font

    def GetFontMetrics(self):
        class FontMetrics:
            ascent = 1
            descent = 1
            height = 10
        fm = FontMetrics()
        fm.height = 10
        return fm

    def GetFullTextExtent(self, text, font):
        return len(text), 10

    def SetTextBackground(self, colour):
        self.colour = colour

    def DrawText(self, text, x, y):
        key = (x,y)
        try:
            rec = self._lines[y]
        except KeyError:
            rec = []
            self._lines[y] = rec
        rec.append((key, text))

    def SetPen(self, color, width):
        pass

    def DrawLine(self, left, top, right, bottom):
        pass

class document_container(litehtmlpy.document_container):
    def __init__(self, parent=None):
        #super().__init__()
        litehtmlpy.document_container.__init__(self)
        self.parent = parent
        self.hfont = 0
        self.fonts = {}
        self.size = [80, 250]
        self.clips = []
        self.reset()

    def SetDC(self, dc):
        self.dc = dc

    def reset(self):
        self.dc = DC(self.size[0], self.size[1])

    def create_font(self, descr):
        face = descr.family
        size = descr.size
        weight = descr.weight
        style = descr.style
        font = Font(face, size, weight, style)
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
        self.dc.SetTextBackground((color.red, color.green, color.blue, color.alpha))
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
        colorLeft = (b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthLeft = int(b.width)

        b = borders.top
        colorTop = (b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthTop = int(b.width)

        b = borders.right
        colorRight = (b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthRight = int(b.width)

        b = borders.bottom
        colorBottom = (b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthBottom = int(b.width)

        self.dc.SetPen(colorLeft, widthLeft)
        self.dc.DrawLine(left, top, left, bottom)
        self.dc.SetPen(colorTop, widthTop)
        self.dc.DrawLine(left, top, right, top)
        self.dc.SetPen(colorRight, widthRight)
        self.dc.DrawLine(right, top, right, bottom)
        self.dc.SetPen(colorBottom, widthBottom)
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
