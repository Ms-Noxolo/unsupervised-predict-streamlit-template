import plotly.graph_objs as go
import pandas as pd

def director_movies_ratings(imdb_df, rating_df):
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

    # Check for movies with 100 or more views
    viewing_counter = rating_df.groupby('movieId').count()['userId']
    # Filter and get movies with 100 or more viewers
    filtered_counter = viewing_counter[viewing_counter >= 10]

    # Check for movies in the ratings table that are in the filtered_counter
    filtered_df = rating_df[rating_df['movieId'].isin(filtered_counter.index)]

    director_df = pd.merge(imdb_df, filtered_df, on='movieId')

    director_rating = director_df.groupby('director')['rating'].mean().clip(upper=10)
    
    fig = go.Figure(
        data=[
            go.Bar(
                x=director_rating,
                y=director_rating.index,
                hoverinfo='y + x'
            )
        ],
        layout=go.Layout(
            title='Average rating of movies for each director',
            title_x=0.5,
            xaxis='Average rating',
            yaxis='Movie director',
            template='none'
        )
    )

    return fig