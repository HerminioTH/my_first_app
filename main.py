import streamlit as st

about_page = st.Page(
	page="views/about.py",
	title="About",
	icon=":material/account_circle:",
)

upload_page = st.Page(
	page="views/upload.py",
	title="Upload files",
	default=True
)

results1_page = st.Page(
	page="views/results_1.py",
	title="View results",
)

# pg = st.navigation(pages=[upload_page, results1_page, about_page])
pg = st.navigation(
	{
		"Info": [about_page],
		"Visualizer": [upload_page, results1_page]
	}
)

pg.run()