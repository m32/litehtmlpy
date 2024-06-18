    py::class_<lh::css_margins>(m, "css_margins")
		.def_readwrite("left", &lh::css_margins::left)
		.def_readwrite("right", &lh::css_margins::right)
		.def_readwrite("top", &lh::css_margins::top)
		.def_readwrite("bottom", &lh::css_margins::bottom)
        //
        .def(py::init<>())
        .def(py::init<const lh::css_margins&>())
		//css_margins& operator=(const css_margins& val)
        .def("to_string", &lh::css_margins::to_string)
    ;
