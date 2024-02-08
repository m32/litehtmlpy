#define PYBIND11_DETAILED_ERROR_MESSAGES

#ifdef MS_WIN64
#define _hypot hypot
#include <cmath>
#else
#include <signal.h>
#define DebugBreak() raise(SIGTRAP)
#endif

#include "pybind11/pybind11.h"
#include "pybind11/stl.h"
#include <litehtml.h>
#include <litehtml/render_item.h>

#include <iostream>
#include <string>

namespace lh = litehtml;
namespace py = pybind11;

static int debuglog = 0;
#define ENTERWRAPPER std::cout << "PyLiteHtml::" << __FUNCTION__ << std::endl;
//#define ENTERWRAPPER

py::tuple fromBorder(const lh::border& b)
{
    return py::make_tuple(
        b.width,
        (int)b.style,
        py::make_tuple(b.color.red, b.color.green, b.color.blue, b.color.alpha)
    );
}

class py_html_tag : public lh::html_tag
{
public:
    using html_tag::html_tag;

/*
        bool                appendChild(const element::ptr &el) override;
        bool                removeChild(const element::ptr &el) override;
        void                clearRecursive() override;
        string_id            tag() const override;
        string_id            id() const override;
        const char*            get_tagName() const override;
        void                set_tagName(const char* tag) override;
        void                set_data(const char* data) override;

        void                set_attr(const char* name, const char* val) override;
        const char*            get_attr(const char* name, const char* def = nullptr) const override;
        void                apply_stylesheet(const litehtml::css& stylesheet) override;
        void                refresh_styles() override;

        bool                is_white_space() const override;
        bool                is_body() const override;
        bool                is_break() const override;
*/
    bool on_mouse_over() override
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE(
            bool,
            html_tag,
            on_mouse_over,
            // no arguments
        );
    }
/*
    bool on_mouse_leave() override
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE(
            bool,
            html_tag,
            on_mouse_leave,
            // no arguments
        );
    }
    bool on_lbutton_down() override
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE(
            bool,
            html_tag,
            on_lbutton_down,
            // no arguments
        );
    }
    bool on_lbutton_up() override
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE(
            bool,
            html_tag,
            on_lbutton_up,
            // no arguments
        );
    }
*/
    void on_click() override
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE(
            void,
            html_tag,
            on_click,
            // no arguments
        );
    }
/*
        bool                set_pseudo_class(string_id cls, bool add) override;
        bool                set_class(const char* pclass, bool add) override;
        bool                is_replaced() const override;
        void                compute_styles(bool recursive = true) override;
*/
    void draw(lh::uint_ptr hdc, int x, int y, const lh::position *clip, const std::shared_ptr<lh::render_item> &ri) override
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE(
            void,
            html_tag,
            draw,
            hdc,x, y, clip, ri
        );
    }
    void draw_background(lh::uint_ptr hdc, int x, int y, const lh::position *clip, const std::shared_ptr<lh::render_item> &ri) override
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE(
            void,
            html_tag,
            draw_background,
            hdc,x, y, clip, ri
        );
    }
