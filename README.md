# Image_Inpainting

Streamlit Web App Setup

GPT-4
Custom instructions details

User
Explain line by line 
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os
from streamlit_option_menu import option_menu
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
    imge1 = load_image("logo.png")
    st.image(imge1)
st.markdown("""
                <style>
                        .custom-text {
                                        padding:0px; /* Adjust the padding as needed */
                                        margin-bottom: -40px}
                                        </style>
            """, unsafe_allow_html=True)

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

with st.container():
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["home","projects","contact us","About"],
            icons=["house","book","envelope","phone"],
            # menu_icon = <i class ="graph-up-arrow" style="font-size: 2rem; color: cornflowerblue;" > < / i >
            #menu_icon="graph-up-arrow",
            #orientation="horizontal",
            default_index=0,
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
    "<p class='custom-text'><h2 style=text-align:center;><span style='color:purple'>Sample Dashboard</span></h2></p>",
    unsafe_allow_html=True)
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    st.write("welcome to streamlit")
    image_nat = load_image("n.png")
    st.image(image_nat, use_column_width=True)


elif selected=="projects":
    st.markdown(
    "<p class='custom-text'><h2 style=text-align:center;><span style='color:purple'>Projects</span></h2></p>",
    unsafe_allow_html=True)
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    with st.container():
        with st.sidebar:
            subselect = option_menu(
                menu_title=None,
                options=["Analysis 1","Analysis 2","Analysis 3"],
                icons=["graph-up-arrow","graph-up-arrow","graph-up-arrow"],
                # menu_icon = <i class ="graph-up-arrow" style="font-size: 2rem; color: cornflowerblue;" > < / i >
                #menu_icon="graph-up-arrow",
                #orientation="horizontal",
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "#f8f5fa"},
                    # "icon": {"color": "orange", "font-size": "15px"},
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                    "menu-icon": {"color": "purple"},
                    "nav-link-selected": {"color": "black", "font-size": "12px", "font-weight": "bold",
                                        "background-color": "#eee"},
                    "icon": {"color": "purple"},
                    #"menu-title": {"font-size": "15px", "font-weight": "bold"}
                }
            )
    if subselect=="Analysis 1":
        st.markdown("""
                        <style>
                                .custom-1 {
                                                padding:0px; /* Adjust the padding as needed */
                                                 margin-bottom: -40px}
                                               </style>
                    """, unsafe_allow_html=True)


        st.markdown("<p class='custom-1'><div style='text-align:center; font-size:24px;'><b>Analysis 1 </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)

        st.markdown('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
        st.sidebar.header("Filter: ")
        st.sidebar.subheader("select date range")
        st.sidebar.date_input("Start Date")
        st.sidebar.date_input("End Date")


        slider_value=st.sidebar.slider("select a value",0,100,50)
        checkbox_option=st.sidebar.checkbox("show data")
        data=pd.DataFrame({'x':np.random.rand(100),'y':np.random.rand(100)})
        if checkbox_option:
            st.subheader("random data")
            st.write(data)
        
        selected_option = st.selectbox("",['line graph', 'bar graph',
                                                    'histogram'])
        if selected_option == "line graph":
            image1_path = load_image("8.png")


        elif selected_option == "bar graph":
            image1_path = load_image("9.png")
            
        elif selected_option == "histogram":
            image1_path = load_image("0.png")
        st.image(image1_path, use_column_width=True)

        
                
        #st.divider()
        tab1, tab2 = st.tabs(["TAB1", "TAB2"])
        with tab1:
            col1, col2 = st.columns((2))
            with col1:
                #st.markdown("\n")
                #st.markdown("\n")
                st.markdown("<h5 style='text-align: center;'>H1</h5>",
                            unsafe_allow_html=True)
                images1_1 = load_image("1.png")
                images1_2 = load_image("6.png")
                st.image(images1_1, caption=" image3", use_column_width=True)
                st.divider()
                st.image(images1_2, caption=" image4", use_column_width=True)
            with col2:
                st.markdown("<h5 style='text-align: center;'>H2</h5>",
                            unsafe_allow_html=True)
                images2_1 = load_image("3.png")
                images2_2 = load_image("4.png")
                st.image(images2_1, caption=" image1", use_column_width=True)
                st.divider()
                st.image(images2_2, caption=" image2", use_column_width=True)
        with tab2:
                images1_1 = load_image("1.png")
                st.image(images1_1, caption=" image3", use_column_width=True)

    if subselect=="Analysis 2":
        st.markdown("""
                        <style>
                                .custom-1 {
                                                padding:0px; /* Adjust the padding as needed */
                                                 margin-bottom: -40px}
                                               </style>
                    """, unsafe_allow_html=True)


        st.markdown("<p class='custom-1'><div style='text-align:center; font-size:24px;'><b>Analysis 2 </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)

        st.markdown('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
        st.sidebar.header("Filter: ")
        st.sidebar.subheader("select date range")
        st.sidebar.date_input("Start Date")
        st.sidebar.date_input("End Date")


        slider_value=st.sidebar.slider("select a value",0,100,50)
        checkbox_option=st.sidebar.checkbox("show data")
        data=pd.DataFrame({'x':np.random.rand(100),'y':np.random.rand(100)})
        if checkbox_option:
            st.subheader("random data")
            st.write(data)
        st.write("Analysis2 report")
    if subselect=="Analysis 3":
        st.markdown("""
                        <style>
                                .custom-1 {
                                                padding:0px; /* Adjust the padding as needed */
                                                 margin-bottom: -40px}
                                               </style>
                    """, unsafe_allow_html=True)


        st.markdown("<p class='custom-1'><div style='text-align:center; font-size:24px;'><b>Analysis 3 </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)

        st.markdown('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
        st.sidebar.header("Filter: ")
        st.sidebar.subheader("select date range")
        st.sidebar.date_input("Start Date")
        st.sidebar.date_input("End Date")


        slider_value=st.sidebar.slider("select a value",0,100,50)
        checkbox_option=st.sidebar.checkbox("show data")
        data=pd.DataFrame({'x':np.random.rand(100),'y':np.random.rand(100)})
        if checkbox_option:
            st.subheader("random data")
            st.write(data)
        st.write("Analysis3 report")

    
elif selected == "contact us":
    st.markdown(
    "<p class='custom-text'><h2 style=text-align:center;><span style='color:purple'>Contact Us</span></h2></p>",
    unsafe_allow_html=True)
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    st.write(':email: <a href="mailto:example@example.com">example@example.com</a>', unsafe_allow_html=True)

    st.write(":phone: xxx-xxxx-xxxx")
    st.write(":link: [Twitter](https://twitter.com/natwestgroup)")
    st.write(":link: [LinkedIn](https://www.linkedin.com/company/natwest-group/mycompany/)")
    st.write(":link: [Instagram](https://www.instagram.com/natwest/)")


    

elif selected=="About":
    st.markdown(
    "<p class='custom-text'><h2 style=text-align:center;><span style='color:purple'>About</span></h2></p>",
    unsafe_allow_html=True)
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    #st.header("hi")
    with st.container():
        with st.sidebar:
            subselect = option_menu(
                menu_title=None,
                options=["About Company","CDIO Team"],
                #icons=["graph-up-arrow","graph-up-arrow","graph-up-arrow"],
                # menu_icon = <i class ="graph-up-arrow" style="font-size: 2rem; color: cornflowerblue;" > < / i >
                #menu_icon="graph-up-arrow",
                #orientation="horizontal",
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "#f8f5fa"},
                    # "icon": {"color": "orange", "font-size": "15px"},
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                    "menu-icon": {"color": "purple"},
                    "nav-link-selected": {"color": "black", "font-size": "12px", "font-weight": "bold",
                                        "background-color": "#eee"},
                    "icon": {"color": "purple"},
                    #"menu-title": {"font-size": "15px", "font-weight": "bold"}
                }
            )
    if subselect=="About Company":
        st.markdown("""
                        <style>
                                .custom-1 {
                                                padding:0px; /* Adjust the padding as needed */
                                                 margin-bottom: -10px}
                                               </style>
                    """, unsafe_allow_html=True)


        st.markdown("<p class='custom-1'><div style='text-align:left; font-size:28px;'><b>NatWest Group </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)
        st.write("NatWest Group is a British banking and insurance holding company, based in Edinburgh, Scotland. The group operates a wide variety of banking brands offering personal and business banking, private banking, investment banking, insurance and corporate finance.")
    if subselect=="CDIO Team":
        st.markdown("<p class='custom-1'><div style='text-align:left; font-size:28px;'><b>CDIO Team </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)
        st.write("About Team")

st.markdown('<style>div.block-container{padding-top:0.05rem;}</style>',unsafe_allow_html=True)


ChatGPT
Certainly, let's break down the code:

Imports:

python
Copy code
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os
from streamlit_option_menu import option_menu
import warnings
These lines import necessary libraries. The most notable ones are streamlit for creating web apps, pandas for data manipulation, numpy for numerical operations, PIL for image processing, and a custom option_menu from streamlit_option_menu.

Warnings Configuration:

python
Copy code
warnings.filterwarnings('ignore')
This line suppresses any warnings that might arise.

Streamlit Page Configuration:

python
Copy code
st.set_page_config(page_title="sample dashboard", page_icon=":bar_chart:", layout="wide")
Configures the Streamlit app's page with a title, icon, and layout.

CSS Styling:

python
Copy code
page_bg_img = ...
st.markdown(page_bg_img, unsafe_allow_html=True)
This section sets up the background and other CSS styles for the Streamlit page using a multi-line string (page_bg_img). The CSS modifies the background, header, toolbar, and sidebar styling.

Image Loading Function:

python
Copy code
def load_image(image_path):
    return Image.open(image_path)
A simple function that, given an image path, returns the opened image.

Setting Up Columns and Loading Logo:

python
Copy code
coli1, coli2 = st.columns([1,4])
with coli1:
    imge1 = load_image("logo.png")
    st.image(imge1)
The page layout is divided into columns (with widths 1 and 4 respectively). An image (logo) is loaded into the first column.

More Styling:

python
Copy code
st.markdown(...)
A couple more CSS style adjustments, mostly targeting text and dividers on the page.

Creating Sidebar Menu:

python
Copy code
with st.container():
    with st.sidebar:
        selected = option_menu(...)
This section initializes the main navigation menu on the sidebar. Options include "home", "projects", "contact us", and "About".

Displaying Content Based on Sidebar Selection:

python
Copy code
if selected == "home":
    ...
elif selected == "projects":
    ...
elif selected == "contact us":
    ...
elif selected == "About":
    ...
These blocks handle the main content display based on the sidebar menu's selected option. Depending on the choice, different content and functionalities are displayed:

For "home", a welcome message and an image are displayed.
"projects" has sub-selections ("Analysis 1", "Analysis 2", "Analysis 3"), each with its own content.
"contact us" displays contact information with clickable links.
"About" offers further options ("About Company", "CDIO Team") to display details about the company or team.
Final Style Adjustment:

python
Copy code
st.markdown('<style>div.block-container{padding-top:0.05rem;}</style>', unsafe_allow_html=True)
This line adjusts the padding at the top of the container.

In summary, this script creates a Streamlit web app with different sections accessible through a sidebar menu. Each section has its own content, and there are additional styles applied to make the page visually appealing.




