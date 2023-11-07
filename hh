dff["date_filter"] = pd.to_datetime(dff["date_filter"])

    # Getting the min and max date
    startDate = pd.to_datetime(dff["date_filter"]).min()
    endDate = pd.to_datetime(dff["date_filter"]).max()

    with co2:
        date1 = pd.to_datetime(st.date_input("Start Date", startDate))
        
        date2 = pd.to_datetime(st.date_input("End Date", endDate))
        #st.write(date1)
        #st.write(date2)

    dff = dff[(dff["date_filter"] >= date1) & (dff["date_filter"] <= date2)].copy()
