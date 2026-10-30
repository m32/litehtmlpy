#!/usr/bin/env vpython3
import logging
import math
import os
import urllib.parse
import wx
from . import litehtmlpy

logger = logging.getLogger(__name__)

TEXT_DECORATION_UNDERLINE = int(litehtmlpy.text_decoration_line_underline)
TEXT_DECORATION_OVERLINE = int(litehtmlpy.text_decoration_line_overline)
TEXT_DECORATION_LINE_THROUGH = int(litehtmlpy.text_decoration_line_line_through)

def wx_colour(color):
    return wx.Colour(color.red, color.green, color.blue, color.alpha)

def rect_of(pos):
    return (pos.x.value, pos.y.value, pos.width.value, pos.height.value)

def add_rounded_rect(path, rect, r):
    # r is border_radiuses; corners are quarter ellipses approximated by bezier curves
    x, y, w, h = rect
    tlx, tly = r.top_left_x.value, r.top_left_y.value
    trx, try_ = r.top_right_x.value, r.top_right_y.value
    brx, bry = r.bottom_right_x.value, r.bottom_right_y.value
    blx, bly = r.bottom_left_x.value, r.bottom_left_y.value
    k = 1 - 0.5523
    path.MoveToPoint(x + tlx, y)
    path.AddLineToPoint(x + w - trx, y)
    path.AddCurveToPoint(x + w - trx * k, y, x + w, y + try_ * k, x + w, y + try_)
    path.AddLineToPoint(x + w, y + h - bry)
    path.AddCurveToPoint(x + w, y + h - bry * k, x + w - brx * k, y + h, x + w - brx, y + h)
    path.AddLineToPoint(x + blx, y + h)
    path.AddCurveToPoint(x + blx * k, y + h, x, y + h - bly * k, x, y + h - bly)
    path.AddLineToPoint(x, y + tly)
    path.AddCurveToPoint(x, y + tly * k, x + tlx * k, y, x + tlx, y)
    path.CloseSubpath()

def gradient_stops(points):
    stops = wx.GraphicsGradientStops(wx_colour(points[0].color), wx_colour(points[-1].color))
    for cp in points:
        stops.Add(wx_colour(cp.color), min(max(cp.offset, 0.0), 1.0))
    return stops

def gradient_colour_at(points, offset):
    if offset <= points[0].offset:
        return wx_colour(points[0].color)
    for a, b in zip(points, points[1:]):
        if offset <= b.offset:
            t = 0 if b.offset == a.offset else (offset - a.offset) / (b.offset - a.offset)
            ca, cb = a.color, b.color
            return wx.Colour(*(int(round(u + (v - u) * t)) for u, v in (
                (ca.red, cb.red), (ca.green, cb.green), (ca.blue, cb.blue), (ca.alpha, cb.alpha))))
    return wx_colour(points[-1].color)