/*
        template<class Type, property_type property_value_type, Type property_value::* property_value_member>
        const Type&            get_property_impl  (string_id name, bool inherited, const Type&   default_value, uint_ptr css_properties_member_offset) const;
        int                    get_enum_property  (string_id name, bool inherited, int           default_value, uint_ptr css_properties_member_offset) const override;
        int                    get_int_property   (string_id name, bool inherited, int           default_value, uint_ptr css_properties_member_offset) const override;
        css_length            get_length_property(string_id name, bool inherited, css_length    default_value, uint_ptr css_properties_member_offset) const override;
        web_color            get_color_property (string_id name, bool inherited, web_color     default_value, uint_ptr css_properties_member_offset) const override;
        string                get_string_property(string_id name, bool inherited, const string& default_value, uint_ptr css_properties_member_offset) const override;
        float                get_number_property(string_id name, bool inherited, float         default_value, uint_ptr css_properties_member_offset) const override;
        string_vector        get_string_vector_property(string_id name, bool inherited, const string_vector& default_value, uint_ptr css_properties_member_offset) const override;
        int_vector            get_int_vector_property   (string_id name, bool inherited, const int_vector&    default_value, uint_ptr css_properties_member_offset) const override;
        length_vector        get_length_vector_property(string_id name, bool inherited, const length_vector& default_value, uint_ptr css_properties_member_offset) const override;
        size_vector            get_size_vector_property  (string_id name, bool inherited, const size_vector&   default_value, uint_ptr css_properties_member_offset) const override;
        string                get_custom_property(string_id name, const string& default_value) const override;

        elements_list&    children();

        int                    select(const string& selector) override;
        int                    select(const css_selector& selector, bool apply_pseudo = true) override;
        int                    select(const css_element_selector& selector, bool apply_pseudo = true) override;
        int                    select_pseudoclass(const css_attribute_selector& sel);
        int                    select_attribute(const css_attribute_selector& sel);

        elements_list        select_all(const string& selector) override;
        elements_list        select_all(const css_selector& selector) override;

        element::ptr        select_one(const string& selector) override;
        element::ptr        select_one(const css_selector& selector) override;

        element::ptr        find_ancestor(const css_selector& selector, bool apply_pseudo = true, bool* is_pseudo = nullptr) override;
        element::ptr        find_adjacent_sibling(const element::ptr& el, const css_selector& selector, bool apply_pseudo = true, bool* is_pseudo = nullptr) override;
        element::ptr        find_sibling(const element::ptr& el, const css_selector& selector, bool apply_pseudo = true, bool* is_pseudo = nullptr) override;
        void                get_text(string& text) override;
        void                parse_attributes() override;

        void                get_content_size(size& sz, int max_width) override;
        void                add_style(const style& style) override;

        bool                is_nth_child(const element::ptr& el, int num, int off, bool of_type) const override;
        bool                is_nth_last_child(const element::ptr& el, int num, int off, bool of_type) const override;
        bool                is_only_child(const element::ptr& el, bool of_type) const override;
        const background*    get_background(bool own_only = false) override;

        string                dump_get_name() override;

    protected:
        void                init_background_paint(position pos, std::vector<background_paint>& bg_paint, const background* bg, const std::shared_ptr<render_item>& ri);
        void                init_one_background_paint(int i, position pos, background_paint& bg_paint, const background* bg, const std::shared_ptr<render_item>& ri);
        void                draw_list_marker( uint_ptr hdc, const position &pos );
        string                get_list_marker_text(int index);
        element::ptr        get_element_before(const style& style, bool create);
        element::ptr        get_element_after(const style& style, bool create);

    private:
        void                handle_counter_properties();

*/
};

