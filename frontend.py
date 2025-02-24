import streamlit as st
import requests

st.title("Person and Activity Extractor")

st.write("Enter a paragraph or single line to extract names and their corresponding activities:")

# Input text area
input_text = st.text_area("Input Text", height=200)

if st.button("Extract"):
    if input_text.strip():
        # Send request to Flask API
        response = requests.post("http://127.0.0.1:5000/extract", json={"text": input_text})
        
        if response.status_code == 200:
            result = response.json()
            if result:
                st.subheader("Extracted Results:")
                for entry in result:
                    st.write(f"**Person:** {entry['Person']}, **Activity:** {entry['Activity']}")
            else:
                st.warning("No names or activities found.")
        else:
            st.error("Error connecting to backend.")
    else:
        st.warning("Please enter some text.")
