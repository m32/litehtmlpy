#!/usr/bin/env vpython3
import os
import sys
import urllib.parse

import logme
from litehtmlpy import litehtmltxt, litehtmlpy

class Button(litehtmlpy.html_tag):
    def __init__(self, parent, attributes, doc):
        super().__init__(doc)
        self.parent = parent
        self.attributes = attributes

    def destroy(self):
        pass

    def draw(self, hdc, x, y, clip, ri):
        super().draw(hdc, x, y, clip, ri)
        pos = ri.pos()
        x += pos.x
        y += pos.y
        w = pos.width
        h = pos.height
        print('Button.draw: x={} y={} w={} h={}'.format(x.value, y.value, w.value, h.value, self.attributes))

    def on_mouse_over(self):
        print('Button.on_mouse_over')
        return True

    def on_mouse_leave(self):
        print('Button.on_mouse_leave')
        return True

    def on_lbutton_down(self):
        print('Button.on_lbutton_down')
        return True

    def on_lbutton_up(self):
        print('Button.on_lbutton_up')
        return True

    def on_click(self):
        print('Button.on_click')
        self.parent.HtmlClick(self)


class Input(litehtmlpy.html_tag):
    def __init__(self, parent, attributes, doc):
        super().__init__(doc)
        self.parent = parent
        self.attributes = attributes

    def destroy(self):
        pass

    def draw(self, hdc, x, y, clip, ri):
        super().draw(hdc, x, y, clip, ri)
        pos = ri.pos()
        x += pos.x
        y += pos.y
        w = pos.width.value
        h = pos.height.value
        print('Input.draw: x={} y={} w={} h={}'.format(int(x.value), int(y.value), int(w), int(h)))

    def on_mouse_over(self):
        return True

    def on_mouse_leave(self):
        return True

    def on_lbutton_down(self):
        print('Input.on_lbutton_down')
        return True

    def on_lbutton_up(self):
        print('Input.on_lbutton_up')
        return True

    def on_click(self):
        print('Input.on_click')
        self.parent.HtmlClick(self)


class Checkbox(litehtmlpy.html_tag):
    def __init__(self, parent, attributes, doc):
        super().__init__(doc)
        self.parent = parent
        self.attributes = attributes

    def destroy(self):
        pass

    def draw(self, hdc, x, y, clip, ri):
        super().draw(hdc, x, y, clip, ri)
        pos = ri.pos()
        x += pos.x
        y += pos.y
        w = pos.width.value
        h = pos.height.value
        print('Checkbox.draw: x={} y={} w={} h={}'.format(int(x.value), int(y.value), int(w), int(h)))

    def on_mouse_over(self):
        return True

    def on_mouse_leave(self):
        return True

    def on_lbutton_down(self):
        print('Checkbox.on_lbutton_down')
        return True

    def on_lbutton_up(self):
        print('Checkbox.on_lbutton_up')
        return True

    def on_click(self):
        print('Checkbox.on_click')
        self.parent.HtmlClick(self)


class DC(litehtmltxt.DC):
    pass

class Dokument(litehtmltxt.document_container):
    classDC = DC
    def __init__(self, fname):
        super().__init__()
        self.fname = fname
        self.handlers = []

    def import_css(self, text, url, base_url):
        url = urllib.parse.urljoin(base_url, url)
        if os.path.exists(url):
            with open(url, 'rt') as fp:
                data = fp.read()
        else:
            data = None
        if data is None:
            print('unknown import_css', url)
            return
        return data

    def create_element(self, tag_name, attributes=None, doc=None):
        if tag_name == 'button':
            tagh = Button(self, attributes, doc)
            self.handlers.append(tagh)
            return tagh
        if tag_name == 'input':
            t = attributes.get('type', '').lower()
            if t == 'text':
                tagh = Input(self, attributes, doc)
                self.handlers.append(tagh)
                return tagh
            elif t == 'submit':
                tagh = Button(self, attributes, doc)
                self.handlers.append(tagh)
                return tagh
            elif t == 'checkbox':
                tagh = Checkbox(self, attributes, doc)
                self.handlers.append(tagh)
                return tagh
        print('create_element', tag_name, attributes, doc)
        return None

    def Run(self):
        with open(self.fname, 'rt') as fp:
            html = fp.read()
        doc = litehtmlpy.fromString(self, html, None, None)
        try:
            doc.render(self.size.width, litehtmlpy.render_all)
            self.size = litehtmlpy.size(int(self.size.width.value), int(doc.height().value))
            self.reset()

            print('DOC:', 'w=', doc.width().value, 'h=', doc.height().value)
            clip = litehtmlpy.position(0, 0, int(doc.width().value), int(doc.height().value))
            doc.draw(0, litehtmlpy.pixel_float_t(0), litehtmlpy.pixel_float_t(0), clip)
            print('done')
            print(self.dc._lines)
            for line in self.dc.lines():
                print('line:', line, self.dc.line(line))
        finally:
            self.SetDC(None)
            del doc

class Main:
    def demo(self):
        if len(sys.argv) > 1:
            fname = sys.argv[1]
        else:
            fname = 'tui.html'
        cls = Dokument(fname)
        cls.Run()

def main():
    app = Main()
    app.demo()

main()