class py_element : public lh::element
{
public:
    using element::element;
/*
	protected:
		std::weak_ptr<element>					m_parent;
		std::weak_ptr<document>					m_doc;
		elements_list							m_children;
		css_properties							m_css;
		std::list<std::weak_ptr<render_item>>	m_renders;
		used_selector::vector					m_used_styles;

		virtual void select_all(const css_selector& selector, elements_list& res);
		element::ptr _add_before_after(int type, const style& style);
    public:
		const css_properties&		css() const;
		css_properties&				css_w();

		bool						in_normal_flow()			const;
		bool						is_inline()					const;	// returns true if element is inline
		bool						is_inline_box()				const;	// returns true if element is inline box (inline-table, inline-box, inline-flex)
		bool						is_block_box()				const;
		position					get_placement()				const;
		bool						is_positioned()				const;
		bool						is_float()					const;
		bool						is_block_formatting_context() const;

		bool						is_root() const;
		element::ptr				parent() const;
		void						parent(const element::ptr& par);
		// returns true for elements inside a table (but outside cells) that don't participate in table rendering
		bool						is_table_skip() const;

		std::shared_ptr<document>	get_document() const;
		const std::list<std::shared_ptr<element>>& children() const;

		virtual elements_list		select_all(const string& selector);
		virtual elements_list		select_all(const css_selector& selector);

		virtual element::ptr		select_one(const string& selector);
		virtual element::ptr		select_one(const css_selector& selector);

		virtual bool				appendChild(const ptr &el);
		virtual bool				removeChild(const ptr &el);
		virtual void				clearRecursive();

		virtual string_id			id() const;
		virtual string_id			tag() const;
		virtual const char*			get_tagName() const;
		virtual void				set_tagName(const char* tag);
		virtual void				set_data(const char* data);

		virtual void				set_attr(const char* name, const char* val);
		virtual const char*			get_attr(const char* name, const char* def = nullptr) const;
		virtual void				apply_stylesheet(const litehtml::css& stylesheet);
		virtual void				refresh_styles();
		virtual bool				is_white_space() const;
		virtual bool				is_space() const;
		virtual bool				is_comment() const;
		virtual bool				is_body() const;
		virtual bool				is_break() const;
		virtual bool				is_text() const;

		virtual bool				on_mouse_over();
		virtual bool				on_mouse_leave();
		virtual bool				on_lbutton_down();
		virtual bool				on_lbutton_up();
		virtual void				on_click();
		virtual bool				set_pseudo_class(string_id cls, bool add);
		virtual bool				set_class(const char* pclass, bool add);
		virtual bool				is_replaced() const;
		virtual void				compute_styles(bool recursive = true);
		virtual void				draw(uint_ptr hdc, int x, int y, const position *clip, const std::shared_ptr<render_item>& ri);
		virtual void				draw_background(uint_ptr hdc, int x, int y, const position *clip, const std::shared_ptr<render_item> &ri);
		virtual int					get_enum_property  (string_id name, bool inherited, int           default_value, uint_ptr css_properties_member_offset) const;
		virtual int					get_int_property   (string_id name, bool inherited, int           default_value, uint_ptr css_properties_member_offset) const;
		virtual css_length			get_length_property(string_id name, bool inherited, css_length    default_value, uint_ptr css_properties_member_offset) const;
		virtual web_color			get_color_property (string_id name, bool inherited, web_color     default_value, uint_ptr css_properties_member_offset) const;
		virtual string				get_string_property(string_id name, bool inherited, const string& default_value, uint_ptr css_properties_member_offset) const;
		virtual float				get_number_property(string_id name, bool inherited, float         default_value, uint_ptr css_properties_member_offset) const;
		virtual string_vector		get_string_vector_property(string_id name, bool inherited, const string_vector& default_value, uint_ptr css_properties_member_offset) const;
		virtual int_vector			get_int_vector_property   (string_id name, bool inherited, const int_vector&    default_value, uint_ptr css_properties_member_offset) const;
		virtual length_vector		get_length_vector_property(string_id name, bool inherited, const length_vector& default_value, uint_ptr css_properties_member_offset) const;
		virtual size_vector			get_size_vector_property  (string_id name, bool inherited, const size_vector&   default_value, uint_ptr css_properties_member_offset) const;
		virtual string				get_custom_property(string_id name, const string& default_value) const;

		virtual void				get_text(string& text);
		virtual void				parse_attributes();
		virtual int					select(const string& selector);
		virtual int					select(const css_selector& selector, bool apply_pseudo = true);
		virtual int					select(const css_element_selector& selector, bool apply_pseudo = true);
		virtual element::ptr		find_ancestor(const css_selector& selector, bool apply_pseudo = true, bool* is_pseudo = nullptr);
		virtual bool				is_ancestor(const ptr &el) const;
		virtual element::ptr		find_adjacent_sibling(const element::ptr& el, const css_selector& selector, bool apply_pseudo = true, bool* is_pseudo = nullptr);
		virtual element::ptr		find_sibling(const element::ptr& el, const css_selector& selector, bool apply_pseudo = true, bool* is_pseudo = nullptr);
		virtual void				get_content_size(size& sz, int max_width);
		virtual bool				is_nth_child(const element::ptr& el, int num, int off, bool of_type) const;
		virtual bool				is_nth_last_child(const element::ptr& el, int num, int off, bool of_type) const;
		virtual bool				is_only_child(const element::ptr& el, bool of_type) const;
		virtual void				add_style(const style& style);
		virtual const background*	get_background(bool own_only = false);

		virtual string				dump_get_name();
		virtual std::vector<std::tuple<string, string>> dump_get_attrs();
		void						dump(litehtml::dumper& cout);

		std::tuple<element::ptr, element::ptr, element::ptr> split_inlines();
		virtual std::shared_ptr<render_item> create_render_item(const std::shared_ptr<render_item>& parent_ri);
		bool requires_styles_update();
		void add_render(const std::shared_ptr<render_item>& ri);
		bool find_styles_changes( position::vector& redraw_boxes);
		element::ptr add_pseudo_before(const style& style)
		{
			return _add_before_after(0, style);
		}
		element::ptr add_pseudo_after(const style& style)
		{
			return _add_before_after(1, style);
		}

		string				get_counter_value(const string& counter_name);
		string				get_counters_value(const string_vector& parameters);
		void				increment_counter(const string_id& counter_name_id, const int increment = 1);
		void				reset_counter(const string_id& counter_name_id, const int value = 0);

	private:
		std::vector<element::ptr> get_siblings_before() const;
		bool				find_counter(const string_id& counter_name_id, std::map<string_id, int>::iterator& map_iterator);
		void				parse_counter_tokens(const string_vector& tokens, const int default_value, std::function<void(const string_id&, const int)> handler) const;
*/
};

