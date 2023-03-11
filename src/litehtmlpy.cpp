#define PYBIND11_DETAILED_ERROR_MESSAGES

#include "pybind11/pybind11.h"
#include <litehtml.h>

#include <iostream>
#include <string>

using namespace litehtml;
namespace py = pybind11;

static int debuglog = 0;
#define ENTERWRAPPER std::cout << "PyLiteHtml::" << __FUNCTION__ << std::endl;

py::tuple fromPosition(const position& pos)
{
    return py::make_tuple(pos.x, pos.y, pos.width, pos.height);
}

py::tuple fromBorder(const border& b)
{
    return py::make_tuple(
        b.width,
        (int)b.style,
        py::make_tuple(b.color.red, b.color.green, b.color.blue, b.color.alpha)
    );
}

class PyLiteHtml : public document_container
{
public:
    document::ptr m_doc;

    uint_ptr create_font(const char* faceName, int size, int weight, font_style italic, unsigned int decoration, font_metrics* fm) override {
        if( debuglog ){
            ENTERWRAPPER
        }
        uint_ptr result = 0;

        py::gil_scoped_acquire gil;
        py::function override = pybind11::get_override(this, "create_font");
        if (override) {
            auto obj = override(faceName, size, weight, (int)italic, (int)decoration);
            if (py::isinstance<py::list>(obj)) {
                py::list l = obj.cast<py::list>();
                result = l[0].cast<int>();
                if( fm ) {
                    fm->ascent   = l[1].cast<int>();
                    fm->descent  = l[2].cast<int>();
                    fm->height   = l[3].cast<int>();
                    fm->x_height = l[4].cast<int>();
                }
            }
        }
        return result;
    }

