# Display a special text message in your Streamlit app
# This text message is customized with specific styling
# It says "Analysis 3" in a large font size and centered on the page
# The text also has a smaller, empty space below it
st.markdown("<p class='custom-1'><div style='text-align:center; font-size:24px;'><b>Analysis 3 </b> <span style = 'font-size:18px;'></span></div></p>", unsafe_allow_html=True)

# Apply a specific style to a container on the page
# This style removes any padding at the top of the container
st.markdown('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
