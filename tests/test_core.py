from tests.common import DummyContainer, render_html
from litehtmlpy import litehtmlpy


def test_parse_simple_html_document():
    doc, container = render_html("<html><body><p>Hello</p></body></html>")
    assert doc.width().value > 0
    assert doc.height().value > 0
    assert container.size.width.value > 0


def test_render_css_block_and_inline_examples():
    for html in (
        "<div style='width: 200px; height: 40px'></div>",
        "<p style='margin: 10px'>x</p>",
        "<span style='color: red'>Hello</span>",
        "<div><span>nested</span></div>",
    ):
        doc, _ = render_html(html)
        assert doc is not None
        assert doc.width().value > 0
        assert doc.height().value > 0


def test_font_metrics_are_positive():
    container = DummyContainer()
    font = container.create_font(None)
    assert len(font) == 5
    assert font[0] > 0
    assert font[1] > 0
    assert litehtmlpy.pixel_float_t(12).value > 0
    assert container.pt_to_px(12).value > 0
    assert container.get_default_font_size().value > 0


def test_fromstring_accepts_malformed_html_without_crashing():
    container = DummyContainer()
    doc = litehtmlpy.fromString(container, "<div><span>broken", None, None)
    assert doc is not None
    doc.render(container.size.width, litehtmlpy.render_all)
    assert doc.width().value > 0


def test_web_color_and_default_values_are_available():
    assert litehtmlpy.web_color.black is not None
    assert litehtmlpy.web_color.white is not None
    assert litehtmlpy.web_color.transparent is not None
    assert litehtmlpy.web_color.current_color is not None


def test_document_container_can_expose_media_features():
    container = DummyContainer(width=640, height=480)
    media = container.get_media_features()
    assert len(media) == 9
    assert media[0] == 2
    assert media[1] == 640
    assert media[2] == 480


def test_anchor_link_is_parsed_without_crashing():
    doc, _ = render_html("<a href='https://example.com'>link</a>")
    assert doc is not None
    assert doc.width().value > 0
    assert doc.height().value > 0


def test_list_markup_renders_stably():
    for html in (
        "<ul><li>one</li><li>two</li></ul>",
        "<ol><li>first</li><li>second</li></ol>",
    ):
        doc, _ = render_html(html)
        assert doc is not None
        assert doc.width().value > 0
        assert doc.height().value > 0


def test_image_tag_render_does_not_crash():
    doc, _ = render_html('<img src="/tmp/test.png" alt="demo" width="32" height="16">')
    assert doc is not None
    assert doc.width().value > 0
    assert doc.height().value > 0


def test_load_image_is_triggered_for_image_tag():
    class ImageContainer(DummyContainer):
        def __init__(self):
            super().__init__()
            self.events = []

        def load_image(self, src, baseurl, redraw_on_ready):
            self.events.append((src, baseurl, redraw_on_ready))

    container = ImageContainer()
    doc = litehtmlpy.fromString(container, '<img src="hero.png" width="32" height="16" alt="demo">', None, None)
    assert doc is not None
    doc.render(container.size.width, litehtmlpy.render_all)
    assert any(item[0] == "hero.png" for item in container.events)


def test_image_tag_with_dimensions_renders():
    html = '<img src="https://example.com/logo.png" width="32" height="16" alt="demo">'
    doc, _ = render_html(html)
    assert doc is not None
    assert doc.width().value > 0
    assert doc.height().value > 0
