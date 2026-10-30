import streamlit as st
 
st.set_page_config(page_title="My Web application", page_icon="🚀", layout="wide")
 
st.title("Hello")
 
tab1, tab2 = st.tabs(["About", "My favourite websites"])
 
with tab1:
    st.header("About")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://avatars.githubusercontent.com/u/96830562?v=4", width=200)
    with col2:
        st.subheader("About this application")
        st.write("This application was made using Streamlit")
with tab2:
    st.header("My favourite websites")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Games")
        st.markdown('[:seedling: Minecraft](https://minecraft.net)')
        st.markdown('[:video_game: Steam](https://store.steampowered.com/)')
    with col2:
        st.subheader("Entertaiment")
        st.markdown('[:video_camera: Youtube](https://youtube.com)')
        st.markdown('[:computer: Github](https://github.com)')
        st.markdown('[:satellite: Discord](https://discord.com)')
    
