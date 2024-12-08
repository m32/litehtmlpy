void litehtml::element::set_inner_html(const litehtml::tchar_t* str, litehtml::css* user_styles)
{
	// parse document into GumboOutput
	GumboOptions		options = kGumboDefaultOptions;

	options.fragment_context = gumbo_tag_enum(get_tagName());

	GumboOutput*		output = gumbo_parse_with_options(&options, str, strlen(str));
	document::ptr		doc = m_doc.lock();

	m_children.clear();

	document::create_node(output->root->v.element.children.data[0], m_children, true, doc);
	gumbo_destroy_output(&kGumboDefaultOptions, output);

	for (auto& child : m_children)
	{
		child->parent(shared_from_this());
	}

	if( doc->is_initialised() )
	{
		for (auto& child : m_children)
		{
			// Let's process created elements tree
			// apply master CSS
			child->apply_stylesheet(doc->get_context()->master_css());

			// parse elements attributes
			child->parse_attributes();

			// Apply parsed styles.
			child->apply_stylesheet(doc->get_styles());

			// Apply user styles if any
			if (user_styles)
			{
				child->apply_stylesheet(*user_styles);
			}

			// Parse applied styles in the elements
			child->parse_styles();

			// Finally initialize elements
			child->init();
		}
	}
}
