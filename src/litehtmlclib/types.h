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

/*
	struct font_item
	{
		uint_ptr		font;
		font_metrics	metrics;
	};

	typedef std::map<string, font_item> fonts_map;
*/

    py::enum_<lh::draw_flag>(m, "draw_flag", py::arithmetic())
        .value("draw_root", lh::draw_flag::draw_root)
        .value("draw_block", lh::draw_flag::draw_block)
        .value("draw_floats", lh::draw_flag::draw_floats)
        .value("draw_inlines", lh::draw_flag::draw_inlines)
        .value("draw_positioned", lh::draw_flag::draw_positioned)
        .export_values()
    ;
#if 0
	struct containing_block_context
	{
		enum cbc_value_type
		{
			cbc_value_type_absolute,	// width/height of containing block is defined as absolute value
			cbc_value_type_percentage,	// width/height of containing block is defined as percentage
			cbc_value_type_auto,		// width/height of containing block is defined as auto
			cbc_value_type_none,		// min/max width/height of containing block is defined as none
		};

		enum cbc_size_mode
		{
			size_mode_normal = 0x00,
			size_mode_exact_width = 0x01,
			size_mode_exact_height = 0x02,
			size_mode_content = 0x04,
		};

		struct typed_int
		{
			int 			value;
			cbc_value_type	type;

			typed_int(int val, cbc_value_type tp)
			{
				value = val;
				type = tp;
			}

			operator int() const
			{
				return value;
			}

			typed_int& operator=(int val)
			{
				value = val;
				return *this;
			}

			typed_int& operator=(const typed_int& v)
			{
				value = v.value;
				type = v.type;
				return *this;
			}
		};

		typed_int width;						// width of the containing block
		typed_int render_width;
		typed_int min_width;
		typed_int max_width;

		typed_int height;						// height of the containing block
		typed_int min_height;
		typed_int max_height;

		int context_idx;
		uint32_t size_mode;

		containing_block_context() :
				width(0, cbc_value_type_auto),
				render_width(0, cbc_value_type_auto),
				min_width(0, cbc_value_type_none),
				max_width(0, cbc_value_type_none),
				height(0, cbc_value_type_auto),
				min_height(0, cbc_value_type_none),
				max_height(0, cbc_value_type_none),
				context_idx(0),
				size_mode(size_mode_normal)
		{}

		containing_block_context new_width(int w, uint32_t _size_mode = size_mode_normal) const
		{
			containing_block_context ret = *this;
			ret.render_width = w - (ret.width - ret.render_width);
			ret.width = w;
			ret.size_mode = _size_mode;
			return ret;
		}

		containing_block_context new_width_height(int w, int h, uint32_t _size_mode = size_mode_normal) const
		{
			containing_block_context ret = *this;
			ret.render_width = w - (ret.width - ret.render_width);
			ret.width = w;
			ret.height = h;
			ret.size_mode = _size_mode;
			return ret;
		}
	};