class py_document : public lh::document
{
};

class py_document_container : public lh::document_container
{
public:
    lh::uint_ptr create_font(const char* faceName, int size, int weight, lh::font_style italic, unsigned int decoration, lh::font_metrics* fm) override {
        if( debuglog ){
            ENTERWRAPPER
        }
        lh::uint_ptr result = 0;

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

    void    delete_font(lh::uint_ptr hFont) override
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
    int     text_width(const char* text, lh::uint_ptr hFont) override
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
    void    draw_text(lh::uint_ptr hdc, const char* text, lh::uint_ptr hFont, lh::web_color color, const lh::position& pos) override
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
    void    draw_list_marker(lh::uint_ptr hdc, const lh::list_marker& marker) override
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
    void    get_image_size(const char* src, const char* baseurl, lh::size& sz) override
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
    void    draw_background(lh::uint_ptr hdc, const std::vector<lh::background_paint>& bg) override
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
    void    draw_borders(lh::uint_ptr hdc, const lh::borders& borders, const lh::position& draw_pos, bool root) override
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
    void    link(const std::shared_ptr<lh::document>& doc, const lh::element::ptr& el) override
    {
        if( debuglog ){
            ENTERWRAPPER
        }
    }
    void    on_anchor_click(const char* url, const lh::element::ptr& el) override
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
    void    transform_text(lh::string& text, lh::text_transform tt) override
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
    void    import_css(lh::string& text, const lh::string& url, lh::string& baseurl) override
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
    void    set_clip(const lh::position& pos, const lh::border_radiuses& bdr_radius) override
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
    void    get_client_rect(lh::position& client) const override
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
    lh::element::ptr create_element( const char* tag_name,
              const lh::string_map& attributes,
              const std::shared_ptr<lh::document>& doc) override
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
            //DebugBreak();
            if (pybind11::detail::cast_is_temporary_value_reference<py_html_tag::ptr>::value) {
                static pybind11::detail::override_caster_t<py_html_tag::ptr> caster;
                return pybind11::detail::cast_ref<py_html_tag::ptr>(std::move(obj), caster);
            } else {
                return pybind11::detail::cast_safe<py_html_tag::ptr>(std::move(obj));
            }
#endif
        }
        return nullptr;
    }
    void    get_media_features(lh::media_features& media) const override
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
    void    get_language(lh::string& language, lh::string& culture) const override
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

