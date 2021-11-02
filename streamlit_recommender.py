import pandas as pd
import numpy as np
import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from gensim.corpora.dictionary import Dictionary
from gensim.models.tfidfmodel import TfidfModel
from gensim.similarities import MatrixSimilarity

def keywords_recommendation(keywords, number_of_hits):
    query_doc_bow = dictionary.doc2bow(keywords) # get a bag of words from the query_doc
    query_doc_tfidf = tfidf[query_doc_bow] #convert the regular bag of words model to a tf-idf model where we have tuples
        # of the movie ID and it's tf-idf value for the movie
    similarity_array = sims[query_doc_tfidf] # get the array of similarity values between our movie and every other movie. 
        #So the length is the number of movies we have. To do this, we pass our list of tf-idf tuples to sims.
    Courses = courses
    similarity_series = pd.Series(similarity_array.tolist(), index=Courses.Title.values) #Convert to a Series
    top_hits = similarity_series.sort_values(ascending=False)[:number_of_hits] #get the top matching results, 
        # i.e. most similar movies
    
    # Print the top matching movies
    # st.write("Our top %s most similar courses for the keywords %s are:" %(number_of_hits, keywords))
    # for idx, (Courses,score) in enumerate(zip(top_hits.index, top_hits)):
    #     st.write("%d '%s' with a similarity score of %.3f" %(idx+1, Courses, score))

    return Courses, top_hits

##Data Preparation
df_udemy = pd.read_csv('D:\\Downloads\\all_udemy_dataset.csv')

## there's rating that has a string inside of it, we will remove the data
df_filtered = df_udemy[pd.to_numeric(df_udemy.Rating, errors='coerce').notnull()]
df_filtered = df_filtered.reset_index(drop=True)
df_filtered['Rating'] = pd.to_numeric(df_filtered['Rating'])

##Pre-Filtering 1 : we rank the courses based on the number of votes and taking the top 20k courses
top_20k_courses = df_filtered.sort_values(by='Rating',ascending=False)[:20000]
top_20k_courses = top_20k_courses.reset_index(drop=True)

##Preparing for modelling
top_20k_courses = top_20k_courses.drop(columns=['Unnamed: 0','index','Summary'],axis=1)

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger') 
courses = top_20k_courses[['Title','topic','Rating','Link']]
keywords = courses['topic'].tolist()
keywords = [word_tokenize(keyword.lower()) for keyword in keywords]
processed_keywords = keywords

dictionary = Dictionary(processed_keywords) # create a dictionary of words from our keywords
corpus = [dictionary.doc2bow(doc) for doc in processed_keywords] #create corpus where the corpus is a bag of words for each document
tfidf = TfidfModel(corpus) #create tfidf model of the corpus
# Create the similarity data structure. This is the most important part where we get the similarities between the movies.
sims = MatrixSimilarity(tfidf[corpus], num_features=len(dictionary))
courses = top_20k_courses[['Title','topic']]

if 'top_hots' not in st.session_state:
    st.session_state['top_hots'] = []

cols_cat = list(set(courses['topic'].values.tolist()))
cols_num = [1,2,3,4,5,6,7,8,9,10]

st.sidebar.markdown(
    '<p class="header-style">Please choose your favorite topic</p>',
    unsafe_allow_html=True
)
category_topic = st.sidebar.selectbox(
    f"Select Topic: ",
    sorted(cols_cat)
)

amount_fetch = st.sidebar.selectbox(
    f"How Many Courses Do You Want To Fetch: ",
    sorted(cols_num)
)

category_topic = str(category_topic)
values_to_predict = np.array(category_topic).reshape(1, -1)


st.markdown(
    """
    <style>
    .header-style {
        font-size:25px;
        font-family:sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .font-style {
        font-size:20px;
        font-family:sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    '<p class="header-style"> Recommender Engine Predictions </p>',
    unsafe_allow_html=True
)


Courses, st.session_state['top_hits'] = keywords_recommendation(values_to_predict,amount_fetch)
filtered_df = courses[courses['topic']==category_topic]
st.write("Our top %s most similar courses for the keywords %s are:" %(amount_fetch, values_to_predict[0,0]))

for idx in range(amount_fetch):
    # st.write(filtered_df['Title'].iloc[idx])
    st.write("%d '%s' " %(idx+1, filtered_df['Title'].iloc[idx]))
# st.write(filtered_df.iloc[0:amount_fetch])
