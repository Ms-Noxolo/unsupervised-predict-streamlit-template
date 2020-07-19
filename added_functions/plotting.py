import streamlit as st
import plotly.graph_objs as go
import pandas as pd 


# RATINGS
def ratings_counter(movie_ratings, orientation='vertical'):
    """
    Returns a bar graph of the number movies in each rating category.
    
    Parameters
    -----------
    movie_ratings: list, np.array, or pd.Series
        A list of movie ratings
    orientation: str, {'vertical', 'horizontal'} default='vertical'
        The orientation of the bar graph
         
    Returns
    --------
    ax : plotly graph object
        Axes object for number of movies in each rating category 
    """

def ratings_distribution(movie_ratings):

    """
    Returns a histogram of the movie ratings distribution.
    
    Parameters
    -----------
    movie_ratings: list, np.array, or pd.Series
        A list of movie ratings
         
    Returns
    --------
    ax : plotly graph object
        Axes object of movie ratings distribution 
    """

    fig = go.Figure()
