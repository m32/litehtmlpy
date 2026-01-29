/*
	typedef std::map<string, string>					string_map;
	typedef std::list< std::shared_ptr<element> >		elements_list;
	typedef std::vector<int>							int_vector;
	typedef std::vector<string>							string_vector;

	const unsigned int font_decoration_none			= 0x00;
	const unsigned int font_decoration_underline	= 0x01;
	const unsigned int font_decoration_linethrough	= 0x02;
	const unsigned int font_decoration_overline		= 0x04;

	typedef unsigned char	byte;
	typedef unsigned int	ucode_t;
*/
    py::class_<lh::margins>(m, "margins")
        .def_readwrite("left", &lh::margins::left)
        .def_readwrite("top", &lh::margins::top)
        .def_readwrite("right", &lh::margins::right)
        .def_readwrite("bottom", &lh::margins::bottom)
        //
        .def(py::init<>())
        .def("width", &lh::margins::width)
        .def("height", &lh::margins::height)
    ;

    py::class_<lh::size>(m, "size")
        //
        .def(py::init<>())
        .def(py::init<int, int>())
        .def_readwrite("width", &lh::size::width)
        .def_readwrite("height", &lh::size::height)
    ;

    py::class_<lh::position>(m, "position")
        .def_readwrite("x", &lh::position::x)
        .def_readwrite("y", &lh::position::y)
        .def_readwrite("width", &lh::position::width)
        .def_readwrite("height", &lh::position::height)
        //
        .def(py::init<>())
        .def(py::init<int,int,int,int>())
        .def("right", &lh::position::right)
        .def("bottom", &lh::position::bottom)
        .def("left", &lh::position::left)
        .def("top", &lh::position::top)
        //.def(py::self += margins)
        //.def(py::self -= margins)
        //=size
        .def("clear", &lh::position::clear)
        .def("move_to", &lh::position::move_to)
        .def("does_intersect", &lh::position::does_intersect)
        .def("empty", &lh::position::empty)
        .def("is_point_inside", &lh::position::is_point_inside)
    ;

    py::class_<lh::font_metrics>(m, "font_metrics")
        .def_readwrite("height", &lh::font_metrics::height)
        .def_readwrite("ascent", &lh::font_metrics::ascent)
        .def_readwrite("descent", &lh::font_metrics::descent)
        .def_readwrite("x_height", &lh::font_metrics::x_height)
        .def_readwrite("draw_spaces", &lh::font_metrics::draw_spaces)
        //
        .def(py::init<>())
        .def("base_line", &lh::font_metrics::base_line)
    ;

#include "types-enum.h"
