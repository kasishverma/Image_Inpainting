# Importing necessary modules
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os
from streamlit_option_menu import option_menu
import warnings

# Ignore warnings for a cleaner output
warnings.filterwarnings('ignore')

# Set page configuration for the dashboard
st.set_page_config(page_title="sample dashboard", page_icon=":bar_chart:",layout="wide")

# CSS for the background and header styling
page_bg_img = '''
# ... [skipping CSS for brevity]
'''

# Applying the CSS to the Streamlit App
st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to load an image using the given path
def load_image(image_path):
        return Image.open(image_path)

# Set up the layout with two columns, with the first column being narrower than the second
coli1, coli2 = st.columns([1, 4])
with coli1:
    # Load and display the logo
    imge1 = load_image("logo.png")
    st.image(imge1)

# More CSS for styling the text and divider
st.markdown("""
# ... [skipping CSS for brevity]
""", unsafe_allow_html=True)

# Begin main content container
with st.container():
    # Sidebar for navigation
    with st.sidebar:
        # Create a navigation menu with icons
        selected = option_menu(
            # ... [menu options and styles]
        )

# Add a divider in the sidebar for aesthetics
st.sidebar.divider()

# Page content based on the selected option from the navigation menu
if selected == "home":
    # Header for the home page
    st.markdown(
    # ... [skipping for brevity]
    )

    # Welcome message for the home page
    st.write("welcome to streamlit")
    # Display a sample image
    image_nat = load_image("n.png")
    st.image(image_nat, use_column_width=True)

# ... [similar logic for other pages such as projects, contact us, and about]

elif selected == "contact us":
    # Header for the contact page
    st.markdown(
    # ... [skipping for brevity]
    )
    # Display contact details including email, phone, and social media links
    st.write(':email: <a href="mailto:example@example.com">example@example.com</a>', unsafe_allow_html=True)
    st.write(":phone: xxx-xxxx-xxxx")
    st.write(":link: [Twitter](https://twitter.com/natwestgroup)")
    st.write(":link: [LinkedIn](https://www.linkedin.com/company/natwest-group/mycompany/)")
    st.write(":link: [Instagram](https://www.instagram.com/natwest/)")

# ... [similar logic for the about page]

# Apply global CSS styles to the app
st.markdown('<style>div.block-container{padding-top:0.05rem;}</style>',unsafe_allow_html=True)
