import streamlit as st
import pandas as pd
import numpy as np
st.title("sample dashboard")
st.divider()
st.write("welcome to streamlit")
st.sidebar.header("user input")
slider_value=st.sidebar.slider("select a value",0,100,50)
checkbox_option=st.sidebar.checkbox("show data")
data=pd.DataFrame({'x':np.random.rand(100),'y':np.random.rand(100)})
if checkbox_option:
    st.subheader("random data")
    st.write(data)
tab1, tab2 = st.tabs(["BUSINESS", "TECHNOLOGY"])
st.subheader("chart")
st.map(data)
if st.button("click me"):
    st.write("button clicked")
option=st.selectbox("select an option",["option1","option2","option3"])
st.write("you selected:",option)