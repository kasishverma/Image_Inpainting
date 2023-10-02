import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os
from streamlit_option_menu import option_menu
import home, contact, projects, about, mailus
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="sample dashboard", page_icon=":bar_chart:",layout="wide")

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
c1,c2,c3,c4=st.columns(4)
with c1:
    images1 = load_image(
            r"C:\Users\vermaks\Downloads\natwest.png")
    st.image(images1,use_column_width=True)

selected=option_menu(
    menu_title=None,
    options=["home","projects","contact","About"], 
    icons=["house","book","envelope","phone"],
    default_index=0,
    orientation="horizontal" ,
    styles={
                "container": {"padding": "0!important", "background-color": "#f8f5fa"},
                # "icon": {"color": "orange", "font-size": "15px"},
                "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                #"menu-icon": {"color": "purple"},
                "nav-link-selected": {"color": "black", "font-size": "12px", "font-weight": "bold",
                                      "background-color": "#eee"},
                "icon": {"color": "purple"},
                #"menu-title": {"font-size": "18px", "font-weight": "bold"}
            }
)

if selected=="home":
    st.title("you selected home")
if selected=="projects":
    st.title("you selected projects")
if selected=="contact":
    st.title("you selected contact")



st.markdown('<style>div.block-container{padding-top:0.05rem;}</style>',unsafe_allow_html=True)


st.markdown(
    "<p class='custom-text'><h2 style=text-align:center;>Dashboard</h2></p>",
    unsafe_allow_html=True)




st.divider()
st.write("welcome to streamlit")


st.sidebar.header("Choose your filter: ")
slider_value=st.sidebar.slider("select a value",0,100,50)
checkbox_option=st.sidebar.checkbox("show data")
data=pd.DataFrame({'x':np.random.rand(100),'y':np.random.rand(100)})
if checkbox_option:
    st.subheader("random data")
    st.write(data)

#def load_image(image_path):
        #return Image.open(image_path)
tab1, tab2 = st.tabs(["TAB1", "TAB2"])
with tab1:
    col1, col2 = st.columns((2))
    with col1:
        #st.markdown("\n")
        #st.markdown("\n")
        st.markdown("<h5 style='text-align: center;'>H1</h5>",
                    unsafe_allow_html=True)
        images1_1 = load_image(
            r"C:\Users\vermaks\Downloads\1.png")
        images1_2 = load_image(
            r"C:\Users\vermaks\Downloads\6.png")
        st.image(images1_1, caption=" image3", use_column_width=True)
        st.divider()
        st.image(images1_2, caption=" image4", use_column_width=True)
    with col2:
        st.markdown("<h5 style='text-align: center;'>H2</h5>",
                    unsafe_allow_html=True)
        images2_1 = load_image(
            r"C:\Users\vermaks\Downloads\3.png")
        images2_2 = load_image(
            r"C:\Users\vermaks\Downloads\4.png")
        st.image(images2_1, caption=" image1", use_column_width=True)
        st.divider()
        st.image(images2_2, caption=" image2", use_column_width=True)
st.divider()
selected_option = st.selectbox("",['line graph', 'bar graph',
                                            'histogram'])
# Define the paths to your images based on the selected option
if selected_option == "line graph":
    image1_path = load_image(
                r"C:\Users\vermaks\Downloads\8.png")


elif selected_option == "bar graph":
    image1_path = load_image(
                r"C:\Users\vermaks\Downloads\9.png")
    
elif selected_option == "histogram":
    image1_path = load_image(
                r"C:\Users\vermaks\Downloads\0.png")
st.image(image1_path, use_column_width=True)