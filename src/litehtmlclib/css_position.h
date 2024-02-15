    py::class_<lh::css_position>(m, "css_position")
		.def_readwrite("x", &lh::css_position::x)
		.def_readwrite("y", &lh::css_position::y)
		.def_readwrite("width", &lh::css_position::width)
		.def_readwrite("height", &lh::css_position::height)
    ;
    py::class_<lh::css_size>(m, "css_size")
		.def_readwrite("width", &lh::css_size::width)
		.def_readwrite("height", &lh::css_size::height)
        //
        .def(py::init<lh::css_length, lh::css_length>())
    ;
