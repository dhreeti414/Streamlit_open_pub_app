import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("open_pubs_modified.csv")

st.set_page_config(page_title="Pub Location", page_icon="📍",layout="wide")
st.header("Nearest *Five* Pubs 🍾")

# code for Euclidian distance to find out nearest pub
def distance(x1, y1, x2, y2):
    return (np.sqrt(x1 - x2) ** 2 + (y1 - y2) ** 2)
 
# Function to calculate K closest points
def kClosest(points, target, K):
    pts = []
    n = len(points)
    d = []
 
    for i in range(n):
        d.append({
            "first": distance(points[i][0], points[i][1], target[0], target[1]),
            "second": i
        })
    

    d = sorted(d, key=lambda l:l["first"])
    
    for i in range(K):
        pt = []
        pt.append(points[d[i]["second"]][0])
        pt.append(points[d[i]["second"]][1])
        pts.append(pt)
   
# Calling DataFrame constructor on list
    df_nearest_loc = pd.DataFrame(pts,columns=['latitude','longitude'])
    st.map(df_nearest_loc)
    
# Driver code
df_geolocation=df[['latitude','longitude']]
points = df_geolocation.values.tolist()

lat = st.number_input('Enter the Latitude',format="%.5f")
lon = st.number_input('Enter the Longitude',format="%.5f",key=int)
if st.button("Submit"):
    target = [lat,lon]
    K = 5

    kClosest(points, target, K)

page_bg_img = '''
<style>
.stApp {
background-image: url("https://wallpapercave.com/wp/wp10307686.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