    void    delete_font(uint_ptr hFont) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            delete_font,
            hFont
        );
    }
    int     text_width(const char* text, uint_ptr hFont) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            int,
            document_container,
            text_width,
            text, hFont
        );
    }
    void    draw_text(uint_ptr hdc, const char* text, uint_ptr hFont, web_color color, const position& pos) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        py::tuple pypos = fromPosition(pos);
        py::tuple pycolor = py::make_tuple(color.red, color.green, color.blue, color.alpha);

        py::gil_scoped_acquire gil;
        py::function override = pybind11::get_override(this, "draw_text");
        if (override) {
            auto obj = override(hdc, text, hFont, pycolor, pypos);
        }
        pypos.release();
        pycolor.release();
    }
    int     pt_to_px(int pt) const override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            int,
            document_container,
            pt_to_px,
            pt
        );
    }
    int     get_default_font_size() const override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            int,
            document_container,
            get_default_font_size,
            // no arguments
        );
    }
    const char*   get_default_font_name() const override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            char*,
            document_container,
            get_default_font_name,
            // no arguments
        );
    }
    void    draw_list_marker(uint_ptr hdc, const list_marker& marker) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            draw_list_marker,
            hdc, marker
        );
    }
    void    load_image(const char* src, const char* baseurl, bool redraw_on_ready) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            load_image,
            src, baseurl, redraw_on_ready
        );
    }
    void    get_image_size(const char* src, const char* baseurl, size& sz) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        py::gil_scoped_acquire gil;
        py::function override = pybind11::get_override(this, "get_image_size");
        if (override) {
            auto obj = override(src, baseurl);
            if (py::isinstance<py::list>(obj)) {
                py::list l = obj.cast<py::list>();
                sz.width = l[0].cast<int>();
                sz.height = l[0].cast<int>();
                l.release();
            }
        }
    }
    void    draw_background(uint_ptr hdc, const std::vector<background_paint>& bg) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        py::gil_scoped_acquire gil;
        py::function override = pybind11::get_override(this, "draw_background");
        if (override) {
            py::list pybg = py::list();
            for (int i = 0; i < (int)bg.size(); i++)
            {
                const auto& b = bg[i];
                py::tuple pycolor = py::make_tuple(b.color.red, b.color.green, b.color.blue, b.color.alpha);
                py::tuple pyradius = py::make_tuple(
                    b.border_radius.top_left_x,
                    b.border_radius.top_left_y,
                    b.border_radius.top_right_x,
                    b.border_radius.top_right_y,
                    b.border_radius.bottom_right_x,
                    b.border_radius.bottom_right_y,
                    b.border_radius.bottom_left_x,
                    b.border_radius.bottom_left_y
                );
                py::tuple pysize = py::make_tuple(b.image_size.width, b.image_size.height);
                py::tuple l = py::make_tuple(
                    b.image,
                    b.baseurl,
                    (int)b.attachment,
                    (int)b.repeat,
                    pycolor,
                    fromPosition(b.clip_box),
                    fromPosition(b.origin_box),
                    fromPosition(b.border_box),
                    pyradius,
                    pysize,
                    b.position_x,
                    b.position_y,
                    b.is_root
                );
                pybg.append(l);
            }
            auto obj = override(hdc, pybg);
            pybg.release();
        }
    }
    void    draw_borders(uint_ptr hdc, const borders& borders, const position& draw_pos, bool root) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        py::gil_scoped_acquire gil;
        py::function override = pybind11::get_override(this, "draw_borders");
        if (override) {
            py::tuple pyborders = py::make_tuple(
                fromBorder(borders.left),
                fromBorder(borders.top),
                fromBorder(borders.right),
                fromBorder(borders.bottom)
            );
            py::tuple pydraw_pos = fromPosition(draw_pos);
            auto obj = override(hdc, pyborders, pydraw_pos, root);
            pydraw_pos.release();
            pyborders.release();
        }
    }

    void    set_caption(const char* caption) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            set_caption,
            caption
        );
    }
    void    set_base_url(const char* base_url) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            set_base_url,
            base_url
        );
    }
    void    link(const std::shared_ptr<document>& doc, const element::ptr& el) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
    }
    void    on_anchor_click(const char* url, const element::ptr& el) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
    }
    void    set_cursor(const char* cursor) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            set_cursor,
            cursor
        );
    }
    void    transform_text(string& text, text_transform tt) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            transform_text,
            text, (int)tt
        );
    }
    void    import_css(string& text, const string& url, string& baseurl) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            import_css,
            text, url, baseurl
        );
    }
    void    set_clip(const position& pos, const border_radiuses& bdr_radius, bool valid_x, bool valid_y) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
    }
    void    del_clip() override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            del_clip,
            // no arguments
        );
    }
    void    get_client_rect(position& client) const override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        py::gil_scoped_acquire gil;
        py::function override = pybind11::get_override(this, "get_client_rect");
        if (override) {
            auto obj = override();
            if (py::isinstance<py::list>(obj)) {
                py::list l = obj.cast<py::list>();
                client.x = l[0].cast<int>();
                client.y = l[1].cast<int>();
                client.width = l[2].cast<int>();
                client.height = l[3].cast<int>();
            }
        }
    }
    element::ptr create_element( const char* tag_name,
              const string_map& attributes,
              const std::shared_ptr<document>& doc) override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        return nullptr;
    }
    void    get_media_features(media_features& media) const override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        py::gil_scoped_acquire gil;
        py::function override = pybind11::get_override(this, "get_media_features");
        if (override) {
            auto obj = override();
            if (py::isinstance<py::list>(obj)) {
                py::list l = obj.cast<py::list>();
                media.type              = (litehtml::media_type)l[0].cast<int>();
                media.width             = l[1].cast<int>();
                media.height            = l[2].cast<int>();
                media.device_width      = l[3].cast<int>();
                media.device_height     = l[4].cast<int>();
                media.color             = l[5].cast<int>();
                media.monochrome        = l[6].cast<int>();
                media.color_index       = l[7].cast<int>();
                media.resolution        = l[8].cast<int>();
            }
        }
    }
    void    get_language(string& language, string& culture) const override 
    {
        if( debuglog ){
            ENTERWRAPPER
        }
/*
        py::gil_scoped_acquire gil;
        py::function override = pybind11::get_override(this, "get_language");
        if (override) {
            auto obj = override();
            if (py::isinstance<py::list>(obj)) {
                py::list l = obj.cast<py::list>();
                language = l[0].cast<string&>();
                culture = l[1].cast<string&>();
            }
        }
*/
    }
#if 0
    string resolve_color(const string& color) const {
        if( debuglog ){
            ENTERWRAPPER
        }
        return string();
    }
    void    split_text(const char* text, const std::function<void(const char*)>& on_word, const std::function<void(const char*)>& on_space) {
        if( debuglog ){
            ENTERWRAPPER
        }
    }
#endif
};

PYBIND11_MODULE(liblitehtmlpy, m) {
    m.def("debuglog", [](int on) {
        debuglog = on;
    })
    ;
    py::class_<document_container, PyLiteHtml, std::unique_ptr<document_container, py::nodelete>>(m, "LiteHtml")
        .def(py::init<>())
        .def("fromString", [](PyLiteHtml &self, char *html) {
            py::gil_scoped_release release;
            self.m_doc = document::createFromString(html, &self);
        })
        .def("render", [](PyLiteHtml &self, int maxWidth) {
            py::gil_scoped_release release;
            self.m_doc->render(maxWidth);
        })
        .def("height", [](PyLiteHtml &self) {
            py::gil_scoped_release release;
            return self.m_doc->height();
        })
        .def("draw", [](PyLiteHtml &self, int x, int y, int clipX, int clipY, int clipWidth, int clipHeight) {
            py::gil_scoped_release release;
            position clip(clipX, clipY, clipWidth, clipHeight);
            self.m_doc->draw((uint_ptr)NULL, x, y, &clip);
        })
    ;
}
