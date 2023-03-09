"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Blood Cancer Predictor")

    # Add image to the home page
    st.image("./images/home.jpeg")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
             Blood cancer is a type of cancer that affects your blood cells. Leukaemia, lymphoma and myeloma are some of the most common types of blood cancer. There are also types called MPNs and MDS. Blood cancer is caused by changes (mutations) in the DNA within blood cells. These symptoms often don't appear until the cancer is advanced. Treatments vary but may include surgery, chemotherapy, radiation therapy, targeted drug therapy and immunotherapy.
        </p>
    """, unsafe_allow_html=True)