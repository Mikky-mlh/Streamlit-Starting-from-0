import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_anim_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

with st.container():
    st.subheader("Hi! I am Yuvraj :wave:")
    st.title("A Student")
    st.write("passionate about Chess")
    st.write("[Learn More >](https://mikky-mlh.github.io/Portfolio/)")
    
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - I am a student at LNCT.
            - I love playing chess and solving complex problems.
            - I am learning web development and data science.
            
            Check out my projects on my GitHub profile.
            """
        )
        st.write("[Github](https://github.com/Mikky-mlh)")
        
with right_column:
    if lottie_anim_coding:
        st_lottie(lottie_anim_coding, height=300, key="coding")
    else:
        st.write("Animation failed to load")
        
