#!/usr/bin/env vpython3
import logging
from . import litehtmlpy

logger = logging.getLogger(__name__)

class document_container(litehtmlpy.container_cairo_pango):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        v = 3.96 * 96 / 72
        self.set_dpi(96)
        self.size = [int(210 * v), int(297 * v)]

    def get_screen_width(self):
        return self.size[0]

    def get_screen_height(self):
        return self.size[1]

    def load_image(self, src, baseurl, redraw_on_ready):
        logger.debug('load_image(%s, %s, %s)', src, baseurl, redraw_on_ready)
        if self.parent is not None:
            self.parent.HtmlLoadImage(self, src, baseurl, redraw_on_ready)

    def set_caption(self, caption):
        logger.debug('set_caption(%s)', caption)

    def set_base_url(self, url):
        logger.debug('set_base_url(%s)', url)

    ##void    link(const std::shared_ptr<document>& doc, const element::ptr& el) override 

    #void    on_anchor_click(const char* url, const element::ptr& el) override 

    def set_cursor(self, cursor):
        logger.debug('set_cursor(%s)', cursor)

    def import_css(self, text, url, base_url):
        logger.debug('import_css(%s, %s, %s)', text, url, base_url)

    def get_client_rect(self, client):
        #logger.debug('get_client_rect(%s)'%client)
        client.clear()
        client.width = self.size[0]
        client.height = self.size[1]
