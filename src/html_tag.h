    py::class_<lh::html_tag, py_html_tag, std::shared_ptr<lh::html_tag>>(m, "html_tag")
/*
	protected:
		string_id				m_tag;
		string_id				m_id;
		string_vector			m_str_classes;
		std::vector<string_id>	m_classes;
		litehtml::style			m_style;
		string_map				m_attrs;
		std::vector<string_id>	m_pseudo_classes;

		void			select_all(const css_selector& selector, elements_list& res) override;
public
*/
        .def(py::init<const std::shared_ptr<py_document>&>())
        //.def(py::init<(const lh::element::ptr& parent, const lh::string& style = "display: block")>())
/*
		bool				appendChild(const element::ptr &el) override;
		bool				removeChild(const element::ptr &el) override;
		void				clearRecursive() override;
		string_id			tag() const override;
		string_id			id() const override;
*/
        .def("get_tagName",&lh::html_tag::get_tagName)
/*
		void				set_tagName(const char* tag) override;
		void				set_data(const char* data) override;
		void				set_attr(const char* name, const char* val) override;
		const char*			get_attr(const char* name, const char* def = nullptr) const override;
		void				apply_stylesheet(const litehtml::css& stylesheet) override;
		void				refresh_styles() override;

		bool				is_white_space() const override;
		bool				is_body() const override;
		bool				is_break() const override;

		bool				on_mouse_over() override;
		bool				on_mouse_leave() override;
		bool				on_lbutton_down() override;
		bool				on_lbutton_up() override;
		void				on_click() override;
		bool				set_pseudo_class(string_id cls, bool add) override;
		bool				set_class(const char* pclass, bool add) override;
		bool				is_replaced() const override;
		void				compute_styles(bool recursive = true) override;
*/
        .def("draw", &lh::html_tag::draw)
        .def("draw_background", &lh::html_tag::draw_background)
/*
		template<class Type, property_type property_value_type, Type property_value::* property_value_member>
		const Type&			get_property_impl  (string_id name, bool inherited, const Type&   default_value, uint_ptr css_properties_member_offset) const;
		int					get_enum_property  (string_id name, bool inherited, int           default_value, uint_ptr css_properties_member_offset) const override;
		int					get_int_property   (string_id name, bool inherited, int           default_value, uint_ptr css_properties_member_offset) const override;
		css_length			get_length_property(string_id name, bool inherited, css_length    default_value, uint_ptr css_properties_member_offset) const override;
		web_color			get_color_property (string_id name, bool inherited, web_color     default_value, uint_ptr css_properties_member_offset) const override;
		string				get_string_property(string_id name, bool inherited, const string& default_value, uint_ptr css_properties_member_offset) const override;
		float				get_number_property(string_id name, bool inherited, float         default_value, uint_ptr css_properties_member_offset) const override;
		string_vector		get_string_vector_property(string_id name, bool inherited, const string_vector& default_value, uint_ptr css_properties_member_offset) const override;
		int_vector			get_int_vector_property   (string_id name, bool inherited, const int_vector&    default_value, uint_ptr css_properties_member_offset) const override;
		length_vector		get_length_vector_property(string_id name, bool inherited, const length_vector& default_value, uint_ptr css_properties_member_offset) const override;
		size_vector			get_size_vector_property  (string_id name, bool inherited, const size_vector&   default_value, uint_ptr css_properties_member_offset) const override;
		string				get_custom_property(string_id name, const string& default_value) const override;

		elements_list&	children();

		int					select(const string& selector) override;
		int					select(const css_selector& selector, bool apply_pseudo = true) override;
		int					select(const css_element_selector& selector, bool apply_pseudo = true) override;
		int					select_pseudoclass(const css_attribute_selector& sel);
		int					select_attribute(const css_attribute_selector& sel);

		elements_list		select_all(const string& selector) override;
		elements_list		select_all(const css_selector& selector) override;

		element::ptr		select_one(const string& selector) override;
		element::ptr		select_one(const css_selector& selector) override;

		element::ptr		find_ancestor(const css_selector& selector, bool apply_pseudo = true, bool* is_pseudo = nullptr) override;
		element::ptr		find_adjacent_sibling(const element::ptr& el, const css_selector& selector, bool apply_pseudo = true, bool* is_pseudo = nullptr) override;
		element::ptr		find_sibling(const element::ptr& el, const css_selector& selector, bool apply_pseudo = true, bool* is_pseudo = nullptr) override;
		void				get_text(string& text) override;
		void				parse_attributes() override;

		void				get_content_size(size& sz, int max_width) override;
		void				add_style(const style& style) override;

		bool				is_nth_child(const element::ptr& el, int num, int off, bool of_type) const override;
		bool				is_nth_last_child(const element::ptr& el, int num, int off, bool of_type) const override;
		bool				is_only_child(const element::ptr& el, bool of_type) const override;
		const background*	get_background(bool own_only = false) override;

		string				dump_get_name() override;

	protected:
		void				init_background_paint(position pos, std::vector<background_paint>& bg_paint, const background* bg, const std::shared_ptr<render_item>& ri);
		void				init_one_background_paint(int i, position pos, background_paint& bg_paint, const background* bg, const std::shared_ptr<render_item>& ri);
		void				draw_list_marker( uint_ptr hdc, const position &pos );
		string				get_list_marker_text(int index);
		element::ptr		get_element_before(const style& style, bool create);
		element::ptr		get_element_after(const style& style, bool create);

	private:
		void				handle_counter_properties();
public:
*/
//        .def("get_placement", &lh::element::get_placement)
        .def("get_placement", &lh::html_tag::get_placement)
    ;
