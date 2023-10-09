# Create a sidebar in the Streamlit app for navigation
with st.sidebar:
    # Create a navigation menu with icons
    
    # Define the selected option using the 'option_menu' function
    selected = option_menu(
        menu_title=None,  # No specific menu title
        options=["home", "projects", "contact us", "About"],  # List of navigation options
        icons=["house", "book", "envelope", "phone"],  # List of icons corresponding to options

        # Additional options that can be customized:
        # menu_icon = <i class="graph-up-arrow" style="font-size: 2rem; color: cornflowerblue;"></i>
        # menu_icon="graph-up-arrow",  # Icon for the menu title
        # orientation="horizontal",  # Orientation of the menu (horizontal or vertical)
        default_index=0,  # Default selected option index

        # Define styles for the navigation menu and its elements
        styles={
            "container": {"padding": "0!important", "background-color": "#f8f5fa"},  # Menu container styling
            # "icon": {"color": "orange", "font-size": "15px"},  # Styling for icons
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},  # Styling for menu links
            "menu-icon": {"color": "grey"},  # Styling for menu icons
            "nav-link-selected": {"color": "black", "font-size": "12px", "font-weight": "bold",
                                  "background-color": "#eee"},  # Styling for selected menu link
            "icon": {"color": "purple"},  # Styling for icons
            # "menu-title": {"font-size": "15px", "font-weight": "bold"}  # Styling for menu title
        }
    )
        
