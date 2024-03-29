import streamlit as st
import base64  

def sidebar_bg(side_bg):
   side_bg_ext = 'png'
   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
side_bg = './music.jpeg'
sidebar_bg(side_bg)
st.header('_Music Recommendation_')
search_choices = ['Song/Track', 'Artist', 'Album']
search_selected = st.sidebar.selectbox("Select your choice : ", search_choices)