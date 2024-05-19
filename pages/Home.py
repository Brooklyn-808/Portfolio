import streamlit as st

st.title("Welcome to My Portfolio!")
st.write("This is the home page of my portfolio website.")
st.write("Feel free to browse around and learn more about me.")
st.sidebar.title("Navigation")
st.sidebar.page_link("About Me.py", label="About")
