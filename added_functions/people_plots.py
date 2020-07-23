import plotly.graph_objs as go
import pandas as pd

def director_movie_ratings(imdb_df, rating_df, num):
    """
    Returns the average ratings of movies based for each director

    Parameters
    -----------
    imdb_df: DataFrame
        Dataframe containing imdb movie info
    rating_df: DataFrame
        Dataframe of ratings for each movie by different users
    num: int
        Minimum number of movies that director has in the database 

    Returns
    --------
    ax : plotly graph object
        Axes object showing movie directors info 
    """

    
    