#endif

    py::enum_<lh::style_display>(m, "style_display", py::arithmetic())
        .value("display_none", lh::style_display::display_none)
        .value("display_block", lh::style_display::display_block)
        .value("display_inline", lh::style_display::display_inline)
        .value("display_inline_block", lh::style_display::display_inline_block)
        .value("display_inline_table", lh::style_display::display_inline_table)
        .value("display_list_item", lh::style_display::display_list_item)
        .value("display_table", lh::style_display::display_table)
        .value("display_table_caption", lh::style_display::display_table_caption)
        .value("display_table_cell", lh::style_display::display_table_cell)
        .value("display_table_column", lh::style_display::display_table_column)
        .value("display_table_column_group", lh::style_display::display_table_column_group)
        .value("display_table_footer_group", lh::style_display::display_table_footer_group)
        .value("display_table_header_group", lh::style_display::display_table_header_group)
        .value("display_table_row", lh::style_display::display_table_row)
        .value("display_table_row_group", lh::style_display::display_table_row_group)
        .value("display_inline_text", lh::style_display::display_inline_text)
        .value("display_flex", lh::style_display::display_flex)
        .value("display_inline_flex", lh::style_display::display_inline_flex)
        .export_values()
        ;

    py::enum_<lh::font_size>(m, "font_size", py::arithmetic())
        .value("font_size_xx_small", lh::font_size::font_size_xx_small)
        .value("font_size_x_small", lh::font_size::font_size_x_small)
        .value("font_size_small", lh::font_size::font_size_small)
        .value("font_size_medium", lh::font_size::font_size_medium)
        .value("font_size_large", lh::font_size::font_size_large)
        .value("font_size_x_large", lh::font_size::font_size_x_large)
        .value("font_size_xx_large", lh::font_size::font_size_xx_large)
        .value("font_size_smaller", lh::font_size::font_size_smaller)
        .value("font_size_larger", lh::font_size::font_size_larger)
        .export_values()
        ;

    py::enum_<lh::line_height>(m, "line_height", py::arithmetic())
        .value("line_height_normal", lh::line_height::line_height_normal)
        .export_values()
        ;

    py::enum_<lh::font_style>(m, "font_style", py::arithmetic())
        .value("font_style_normal", lh::font_style::font_style_normal)
        .value("font_style_italic", lh::font_style::font_style_italic)
        .export_values()
        ;

    py::enum_<lh::font_variant>(m, "font_variant", py::arithmetic())
        .value("font_variant_normal", lh::font_variant::font_variant_normal)
        .value("font_variant_small_caps", lh::font_variant::font_variant_small_caps)
        .export_values()
        ;

    py::enum_<lh::font_weight>(m, "font_weight", py::arithmetic())
        .value("font_weight_normal", lh::font_weight::font_weight_normal)
        .value("font_weight_bold", lh::font_weight::font_weight_bold)
        .value("font_weight_bolder", lh::font_weight::font_weight_bolder)
        .value("font_weight_lighter", lh::font_weight::font_weight_lighter)
        .value("font_weight_100", lh::font_weight::font_weight_100)
        .value("font_weight_200", lh::font_weight::font_weight_200)
        .value("font_weight_300", lh::font_weight::font_weight_300)
        .value("font_weight_400", lh::font_weight::font_weight_400)
        .value("font_weight_500", lh::font_weight::font_weight_500)
        .value("font_weight_600", lh::font_weight::font_weight_600)
        .value("font_weight_700", lh::font_weight::font_weight_700)
        .value("font_weight_800", lh::font_weight::font_weight_800)
        .value("font_weight_900", lh::font_weight::font_weight_900)
        .export_values()
        ;

    py::enum_<lh::list_style_type>(m, "list_style_type", py::arithmetic())
        .value("list_style_type_none", lh::list_style_type::list_style_type_none)
        .value("list_style_type_circle", lh::list_style_type::list_style_type_circle)
        .value("list_style_type_disc", lh::list_style_type::list_style_type_disc)
        .value("list_style_type_square", lh::list_style_type::list_style_type_square)
        .export_values()
        ;
#if 0
	enum list_style_type
	{
		list_style_type_armenian,
		list_style_type_cjk_ideographic,
		list_style_type_decimal,
		list_style_type_decimal_leading_zero,
		list_style_type_georgian,
		list_style_type_hebrew,
		list_style_type_hiragana,
		list_style_type_hiragana_iroha,
		list_style_type_katakana,
		list_style_type_katakana_iroha,
		list_style_type_lower_alpha,
		list_style_type_lower_greek,
		list_style_type_lower_latin,
		list_style_type_lower_roman,
		list_style_type_upper_alpha,
		list_style_type_upper_latin,
		list_style_type_upper_roman,
	};

#define  list_style_position_strings	"inside;outside"

	enum list_style_position
	{
		list_style_position_inside,
		list_style_position_outside
	};

#define  vertical_align_strings	"baseline;sub;super;top;text-top;middle;bottom;text-bottom"

	enum vertical_align
	{
		va_baseline,
		va_sub,
		va_super,
		va_top,
		va_text_top,
		va_middle,
		va_bottom,
		va_text_bottom
	};

#define  border_width_strings	"thin;medium;thick"

	enum border_width
	{
		border_width_thin,
		border_width_medium,
		border_width_thick
	};

	const float border_width_thin_value = 1;
	const float border_width_medium_value = 3;
	const float border_width_thick_value = 5;
	const float border_width_values[] = { border_width_thin_value, border_width_medium_value, border_width_thick_value };

#define  border_style_strings	"none;hidden;dotted;dashed;solid;double;groove;ridge;inset;outset"

	enum border_style
	{
		border_style_none,
		border_style_hidden,
		border_style_dotted,
		border_style_dashed,
		border_style_solid,
		border_style_double,
		border_style_groove,
		border_style_ridge,
		border_style_inset,
		border_style_outset
	};

#define  element_float_strings	"none;left;right"

	enum element_float
	{
		float_none,
		float_left,
		float_right
	};

#define  element_clear_strings	"none;left;right;both"

	enum element_clear
	{
		clear_none,
		clear_left,
		clear_right,
		clear_both
	};

