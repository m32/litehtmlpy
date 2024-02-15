    py::class_<lh::css_offsets>(m, "css_offsets")
		.def_readwrite("left", &lh::css_offsets::left)
		.def_readwrite("right", &lh::css_offsets::right)
		.def_readwrite("top", &lh::css_offsets::top)
		.def_readwrite("bottom", &lh::css_offsets::bottom)
        //
        .def(py::init<>())
        .def(py::init<const lh::css_offsets&>())
		//css_offsets& operator=(const css_offsets& val)
        .def("to_string", &lh::css_offsets::to_string)
    ;
