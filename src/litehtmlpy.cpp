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

#include <litehtml/background.h>
#include <litehtml/borders.h>
#include <litehtml/css_length.h>

#include <iostream>
#include <string>

namespace lh = litehtml;
namespace py = pybind11;

static int debuglog = 0;
#define ENTERWRAPPER std::cout << "PyLiteHtml::" << __FUNCTION__ << std::endl;
//#define ENTERWRAPPER

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
            hdc, x, y, clip, ri
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
            hdc, x, y, clip, ri
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
#if 0
        py::gil_scoped_acquire gil;
        py::function override = pybind11::get_override(this, "get_image_size");
        if (override) {
            std::cout << "get_image_size.1: " << src;
            std::cout << "," << (baseurl != nullptr ? baseurl : "NULL" ); 
            std::cout << ",(" << sz.width;
            std::cout << "," << sz.height;
            std::cout << ")" << std::endl; 
            auto obj = override(src, baseurl, &sz);
            std::cout << "get_image_size.2: " << src;
            std::cout << "," << (baseurl != nullptr ? baseurl : "NULL" ); 
            std::cout << ",(" << sz.width;
            std::cout << "," << sz.height;
            std::cout << ")" << std::endl; 
        } else {
            std::cout << "get_image_size is pure" << std::endl; 
        }
#else
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            get_image_size,
            src, baseurl, &sz
        );
#endif
    }
    void    draw_background(lh::uint_ptr hdc, const std::vector<lh::background_paint>& bg) override
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            draw_background,
            hdc, bg
        );
    }
    void    draw_borders(lh::uint_ptr hdc, const lh::borders& borders, const lh::position& draw_pos, bool root) override
    {
        if( debuglog ){
            ENTERWRAPPER
        }
        PYBIND11_OVERRIDE_PURE(
            void,
            document_container,
            draw_borders,
            hdc, borders, draw_pos, root
        );
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
            url, el
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
            text, tt
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
            &client
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

#include "litehtmlclib/background.h"
#include "litehtmlclib/borders.h"
#include "litehtmlclib/css_length.h"
#include "litehtmlclib/css_margins.h"
#include "litehtmlclib/css_offsets.h"
#include "litehtmlclib/css_position.h"
#include "litehtmlclib/css_properties.h"
//#include "litehtmlclib/css_selector.h"
#include "litehtmlclib/document.h"
#include "litehtmlclib/document_container.h"
#include "litehtmlclib/element.h"
//#include "litehtmlclib/flex_item.h"
//#include "litehtmlclib/flex_line.h"
//#include "litehtmlclib/formatting_context.h"
//#include "litehtmlclib/html.h"
#include "litehtmlclib/html_tag.h"
//#include "litehtmlclib/iterators.h"
//#include "litehtmlclib/line_box.h"
//#include "litehtmlclib/litehtml.h"
//#include "litehtmlclib/master_css.h"
//#include "litehtmlclib/media_query.h"
//#include "litehtmlclib/num_cvt.h"
//#include "litehtmlclib/os_types.h"
//#include "litehtmlclib/render_block.h"
//#include "litehtmlclib/render_block_context.h"
//#include "litehtmlclib/render_flex.h"
//#include "litehtmlclib/render_image.h"
//#include "litehtmlclib/render_inline.h"
//#include "litehtmlclib/render_inline_context.h"
#include "litehtmlclib/render_item.h"
//#include "litehtmlclib/render_table.h"
//#include "litehtmlclib/string_id.h"
//#include "litehtmlclib/style.h"
//#include "litehtmlclib/stylesheet.h"
//#include "litehtmlclib/table.h"
//#include "litehtmlclib/tstring_view.h"
#include "litehtmlclib/types.h"
#include "litehtmlclib/web_color.h"
}
