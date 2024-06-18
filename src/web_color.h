    py::class_<lh::web_color>(m, "web_color")
        .def_readwrite("red", &lh::web_color::red)
        .def_readwrite("green", &lh::web_color::green)
        .def_readwrite("blue", &lh::web_color::blue)
        .def_readwrite("alpha", &lh::web_color::alpha)
        .def_readwrite("is_current_color", &lh::web_color::is_current_color)
        .def_property_readonly_static("transparent", [](const py::object &) { return &lh::web_color::transparent; })
        .def_property_readonly_static("black", [](const py::object &) { return &lh::web_color::black; })
        .def_property_readonly_static("white", [](const py::object &) { return &lh::web_color::white; })
        .def_property_readonly_static("current_color", [](const py::object &) { return &lh::web_color::current_color; })
        //
        .def(py::init<>())
        .def(py::init<int,int,int,int>(), "r"_a, "g"_a, "b"_a, "a"_a=255)

        .def("__eq__", &lh::web_color::operator==, py::is_operator())
        .def("__ne__", &lh::web_color::operator!=, py::is_operator())

        .def("darken", &lh::web_color::darken, "fraction"_a)
        .def("__str__", &lh::web_color::to_string)
    ;