#define  css_units_strings	"none;%;in;cm;mm;em;ex;pt;pc;px;dpi;dpcm;vw;vh;vmin;vmax;rem"

	enum css_units : byte
	{
		css_units_none,
		css_units_percentage,
		css_units_in,
		css_units_cm,
		css_units_mm,
		css_units_em,
		css_units_ex,
		css_units_pt,
		css_units_pc,
		css_units_px,
		css_units_dpi,
		css_units_dpcm,
		css_units_vw,
		css_units_vh,
		css_units_vmin,
		css_units_vmax,
		css_units_rem,
	};

#define  background_attachment_strings	"scroll;fixed"

	enum background_attachment
	{
		background_attachment_scroll,
		background_attachment_fixed
	};

#define  background_repeat_strings	"repeat;repeat-x;repeat-y;no-repeat"

	enum background_repeat
	{
		background_repeat_repeat,
		background_repeat_repeat_x,
		background_repeat_repeat_y,
		background_repeat_no_repeat
	};

#define  background_box_strings	"border-box;padding-box;content-box"

	enum background_box
	{
		background_box_border,
		background_box_padding,
		background_box_content
	};

#define  background_position_strings	"top;bottom;left;right;center"

	enum background_position
	{
		background_position_top,
		background_position_bottom,
		background_position_left,
		background_position_right,
		background_position_center,
	};

#define element_position_strings	"static;relative;absolute;fixed"

	enum element_position
	{
		element_position_static,
		element_position_relative,
		element_position_absolute,
		element_position_fixed,
	};

#define text_align_strings		"left;right;center;justify"

	enum text_align
	{
		text_align_left,
		text_align_right,
		text_align_center,
		text_align_justify
	};
#endif

    py::enum_<lh::text_transform>(m, "text_transform", py::arithmetic())
        .value("text_transform_none", lh::text_transform::text_transform_none)
        .value("text_transform_capitalize", lh::text_transform::text_transform_capitalize)
        .value("text_transform_uppercase", lh::text_transform::text_transform_uppercase)
        .value("text_transform_lowercase", lh::text_transform::text_transform_lowercase)
        .export_values()
    ;
#if 0

#define white_space_strings		"normal;nowrap;pre;pre-line;pre-wrap"

	enum white_space
	{
		white_space_normal,
		white_space_nowrap,
		white_space_pre,
		white_space_pre_line,
		white_space_pre_wrap
	};

#define overflow_strings		"visible;hidden;scroll;auto;no-display;no-content"

	enum overflow
	{
		overflow_visible,
		overflow_hidden,
		overflow_scroll,
		overflow_auto,
		overflow_no_display,
		overflow_no_content
	};

#define background_size_strings		"auto;cover;contain"

	enum background_size
	{
		background_size_auto,
		background_size_cover,
		background_size_contain,
	};

#define visibility_strings			"visible;hidden;collapse"

	enum visibility
	{
		visibility_visible,
		visibility_hidden,
		visibility_collapse,
	};

#define border_collapse_strings		"collapse;separate"

	enum border_collapse
	{
		border_collapse_collapse,
		border_collapse_separate,
	};

