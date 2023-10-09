elif selected == "About":
    st.markdown(
        "<p class='custom-text'><h2 style=text-align:center;><span style='color:purple'>About</span></h2></p>",
        unsafe_allow_html=True)
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    # st.header("hi")
    with st.container():
        with st.sidebar:
            subselect = option_menu(
                menu_title=None,
                options=["About Company", "CDIO Team"],
                # icons=["graph-up-arrow","graph-up-arrow","graph-up-arrow"],
                # menu_icon = <i class ="graph-up-arrow" style="font-size: 2rem; color: cornflowerblue;" > < / i >
                # menu_icon="graph-up-arrow",
                # orientation="horizontal",
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "#f8f5fa"},
                    # "icon": {"color": "orange", "font-size": "15px"},
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                    "menu-icon": {"color": "purple"},
                    "nav-link-selected": {"color": "black", "font-size": "12px", "font-weight": "bold",
                                          "background-color": "#eee"},
                    "icon": {"color": "purple"},
                    # "menu-title": {"font-size": "15px", "font-weight": "bold"}
                }
            )
    if subselect == "About Company":
        st.markdown("""
                        <style>
                                .custom-1 {
                                                padding:0px; /* Adjust the padding as needed */
                                                 margin-bottom: -10px}
                                               </style>
                    """, unsafe_allow_html=True)

        st.markdown("<p class='custom-1'><div style='text-align:left; font-size:28px;'><b>NatWest Group </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)
        st.write("NatWest Group is a British banking and insurance holding company, based in Edinburgh, Scotland. The group operates a wide variety of banking brands offering personal and business banking, private banking, investment banking, insurance and corporate finance.")
    if subselect == "CDIO Team":
        st.markdown("<p class='custom-1'><div style='text-align:left; font-size:28px;'><b>CDIO Team </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)
        st.write("About Team")
