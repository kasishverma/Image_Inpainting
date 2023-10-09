tab1, tab2 = st.tabs(["TAB1", "TAB2"])
        with tab1:
            col1, col2 = st.columns((2)) #create two columns within TAB1
            with col1:
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

    if subselect == "Analysis 2":
        st.markdown("""
                        <style>
                                .custom-1 {
                                                padding:0px; /* Adjust the padding as needed */
                                                 margin-bottom: -40px}
                                               </style>
                    """, unsafe_allow_html=True)

        st.markdown("<p class='custom-1'><div style='text-align:center; font-size:24px;'><b>Analysis 2 </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)

        st.markdown(
            '<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
        st.sidebar.header("Filter: ")
        st.sidebar.subheader("select date range")
        st.sidebar.date_input("Start Date")
        st.sidebar.date_input("End Date")

        slider_value = st.sidebar.slider("select a value", 0, 100, 50)
        checkbox_option = st.sidebar.checkbox("show data")
        data = pd.DataFrame(
            {'x': np.random.rand(100), 'y': np.random.rand(100)})
        if checkbox_option:
            st.subheader("random data")
            st.write(data)
        st.write("Analysis2 report")
    if subselect == "Analysis 3":
        st.markdown("""
                        <style>
                                .custom-1 {
                                                padding:0px; /* Adjust the padding as needed */
                                                 margin-bottom: -40px}
                                               </style>
                    """, unsafe_allow_html=True)

        st.markdown("<p class='custom-1'><div style='text-align:center; font-size:24px;'><b>Analysis 3 </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)

        st.markdown(
            '<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
        st.sidebar.header("Filter: ")
        st.sidebar.subheader("select date range")
        st.sidebar.date_input("Start Date")
        st.sidebar.date_input("End Date")

        slider_value = st.sidebar.slider("select a value", 0, 100, 50)
        checkbox_option = st.sidebar.checkbox("show data")
        data = pd.DataFrame(
            {'x': np.random.rand(100), 'y': np.random.rand(100)})
        if checkbox_option:
            st.subheader("random data")
            st.write(data)
        st.write("Analysis3 report")
