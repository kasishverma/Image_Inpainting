with st.sidebar:
        # Create a navigation menu with icons
        selected = option_menu(
            menu_title=None,
            options=["home", "projects", "contact us", "About"],
            icons=["house", "book", "envelope", "phone"],
            # menu_icon = <i class ="graph-up-arrow" style="font-size: 2rem; color: cornflowerblue;" > < / i >
            # menu_icon="graph-up-arrow",
            # orientation="horizontal",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#f8f5fa"},
                # "icon": {"color": "orange", "font-size": "15px"},
                "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "menu-icon": {"color": "grey"},
                "nav-link-selected": {"color": "black", "font-size": "12px", "font-weight": "bold",
                                      "background-color": "#eee"},
                "icon": {"color": "purple"},
                # "menu-title": {"font-size": "15px", "font-weight": "bold"}
            }
        )
