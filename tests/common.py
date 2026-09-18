import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from litehtmlpy import litehtml, litehtmlpy


class DummyContainer(litehtml.document_container):
    def __init__(self, width=800, height=1200):
        super().__init__()
        self.size = litehtmlpy.size(width, height)
        self._font_id = 0

    def create_font(self, descr):
        self._font_id += 1
        return [self._font_id, 15, 4, 19, 19]

    def delete_font(self, hFont):
        pass

    def text_width(self, text, hFont):
        return litehtmlpy.pixel_float_t(len(text) * 12)

    def draw_text(self, hdc, text, hFont, color, pos):
        pass

    def pt_to_px(self, pt):
        return litehtmlpy.pixel_float_t(float(pt))

    def get_default_font_size(self):
        return litehtmlpy.pixel_float_t(12)

    def get_default_font_name(self):
        return "sans-serif"

    def draw_list_marker(self, hdc, marker):
        pass

    def load_image(self, src, baseurl, redraw_on_ready):
        pass

    def get_image_size(self, src, baseurl, size):
        size.width.value = 0
        size.height.value = 0

    def draw_image(self, hdc, layer, url, base_url):
        pass

    def draw_solid_fill(self, hdc, layer, color):
        pass

    def draw_linear_gradient(self, hdc, layer, gradient):
        pass

    def draw_radial_gradient(self, hdc, layer, gradient):
        pass

    def draw_conic_gradient(self, hdc, layer, gradient):
        pass

    def draw_borders(self, hdc, borders, draw_pos, root):
        pass

    def set_caption(self, caption):
        pass

    def set_base_url(self, url):
        pass

    def on_mouse_event(self, el, event):
        pass

    def set_cursor(self, cursor):
        pass

    def transform_text(self, text, tt):
        pass

    def import_css(self, text, url, base_url):
        pass

    def set_clip(self, pos, radius):
        pass

    def del_clip(self):
        pass

    def get_viewport(self, viewport):
        viewport.clear()
        viewport.set_size(self.size.width, self.size.height)

    def get_media_features(self):
        return (
            2,
            int(self.size.width.value),
            int(self.size.height.value),
            1024,
            768,
            8,
            0,
            0,
            96,
        )


def render_html(html, width=800, height=1200):
    container = DummyContainer(width=width, height=height)
    doc = litehtmlpy.fromString(container, html, None, None)
    assert doc is not None
    doc.render(container.size.width, litehtmlpy.render_all)
    return doc, container
