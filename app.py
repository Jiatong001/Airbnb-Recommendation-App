import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px
from PIL import Image
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objects as go
import plotly.graph_objs as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from iso3166 import countries
from io import StringIO

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
     page_title="Airbnb User Recommendation System",
     page_icon="A",
     layout="wide",
     initial_sidebar_state="expanded",
)

st.title("Airbnb User Recommendation Service 🏡 (Demo)")
st.markdown("Seek your perfect fit here ❤️")

st.sidebar.title("Airbnb User Recommendation Service 🏡")

st.sidebar.subheader("Registered on Airbnb already?")
id = st.sidebar.text_input('Key in your id',key='id',max_chars=10)
if st.sidebar.button('Here we go!'):
     image = Image.open('./sample.png')
     st.image(image, use_column_width=True)

dest = st.selectbox('Where do you want to go?',['Raffles Place, Marina, Cecil','Tanjong Pagar, Chinatown','Tiong Bahru, Alexandra, Queenstown','Mount Faber, Telok Blangah, Harbourfront','Buona Vista, Pasir Panjang, Clementi','Clarke Quay, City Hall','Bugis, Beach Road, Golden Mile','Little India, Farrer Park'],key='dest')
col1,col2 = st.beta_columns(2)
with col1: 
     date_from = st.date_input('From when are you booking?',min_value=datetime.date.today(),key='when1')
with col2:
     date_to = st.date_input('To when are you booking?',min_value=date_from,key='when2')
price = st.slider('What price range do you prefer?',10, 500, value=(50,250),step=10, key='price')
room_type = st.multiselect('What room type do you want?',('Single room','double room','triple room','quad room','queen room','king room'))
sort = st.radio('Sort the result by:',('Ratings','Number of reviews','Number of history bookings'))
host = st.checkbox('Superhost only',key='super')
if st.button('Find me the rooms!!!',key='fireaway'):
     col1,col2 = st.beta_columns(2)
     with col1:
          image = Image.open('./listing.png')
          st.image(image, use_column_width=True)
     with col2:
          df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [1.35, 103.82],columns=['lat', 'lon'])
          st.map(df)


with st.sidebar.beta_expander("See explanation"):
     st.markdown('The listing is only for reference. And the filtering criteria are not taken into account for now.') 
                 





