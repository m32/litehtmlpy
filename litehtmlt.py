#!/usr/bin/env vpython3
import logme

from litehtmlpy import litehtml, litehtmlpy

class Button(litehtml.litehtmlpy.html_tag):
    def __init__(self, attributes, doc):
        super().__init__(doc)
        print('i`m the button', attributes, 'tagName=', self.get_tagName())
    def draw(self, hdc, x, y, clip, ri):
        super().draw(hdc, x, y, clip, ri)
        print('Button.draw', hdc, x, y, clip, ri.pos())

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
            if doc is not None:
                tagh = Button(attributes, doc)
                self.handlers.append(tagh)
                return tagh
            return True

def main():
    #litehtml.litehtml.liblitehtmlpy.debuglog(1)
    html = open('litehtmlt.html', 'rt').read()
    cntr = document_container()

    doc = litehtmlpy.fromString(cntr, html, None, None)
    doc.render(cntr.size[0], litehtmlpy.render_all)
    clip = litehtmlpy.position(0, 0, doc.width(), doc.height())
    doc.draw(0, 0, 0, clip)
    del doc, cntr

main()