class document_container(litehtmlpy.document_container):
    def __init__(self, parent=None):
        #super().__init__()
        litehtmlpy.document_container.__init__(self)
        self.parent = parent
        self.hfont = 0
        self.fonts = {}
        v = 3.96 * 96 / 72
        self.size = litehtmlpy.size(int(210 * v), int(297 * v))
        self.clips = []
        self.dc = None
        self.images = {}
        self.overline_fonts = set()
        self.base_url = ''

    def SetDC(self, dc):
        if dc is None:
            if isinstance(self.dc, wx.MemoryDC):
                self.dc.SelectObject(wx.NullBitmap)
            self.dc.SetBackground(wx.NullBrush)
            self.dc = None
            return
        self.dc = dc
        # only memory dc needs its own bitmap, printer dc draws on the page
        if isinstance(dc, wx.MemoryDC):
            self.bmp = wx.Bitmap(int(self.size.width.value), int(self.size.height.value), 32)
            self.dc.SelectObject(self.bmp)
        self.dc.SetBackground(wx.Brush(wx.WHITE))
        self.dc.Clear()
        self.ppi = self.dc.GetPPI()
        self.px_per_pt = self.measure_px_per_pt()

    def measure_px_per_pt(self):
        # device pixels per font point; GetPPI() is not reliable for that
        # (wxGTK printer dc), so compare with a screen memory dc (ppi/72)
        font = wx.Font(wx.FontInfo(100))
        self.dc.SetFont(font)
        height = self.dc.GetFontMetrics().height
        ref = wx.MemoryDC(wx.Bitmap(1, 1))
        ref.SetFont(font)
        return height / ref.GetFontMetrics().height * ref.GetPPI()[1] / 72.0

    def reset(self):
        self.SetDC(wx.MemoryDC())

    def create_font(self, descr):
        face = descr.family
        size = int(descr.size.value)
        weight = descr.weight
        italic = descr.style == litehtmlpy.font_style_italic
        decoration = int(descr.decoration_line)
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
            
        underline = bool(decoration & TEXT_DECORATION_UNDERLINE)
        font = wx.Font(size, wx.FONTFAMILY_DEFAULT, style, weight, underline, face)
        if decoration & TEXT_DECORATION_LINE_THROUGH:
            font.SetStrikethrough(True)
        # css px is em-size; font point size is em-size too, so convert px -> pt
        font.SetFractionalPointSize(descr.size.value / self.px_per_pt)
        self.hfont += 1
        self.fonts[self.hfont] = font
        if decoration & TEXT_DECORATION_OVERLINE:
            # wx fonts have no overline, draw_text draws it
            self.overline_fonts.add(self.hfont)
        self.dc.SetFont(font)
        fm = self.dc.GetFontMetrics()
        result = [
            self.hfont,
            size,      # font size
            fm.height, # height
            fm.ascent, # ascent
            fm.descent,# descent
            fm.ascent // 2,          # x height (approximation)
            self.dc.GetTextExtent('0')[0],  # 0 width
        ]
        return result

    def delete_font(self, hFont):
        logger.debug('delete_font(%d)', hFont)
        del self.fonts[hFont]
        self.overline_fonts.discard(hFont)

    def text_width(self, text, hFont):
        logger.debug('text_width(%s, %s)', text, hFont)
        font = self.fonts[hFont]
        width = self.dc.GetFullTextExtent(text, font)[0]
        return litehtmlpy.pixel_float_t(width)

    def draw_text(self, hdc, text, hFont, color, pos):
        logger.debug('draw_text(%d, %s, %d, %s, %s)', hdc, text, hFont, color, (pos.x, pos.y, pos.width, pos.height))
        font = self.fonts[hFont]
        color = wx.Colour(color.red, color.green, color.blue, color.alpha)
        self.dc.SetTextForeground(color)
        self.dc.SetFont(font)
        self.dc.DrawText(text, int(pos.x.value), int(pos.y.value))
        if hFont in self.overline_fonts:
            x, y, w, h = rect_of(pos)
            self.dc.SetPen(wx.Pen(color, max(1, int(h) // 14)))
            self.dc.DrawLine(int(x), int(y), int(x + w), int(y))

    def pt_to_px(self, pt):
        logger.debug('pt_to_px(%s)', pt)
        pt = int(pt * self.ppi[1] / 72.0)
        return litehtmlpy.pixel_float_t(pt)

    def get_default_font_size(self):
        logger.debug('get_default_font_size()')
        return litehtmlpy.pixel_float_t(12)

    def get_default_font_name(self):
        logger.debug('get_default_font_name()')
        return 'Times New Roman'

    def draw_list_marker(self, hdc, marker):
        logger.debug('draw_list_marker(%d, %s)', hdc, marker)
        gc = self.create_gc()
        if marker.image:
            img = self.get_image(marker.image, marker.baseurl)
            if img is not None:
                gc.DrawBitmap(wx.Bitmap(img), marker.pos.x.value, marker.pos.y.value, img.Width, img.Height)
            return
        x, y, w, h = rect_of(marker.pos)
        colour = wx_colour(marker.color)
        if marker.marker_type == litehtmlpy.list_style_type_circle:
            gc.SetPen(wx.Pen(colour, 1))
            gc.SetBrush(wx.TRANSPARENT_BRUSH)
            gc.DrawEllipse(x, y, w, h)
        elif marker.marker_type == litehtmlpy.list_style_type_disc:
            gc.SetPen(wx.TRANSPARENT_PEN)
            gc.SetBrush(wx.Brush(colour))
            gc.DrawEllipse(x, y, w, h)
        elif marker.marker_type == litehtmlpy.list_style_type_square:
            gc.SetPen(wx.TRANSPARENT_PEN)
            gc.SetBrush(wx.Brush(colour))
            gc.DrawRectangle(x, y, w, h)

    def image_url(self, src, baseurl):
        return urllib.parse.urljoin(baseurl or self.base_url, src)

    def load_image(self, src, baseurl, redraw_on_ready):
        logger.debug('load_image(%s, %s, %s)', src, baseurl, redraw_on_ready)
        if self.parent is not None:
            self.parent.HtmlLoadImage(src, baseurl, redraw_on_ready)
            return
        # without parent only local files are supported
        url = self.image_url(src, baseurl)
        path = urllib.parse.urlparse(url).path if url.startswith('file:') else url
        if url not in self.images and os.path.isfile(path):
            img = wx.Image(path)
            if img.IsOk():
                self.images[url] = img

    def get_image(self, src, baseurl):
        if self.parent is not None:
            return self.parent.HtmlGetImage(src, baseurl)
        return self.images.get(self.image_url(src, baseurl))

    def get_image_size(self, src, baseurl, size):
        logger.debug('get_image_size(%s, %s)', src, baseurl)
        img = self.get_image(src, baseurl)
        if img is None:
            size.width.value = 0
            size.height.value = 0
        else:
            sz = img.GetSize()
            size.width.value = sz[0]
            size.height.value = sz[1]

    def create_gc(self):
        # graphics context (antialiasing, gradients) with active clips applied;
        # it draws on the dc when released
        gc = wx.GraphicsContext.Create(self.dc)
        for rect in self.clips:
            gc.Clip(*rect)
        return gc

    def create_layer_gc(self, layer):
        # gc clipped to the background layer and the path of its rounded border box
        gc = self.create_gc()
        gc.Clip(*rect_of(layer.clip_box))
        path = gc.CreatePath()
        add_rounded_rect(path, rect_of(layer.border_box), layer.border_radius)
        return gc, path

    def layer_tiles(self, layer, tile_w, tile_h):
        # top-left corners of background tiles covering the clip box
        if tile_w <= 0 or tile_h <= 0:
            return []
        ox, oy = layer.origin_box.x.value, layer.origin_box.y.value
        cx, cy, cw, ch = rect_of(layer.clip_box)
        xs = [ox]
        ys = [oy]
        if layer.repeat in (litehtmlpy.background_repeat_repeat, litehtmlpy.background_repeat_repeat_x):
            x0 = ox - math.ceil((ox - cx) / tile_w) * tile_w
            xs = [x0 + i * tile_w for i in range(math.ceil((cx + cw - x0) / tile_w))]
        if layer.repeat in (litehtmlpy.background_repeat_repeat, litehtmlpy.background_repeat_repeat_y):
            y0 = oy - math.ceil((oy - cy) / tile_h) * tile_h
            ys = [y0 + i * tile_h for i in range(math.ceil((cy + ch - y0) / tile_h))]
        return [(x, y) for y in ys for x in xs]

    def draw_image(self, hdc, layer, url, base_url):
        logger.debug('draw_image(%d, %s, %s, %s)', hdc, layer, url, base_url)
        img = self.get_image(url, base_url)
        if img is None:
            return
        w = int(round(layer.origin_box.width.value))
        h = int(round(layer.origin_box.height.value))
        if w <= 0 or h <= 0:
            return
        if img.GetSize() != (w, h):
            img = img.Scale(w, h, wx.IMAGE_QUALITY_HIGH)
        bmp = wx.Bitmap(img)
        gc, path = self.create_layer_gc(layer)
        gc.Clip(*rect_of(layer.border_box))
        for x, y in self.layer_tiles(layer, w, h):
            gc.DrawBitmap(bmp, x, y, w, h)

    def draw_solid_fill(self, hdc, layer, color):
        logger.debug('draw_solid_fill(%d, %s, %s)', hdc, layer, color)
        if color.alpha == 0:
            return
        gc, path = self.create_layer_gc(layer)
        gc.SetPen(wx.TRANSPARENT_PEN)
        gc.SetBrush(wx.Brush(wx_colour(color)))
        gc.FillPath(path)

    def fill_gradient(self, layer, make_brush):
        # make_brush(gc, dx, dy) creates the brush for the tile moved by (dx, dy) from the origin box
        ow, oh = layer.origin_box.width.value, layer.origin_box.height.value
        gc, path = self.create_layer_gc(layer)
        for x, y in self.layer_tiles(layer, ow, oh):
            gc.PushState()
            gc.Clip(x, y, ow, oh)
            gc.SetBrush(make_brush(gc, x - layer.origin_box.x.value, y - layer.origin_box.y.value))
            gc.FillPath(path)
            gc.PopState()

    def draw_linear_gradient(self, hdc, layer, gradient):
        logger.debug('draw_linear_gradient(%d, %s, %s)', hdc, layer, gradient)
        points = list(gradient.color_points)
        if not points:
            return
        stops = gradient_stops(points)
        def brush(gc, dx, dy):
            return gc.CreateLinearGradientBrush(
                gradient.start.x + dx, gradient.start.y + dy,
                gradient.end.x + dx, gradient.end.y + dy, stops)
        self.fill_gradient(layer, brush)

    def draw_radial_gradient(self, hdc, layer, gradient):
        logger.debug('draw_radial_gradient(%d, %s, %s)', hdc, layer, gradient)
        points = list(gradient.color_points)
        rx, ry = gradient.radius.x, gradient.radius.y
        if not points or rx <= 0 or ry <= 0:
            return
        stops = gradient_stops(points)
        def brush(gc, dx, dy):
            cx, cy = gradient.position.x + dx, gradient.position.y + dy
            # ellipse: circle of radius rx scaled vertically by ry / rx around the center
            matrix = gc.CreateMatrix()
            matrix.Translate(cx, cy)
            matrix.Scale(1.0, ry / rx)
            matrix.Translate(-cx, -cy)
            return gc.CreateRadialGradientBrush(cx, cy, cx, cy, rx, stops, matrix)
        self.fill_gradient(layer, brush)

    def draw_conic_gradient(self, hdc, layer, gradient):
        logger.debug('draw_conic_gradient(%d, %s, %s)', hdc, layer, gradient)
        points = list(gradient.color_points)
        if not points:
            return
        # wx has no conic brush: draw a fan of one degree wedges
        ow, oh = layer.origin_box.width.value, layer.origin_box.height.value
        radius = gradient.radius or math.hypot(ow, oh)
        gc, path = self.create_layer_gc(layer)
        gc.Clip(*rect_of(layer.border_box))
        gc.SetPen(wx.TRANSPARENT_PEN)
        # antialiased wedge edges leave visible seams
        gc.SetAntialiasMode(wx.ANTIALIAS_NONE)
        steps = 360
        for x, y in self.layer_tiles(layer, ow, oh):
            cx = gradient.position.x + x - layer.origin_box.x.value
            cy = gradient.position.y + y - layer.origin_box.y.value
            gc.PushState()
            gc.Clip(x, y, ow, oh)
            for i in range(steps):
                # 0 deg is at the top, clockwise; wedges overlap a bit to avoid seams
                a0 = math.radians(gradient.angle + i * 360.0 / steps) - math.pi / 2
                a1 = math.radians(gradient.angle + (i + 1.5) * 360.0 / steps) - math.pi / 2
                gc.SetBrush(wx.Brush(gradient_colour_at(points, (i + 0.5) / steps)))
                wedge = gc.CreatePath()
                wedge.MoveToPoint(cx, cy)
                wedge.AddLineToPoint(cx + radius * math.cos(a0), cy + radius * math.sin(a0))
                wedge.AddLineToPoint(cx + radius * math.cos(a1), cy + radius * math.sin(a1))
                wedge.CloseSubpath()
                gc.FillPath(wedge)
            gc.PopState()

    def draw_borders(self, hdc, borders, draw_pos, root):
        logger.debug('draw_borders(%d, %s, %s, %s)', hdc, borders, draw_pos, root)
        left = int(draw_pos.x.value)
        top = int(draw_pos.y.value)
        right = int(left + draw_pos.width.value)
        bottom = int(top + draw_pos.height.value)

        b = borders.left
        colorLeft = wx.Colour(b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthLeft = int(b.width.value)

        b = borders.top
        colorTop = wx.Colour(b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthTop = int(b.width.value)

        b = borders.right
        colorRight = wx.Colour(b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthRight = int(b.width.value)

        b = borders.bottom
        colorBottom = wx.Colour(b.color.red, b.color.green, b.color.blue, b.color.alpha)
        widthBottom = int(b.width.value)

        self.dc.SetPen(wx.Pen(colorLeft, widthLeft))
        self.dc.DrawLine(left, top, left, bottom)
        self.dc.SetPen(wx.Pen(colorTop, widthTop))
        self.dc.DrawLine(left, top, right, top)
        self.dc.SetPen(wx.Pen(colorRight, widthRight))
        self.dc.DrawLine(right, top, right, bottom)
        self.dc.SetPen(wx.Pen(colorBottom, widthBottom))
        self.dc.DrawLine(left, bottom, right, bottom)

    def set_caption(self, caption):
        logger.debug('set_caption(%s)', caption)

    def set_base_url(self, url):
        logger.debug('set_base_url(%s)', url)
        self.base_url = url or ''

    #void    link(const std::shared_ptr<document>& doc, const element::ptr& el) override 

    #void    on_anchor_click(const char* url, const element::ptr& el) override 
    def on_mouse_event(self, el, event):
        logger.debug('on_mouse_event(%s, %s)', el, event)

    def set_cursor(self, cursor):
        logger.debug('set_cursor(%s)', cursor)

    def transform_text(self, text, tt):
         logger.debug('transform_text(%s, %d)', text, tt)

    def import_css(self, text, url, base_url):
        logger.debug('import_css(%s, %s, %s)', text, url, base_url)

    def set_clip(self, pos, radius):
        logger.debug('set_clip(%s, %s)', pos, radius)
        # keep a copy of the box, pos does not outlive the call; rounded corners are ignored
        self.clips.append(rect_of(pos))
        self.apply_dc_clip()

    def del_clip(self):
        logger.debug('del_clip()')
        if self.clips:
            self.clips.pop()
        self.apply_dc_clip()

    def apply_dc_clip(self):
        # text and borders are drawn on the dc directly
        self.dc.DestroyClippingRegion()
        for rect in self.clips:
            # SetClippingRegion intersects with the current region
            self.dc.SetClippingRegion(*(int(round(v)) for v in rect))

    def get_viewport(self, viewport):
        logger.debug('get_viewport()')
        viewport.clear()
        viewport.width.value = int(self.size.width.value)
        viewport.height.value = int(self.size.height.value)

    #element::ptr create_element( const char* tag_name, const string_map& attributes, const std::shared_ptr<document>& doc) override 

    def get_media_features(self):
        logger.debug('get_media_features()')
        return (
            2, # media_type_screen
            self.size.width,
            self.size.width,
            1024, # device width (screen width)
            800, # device height (screen height)
            8, # color
            0, # monochrome
            256, # color index
            96, # resolution
        )

    def get_language(self):
        logger.debug('get_language()')
        return ('en', '')
