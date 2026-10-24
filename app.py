import streamlit as st
 
st.set_page_config(page_title="My Web application", page_icon="🚀", layout="wide")
 
st.title("Hello")
 
tab1, tab2 = st.tabs(["About", "1"])
 
with tab1:
    st.header("About")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://avatars.githubusercontent.com/u/45109972?s=280&v=4", width=200)
    with col2:
        st.subheader("About this application")
        st.write("This application was made using Streamlit")
