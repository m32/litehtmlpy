#!/usr/bin/env vpython3
import logme

from litehtmlpy import litehtml, litehtmlpy

class Button(litehtml.litehtmlpy.html_tag):
    def __init__(self, attributes, doc):
        super().__init__(doc)
        print('i`m the button', attributes, 'tagName=', self.get_tagName())
    def draw(self, hdc, x, y, clip, ri):
        super().draw(hdc, x, y, clip, ri)
        pos = ri.pos()
        print(f'Button.draw({hdc}, {x}, {y}, ({clip.x}, {clip.y}, {clip.width}, {clip.height}), ({pos.x}, {pos.y})')


class Input(litehtml.litehtmlpy.html_tag):
    def __init__(self, attributes, doc):
        super().__init__(doc)
        self.attributes = attributes
        print('i`m the input', attributes, 'tagName=', self.get_tagName())

    def draw(self, hdc, x, y, clip, ri):
        super().draw(hdc, x, y, clip, ri)
        pos = ri.pos()
        #print('input.draw', ri.left(), ri.top(), ri.right(), ri.bottom())
        x += pos.x
        y += pos.y
        w = pos.width
        h = pos.height
        css = self.css()
        lh = css.line_height()
        fh = css.get_font_size()
        lh = css.line_height()
        y = y + (h - lh) // 2
        h = pos.height
        print('Input.draw', hdc, x, y, w, h)


class document_container(litehtml.document_container):
    def __init__(self):
        super().__init__()
        self.handlers = []

    def import_css(self, text, url, base_url):
        url = urllib.parse.urljoin(base_url, url)
        if os.path.exists(url):
            with open(url, 'rt') as fp:
                data = fp.read()
        elif url.split(':')[0] in ('http', 'https'):
            r = requests.get(url)
            if r.headers['Content-Type'] == 'text/css':
                data = r.text
        if data is None:
            print('unknown import_css', url)
            return
        return data

    def create_element(self, tag_name, attributes=None, doc=None):
        if tag_name == 'button':
            tagh = Button(attributes, doc)
            self.handlers.append(tagh)
            return tagh
        if tag_name == 'input':
            t = attributes.get('type', '').lower()
            if t == 'text':
                tagh = Input(attributes, doc)
                self.handlers.append(tagh)
                return tagh
            elif t == 'submit':
                tagh = Button(attributes, doc)
                self.handlers.append(tagh)
                return tagh

def main():
    #litehtml.litehtml.liblitehtmlpy.debuglog(1)
    html = open('litehtmlt.html', 'rt').read()
    cntr = document_container()

    doc = litehtmlpy.fromString(cntr, html, None, None)
    doc.render(cntr.size[0], litehtmlpy.render_all)
    clip = litehtmlpy.position(0, 0, int(doc.width()), int(doc.height()))
    doc.draw(0, 0, 0, clip)
    del doc, cntr

main()
