from tests.common import DummyContainer, render_html
from litehtmlpy import litehtmlpy


def test_media_queries_like_width_and_color_are_accepted():
    html = """
    <style>
      @media (max-width: 600px) { body { color: red; } }
      @media (min-width: 601px) { body { color: blue; } }
    </style>
    <p>Responsive</p>
    """
    doc, _ = render_html(html, width=800)
    assert doc is not None
    assert doc.width().value > 0
    assert doc.height().value > 0


def test_table_layout_renders_without_exception():
    html = """
    <table style='border: 1px solid black; width: 300px;'>
      <tr><td>One</td><td>Two</td></tr>
    </table>
    """
    doc, _ = render_html(html)
    assert doc is not None
    assert doc.width().value > 0
    assert doc.height().value > 0


def test_external_css_import_is_called_for_linked_stylesheet(tmp_path):
    css_file = tmp_path / "style.css"
    css_file.write_text("body { color: red; } p { margin: 12px; }", encoding="utf-8")

    class CSSContainer(DummyContainer):
        def __init__(self):
            super().__init__()
            self.imported_css = []

        def import_css(self, text, url, base_url):
            self.imported_css.append((url, text))

    container = CSSContainer()
    html = f'<html><head><link rel="stylesheet" href="{css_file.as_posix()}"></head><body><p>Hello</p></body></html>'
    doc = litehtmlpy.fromString(container, html, None, None)
    assert doc is not None
    doc.render(container.size.width, litehtmlpy.render_all)
    assert container.imported_css


def test_complex_nested_layout_and_media_queries_render_stably():
    html = """
    <style>
      body { margin: 0; font-family: sans-serif; }
      .card { display: flex; width: 90%; gap: 12px; }
      .left, .right { flex: 1 1 40%; padding: 8px; }
      @media (max-width: 700px) {
        .card { flex-direction: column; }
        .left, .right { flex-basis: 100%; }
      }
      @media (min-width: 701px) {
        .card { border: 1px solid #999; }
      }
    </style>
    <div class="card">
      <div class="left"><p>Alpha</p><p>Beta</p></div>
      <div class="right"><ul><li>One</li><li>Two</li></ul></div>
    </div>
    """
    doc, _ = render_html(html, width=800)
    assert doc is not None
    assert doc.width().value > 0
    assert doc.height().value > 0


def test_background_image_and_gradient_css_render_do_not_crash():
    html = """
    <div style="background-image: url('bg.png'); background: linear-gradient(red, blue); width: 200px; height: 60px;">
      test
    </div>
    """
    doc, _ = render_html(html)
    assert doc is not None
    assert doc.width().value > 0
    assert doc.height().value > 0


def test_background_position_border_radius_and_box_shadow_render_stably():
    html = """
    <style>
      body { margin: 0; }
      .demo {
        width: 220px;
        height: 120px;
        background-image: url('bg.png');
        background-position: center center;
        background-repeat: no-repeat;
        border: 2px solid #333;
        border-radius: 16px 24px 12px 8px;
        box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.35);
      }
    </style>
    <div class="demo">Hello</div>
    """
    doc, _ = render_html(html)
    assert doc is not None
    assert doc.width().value > 0
    assert doc.height().value > 0
