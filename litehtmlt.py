#!/usr/bin/env vpython3
import gc
gc.enable()

import logme

from litehtmlpy import litehtml

class Button(litehtml.litehtmlpy.PyHtmlTag):
    def __init__(self, attributes, doc):
        super().__init__(doc)
        print('i`m the button', attributes)
        tt = self.get_tagName()
        print('tt=', tt)
        print(dir(self))
    def draw(self, hdc, x, y, clip, ri):
        p = ri.pos()
        print('Button.draw', hdc, x, y, clip.x, clip.y, clip.width, clip.height, p.x, p.y, p.width, p.height)
        print(ri.left(), ri.top(), ri.right(), ri.bottom())
        print(dir(ri))
        #super().draw(hdc, x, y, clip, ri)

class LiteHtml(litehtml.LiteHtml):
    def __init__(self):
        super().__init__()
        self.handlers = []

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
    cls = LiteHtml()
    cls.fromString(html)
    cls.draw(
        0, 0,
        0, 0, cls.size[0], cls.size[1])
main()
