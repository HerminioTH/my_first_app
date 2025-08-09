import streamlit as st
import json
import matplotlib.pyplot as plt

def show_results():
	st.title("Results Viewer")
	if "uploaded_data" not in st.session_state:
		st.warning("Please upload a file first on the Upload page")
		# st.subheader(f"Viewing: {st.session_state.get('file_name', 'Unknown file')}")
		return
    
	st.subheader(f"Viewing: {st.session_state.get('file_name', 'Unknown file')}")
    
	if "uploaded_data" in st.session_state:
		# Access the uploaded data
		uploaded_file = st.session_state.uploaded_data

		print(uploaded_file)
		# data = json.load(uploaded_file)
		# print(data)


		fig, ax = plt.subplots()
		ax.plot(uploaded_file["x"], uploaded_file["y"], ".-")
		st.pyplot(fig)	    

show_results()