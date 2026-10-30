import io
from pathlib import Path

import pytest

from tests.common import DummyContainer, render_html
from litehtmlpy import litehtmlpy


def test_render_from_repo_sample_files():
    repo_root = Path(__file__).resolve().parents[1]
    sample_files = [
        repo_root / "demo.html",
        repo_root / "test-01.html",
        repo_root / "test-02.html",
    ]

    for sample in sample_files:
        html = sample.read_text(encoding="utf-8")
        doc, _ = render_html(html)
        assert doc is not None
        assert doc.width().value > 0
        assert doc.height().value > 0


def test_on_mouse_event_is_emitted_on_hover_and_leave():
    class MouseContainer(DummyContainer):
        def __init__(self):
            super().__init__()
            self.events = []

        def on_mouse_event(self, el, event):
            self.events.append(str(event))

    container = MouseContainer()
    doc = litehtmlpy.fromString(container, '<a href="https://example.com">link</a>', None, None)
    assert doc is not None
    doc.render(container.size.width, litehtmlpy.render_all)
    doc.on_mouse_over(10, 10, 0, 0)
    doc.on_mouse_leave()
    assert any("mouse_event_enter" in event for event in container.events)
    assert any("mouse_event_leave" in event for event in container.events)


@pytest.mark.skipif(not hasattr(litehtmlpy, "container_cairo_pango"), reason="Cairo bindings not enabled")
def test_cairo_container_can_render_png_bytes():
    class CairoContainer(litehtmlpy.container_cairo_pango):
        def __init__(self):
            super().__init__()
            self.set_dpi(96)
            self.size = litehtmlpy.size(320, 200)

        def get_screen_width(self):
            return int(self.size.width.value)

        def get_screen_height(self):
            return int(self.size.height.value)

        def get_viewport(self, viewport):
            viewport.clear()
            viewport.set_size(self.size.width, self.size.height)

        def load_image(self, src, baseurl, redraw_on_ready):
            pass

        def set_caption(self, caption):
            pass

        def set_base_url(self, url):
            pass

        def on_mouse_event(self, el, event):
            pass

        def set_cursor(self, cursor):
            pass

        def import_css(self, text, url, base_url):
            pass

    container = CairoContainer()
    html = """
    <html><body><div style="width: 300px; height: 120px; background: linear-gradient(#fff, #aaa);">Hello</div></body></html>
    """
    doc = container.fromString(html, None, None)
    assert doc is not None
    doc.render(litehtmlpy.pixel_float_t(container.size.width.value), litehtmlpy.render_all)
    hdc = container.surface(int(doc.width().value), int(doc.height().value))
    clip = litehtmlpy.position(0, 0, int(doc.width().value), int(doc.height().value))
    doc.draw(hdc, litehtmlpy.pixel_float_t(0), litehtmlpy.pixel_float_t(0), clip)
    buffer = io.BytesIO()
    rc = container.savestream(buffer.write)
    assert rc == 0
    assert buffer.getbuffer()[:8]


class RecordingContainer(DummyContainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calls = []

    def draw_list_marker(self, hdc, marker):
        self.calls.append(('marker', marker.marker_type))

    def draw_linear_gradient(self, hdc, layer, gradient):
        self.calls.append(('linear', len(gradient.color_points)))

    def draw_radial_gradient(self, hdc, layer, gradient):
        self.calls.append(('radial', gradient.radius.x > 0))

    def draw_conic_gradient(self, hdc, layer, gradient):
        self.calls.append(('conic', len(gradient.color_points)))


def draw_calls(html):
    container = RecordingContainer()
    doc = litehtmlpy.fromString(container, html, None, None)
    doc.render(container.size.width, litehtmlpy.render_all)
    doc.draw(0, litehtmlpy.pixel_float_t(0), litehtmlpy.pixel_float_t(0),
             litehtmlpy.position(0, 0, 800, 1000))
    return container.calls


def test_list_markers_are_passed_to_python():
    calls = draw_calls('<ul><li>a</li><li style="list-style-type: square">b</li></ul>')
    assert calls == [
        ('marker', litehtmlpy.list_style_type_disc),
        ('marker', litehtmlpy.list_style_type_square),
    ]


def test_gradients_are_passed_to_python():
    calls = draw_calls(
        '<div style="height:10px; background: linear-gradient(red, blue)"></div>'
        '<div style="height:10px; background: radial-gradient(red, blue)"></div>'
        '<div style="height:10px; background: conic-gradient(red, lime, blue)"></div>'
    )
    assert calls == [('linear', 2), ('radial', True), ('conic', 3)]


@pytest.mark.parametrize("set_size", ["in_place", "return_tuple"])
def test_get_image_size_is_used_for_layout(set_size):
    class ImageContainer(DummyContainer):
        def get_image_size(self, src, baseurl, size):
            if set_size == "return_tuple":
                return (40, 30)
            size.width.value = 40
            size.height.value = 30

    container = ImageContainer()
    doc = litehtmlpy.fromString(container, '<div style="display:inline-block"><img src="x.png"></div>', None, None)
    doc.render(container.size.width, litehtmlpy.render_all)
    assert doc.height().value >= 30
