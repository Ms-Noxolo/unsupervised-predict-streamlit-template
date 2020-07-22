"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Added Custom Libraries
from added_functions.webscrapper import poster, overview
from added_functions.ratings_plots import counting_plot, distribution_plot
from added_functions.year_plots import release_year
from added_functions.runtime import movie_duration
import added_markdown.text as txt

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# Custom Data loading
ratings = pd.read_csv('resources/data/ratings.csv')
movies = pd.read_csv('resources/data/movies.csv')
links = pd.read_csv('../data/links.csv', nrows=10)
metadata = pd.read_csv('../data/imdb_data.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview", "EDA", "Movie App"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Description of our winning approach")

        st.markdown("""We have deployed Machine Learning models which are recommender systems.
        These systems are useful in the prediction of the "rating" or "preference" that a user 
        would give to an item. They are very popular among major tech companies such as 
        Amazon who use it to suggest products to customers, Netflix who use it to recommend movies/TvShows to the users
        as well as YouTube who use it to decide which video to play next on autoplay.
        These are also popular in social media platform such as Facebook uses it to recommend pages to like and people to follow.""")

        st.write("Broadly, recommender systems can be classified into 3 types:")

        st.write("Simple recommenders: These are offer generalized recommendations to every user, based on movie popularity and/or genre.")
        st.write("Content-based recommenders: These suggest similar items based on a particular item. This system uses item metadata, such as genre, director, description, actors, etc. for movies, to make these recommendations. ")
        st.write("Collaborative filtering engines: These systems are widely used, and they try to predict the rating or preference that a user would give an item-based on past ratings and preferences of other users. ")

        from PIL import Image
        image = Image.open('resources/imgs/download.png')

        st.image(image, caption='Recommenders', use_column_width=True)

        st.write(" We considered both the content-based and collaborative filter approaches")

        st.info("Content-based Engine")
        st.markdown("""To achieve a Content-based engine, we considered pairwise cosine 
        similarity scores, which is is a metric used to measure how similar the documents are irrespective of their size
        for all movies based on their plot descriptions and the provided recommendations based on that similarity score threshold.""")
        st.write(" The algorithm summary")
        st.write("Get the index of the movie given its title.")
        st.write("Get the list of cosine similarity scores for that particular movie with all movies,  Convert it into a list of tuples with the first element is its position, and the second is the similarity score.")
        st.write("Sort the aforementioned list based on the similarity scores.")
        stwrite("Get the top 10 elements of this list. Ignore the first element as it refers to self.")
        st.markdown("""The quality of any recommender would be increased with the usage of better metadata and by capturing more of the finer details.
        We thus built a recommender system based on the following metadata: the 3 top actors, the director, related genres, and the movie plot keywords.
        The metadatada can also provide similarity score threshold which as seen as above is very handy in recommendations.""")
        
        from PIL import Image
        image = Image.open('resources/imgs/CF_vs_CBF.png')


        st.info(" Collaborative filtering Engine")
        st.write("Collaborative filters can further be classified into two types:")
        st.write("User-based Filtering: These are systems that recommend products to a user that similar users have liked.")
        st.write("Item-based Filtering: These systems are extremely similar to the content recommendation engine that you built. These systems identify similar items based on how people have rated it in the past.")

        from PIL import Image
        image = Image.open('resources/imgs/Fig_HTML.png')

     

    # You may want to add more sections here for aspects such as an EDcompanies A,
    # or to provide your business pitch.

    # Data manipulation
    df = pd.merge(links, movies, on='movieId')
    metadata.dropna(subset=['runtime'])
    casting_database = pd.merge(metadata, movies, on='movieId')
    ## converting the column to numeric
    metadata['runtime'] = pd.to_numeric(metadata['runtime'])

    ## Runtime slider inputs
    min_runtime = int(metadata['runtime'].min())
    max_runtime = int(metadata['runtime'].max())

    if page_selection == "EDA":
        st.title("Exploratory Data Analysis")

        st.write(txt.introduction)
        show_ratings = st.checkbox("Movie ratings")


        if show_ratings:
            ratings_count = counting_plot(ratings, 'rating')

            st.plotly_chart(ratings_count)
            st.write(txt.ratings_countplot_markdown)

            ratings_distribution = distribution_plot(ratings, 'movieId', 'rating')

            st.plotly_chart(ratings_distribution)
            st.write(txt.avg_ratings_markdown)


        show_yearly = st.checkbox("Yearly releases")

        if show_yearly:
            yearly_counter = release_year(movies)

            st.plotly_chart(yearly_counter)


        length_of_movie = st.checkbox("Movie runtime")
        
        if length_of_movie:

            duration = st.slider(
                label='Max duration of movie runtime',
                min_value=min_runtime,
                max_value=max_runtime,
                value=200,
                step=10
            )

            runtime = movie_duration(metadata, duration)

            st.plotly_chart(runtime)




    if page_selection == "Movie App":        
        st.title('The Movies App')

        option = st.sidebar.selectbox(
            label='Movie',
            options=df['title'],
            index=0
        )

        # Get the movie poster and genre
        movie_id = df[df['title'] == option]['imdbId'].iloc[0]
        genres = df[df['title'] == option]['genres'].iloc[0]
        
        # Casting and Director
        director = casting_database[casting_database['title'] == option]['director'].iloc[0]
        casts = casting_database[casting_database['title'] == option]['title_cast'].iloc[0]

        
        img = poster(movie_id)
        st.sidebar.image(img)

        # Plot summary of the movie
        st.subheader("Summary")
        plot_summary = overview(movie_id)
        st.write(plot_summary)
        
        st.subheader("Genre")
        if '|' in genres:
            genre = genres.replace('|', ', ')
            st.write(genre)
        else:
            st.write(genres)  

        st.subheader("Director")
        st.write(director)

        st.subheader("Cast")

        # Check if there is casting members
        if '|' in casts:
            for cast in casts.split('|'):
                st.write(cast)
        else:
            st.write(casts)        

if __name__ == '__main__':
    main()
