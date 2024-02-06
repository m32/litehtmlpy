#define PYBIND11_DETAILED_ERROR_MESSAGES

#ifdef MS_WIN64
#define _hypot hypot
#include <cmath>
#endif

#include "pybind11/pybind11.h"
#include <litehtml.h>
#include <litehtml/render_item.h>

#include <iostream>
#include <string>

using namespace litehtml;
namespace py = pybind11;

static int debuglog = 0;
#define ENTERWRAPPER std::cout << "PyLiteHtml::" << __FUNCTION__ << std::endl;
//#define ENTERWRAPPER

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
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            draw_text,
            hdc, text, hFont, color, pos
        );
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
#if 0
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            draw_list_marker,
            hdc, marker
        );
#endif
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
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            get_image_size,
            src, baseurl, sz
        );
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
                    b.color,
                    b.clip_box,
                    b.origin_box,
                    b.border_box,
                    pyradius,
                    b.image_size,
                    b.position_x,
                    b.position_y,
                    b.is_root
                );
                pybg.append(l);
            }
            auto obj = override(hdc, pybg);
            //pybg.release();
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
            auto obj = override(hdc, pyborders, draw_pos, root);
            //pydraw_pos.release();
            //pyborders.release();
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
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            on_anchor_click,
            url,
            el
        );
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
    void    set_clip(const litehtml::position& pos, const litehtml::border_radiuses& bdr_radius) override
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            set_clip,
            pos, bdr_radius
        );
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
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            get_client_rect,
            client
        );
    }
    element::ptr create_element( const char* tag_name,
              const string_map& attributes,
              const std::shared_ptr<document>& doc) override
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        py::gil_scoped_acquire gil;
        py::function override = pybind11::get_override(this, "create_element");
        if (override) {
            py::bool_ create = override(tag_name);
            if( !bool(create) )
                return nullptr;
            auto pyattributes = py::dict();
			for (auto& cls : attributes)
                pyattributes[py::str(cls.first)] = py::str(cls.second);
#if 0
            py::object obj = override(tag_name, pyattributes, doc);
            if( py::isinstance<py::none>(obj) )
                return obj;
#else
            auto obj = override(tag_name, pyattributes, doc);
            if (pybind11::detail::cast_is_temporary_value_reference<html_tag::ptr>::value) {
                static pybind11::detail::override_caster_t<html_tag::ptr> caster;
                return pybind11::detail::cast_ref<html_tag::ptr>(std::move(obj), caster);
            } else {
                return pybind11::detail::cast_safe<html_tag::ptr>(std::move(obj));
            }
#endif
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

class PyHtmlTag : public html_tag
{
public:
    using html_tag::html_tag;

    void draw(uint_ptr hdc, int x, int y, const position *clip, const std::shared_ptr<render_item> &ri) override
    {
std::cout << "PyHtmlTag.draw" << std::endl;
        py::gil_scoped_acquire gil;
        py::function override = pybind11::get_override(this, "draw");
        if (override) {
            auto obj = override(hdc, x, y, clip, ri);
        } else {
std::cout << "undefined method draw" << std::endl;
        }
std::cout << "/PyHtmlTag.draw" << std::endl;
    }
};

PYBIND11_MODULE(litehtmlpy, m) {
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
    py::class_<document, std::shared_ptr<document>>(m, "document")
        .def("width", [](document &self) {
            return self.width();
        })
        .def("height", [](document &self) {
            return self.height();
        })
    ;
/*
	struct list_marker
	{
		string			image;
		const char*		baseurl;
		list_style_type	marker_type;
		web_color		color;
		position		pos;
		int				index;
		uint_ptr		font;
	};
*/
    py::class_<web_color>(m, "web_color")
        .def(py::init<int,int,int,int>())
        .def_readwrite("red", &web_color::red)
        .def_readwrite("green", &web_color::green)
        .def_readwrite("blue", &web_color::blue)
        .def_readwrite("alpha", &web_color::alpha)
    ;
    py::class_<margins>(m, "margins")
        .def(py::init<>())
        .def_readwrite("left", &margins::left)
        .def_readwrite("top", &margins::top)
        .def_readwrite("right", &margins::right)
        .def_readwrite("bottom", &margins::bottom)
        .def("width", &margins::width)
        .def("height", &margins::height)
    ;
    py::class_<size>(m, "size")
        .def(py::init<>())
        .def(py::init<int, int>())
        .def_readwrite("width", &size::width)
        .def_readwrite("height", &size::height)
    ;
    py::class_<position>(m, "position")
        .def(py::init<int,int,int,int>())
        .def_readwrite("x", &position::x)
        .def_readwrite("y", &position::y)
        .def_readwrite("width", &position::width)
        .def_readwrite("height", &position::height)
        .def("left", &position::left)
        .def("top", &position::top)
        .def("right", &position::right)
        .def("bottom", &position::bottom)
        //.def(py::self += margins)
        //.def(py::self -= margins)
        //=size
        .def("clear", &position::clear)
        .def("move_to", &position::move_to)
        .def("does_intersect", &position::does_intersect)
        .def("empty", &position::empty)
        .def("is_point_inside", &position::is_point_inside)
    ;

    py::class_<render_item, std::shared_ptr<render_item>>(m, "render_item")
        .def("pos", &render_item::pos)
        //.def("skip", &render_item::skip)
        //void skip(bool val)
        .def("right", &render_item::right)
        .def("left", &render_item::left)
        .def("top", &render_item::top)
        .def("bottom", &render_item::bottom)
        .def("height", &render_item::height)
        .def("width", &render_item::width)
        .def("padding_right", &render_item::padding_right)
        .def("padding_left", &render_item::padding_left)
        .def("padding_top", &render_item::padding_top)
        .def("padding_bottom", &render_item::padding_bottom)
        .def("border_right", &render_item::border_right)
        .def("border_left", &render_item::border_left)
        .def("border_top", &render_item::border_top)
        .def("border_bottom", &render_item::border_bottom)
        .def("margin_right", &render_item::margin_right)
        .def("margin_left", &render_item::margin_left)
        .def("margin_top", &render_item::margin_top)
        .def("margin_bottom", &render_item::margin_bottom)
/*
        //std::shared_ptr<render_item> parent() const
        margins& get_margins()
        margins& get_paddings()
		void set_paddings(const margins& val)
        margins& get_borders()
        int content_offset_top() const
        inline int content_offset_bottom() const
        int content_offset_left() const
        int content_offset_right() const
        int content_offset_width() const
        int content_offset_height() const
		int box_sizing_left() const
		int box_sizing_right() const
		int box_sizing_width() const
		int box_sizing_top() const
		int box_sizing_bottom() const
		int box_sizing_height() const
        void parent(const std::shared_ptr<render_item>& par)
        const std::shared_ptr<element>& src_el() const
		const css_properties& css() const
        void add_child(const std::shared_ptr<render_item>& ri)
		bool is_root() const
        bool collapse_top_margin() const
        bool collapse_bottom_margin() const
        bool is_visible() const
*/
    ;

    py::class_<html_tag, PyHtmlTag, std::shared_ptr<html_tag>>(m, "PyHtmlTag")
        .def(py::init<const std::shared_ptr<document>&>())
//        .def("draw", &html_tag::draw)
        .def("get_tagName",[](PyHtmlTag &self) {
            return self.get_tagName();
        })
    ;
}
