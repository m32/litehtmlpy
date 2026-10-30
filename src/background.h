    py::class_<lh::background_layer>(m, "background_layer")
        .def_readwrite("border_box", &lh::background_layer::border_box)
        .def_readwrite("border_radius", &lh::background_layer::border_radius)
        .def_readwrite("clip_box", &lh::background_layer::clip_box)
        .def_readwrite("origin_box", &lh::background_layer::origin_box)
        .def_readwrite("attachment", &lh::background_layer::attachment)
        .def_readwrite("repeat", &lh::background_layer::repeat)
        .def_readwrite("is_root", &lh::background_layer::is_root)
        //
        .def(py::init<>())
    ;
    py::class_<lh::background_layer::image>(m, "background_layer_image")
        .def_readwrite("url", &lh::background_layer::image::url)
        .def_readwrite("base_url", &lh::background_layer::image::base_url)
    ;
    py::class_<lh::background_layer::color_point>(m, "background_layer_color_point")
        .def_readwrite("offset", &lh::background_layer::color_point::offset)
        .def_readwrite("color", &lh::background_layer::color_point::color)
        .def_readwrite("hint", &lh::background_layer::color_point::hint)
        //
        .def(py::init<>())
        .def(py::init<float, lh::web_color>(), "offset"_a, "color"_a)
    ;
    py::class_<lh::background_layer::color>(m, "background_layer_color")
        .def_readwrite("color", &lh::background_layer::color::color)
    ;
    py::class_<lh::background_layer::gradient_base>(m, "background_layer_gradient_base")
        .def_readwrite("color_points", &lh::background_layer::gradient_base::color_points)
    ;
    py::class_<lh::background_layer::linear_gradient, lh::background_layer::gradient_base>(m, "background_layer_linear_gradient")
        .def_readwrite("start", &lh::background_layer::linear_gradient::start)
        .def_readwrite("end", &lh::background_layer::linear_gradient::end)
    ;
    py::class_<lh::background_layer::radial_gradient, lh::background_layer::gradient_base>(m, "background_layer_radial_gradient")
        .def_readwrite("position", &lh::background_layer::radial_gradient::position)
        .def_readwrite("radius", &lh::background_layer::radial_gradient::radius)
    ;
    py::class_<lh::background_layer::conic_gradient, lh::background_layer::gradient_base>(m, "background_layer_conic_gradient")
        .def_readwrite("position", &lh::background_layer::conic_gradient::position)
        .def_readwrite("angle", &lh::background_layer::conic_gradient::angle)
        .def_readwrite("radius", &lh::background_layer::conic_gradient::radius)
    ;
    py::enum_<lh::background::layer_type>(m, "layer_type")
        .value("type_none", lh::background::layer_type::type_none)
        .value("type_color", lh::background::layer_type::type_color)
        .value("type_image", lh::background::layer_type::type_image)
        .value("type_linear_gradient", lh::background::layer_type::type_linear_gradient)
        .value("type_radial_gradient", lh::background::layer_type::type_radial_gradient)
        .value("type_conic_gradient", lh::background::layer_type::type_conic_gradient)
    ;

    py::class_<lh::background>(m, "background")
        .def_readwrite("m_image", &lh::background::m_image)
        .def_readwrite("m_baseurl", &lh::background::m_baseurl)
        .def_readwrite("m_color", &lh::background::m_color)
        .def_readwrite("m_attachment", &lh::background::m_attachment)
        .def_readwrite("m_position_x", &lh::background::m_position_x)
        .def_readwrite("m_position_y", &lh::background::m_position_y)
        .def_readwrite("m_size", &lh::background::m_size)
        .def_readwrite("m_repeat", &lh::background::m_repeat)
        .def_readwrite("m_clip", &lh::background::m_clip)
        .def_readwrite("m_origin", &lh::background::m_origin)
        //
        .def("is_empty", &lh::background::is_empty)
        .def("get_layers_number", &lh::background::get_layers_number)
        .def("get_layer", &lh::background::get_layer, "idx"_a, "pos"_a, "el"_a, "ri"_a, "layer"_a)
        .def("get_layer_type", &lh::background::get_layer_type, "idx"_a)
        .def("get_image_layer", &lh::background::get_image_layer, "idx"_a)
        .def("get_color_layer", &lh::background::get_color_layer, "idx"_a)
        .def("get_linear_gradient_layer", &lh::background::get_linear_gradient_layer, "idx"_a, "layer"_a)
        .def("get_radial_gradient_layer", &lh::background::get_radial_gradient_layer, "idx"_a, "layer"_a)
        .def("get_conic_gradient_layer", &lh::background::get_conic_gradient_layer, "idx"_a, "layer"_a)
        .def("draw_layer", &lh::background::draw_layer, "hdc"_a, "idx"_a, "layer"_a, "container"_a)
    ;