PYBIND11_MODULE(litehtmlpy, m) {
    m.def("debuglog", [](int on) {
        debuglog = on;
    })
    ;
    py::class_<lh::document_container, py_document_container, std::unique_ptr<lh::document_container, py::nodelete>>(m, "document_container")
        .def(py::init<>())
    ;
    m.def("fromString", [](py_document_container *container, char *html, const char *master_css = lh::master_css, const char *user_styles = "") {
        py::gil_scoped_release release;
        if( master_css == nullptr )
            master_css = lh::master_css;
        if( user_styles == nullptr )
            user_styles = "";
        py_document::ptr doc = py_document::createFromString(html, container, master_css, user_styles);
        return doc;
    })
    ;
    py::class_<lh::document, py_document, std::shared_ptr<lh::document>>(m, "document")
        //document_container*                container()    { return m_container; }
        //uint_ptr                        get_font(const char* name, int size, const char* weight, const char* style, const char* decoration, font_metrics* fm);
        .def("render", &lh::document::render)
        .def("draw", &lh::document::draw)
        //web_color                        get_def_color()    { return m_def_color; }
        //int                                to_pixels(const char* str, int fontSize, bool* is_percent = nullptr) const;
        //void                             cvt_units(css_length& val, int fontSize, int size = 0) const;
        //int                                to_pixels(const css_length& val, int fontSize, int size = 0) const;
        .def("width", &lh::document::width)
        .def("height", &lh::document::height)
        .def("content_width", &lh::document::content_width)
        .def("content_height", &lh::document::content_height)
/*
        void                            add_stylesheet(const char* str, const char* baseurl, const char* media);
*/
        .def("on_mouse_over", &lh::document::on_mouse_over)
        .def("on_lbutton_down", &lh::document::on_lbutton_down)
        .def("on_lbutton_up", &lh::document::on_lbutton_up)
/*
        .def("on_lbutton_up", [](py_document &self, int x, int y, int cx, int cy, lh::position::vector& redraw_boxes){
            DebugBreak();
            py::gil_scoped_release release;
            bool rc = self.on_lbutton_up(x, y, cx, cy, redraw_boxes);
            return rc;
        })
*/
        .def("on_mouse_leave", &lh::document::on_mouse_leave)
/*
        element::ptr                    create_element(const char* tag_name, const string_map& attributes);
        element::ptr                    root();
        void                            get_fixed_boxes(position::vector& fixed_boxes);
        void                            add_fixed_box(const position& pos);
        void                            add_media_list(const media_query_list::ptr& list);
        bool                            media_changed();
        bool                            lang_changed();
        bool                            match_lang(const string& lang);
        void                            add_tabular(const std::shared_ptr<render_item>& el);
        element::const_ptr              get_over_element() const { return m_over_element; }

        void                            append_children_from_string(element& parent, const char* str);
*/
    ;
/*
    struct list_marker
    {
        string            image;
        const char*        baseurl;
        list_style_type    marker_type;
        web_color        color;
        position        pos;
        int                index;
        uint_ptr        font;
    };
*/
    py::enum_<lh::render_type>(m, "render_type", py::arithmetic())
        .value("render_all", lh::render_type::render_all)
        .value("render_no_fixed", lh::render_type::render_no_fixed)
        .value("render_fixed_only", lh::render_type::render_fixed_only)
        .export_values()
    ;
/*
    struct def_color
    {
        const char*    name;
        const char*    rgb;
    };

    extern def_color g_def_colors[];
*/
    py::class_<lh::web_color>(m, "web_color")
        .def(py::init<>())
        .def(py::init<int,int,int,int>())
        .def_readwrite("red", &lh::web_color::red)
        .def_readwrite("green", &lh::web_color::green)
        .def_readwrite("blue", &lh::web_color::blue)
        .def_readwrite("alpha", &lh::web_color::alpha)
/*
        static const web_color transparent;
        static const web_color black;
        static const web_color white;

        bool operator==(web_color color) const { return red == color.red && green == color.green && blue == color.blue && alpha == color.alpha; }
        bool operator!=(web_color color) const { return !(*this == color); }

        string to_string() const;
        static web_color    from_string(const string& str, document_container* callback);
        static string        resolve_name(const string& name, document_container* callback);
        static bool            is_color(const string& str, document_container* callback);
*/
    ;
    py::class_<lh::margins>(m, "margins")
        .def(py::init<>())
        .def_readwrite("left", &lh::margins::left)
        .def_readwrite("top", &lh::margins::top)
        .def_readwrite("right", &lh::margins::right)
        .def_readwrite("bottom", &lh::margins::bottom)
        .def("width", &lh::margins::width)
        .def("height", &lh::margins::height)
    ;
    py::class_<lh::size>(m, "size")
        .def(py::init<>())
        .def(py::init<int, int>())
        .def_readwrite("width", &lh::size::width)
        .def_readwrite("height", &lh::size::height)
    ;
    py::class_<lh::position>(m, "position")
        .def(py::init<>())
        .def(py::init<int,int,int,int>())
        .def_readwrite("x", &lh::position::x)
        .def_readwrite("y", &lh::position::y)
        .def_readwrite("width", &lh::position::width)
        .def_readwrite("height", &lh::position::height)
        .def("left", &lh::position::left)
        .def("top", &lh::position::top)
        .def("right", &lh::position::right)
        .def("bottom", &lh::position::bottom)
        //.def(py::self += margins)
        //.def(py::self -= margins)
        //=size
        .def("clear", &lh::position::clear)
        .def("move_to", &lh::position::move_to)
        .def("does_intersect", &lh::position::does_intersect)
        .def("empty", &lh::position::empty)
        .def("is_point_inside", &lh::position::is_point_inside)
    ;
    py::class_<lh::font_metrics>(m, "font_metrics")
        .def(py::init<>())
        .def_readwrite("height", &lh::font_metrics::height)
        .def_readwrite("ascent", &lh::font_metrics::ascent)
        .def_readwrite("descent", &lh::font_metrics::descent)
        .def_readwrite("x_height", &lh::font_metrics::x_height)
        .def_readwrite("draw_spaces", &lh::font_metrics::draw_spaces)
        .def("base_line", &lh::font_metrics::base_line)
    ;
/*
    struct font_item
    {
        uint_ptr        font;
        font_metrics    metrics;
    };
    typedef std::map<string, font_item> fonts_map;
*/
    py::class_<lh::render_item, std::shared_ptr<lh::render_item>>(m, "render_item")
        .def("pos", &lh::render_item::pos)
        //.def("skip", &render_item::skip)
        //void skip(bool val)
        .def("right", &lh::render_item::right)
        .def("left", &lh::render_item::left)
        .def("top", &lh::render_item::top)
        .def("bottom", &lh::render_item::bottom)
        .def("height", &lh::render_item::height)
        .def("width", &lh::render_item::width)
        .def("padding_right", &lh::render_item::padding_right)
        .def("padding_left", &lh::render_item::padding_left)
        .def("padding_top", &lh::render_item::padding_top)
        .def("padding_bottom", &lh::render_item::padding_bottom)
        .def("border_right", &lh::render_item::border_right)
        .def("border_left", &lh::render_item::border_left)
        .def("border_top", &lh::render_item::border_top)
        .def("border_bottom", &lh::render_item::border_bottom)
        .def("margin_right", &lh::render_item::margin_right)
        .def("margin_left", &lh::render_item::margin_left)
        .def("margin_top", &lh::render_item::margin_top)
        .def("margin_bottom", &lh::render_item::margin_bottom)
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

    py::class_<lh::html_tag, py_html_tag, std::shared_ptr<lh::html_tag>>(m, "html_tag")
        .def(py::init<const std::shared_ptr<py_document>&>())
        //.def(py::init<(const lh::element::ptr& parent, const lh::string& style = "display: block")>())
        .def("draw", &lh::html_tag::draw)
        .def("draw_background", &lh::html_tag::draw_background)
        .def("get_tagName",&lh::html_tag::get_tagName)
        .def("get_placement", &lh::html_tag::get_placement)
    ;
    py::class_<lh::element, py_element, std::shared_ptr<lh::element>>(m, "element")
        .def(py::init<const std::shared_ptr<py_document>&>())
        .def("get_placement", &lh::element::get_placement)
    ;
}
