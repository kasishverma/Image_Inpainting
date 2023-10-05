import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os
from streamlit_option_menu import option_menu
#import home, contact, projects, about, mailus
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
coli1,coli2 = st.columns([1,4])
with coli1:
    imge1 = load_image(r"C:\Users\vermaks\Downloads\logo.png")
    st.image(imge1)
st.markdown("""
                <style>
                        .custom-text {
                                        padding:0px; /* Adjust the padding as needed */
                                        margin-bottom: -30px}
                                        </style>
            """, unsafe_allow_html=True)


st.markdown(
    "<p class='custom-text'><h2 style=text-align:center;><span style='color:purple'>Sample Dashboard</span></h2></p>",
    unsafe_allow_html=True)

st.markdown("""
        <style>
            .custom-divider {
                height: 1px; /* Adjust the height of the divider line */
                background-color: #333; /* Adjust the color of the divider line */
                margin-top: -20px; /* Adjust the top margin to reduce the gap */
                margin-bottom: 5px; /* Adjust the bottom margin to reduce the gap */
            }
        </style>
    """, unsafe_allow_html=True)

    # Create a custom divider
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)



with st.container():
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["home","projects","contact us","About"],
            icons=["house","book","envelope","phone"],
            # menu_icon = <i class ="graph-up-arrow" style="font-size: 2rem; color: cornflowerblue;" > < / i >
            #menu_icon="graph-up-arrow",
            #orientation="horizontal",
            default_index=3,
            styles={
                "container": {"padding": "0!important", "background-color": "#f8f5fa"},
                # "icon": {"color": "orange", "font-size": "15px"},
                "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "menu-icon": {"color": "grey"},
                "nav-link-selected": {"color": "black", "font-size": "12px", "font-weight": "bold",
                                      "background-color": "#eee"},
                "icon": {"color": "purple"},
                #"menu-title": {"font-size": "15px", "font-weight": "bold"}
            }
        )

st.sidebar.divider()

if selected=="home":
    st.markdown(
        "<p class='custom-text'><h2 style=text-align:center;>Dashboard</h2></p>",
        unsafe_allow_html=True)




    st.divider()
    st.write("welcome to streamlit")


    st.sidebar.header("Filter: ")
#with col1:
    ##date1 = pd.to_datetime(st.date_input("Start Date", startDate))

#with col2:
    #date2 = pd.to_datetime(st.date_input("End Date", endDate))
    slider_value=st.sidebar.slider("select a value",0,100,50)
    checkbox_option=st.sidebar.checkbox("show data")
    data=pd.DataFrame({'x':np.random.rand(100),'y':np.random.rand(100)})
    if checkbox_option:
        st.subheader("random data")
        st.write(data)

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


if selected=="projects":
    with st.sidebar:
    #st.sidebar.header("")
        selected=option_menu(
            menu_title=None,
            options=["Analysis 1","Analysis 2","Analysis 3"], 
        #icons=["house","book","envelope","phone"],
            #default_index=0,
            #orientation="vertical" ,
        #styles={
                    #"container": {"padding": "0!important", "background-color": "#f8f5fa"},
                    # "icon": {"color": "orange", "font-size": "15px"},
                    #"nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                    #"menu-icon": {"color": "purple"},
                    #"nav-link-selected": {"color": "black", "font-size": "12px", "font-weight": "bold",
                    #                    "background-color": "#eee"},
                    #"icon": {"color": "purple"},
                    #"menu-title": {"font-size": "18px", "font-weight": "bold"}
                #}
    )

    if selected=="Analysis 1":
        st.write("Analysis1 report")
    if selected=="Analysis 2":
        st.write("Analysis2 report")
    if selected=="Analysis 3":
        st.write("Analysis3 report")

if selected=="contact us":
    
    add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Contact number", "LinkedIn")
    )
    if add_selectbox=="Email":
        st.sidebar.markdown('<a href="mailto:hello@streamlit.io">Contact us !</a>', unsafe_allow_html=True)
        st.sidebar.write("opening mail..")
    if add_selectbox=="Contact number":
        st.sidebar.write("calling..")
    if add_selectbox=="LinkedIn":
        st.sidebar.write("opening LinkedIn..")
    #with st.sidebar:
    #    selected=option_menu(
    #        menu_title=None,
    #        options=["department1"," 2"," 3"], 
    #   
    #)
   # 
   # if selected=="department1":
   #     st.write("1..")
   # if selected==" 2":
   #     st.write("2...")
   # if selected==" 3":
   #     st.write("3....")



if selected=="About":
    
    st.header("hi")


st.markdown('<style>div.block-container{padding-top:0.05rem;}</style>',unsafe_allow_html=True)


