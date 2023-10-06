# Checking if the user has selected the "projects" option from the sidebar menu
elif selected=="projects":
    
    # Setting the header for the projects page
    # Sample: st.markdown("<your_html_content>", unsafe_allow_html=True)
    st.markdown(
    "<p class='custom-text'><h2 style=text-align:center;><span style='color:purple'>Projects</span></h2></p>",
    unsafe_allow_html=True)
    
    # Adding a custom divider for aesthetic purposes
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    # Create a container for the projects content
    with st.container():
        
        # Adding a sub-menu in the sidebar for different analyses within the projects
        with st.sidebar:
            
            # Define the sub-menu options for different project analyses
            subselect = option_menu(
                # ... [your menu configurations here for the sub-menu]
            )
    
    # Content for Analysis 1 under the "projects" page
    if subselect=="Analysis 1":
        
        # Styling specific elements for Analysis 1
        # Sample: st.markdown("<your_html_content>", unsafe_allow_html=True)
        st.markdown("""
                        <style>
                                .custom-1 {
                                                padding:0px; /* Adjust the padding as needed */
                                                 margin-bottom: -40px}
                                               </style>
                    """, unsafe_allow_html=True)
        
        # Setting the header for Analysis 1
        st.markdown("<p class='custom-1'><div style='text-align:center; font-size:24px;'><b>Analysis 1 </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)
        
        # Displaying filtering options in the sidebar
        st.sidebar.header("Filter: ")
        st.sidebar.subheader("select date range")
        st.sidebar.date_input("Start Date")
        st.sidebar.date_input("End Date")
        
        # Slider and checkbox for additional filtering options
        slider_value=st.sidebar.slider("select a value",0,100,50)
        checkbox_option=st.sidebar.checkbox("show data")
        
        # Sample data for display purposes, replace with your actual data
        data=pd.DataFrame({'x':np.random.rand(100),'y':np.random.rand(100)})
        if checkbox_option:
            st.subheader("random data")
            st.write(data)
        
        # Dropdown menu for selecting the type of graph
        selected_option = st.selectbox("",['line graph', 'bar graph', 'histogram'])
        
        # Displaying a corresponding image based on the selected graph type
        # Sample: if selected_option == "<your_option>": load_image("<your_image_path>")
        if selected_option == "line graph":
            image1_path = load_image("8.png")
        elif selected_option == "bar graph":
            image1_path = load_image("9.png")
        elif selected_option == "histogram":
            image1_path = load_image("0.png")
        
        # Displaying the loaded image
        st.image(image1_path, use_column_width=True)
        
        # Tabs for additional content. Replace "TAB1" and "TAB2" with your tab names.
        tab1, tab2 = st.tabs(["TAB1", "TAB2"])
        
        # Content within the first tab
        with tab1:
            # ... [your content for TAB1]
        
        # Content within the second tab
        with tab2:
            # ... [your content for TAB2]
    
    # Similarly, you can define content for other analyses like "Analysis 2", "Analysis 3", etc.
    # ...
    # Example:
    # elif subselect == "<your_analysis_option>":
    #     st.write("Your content for the selected analysis")
