    py::class_<lh::document_container, py_document_container, std::unique_ptr<lh::document_container, py::nodelete>>(m, "document_container")
        .def(py::init<>())
    ;
