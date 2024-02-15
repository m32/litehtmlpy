    py::class_<lh::render_item, std::shared_ptr<lh::render_item>>(m, "render_item")
/*
        explicit render_item(std::shared_ptr<element>  src_el);

        virtual ~render_item() = default;

        std::list<std::shared_ptr<render_item>>& children()
        {
            return m_children;
        }
*/
        .def("pos", &lh::render_item::pos)
        //.def("skip", &lh::render_item::skip)
        //void skip(bool val)
        .def("right", &lh::render_item::right)
        .def("left", &lh::render_item::left)
        .def("top", &lh::render_item::top)
        .def("bottom", &lh::render_item::bottom)
        .def("height", &lh::render_item::height)
        .def("width", &lh::render_item::width)
        .def("padding_top", &lh::render_item::padding_top)
        .def("padding_bottom", &lh::render_item::padding_bottom)
        .def("padding_left", &lh::render_item::padding_left)
        .def("padding_right", &lh::render_item::padding_right)
        .def("border_top", &lh::render_item::border_top)
        .def("border_bottom", &lh::render_item::border_bottom)
        .def("border_left", &lh::render_item::border_left)
        .def("border_right", &lh::render_item::border_right)
        .def("margin_top", &lh::render_item::margin_top)
        .def("margin_bottom", &lh::render_item::margin_bottom)
        .def("margin_left", &lh::render_item::margin_left)
        .def("margin_right", &lh::render_item::margin_right)
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
		bool is_flex_item() const
		int render(int x, int y, const containing_block_context& containing_block_size, formatting_context* fmt_ctx, bool second_pass = false);
        void apply_relative_shift(const containing_block_context &containing_block_size);
        void calc_outlines( int parent_width );
        int calc_auto_margins(int parent_width);	// returns left margin

        virtual std::shared_ptr<render_item> init();
        virtual void apply_vertical_align() {}
		virtual int get_first_baseline() { return height() - margin_bottom(); }
		virtual int get_last_baseline() { return height() - margin_bottom(); }

        virtual std::shared_ptr<render_item> clone()
        {
            return std::make_shared<render_item>(src_el());
        }
        std::tuple<
                std::shared_ptr<litehtml::render_item>,
                std::shared_ptr<litehtml::render_item>,
                std::shared_ptr<litehtml::render_item>
                > split_inlines();
        bool fetch_positioned();
        void render_positioned(render_type rt = render_all);
        void add_positioned(const std::shared_ptr<litehtml::render_item> &el);
        void get_redraw_box(litehtml::position& pos, int x = 0, int y = 0);
        void calc_document_size( litehtml::size& sz, litehtml::size& content_size, int x = 0, int y = 0 );
		virtual void get_inline_boxes( position::vector& boxes ) const {};
		virtual void set_inline_boxes( position::vector& boxes ) {};
		virtual void add_inline_box( const position& box ) {};
		virtual void clear_inline_boxes() {};
        void draw_stacking_context( uint_ptr hdc, int x, int y, const position* clip, bool with_positioned );
        virtual void draw_children( uint_ptr hdc, int x, int y, const position* clip, draw_flag flag, int zindex );
        virtual int get_draw_vertical_offset() { return 0; }
        virtual std::shared_ptr<element> get_child_by_point(int x, int y, int client_x, int client_y, draw_flag flag, int zindex);
        std::shared_ptr<element> get_element_by_point(int x, int y, int client_x, int client_y);
        bool is_point_inside( int x, int y );
        void dump(litehtml::dumper& cout);
        position get_placement() const;
        void get_rendering_boxes( position::vector& redraw_boxes);
*/
    ;
