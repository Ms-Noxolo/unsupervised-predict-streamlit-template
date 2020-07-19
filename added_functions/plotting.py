import streamlit as st
import plotly.graph_objs as go
import pandas as pd 


def counting_plot(data_frame, column_name):
    """
    Returns a bar graph of the number movies in each rating category.
    
    Parameters
    -----------
    data_frame: DataFrame
        A list of movie ratings
    column_name: str
        A column name in df consisting of categorical values
         
    Returns
    --------
    ax : plotly graph object
        Axes object for number of movies in each rating category 
    """

    movie_ratings = data_frame[column_name].value_counts().sort_index()

    fig = go.Figure(
        data=[
            go.Bar(
                y=movie_ratings,
                x=movie_ratings.index,
                hoverinfo='y',
                orientation='v'
            )
        ],
        layout=go.Layout(
            title='Number of movies in each ratings category',
            xaxis={
                'title': 'Movie rating', 
                'type': 'category'
            },
            yaxis={'title': 'Count'}
        )
    )

    return fig





def distribution_plot(data_frame, column_name):

    """
    Returns a histogram of the movie ratings distribution.
    
    Parameters
    -----------
    data_frame: DataFrame
        A dataframe of movie ratings
    column_name: str
        A column name in df consisting of numeric values
         
    Returns
    --------
    ax : plotly graph object
        Axes object of movie ratings distribution 
    """

    fig = go.Figure()
