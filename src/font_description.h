    py::class_<lh::font_description>(m, "font_description")
        .def_readwrite("family", &lh::font_description::family)
        .def_readwrite("size", &lh::font_description::size)
        .def_readwrite("style", &lh::font_description::style)
        .def_readwrite("weight", &lh::font_description::weight)
        .def_readwrite("decoration_line", &lh::font_description::decoration_line)
        .def_readwrite("decoration_thickness", &lh::font_description::decoration_thickness)
        .def_readwrite("decoration_style", &lh::font_description::decoration_style)
        .def_readwrite("decoration_color", &lh::font_description::decoration_color)
        //
        .def(py::init<>())
    ;

