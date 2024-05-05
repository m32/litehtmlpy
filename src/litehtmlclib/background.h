    py::class_<lh::background_layer>(m, "background_layer")
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
	;
