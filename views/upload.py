import streamlit as st
import json

st.set_page_config(layout="wide") 

# uploaded_file = st.file_uploader("File upload")
# if uploaded_file is not None:
# 	data = json.load(uploaded_file)
# 	print(data)


def upload_file():
    uploaded_file = st.file_uploader("Upload JSON file", type=["json"])
    
    if uploaded_file is not None:
        try:
            st.session_state.uploaded_data = json.load(uploaded_file)
            st.session_state.file_name = uploaded_file.name
            st.success("File uploaded successfully!")
        except json.JSONDecodeError:
            st.error("Invalid JSON file")

upload_file()