#!/usr/bin/env vpython3
import logging
from . import litehtmlpy

logger = logging.getLogger(__name__)

class document_container(litehtmlpy.container_cairo_pango):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        v = 3.96 * 96 / 72
        self.size = [int(210 * v), int(297 * v)]

    def get_screen_dpi(self):
        return 96

    def get_screen_width(self):
        return self.size[0]

    def get_screen_height(self):
        return self.size[1]

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

    def set_caption(self, caption):
        logger.debug('set_caption(%s)', caption)

    def set_base_url(self, url):
        logger.debug('set_base_url(%s)', url)

    #void    link(const std::shared_ptr<document>& doc, const element::ptr& el) override 

    #void    on_anchor_click(const char* url, const element::ptr& el) override 

    def set_cursor(self, cursor):
        logger.debug('set_cursor(%s)', cursor)

    def import_css(self, text, url, base_url):
        logger.debug('import_css(%s, %s, %s)', text, url, base_url)

    def get_client_rect(self, client):
        logger.debug('get_client_rect(%s)'%client)
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
            256, # color index
            96, # resolution
        )

    def get_language(self):
        logger.debug('get_language()')
        return ('en', '')
