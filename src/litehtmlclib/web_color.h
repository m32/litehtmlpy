/*
	struct def_color
	{
		const char*	name;
		const char*	rgb;
	};

	extern def_color g_def_colors[];
*/

    py::class_<lh::web_color>(m, "web_color")
        .def_readwrite("red", &lh::web_color::red)
        .def_readwrite("green", &lh::web_color::green)
        .def_readwrite("blue", &lh::web_color::blue)
        .def_readwrite("alpha", &lh::web_color::alpha)
        //
        .def(py::init<>())
        .def(py::init<int,int,int,int>())
/*
        static const web_color transparent;
        static const web_color black;
        static const web_color white;

        bool operator==(web_color color) const { return red == color.red && green == color.green && blue == color.blue && alpha == color.alpha; }
        bool operator!=(web_color color) const { return !(*this == color); }

        string to_string() const;
        static web_color    from_string(const string& str, document_container* callback);
        static string        resolve_name(const string& name, document_container* callback);
        static bool            is_color(const string& str, document_container* callback);
*/
    ;
