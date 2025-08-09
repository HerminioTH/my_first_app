import streamlit as st

st.set_page_config(layout="wide") 

col1, col2, col3 = st.columns([1,2,1])

col1.markdown(" # Welcome to my app")
col1.markdown(" Here is some info about the app.")


uploaded_data = col2.file_uploader("File upload")
col2.success("File uploaded successfully")

photo_cam = col2.camera_input("Take a photo")
col2.success("Photo uploaded successfully")


col3.metric(label="Temperature", value="60 degC", delta="3 degG")

with col2.expander("Click to read more"):
	st.write("Here are more details on this topic that you could probably interested in.")

	if uploaded_data is None:
		st.write("Not data uploaded.")
	else:
		st.write("Data has been uploaded.")
  