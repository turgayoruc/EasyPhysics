
import streamlit as st
import streamlit.components.v1 as components

def run():
    st.set_page_config(initial_sidebar_state="collapsed")
    iframe_src = "https://turgayoruc.github.io/WebGL_Kacis"
    st.components.v1.iframe(iframe_src,width=800,height=600)
   # You can add height and width to the component of course.


run()
