import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("open_pubs_modified.csv")

st.set_page_config(page_title="Pub Location", page_icon="🗺️", layout="wide")
st.header("Locations of all the Pubs in UK:")
st.caption("Search for all the pubs present at a specific location of UK")
loc_authority = st.selectbox('Select a Local Authority', list(df['local_authority'].unique()))

button_click = st.button('Search')
if button_click == True: 
    authority = df[df['local_authority'] == loc_authority]
    st.write("Number of Pubs under the selected Local Authority:", len(authority))
    locations = authority[['latitude','longitude']]
    st.map(locations)

page_bg_img = '''
<style>
.stApp {
background-image: url("https://wallpapercave.com/wp/wp10307686.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
