import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title("Movie Recommendation Tool")
st.header("Due to several limitation in the data, accuracy level is to be improved")
movie_df=pickle.load(open("movie_recm.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
list_movie=np.array(movie_df["film_title"])
option = st.selectbox(
"Select Your Favorite Movie ",
(list_movie))

# def show_url(movie):
#      x=[]
#      index = movie_df[movie_df['film_title'] == movie].index[0]
#      distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#      for i in distances[1:6]:

#           x.append(movie_df.iloc[i[0]].urls)
#      return(x)
def movie_recommend(movie):
     index = movie_df[movie_df['film_title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     l=[]
     for i in distances[1:6]:
          l.append("{}".format(movie_df.iloc[i[0]].film_title))
          # return("{} {}".format(movie_df.iloc[i[0]].title, movie_df.iloc[i[0]].urls))
     return(l)
if st.button('Recommend Me'):
     st.write('5 Recommended Movies for You:')
     # st.write(movie_recommend(option),show_url(option))
     df = pd.DataFrame({
          'Movie Recomendation': movie_recommend(option),
        #   'Movie Url': show_url(option)
     })

     st.table(df)