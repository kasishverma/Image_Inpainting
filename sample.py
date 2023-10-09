# Define a CSS style for setting a background image for the entire page
page_bg_img = '''
<style>
    # Set a linear gradient background from #cd9cf2 to #f6f3ff from top to bottom
    [data-testid="stAppViewContainer"]{
        background-image: linear-gradient(to top, #cd9cf2 0%, #f6f3ff 100%);
    }

    # Make the header background color transparent
    [data-testid="stHeader"]{
        background-color: rgba(0,0,0,0);
    }

    # Adjust the position of the toolbar to the right by 2rem
    [data-testid="stToolbar"]{
        right: 2rem;
    }

    # No specific styling for the sidebar is defined here
    [data-testid="stSidebar"]{
    }
</style>
'''

# The above CSS code is intended to be applied to a Streamlit app's appearance
