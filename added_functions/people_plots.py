import plotly.graph_objs as go
import pandas as pd

def director_movies_ratings(imdb_df, rating_df, switch):
    """
    Returns the average ratings of movies based for each director

    Parameters
    -----------
    imdb_df: DataFrame
        Dataframe containing imdb movie info
    rating_df: DataFrame
        Dataframe of ratings for each movie by different users
    switch: str
        Switch button between average ratings and number of ratings 

    Returns
    --------
    ax : plotly graph object
        Axes object showing movie directors info 
    """

    # Check for movies with 10 or more views
    viewing_counter = rating_df.groupby('movieId').count()['userId']
    # Filter and get movies with 10 or more viewers
    filtered_counter = viewing_counter[viewing_counter >= 10]
    
    # Check for movies in the ratings table that are in the filtered_counter
    filtered_df = rating_df[rating_df['movieId'].isin(filtered_counter.index)]

    director_df = pd.merge(imdb_df, filtered_df, on='movieId')

    if switch == 'Number of ratings':
        director_rating = director_df.groupby('director')['rating'].count().sort_values(ascending=False)[:10]
        title = "Top 10 director's movies watched"
        yaxis = "Number of ratings"
    elif switch == 'Average ratings':
        director_rating = director_df.groupby('director')['rating'].mean().sort_values(ascending=False)[:10]
        title = 'Top 10 director average movie ratings with 10 or more viewers'
        yaxis = 'Average rating'
    else:
        director_rating = imdb_df[imdb_df['director'] != 'See full summary'].groupby('director')['movieId'].count().sort_values(ascending=False)[:10]
        title = "Director's count of movies"
        yaxis = 'Number of movies directed'

    fig = go.Figure(
        data=[
            go.Bar(
                y=director_rating,
                x=director_rating.index,
                hoverinfo='y + x',
                orientation='v'
            )
        ],
        layout=go.Layout(
            title=title,
            title_x=0.5,
            yaxis={'title': yaxis},
            template='none'
        )
    )

    return fig


def director_movies_counter(imdb_df, rating_df):
    """
    Returns the average ratings of movies based for each director

    Parameters
    -----------
    imdb_df: DataFrame
        Dataframe containing imdb movie info
    rating_df: DataFrame
        Dataframe of ratings for each movie by different users

    Returns
    --------
    ax : plotly graph object
        Axes object showing movie directors info 
    """

    # Check for movies with 10 or more views
    viewing_counter = rating_df.groupby('movieId').count()['userId']
    # Filter and get movies with 10 or more viewers
    filtered_counter = viewing_counter[viewing_counter >= 10]

    # Check for movies in the ratings table that are in the filtered_counter
    filtered_df = rating_df[rating_df['movieId'].isin(filtered_counter.index)]

    director_df = pd.merge(imdb_df, filtered_df, on='movieId')

    director_rating = director_df.groupby('director')['rating'].mean().sort_values(ascending=False)[:10]
    
    fig = go.Figure(
        data=[
            go.Bar(
                y=director_rating,
                x=director_rating.index,
                hoverinfo='y + x',
                orientation='v'
            )
        ],
        layout=go.Layout(
            title='Top 10 director average movie ratings with 10 or more viewers',
            title_x=0.5,
            yaxis={'title': 'Average rating'},
            template='none'
        )
    )

    return fig