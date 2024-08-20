import logging
from . import litehtmlpy

logger = logging.getLogger(__name__)

class document_container(litehtmlpy.document_container):
    def __init__(self):
        #super().__init__()
        litehtmlpy.document_container.__init__(self)
        self.hfont = 0
        self.fonts = {}
        v = 3.96 * 96 / 72
        self.size = [int(210 * v), int(297 * v)]
        self.ppi = (96, 96)
        self.clips = []

    def create_font(self, face, size, weight, italic, decoration):
        logger.debug('create_font(%s, %s, %d, %d, %d)', face, size, weight, italic, decoration)
        self.hfont += 1
        self.fonts[self.hfont] = None
        return [self.hfont, 15, 4, 19, 19]

    def delete_font(self, hFont):
        logger.debug('delete_font(%d)', hFont)
        del self.fonts[hFont]

    def text_width(self, text, hFont):
        logger.debug('text_width(%s, %s)', text, hFont)
        return len(text)*12

    def draw_text(self, hdc, text, hFont, color, pos):
        logger.debug('draw_text(%d, %s, %d, %s, %s)', hdc, text, hFont, color, pos)

    def pt_to_px(self, pt):
        logger.debug('pt_to_px(%d)', pt)
        pt = int(pt * self.ppi[1] / 72)
        return pt

    def get_default_font_size(self):
        return 12

    def get_default_font_name(self):
        return 'Times New Roman'

    def draw_list_marker(self, hdc, marker):
        logger.debug('draw_list_marker(%d, %s)', hdc, marker)

    def load_image(self, src, baseurl, redraw_on_ready):
        logger.debug('load_image(%s, %s, %s)', src, baseurl, redraw_on_ready)

    def get_image_size(self, src, baseurl, size):
        logger.debug('get_image_size(%s, %s)', src, baseurl)
        size.width = 0
        size.height = 0

    def draw_image(self, hdc, layer, url, base_url):
        logger.debug('draw_image(%d, %s, %s, %s)', hdc, layer, url, base_url)

    def draw_solid_fill(self, hdc, layer, color):
        logger.debug('draw_solid_fill(%d, %s, %s)', hdc, layer, color)

    def draw_linear_gradient(self, hdc, layer, gradient):
        logger.debug('draw_linear_gradient(%d, %s, %s)', hdc, layer, gradient)

    def draw_radial_gradient(self, hdc, layer, gradient):
        logger.debug('draw_radial_gradient(%d, %s, %s)', hdc, layer, gradient)

    def draw_conic_gradient(self, hdc, layer, gradient):
        logger.debug('draw_conic_gradient(%d, %s, %s)', hdc, layer, gradient)

    def draw_borders(self, hdc, borders, draw_pos, root):
        logger.debug('draw_borders(%d, %s, %s, %s)', hdc, borders, draw_pos, root)

    def set_caption(self, caption):
        logger.debug('set_caption(%s)', caption)

    def set_base_url(self, url):
        logger.debug('set_base_url(%s)', url)

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
        self.clips.push((pos, radius))

    def del_clip(self):
        logger.debug('del_clip()')
        if self.clips:
            self.clips.pop()

    def get_client_rect(self, client):
        logger.debug('get_client_rect(%s, %s, %s, %s)', client.x, client.y, client.width, client.height)
        client.clear()
        client.width = self.size[0]
        client.height = self.size[1]

    #element::ptr create_element( const char* tag_name, const string_map& attributes, const std::shared_ptr<document>& doc) override 

    def get_media_features(self):
        logger.debug('get_media_features()')
        return (
            2, # media_type_screen
            self.size[0],
            self.size[1],
            1024, # device width (screen width)
            800, # device height (screen height)
            8, # color
            0, # monochrome
            0, # color index
            96, # resolution
        )

    def get_language(self):
        logger.debug('get_language()')
        return ('en', '')
