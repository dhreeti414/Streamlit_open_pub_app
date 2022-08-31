import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("open_pubs_modified.csv")

st.set_page_config(page_title="Home", page_icon="🍻",layout="wide")
st.title("🥂Cheers to pour decisions🥂")
st.subheader("✨Welcome to my first Streamlit application!✨")
st.header("Details:-")
total_pubs= len(df['fsa_id'].unique())
total_localAuthority= len(df['local_authority'].unique())
total_postalCodes= len(df['postcode'].unique())
st.subheader(f"Total pub present in United Kingdom is {total_pubs}")
st.subheader(f"Total local authorities of pubs is {total_localAuthority}")
st.subheader(f"Total pub present in United Kingdom is {total_postalCodes}")
st.markdown(
    """
<style>
.streamlit-expanderHeader {
    font-size: x-large;
}
</style>
""",
    unsafe_allow_html=True,
)
with st.expander(label="Glimpse of dataset:-",expanded=False):
    st.dataframe(df.head(20))
page_bg_img = '''
<style>
.stApp {
background-image: url("https://wallpapercave.com/wp/wp10307686.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
