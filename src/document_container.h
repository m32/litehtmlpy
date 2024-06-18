    py::class_<lh::document_container, py_document_container, std::unique_ptr<lh::document_container, py::nodelete>>(m, "document_container")
        .def(py::init<>())
    ;
#ifdef USE_CAIRO_CONTAINERS
#if 0
    py::class_<container_cairo, py_document_container_cairo, std::unique_ptr<container_cairo, py::nodelete>>(m, "container_cairo")
        .def(py::init<>())
    ;
#endif
    py::class_<container_cairo_pango, py_document_container_cairo_pango, std::unique_ptr<container_cairo_pango, py::nodelete>>(m, "container_cairo_pango")
        .def(py::init<>())
        .def("surface", &container_cairo_pango::surface, "width"_a, "height"_a)
        .def("save", &container_cairo_pango::save, "fname"_a)
        .def("fromString", [](
            py_document_container_cairo_pango &self,
            char *html,
            const char *master_css = lh::master_css,
            const char *user_styles = ""
        ) {
            py::gil_scoped_release release;
            if( master_css == nullptr )
                master_css = lh::master_css;
            if( user_styles == nullptr )
                user_styles = "";
            lh::document::ptr doc = lh::document::createFromString(html, &self, master_css, user_styles);
            return doc;
    })
    ;
    ;
#endif
