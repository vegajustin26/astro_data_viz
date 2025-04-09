import streamlit as st
import os
import base64
import streamlit.components.v1 as components

st.set_page_config(page_title="Astro Data", page_icon="🌌", layout="centered")

st.markdown("<h1 style='text-align: center;'>🌌 Justin's Fav Data Visualizations</h1>", unsafe_allow_html=True)
st.markdown("###")

def load_image(image_file):
    img = open(image_file, "rb").read()
    data_url = base64.b64encode(img).decode("utf-8")
    
    return data_url

st.markdown("## Image reconstruction of the M87 black hole")  
M87 = load_image("M87_230GHz_ch2.gif")
angelina = load_image("angelina.gif")

st.markdown(
    f'<img src="data:image/gif;base64,{M87}" alt="M87 gif">',
    unsafe_allow_html=True,)
text = """*A movie of a black hole, simulated from a realistic observation of M87 at 230 GHz. We are seeing the shadow of the black hole as illuminated by the light behind it. On the left is a realistic simulation of the black hole as viewed with "perfect resolution". On the right is a reconstruction of what you would see from data collected by a configuration of the next-generation Event Horizon Telescope. As seen in [this paper](https://www.mdpi.com/2075-4434/11/1/12).*"""
st.markdown(text)

st.write("#")
st.markdown("## Asteroid transiting TIC 398572494")  

c1, c2, c3 = st.columns([0.2, 0.7, 0.1])

with c2:
    st.markdown(f"""<img src="data:image/gif;base64,{angelina}" alt="angelina asteroid" width="400">""", unsafe_allow_html=True,)

text1 = """
                <div style="text-align: center">
                <i>An animation of asteroid 64 Angelina "photobombing" star TIC 398572494, as captured by the Transiting Exoplanet Survey Satellite. Made possible by <a href="https://github.com/ben-cassese/jorbit">jorbit</a> [paper in prep].</i>
                </div> 
                """

# text = """*"""
st.markdown(text1, unsafe_allow_html=True)