#define content_property_string		"none;normal;open-quote;close-quote;no-open-quote;no-close-quote"

	enum content_property
	{
		content_property_none,
		content_property_normal,
		content_property_open_quote,
		content_property_close_quote,
		content_property_no_open_quote,
		content_property_no_close_quote,
	};

	class render_item;

	struct floated_box
	{
		position		                pos;
		element_float	                float_side;
		element_clear	                clear_floats;
		std::shared_ptr<render_item>	el;
		int								context;
		int 							min_width;

		floated_box() = default;
		floated_box(const floated_box& val)
		{
			pos = val.pos;
			float_side = val.float_side;
			clear_floats = val.clear_floats;
			el = val.el;
			context = val.context;
			min_width = val.min_width;
		}
		floated_box& operator=(const floated_box& val)
		{
			pos = val.pos;
			float_side = val.float_side;
			clear_floats = val.clear_floats;
			el = val.el;
			context = val.context;
			min_width = val.min_width;
			return *this;
		}
		floated_box(floated_box&& val)
		{
			pos = val.pos;
			float_side = val.float_side;
			clear_floats = val.clear_floats;
			el = std::move(val.el);
			context = val.context;
			min_width = val.min_width;
		}
		void operator=(floated_box&& val)
		{
			pos = val.pos;
			float_side = val.float_side;
			clear_floats = val.clear_floats;
			el = std::move(val.el);
			context = val.context;
			min_width = val.min_width;
		}
	};

	struct int_int_cache
	{
		int		hash;
		int		val;
		bool	is_valid;
		bool	is_default;

		int_int_cache()
		{
			hash		= 0;
			val			= 0;
			is_valid	= false;
			is_default	= false;
		}
		void invalidate()
		{
			is_valid	= false;
			is_default	= false;
		}
		void set_value(int vHash, int vVal)
		{
			hash		= vHash;
			val			= vVal;
			is_valid	= true;
		}
	};

	enum select_result
	{
		select_no_match				= 0x00,
		select_match				= 0x01,
		select_match_pseudo_class	= 0x02,
		select_match_with_before	= 0x10,
		select_match_with_after		= 0x20,
	};

	template<class T>
	class def_value
	{
		T		m_val;
		bool	m_is_default;
	public:
		def_value(T def_val)
		{
			m_is_default	= true;
			m_val			= def_val;
		}
		void reset(T def_val)
		{
			m_is_default	= true;
			m_val			= def_val;
		}
		bool is_default() const
		{
			return m_is_default;
		}
		T operator=(T new_val)
		{
			m_val			= new_val;
			m_is_default	= false;
			return m_val;
		}
		operator T() const
		{
			return m_val;
		}
	};

	class baseline
	{
	public:
		enum _baseline_type
		{
			baseline_type_none,
			baseline_type_top,
			baseline_type_bottom,
		};

	public:
		baseline() : m_value(0), m_type(baseline_type_none) {}
		baseline(int _value, _baseline_type _type) : m_value(_value), m_type(_type) {}

		int value() const				{ return m_value; 	}
		void value(int _value) 			{ m_value = _value; }
		_baseline_type type() const		{ return m_type; 	}
		void type(_baseline_type _type)	{ m_type = _type; 	}

		operator int() const	{ return m_value; 	}
		baseline& operator=(int _value) { m_value = _value; return *this; }

		void set(int _value, _baseline_type _type)	{ m_value = _value; m_type =_type; }
		/**
		 * Get baseline offset from top of element with specified height
		 * @param height - element height
		 * @return baseline offset
		 */
		int get_offset_from_top(int height) const
		{
			if(m_type == baseline_type_top) return m_value;
			return height - m_value;
		}
		/**
		 * Get baseline offset from bottom of element with specified height
		 * @param height - element height
		 * @return baseline offset
		 */
		int get_offset_from_bottom(int height) const
		{
			if(m_type == baseline_type_bottom) return m_value;
			return height - m_value;
		}
		/**
		 * Calculate baseline by top and bottom positions of element aligned by baseline == 0
		 * @param top - top of the aligned element
		 * @param bottom - bottom of the aligned element
		 */
		void calc(int top, int bottom)
		{
			if(m_type == baseline_type_top)
				m_value = -top;
			else if(m_type == baseline_type_bottom)
				m_value = bottom;
		}
	private:
		int m_value;
		_baseline_type m_type;
	};


#define media_orientation_strings		"portrait;landscape"

	enum media_orientation
	{
		media_orientation_portrait,
		media_orientation_landscape,
	};

#define media_feature_strings		"none;width;min-width;max-width;height;min-height;max-height;device-width;min-device-width;max-device-width;device-height;min-device-height;max-device-height;orientation;aspect-ratio;min-aspect-ratio;max-aspect-ratio;device-aspect-ratio;min-device-aspect-ratio;max-device-aspect-ratio;color;min-color;max-color;color-index;min-color-index;max-color-index;monochrome;min-monochrome;max-monochrome;resolution;min-resolution;max-resolution"

	enum media_feature
	{
		media_feature_none,

		media_feature_width,
		media_feature_min_width,
		media_feature_max_width,

		media_feature_height,
		media_feature_min_height,
		media_feature_max_height,

		media_feature_device_width,
		media_feature_min_device_width,
		media_feature_max_device_width,

		media_feature_device_height,
		media_feature_min_device_height,
		media_feature_max_device_height,

		media_feature_orientation,

		media_feature_aspect_ratio,
		media_feature_min_aspect_ratio,
		media_feature_max_aspect_ratio,

		media_feature_device_aspect_ratio,
		media_feature_min_device_aspect_ratio,
		media_feature_max_device_aspect_ratio,

		media_feature_color,
		media_feature_min_color,
		media_feature_max_color,

		media_feature_color_index,
		media_feature_min_color_index,
		media_feature_max_color_index,

		media_feature_monochrome,
		media_feature_min_monochrome,
		media_feature_max_monochrome,

		media_feature_resolution,
		media_feature_min_resolution,
		media_feature_max_resolution,
	};

#define box_sizing_strings		"content-box;border-box"

	enum box_sizing
	{
		box_sizing_content_box,
		box_sizing_border_box,
	};


