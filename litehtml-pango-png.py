#!/usr/bin/env vpython3
import sys
import os
import io
import logging
import urllib.parse
import logme
from litehtmlpy import litehtmlpango, litehtmlpy

litehtmlpy.debuglog(1)

logger = logging.getLogger(__name__)

class document_container(litehtmlpango.document_container):
    pass

class App:
    images = {}
    url = ''

    def GetUrlData(self, url, html=True):
        data = None
        print('GetUrlData', url)
        if os.path.exists(url):
            with open(url, 'rb') as fp:
                data = fp.read()
        elif url.split(':')[0] in ('http', 'https'):
            r = requests.get(url)
            print(r.headers)
            if html:
                if r.headers['Content-Type'] == 'text/html':
                    data = r.text
            else:
                if r.headers['Content-Type'] == 'image/png':
                    data = r.content
        if data is None:
            print('unknown url', url)
            return None
        return data

    def HtmlLoadImage(self, src, baseurl, redraw_on_ready):
        if baseurl is not None:
            url = urllib.parse.urljoin(baseurl, src)
        else:
            url = urllib.parse.urljoin(self.url, src)
        data = self.GetUrlData(url, False)
        if data is None:
            return
        #self.images[url] = img

    def HtmlGetImage(self, src, baseurl):
        if baseurl is not None:
            url = urllib.parse.urljoin(baseurl, src)
        else:
            url = urllib.parse.urljoin(self.url, src)
        return self.images.get(url, None)


class Main:
    def demo(self):
        app = App()
        if len(sys.argv) > 1:
            fname = sys.argv[1]
        else:
            fname = 'demo.html'
            fname = 'litehtmlt.html'
        html = open(fname, 'rt').read()

        cntr = document_container(app)
        print('max size=', cntr.size)

        doc = cntr.fromString(html, None, None)
        doc.render(cntr.size[0], litehtmlpy.render_all)
        print('doc: width:', doc.width(), 'height:', doc.height())

        cntr.size[1] = doc.height()
        hdc = cntr.surface(doc.width(), doc.height())

        print('*'*10, 'draw')
        clip = litehtmlpy.position(0, 0, doc.width(), doc.height())
        doc.draw(hdc, 0, 0, clip)

        cntr.save('demo.png')

        del doc
        del cntr

def main():
    app = Main()
    app.demo()

main()
