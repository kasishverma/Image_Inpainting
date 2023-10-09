# Import the necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# Create two tabs: "TAB1" and "TAB2"
tab1, tab2 = st.tabs(["TAB1", "TAB2"])

# Inside "TAB1"
with tab1:
    # Create two columns within "TAB1"
    col1, col2 = st.columns((2))

    # Inside the first column (col1)
    with col1:
        # Add a centered heading with HTML formatting
        st.markdown("<h5 style='text-align: center;'>H1</h5>", unsafe_allow_html=True)
        
        # Load and display an image (1.png) with a caption in the first column
        images1_1 = load_image("1.png")
        st.image(images1_1, caption="image3", use_column_width=True)
        
        # Add a horizontal divider
        st.divider()
        
        # Load and display another image (6.png) with a caption in the first column
        images1_2 = load_image("6.png")
        st.image(images1_2, caption="image4", use_column_width=True)

    # Inside the second column (col2)
    with col2:
        # Add a centered heading with HTML formatting
        st.markdown("<h5 style='text-align: center;'>H2</h5>", unsafe_allow_html=True)
        
        # Load and display an image (3.png) with a caption in the second column
        images2_1 = load_image("3.png")
        st.image(images2_1, caption="image1", use_column_width=True)
        
        # Add a horizontal divider
        st.divider()
        
        # Load and display another image (4.png) with a caption in the second column
        images2_2 = load_image("4.png")
        st.image(images2_2, caption="image2", use_column_width=True)

# Inside "TAB2"
with tab2:
    # Load and display an image (1.png) with a caption in "TAB2"
    images1_1 = load_image("1.png")
    st.image(images1_1, caption="image3", use_column_width=True)

# Depending on the selected option in your interface ("subselect"), do the following:

# If "Analysis 2" is selected
if subselect == "Analysis 2":
    # Apply some custom HTML styling
    st.markdown("""
        <style>
            .custom-1 {
                padding:0px; /* Adjust the padding as needed */
                margin-bottom: -40px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Add a custom HTML heading for "Analysis 2"
    st.markdown("<p class='custom-1'><div style='text-align:center; font-size:24px;'><b>Analysis 2 </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)

    # Apply some more custom HTML styling
    st.markdown('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
    
    # Create a sidebar header and subheader
    st.sidebar.header("Filter: ")
    st.sidebar.subheader("Select date range")
    
    # Add date input widgets in the sidebar
    st.sidebar.date_input("Start Date")
    st.sidebar.date_input("End Date")
    
    # Create a slider widget in the sidebar
    slider_value = st.sidebar.slider("Select a value", 0, 100, 50)
    
    # Create a checkbox widget in the sidebar
    checkbox_option = st.sidebar.checkbox("Show data")
    
    # Generate and display random data if the checkbox is checked
    data = pd.DataFrame({'x': np.random.rand(100), 'y': np.random.rand(100)})
    if checkbox_option:
        st.subheader("Random data")
        st.write(data)
    
    # Display a report for "Analysis 2"
    st.write("Analysis 2 report")

# If "Analysis 3" is selected (similar structure to "Analysis 2")
if subselect == "Analysis 3":
    # ...
        
