    py::class_<lh::css_text>(m, "css_text")
		.def_readwrite("text", &lh::css_text::text)
		.def_readwrite("baseurl", &lh::css_text::baseurl)
		.def_readwrite("media", &lh::css_text::media)
        //
        .def(py::init<>())
        .def(py::init<const lh::css_text&>())
    ;
#if 0
    class dumper
    {
    public:
        virtual ~dumper() {}
        virtual void begin_node(const litehtml::string& descr) = 0;
        virtual void end_node() = 0;
        virtual void begin_attrs_group(const litehtml::string& descr) = 0;
        virtual void end_attrs_group() = 0;
        virtual void add_attr(const litehtml::string& name, const litehtml::string& value) = 0;
    };
#endif

    py::class_<lh::document, py_document, std::shared_ptr<lh::document>>(m, "document")
		//document(document_container* objContainer);
		//virtual ~document();
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
		void							dump(dumper& cout);
*/
    ;

    m.def("fromString", [](py_document_container *container, char *html, const char *master_css = lh::master_css, const char *user_styles = "") {
        py::gil_scoped_release release;
        if( master_css == nullptr )
            master_css = lh::master_css;
        if( user_styles == nullptr )
            user_styles = "";
#if 1
        lh::document::ptr doc = lh::document::createFromString(html, container, master_css, user_styles);
        return doc;
#else
        auto doc = lh::document::createFromString(html, container, master_css, user_styles);
        py::object o = py::cast(doc, py::return_value_policy::reference);
        return o;
#endif
    })
    ;
