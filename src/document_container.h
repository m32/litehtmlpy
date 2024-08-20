/*
typedef struct
{
    unsigned char *current_position;
    unsigned char *end_of_array;
} png_stream_to_byte_array_closure_t;

static cairo_status_t write_png_stream_to_byte_array (void *in_closure, const unsigned char *data, unsigned int length)
{
    png_stream_to_byte_array_closure_t *closure = (png_stream_to_byte_array_closure_t *) in_closure;
    if ((closure->current_position + length) > (closure->end_of_array))
        return CAIRO_STATUS_WRITE_ERROR;
    memcpy (closure->current_position, data, length);
    closure->current_position += length;
    return CAIRO_STATUS_SUCCESS;
}

    closure.current_position = byte_array;
    closure.end_of_array = byte_array + sizeof (byte_array);
    cairo_surface_write_to_png_stream (surface, write_png_stream_to_byte_array, &closure);

*/
    py::enum_<lh::mouse_event>(m, "mouse_event")
        .value("mouse_event_enter", lh::mouse_event::mouse_event_enter)
        .value("mouse_event_leave", lh::mouse_event::mouse_event_leave)
    ;

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
        .def("savestream", [](
            py_document_container_cairo_pango &self,
            const py::function &pyfunc
        ) {
            cairo_surface_t *surface = self.getsurface();
            cairosavestream_t st; st.pyfunc = pyfunc;
            cairo_status_t status = cairo_surface_write_to_png_stream(surface, &cairosavestream, &st);
            return (int)status;
        })
        .def("clear_images", [](
            py_document_container_cairo_pango &self
        ) {
            return self.clear_images();
        })
        .def("put_image", [](
            py_document_container_cairo_pango &self,
            const std::string& url,
            py::bytearray data,
            int width,
            int height
        ) {
            return self.put_image(url, data, width, height);
        })
        .def("set_dpi", [](
            py_document_container_cairo_pango &self,
            int dpi
        ) {
            self.set_dpi(dpi);
        })
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
