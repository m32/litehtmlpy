    py::class_<lh::css_border>(m, "css_border")
		.def_readwrite("width", &lh::css_border::width)
		.def_readwrite("style", &lh::css_border::style)
		.def_readwrite("style", &lh::css_border::color)
        //
        .def(py::init<>())
        .def(py::init<const lh::css_border&>())
		//css_border& operator=(const css_border& val)
        .def("to_string", &lh::css_border::to_string)
	;

    py::class_<lh::border>(m, "border")
		.def_readwrite("width", &lh::border::width)
		.def_readwrite("style", &lh::border::style)
		.def_readwrite("color", &lh::border::color)
        //
        .def(py::init<>())
        .def(py::init<const lh::border&>())
        .def(py::init<const lh::css_border&>())
		//border& operator=(const border& val)
		//border& operator=(const css_border& val)
	;

    py::class_<lh::border_radiuses>(m, "border_radiuses")
		.def_readwrite("top_left_x", &lh::border_radiuses::top_left_x)
		.def_readwrite("top_left_y", &lh::border_radiuses::top_left_y)
        .def_readwrite("top_right_x", &lh::border_radiuses::top_right_x)
		.def_readwrite("top_right_y", &lh::border_radiuses::top_right_y)
        .def_readwrite("bottom_right_x", &lh::border_radiuses::bottom_right_x)
		.def_readwrite("bottom_right_y", &lh::border_radiuses::bottom_right_y)
        .def_readwrite("bottom_left_x", &lh::border_radiuses::bottom_left_x)
		.def_readwrite("bottom_left_y", &lh::border_radiuses::bottom_left_y)
        //
        .def(py::init<>())
        .def(py::init<const lh::border_radiuses&>())
		//border_radiuses& operator = (const border_radiuses& val)
		//void operator += (const margins& mg)
		//void operator -= (const margins& mg)
		//.def("fix_values", &lh::border_radiuses::fix_values)
		//void fix_values(int width, int height)
	;

    py::class_<lh::css_border_radius>(m, "css_border_radius")
		.def_readwrite("top_left_x", &lh::css_border_radius::top_left_x)
		.def_readwrite("top_left_y", &lh::css_border_radius::top_left_y)
        .def_readwrite("top_right_x", &lh::css_border_radius::top_right_x)
		.def_readwrite("top_right_y", &lh::css_border_radius::top_right_y)
        .def_readwrite("bottom_right_x", &lh::css_border_radius::bottom_right_x)
		.def_readwrite("bottom_right_y", &lh::css_border_radius::bottom_right_y)
        .def_readwrite("bottom_left_x", &lh::css_border_radius::bottom_left_x)
		.def_readwrite("bottom_left_y", &lh::css_border_radius::bottom_left_y)
        //
        .def(py::init<>())
        .def(py::init<const lh::css_border_radius&>())
		//css_border_radius& operator=(const css_border_radius& val)
		//border_radiuses calc_percents(int width, int height) const
	;

    py::class_<lh::css_borders>(m, "css_borders")
		.def_readwrite("left", &lh::css_borders::left)
		.def_readwrite("top", &lh::css_borders::top)
		.def_readwrite("right", &lh::css_borders::right)
		.def_readwrite("bottom", &lh::css_borders::bottom)
		.def_readwrite("radius", &lh::css_borders::radius)
        //
		//?css_borders() = default;
        .def(py::init<>())
        //.def(py::init<const &lh::css_borders&>())
		.def("is_visible", &lh::css_borders::is_visible)
		//css_borders& operator=(const css_borders& val)
		.def("to_string", &lh::css_borders::to_string)
	;

    py::class_<lh::borders>(m, "borders")
		.def_readwrite("left", &lh::borders::left)
		.def_readwrite("top", &lh::borders::top)
		.def_readwrite("right", &lh::borders::right)
		.def_readwrite("bottom", &lh::borders::bottom)
		.def_readwrite("radius", &lh::borders::radius)

		//?borders() = default;
        .def(py::init<>())
        //.def(py::init<const &lh::borders&>())
        //.def(py::init<const &lh::css_borders&>())
		.def("is_visible", &lh::borders::is_visible)
		//borders& operator=(const borders& val)
		//borders& operator=(const css_borders& val)
	;