#define media_type_strings		"none;all;screen;print;braille;embossed;handheld;projection;speech;tty;tv"

	enum media_type
	{
		media_type_none,
		media_type_all,
		media_type_screen,
		media_type_print,
		media_type_braille,
		media_type_embossed,
		media_type_handheld,
		media_type_projection,
		media_type_speech,
		media_type_tty,
		media_type_tv,
	};

	struct media_features
	{
		media_type	type;
		int			width;			// (pixels) For continuous media, this is the width of the viewport including the size of a rendered scroll bar (if any). For paged media, this is the width of the page box.
		int			height;			// (pixels) The height of the targeted display area of the output device. For continuous media, this is the height of the viewport including the size of a rendered scroll bar (if any). For paged media, this is the height of the page box.
		int			device_width;	// (pixels) The width of the rendering surface of the output device. For continuous media, this is the width of the screen. For paged media, this is the width of the page sheet size.
		int			device_height;	// (pixels) The height of the rendering surface of the output device. For continuous media, this is the height of the screen. For paged media, this is the height of the page sheet size.
		int			color;			// The number of bits per color component of the output device. If the device is not a color device, the value is zero.
		int			color_index;	// The number of entries in the color lookup table of the output device. If the device does not use a color lookup table, the value is zero.
		int			monochrome;		// The number of bits per pixel in a monochrome frame buffer. If the device is not a monochrome device, the output device value will be 0.
		int			resolution;		// The resolution of the output device (in DPI)

		media_features()
		{
			type = media_type::media_type_none,
			width =0;
			height = 0;
			device_width = 0;
			device_height = 0;
			color = 0;
			color_index = 0;
			monochrome = 0;
			resolution = 0;
		}
	};
#endif

    py::enum_<lh::render_type>(m, "render_type", py::arithmetic())
        .value("render_all", lh::render_type::render_all)
        .value("render_no_fixed", lh::render_type::render_no_fixed)
        .value("render_fixed_only", lh::render_type::render_fixed_only)
        .export_values()
    ;

#if 0
	// List of the Void Elements (can't have any contents)
	const char* const void_elements = "area;base;br;col;command;embed;hr;img;input;keygen;link;meta;param;source;track;wbr";

#define flex_direction_strings		"row;row-reverse;column;column-reverse"

	enum flex_direction
	{
		flex_direction_row,
		flex_direction_row_reverse,
		flex_direction_column,
		flex_direction_column_reverse
	};

#define flex_wrap_strings		"nowrap;wrap;wrap-reverse"

	enum flex_wrap
	{
		flex_wrap_nowrap,
		flex_wrap_wrap,
		flex_wrap_wrap_reverse
	};

#define flex_justify_content_strings		"normal;flex-start;flex-end;center;space-between;space-around;start;end;left;right;space-evenly;stretch"

	enum flex_justify_content
	{
		flex_justify_content_normal,
		flex_justify_content_flex_start,
		flex_justify_content_flex_end,
		flex_justify_content_center,
		flex_justify_content_space_between,
		flex_justify_content_space_around,
		flex_justify_content_start,
		flex_justify_content_end,
		flex_justify_content_left,
		flex_justify_content_right,
		flex_justify_content_space_evenly,
		flex_justify_content_stretch,
	};

#define flex_align_items_strings		"normal;flex-start;flex-end;center;start;end;baseline;stretch;auto"

	enum flex_align_items
	{
		flex_align_items_flex_normal,
		flex_align_items_flex_start,
		flex_align_items_flex_end,
		flex_align_items_center,
		flex_align_items_start,
		flex_align_items_end,
		flex_align_items_baseline,
		flex_align_items_stretch,
		flex_align_items_auto, // used for align-self property only
		flex_align_items_first = 0x100,
		flex_align_items_last = 0x200,
		flex_align_items_unsafe = 0x400,
		flex_align_items_safe  = 0x800,
	};

#define flex_align_content_strings		"flex-start;start;flex-end;end;center;space-between;space-around;stretch"

	enum flex_align_content
	{
		flex_align_content_flex_start,
		flex_align_content_start,
		flex_align_content_flex_end,
		flex_align_content_end,
		flex_align_content_center,
		flex_align_content_space_between,
		flex_align_content_space_around,
		flex_align_content_stretch
	};

#define flex_basis_strings		"auto;content;fit-content;min-content;max-content"

	enum flex_basis
	{
		flex_basis_auto,
		flex_basis_content,
		flex_basis_fit_content,
		flex_basis_min_content,
		flex_basis_max_content,
	};

#define caption_side_strings		"top;bottom"

	enum caption_side
	{
		caption_side_top,
		caption_side_bottom
	};
}

#endif
