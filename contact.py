import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os
from streamlit_option_menu import option_menu
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")

page_bg_img='''
<style>

[data-testid="stAppViewContainer"]{
    background-image: linear-gradient(to top, #cd9cf2 0%, #f6f3ff 100%);
}

[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}

[data-testid="stToolbar"]{
    right: 2rem
}

[data-testid="stSidebar"]{
}

</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

def load_image(image_path):
    return Image.open(image_path)
coli1, coli2 = st.columns([1, 4])
with coli1:
    imge1 = load_image(r"1.png")
    st.image(imge1)

# Page selection logic:
with st.container():
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["home", "projects", "contact us", "About"],
            icons=["house", "book", "envelope", "phone"],
            default_index=3,
            styles={
                "container": {"padding": "0!important", "background-color": "#f8f5fa"},
                "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "menu-icon": {"color": "grey"},
                "nav-link-selected": {"color": "black", "font-size": "12px", "font-weight": "bold", "background-color": "#eee"},
                "icon": {"color": "purple"}
            }
        )

    if selected == "home":
        st.markdown(
            "<p class='custom-text'><h2 style=text-align:center;><span style='color:purple'>Sample Dashboard</span></h2></p>",
            unsafe_allow_html=True)
        # Add your home page content below this comment.

    elif selected == "contact us":
        st.markdown(
            "<p class='custom-text'><h2 style=text-align:center;><span style='color:purple'>Contact Us</span></h2></p>",
            unsafe_allow_html=True)
        add_selectbox = st.sidebar.selectbox(
            "How would you like to be contacted?",
            ("Email", "Contact number", "LinkedIn")
        )
        if add_selectbox == "Email":
            st.sidebar.markdown('<a href="mailto:example@example.com">:email: Contact us!</a>', unsafe_allow_html=True)
            st.write(":email: Email: example@example.com")
        if add_selectbox == "Contact number":
            st.sidebar.write(":phone: Phone Number: xxx-xxxx-xxxx")
        if add_selectbox == "LinkedIn":
            st.sidebar.markdown('<a href="https://www.linkedin.com/in/example/">:link: LinkedIn Profile</a>', unsafe_allow_html=True)
        st.write(":link: LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/example/)")

    # Here, you can add more conditional blocks for "projects" and "About" tabs similarly.

st.markdown('<style>div.block-container{padding-top:0.05rem;}</style>', unsafe_allow_html=True)
