st.markdown("<p class='custom-1'><div style='text-align:center; font-size:24px;'><b>TNTR Analysis </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)
    # Apply a specific style to a container on the page. removes any padding at the top of the container
    st.markdown(
        '<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
    co1,co2=st.columns(2)
    with co1:
        fl = st.file_uploader(":file_folder: Upload a file", type=(["json"]))
        if fl is not None:
            filename = fl.name
            st.write(filename)
            # df_2 = pd.read_json(filename, encoding = "ISO-8859-1")
            #df_2=pd.read_csv(pd.concat("r'\\rbsres01\shareddata\rassre\AIMLData\TNTR\", filename))
            df_2 = pd.read_json(filename)

        else:
            df_2 = pd.read_json(
                r'\\rbsres01\shareddata\rassre\AIMLData\TNTR\TNTR_trade_prodprl_sample_sept.json\TNTR_trade_prodprl_sample_sept.json')
