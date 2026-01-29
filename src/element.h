    py::class_<lh::element, py_element, std::shared_ptr<lh::element>>(m, "element")
        .def(py::init<const std::shared_ptr<py_document>&>())
        .def("css", &lh::element::css)
		.def("in_normal_flow", &lh::element::in_normal_flow)
		.def("is_inline", &lh::element::is_inline)
		.def("is_inline_box", &lh::element::is_inline_box)
		.def("is_block_box", &lh::element::is_block_box)
        .def("get_placement", &lh::element::get_placement)
		.def("is_positioned", &lh::element::is_positioned)
		.def("is_float", &lh::element::is_float)
		.def("is_block_formatting_context", &lh::element::is_block_formatting_context)
		.def("is_root", &lh::element::is_root)
//		.def("parent", &lh::element::parent)
//		void						parent(const element::ptr& par)
		.def("is_table_skip", &lh::element::is_table_skip)
		.def("children", &lh::element::children)

//		virtual elements_list		select_all(const string& selector)
//		virtual elements_list		select_all(const css_selector& selector)

//		virtual element::ptr		select_one(const string& selector)
//		virtual element::ptr		select_one(const css_selector& selector)

//		virtual bool				appendChild(const ptr &el)
//		virtual bool				removeChild(const ptr &el)
//		virtual void				.def("clearRecursive", &lh::element::clearRecursive)

		.def("id", &lh::element::id)
		.def("tag", &lh::element::tag)
		.def("get_tagName", &lh::element::get_tagName)
//		virtual void				set_tagName(const char* tag);
//		virtual void				set_data(const char* data);

//		virtual void				set_attr(const char* name, const char* val);
//		virtual const char*			get_attr(const char* name, const char* def = nullptr) const;
//		virtual void				apply_stylesheet(const litehtml::css& stylesheet);
		.def("refresh_styles", &lh::element::refresh_styles)
		.def("is_white_space", &lh::element::is_white_space)
		.def("is_space", &lh::element::is_space)
		.def("is_comment", &lh::element::is_comment)
		.def("is_body", &lh::element::is_body)
		.def("is_break", &lh::element::is_break)
		.def("is_text", &lh::element::is_text)

		.def("on_mouse_over", &lh::element::on_mouse_over)
		.def("on_mouse_leave", &lh::element::on_mouse_leave)
		.def("on_lbutton_down", &lh::element::on_lbutton_down)
		.def("on_lbutton_up", &lh::element::on_lbutton_up)
		.def("on_click", &lh::element::on_click)
//		virtual bool				set_pseudo_class(string_id cls, bool add);
//		virtual bool				set_class(const char* pclass, bool add);
		.def("is_replaced", &lh::element::is_replaced)
//		virtual void				compute_styles(bool recursive = true);
//		virtual void				draw(uint_ptr hdc, int x, int y, const position *clip, const std::shared_ptr<render_item>& ri);
//		virtual void				draw_background(uint_ptr hdc, int x, int y, const position *clip, const std::shared_ptr<render_item> &ri);
//		virtual int					get_enum_property  (string_id name, bool inherited, int           default_value, uint_ptr css_properties_member_offset) const;
//		virtual int					get_int_property   (string_id name, bool inherited, int           default_value, uint_ptr css_properties_member_offset) const;
//		virtual css_length			get_length_property(string_id name, bool inherited, css_length    default_value, uint_ptr css_properties_member_offset) const;
//		virtual web_color			get_color_property (string_id name, bool inherited, web_color     default_value, uint_ptr css_properties_member_offset) const;
//		virtual string				get_string_property(string_id name, bool inherited, const string& default_value, uint_ptr css_properties_member_offset) const;
//		virtual float				get_number_property(string_id name, bool inherited, float         default_value, uint_ptr css_properties_member_offset) const;
//		virtual string_vector		get_string_vector_property(string_id name, bool inherited, const string_vector& default_value, uint_ptr css_properties_member_offset) const;
//		virtual int_vector			get_int_vector_property   (string_id name, bool inherited, const int_vector&    default_value, uint_ptr css_properties_member_offset) const;
//		virtual length_vector		get_length_vector_property(string_id name, bool inherited, const length_vector& default_value, uint_ptr css_properties_member_offset) const;
//		virtual size_vector			get_size_vector_property  (string_id name, bool inherited, const size_vector&   default_value, uint_ptr css_properties_member_offset) const;
//		virtual string				get_custom_property(string_id name, const string& default_value) const;

//		virtual void				get_text(string& text);
//		virtual void				parse_attributes();
//		virtual int					select(const string& selector);
//		virtual int					select(const css_selector& selector, bool apply_pseudo = true);
//		virtual int					select(const css_element_selector& selector, bool apply_pseudo = true);
//		virtual element::ptr		find_ancestor(const css_selector& selector, bool apply_pseudo = true, bool* is_pseudo = nullptr);
//		virtual bool				is_ancestor(const ptr &el) const;
//		virtual element::ptr		find_adjacent_sibling(const element::ptr& el, const css_selector& selector, bool apply_pseudo = true, bool* is_pseudo = nullptr);
//		virtual element::ptr		find_sibling(const element::ptr& el, const css_selector& selector, bool apply_pseudo = true, bool* is_pseudo = nullptr);
//		virtual void				get_content_size(size& sz, int max_width);
//		virtual bool				is_nth_child(const element::ptr& el, int num, int off, bool of_type) const;
//		virtual bool				is_nth_last_child(const element::ptr& el, int num, int off, bool of_type) const;
//		virtual bool				is_only_child(const element::ptr& el, bool of_type) const;
//		virtual void				add_style(const style& style);
//		virtual const background*	get_background(bool own_only = false);

//		virtual string				dump_get_name();
//		virtual std::vector<std::tuple<string, string>> dump_get_attrs();
//		void						dump(litehtml::dumper& cout);

//		std::tuple<element::ptr, element::ptr, element::ptr> split_inlines();
//		virtual std::shared_ptr<render_item> create_render_item(const std::shared_ptr<render_item>& parent_ri);
//		bool requires_styles_update();
//		void add_render(const std::shared_ptr<render_item>& ri);
//		bool find_styles_changes( position::vector& redraw_boxes);
//		element::ptr add_pseudo_before(const style& style)
//		element::ptr add_pseudo_after(const style& style)
//		string				get_counter_value(const string& counter_name);
//		string				get_counters_value(const string_vector& parameters);
//		void				increment_counter(const string_id& counter_name_id, const int increment = 1);
//		void				reset_counter(const string_id& counter_name_id, const int value = 0);
    ;
