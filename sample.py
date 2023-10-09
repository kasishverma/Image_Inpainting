# Check if the user has selected "About" from the options
elif selected == "About":
    # Add a custom HTML heading for "About" with purple text color and centered alignment
    st.markdown(
        "<p class='custom-text'><h2 style=text-align:center;><span style='color:purple'>About</span></h2></p>",
        unsafe_allow_html=True)
    
    # Add a custom HTML divider line
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
    # Create a container for layout organization
    with st.container():
        with st.sidebar:
            # Create an option menu in the sidebar with two choices: "About Company" and "CDIO Team"
            subselect = option_menu(
                menu_title=None,
                options=["About Company", "CDIO Team"],
                default_index=0,  # Default selection
                styles={
                    "container": {"padding": "0!important", "background-color": "#f8f5fa"},
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                    "menu-icon": {"color": "purple"},
                    "nav-link-selected": {"color": "black", "font-size": "12px", "font-weight": "bold",
                                          "background-color": "#eee"},
                    "icon": {"color": "purple"},
                }
            )
    
    # If "About Company" is selected
    if subselect == "About Company":
        # Apply some custom HTML styling
        st.markdown("""
            <style>
                .custom-1 {
                    padding: 0px; /* Adjust the padding as needed */
                    margin-bottom: -10px;
                }
            </style>
        """, unsafe_allow_html=True)

        # Add a custom HTML heading for "NatWest Group"
        st.markdown("<p class='custom-1'><div style='text-align:left; font-size:28px;'><b>NatWest Group </b> <span style='font-size:18px;'></span></div></p>", unsafe_allow_html=True)
        
        # Provide information about NatWest Group
        st.write("NatWest Group is a British banking and insurance holding company, based in Edinburgh, Scotland. The group operates a wide variety of banking brands offering personal and business banking, private banking, investment banking, insurance, and corporate finance.")
    
    # If "CDIO Team" is selected
    if subselect == "CDIO Team":
        # Add a custom HTML heading for "CDIO Team"
        st.markdown("<p class='custom-1'><div style='text-align:left; font-size:28px;'><b>CDIO Team </b> <span style='font-size:18px;'></span></div></p>", unsafe_allow_html=True)
        
        # Provide information about the CDIO Team
        st.write("About Team")
        
