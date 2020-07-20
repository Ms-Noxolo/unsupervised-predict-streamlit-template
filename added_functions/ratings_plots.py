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
            title_x=0.5,
            xaxis={
                'title': 'Movie rating', 
                'type': 'category'
            },
            yaxis={'title': 'Count'},
            template='none'
        )
    )

    return fig



def distribution_plot(data_frame, groupby_column, column_name):

    """
    Returns a histogram of the movie ratings distribution.
    
    Parameters
    -----------
    data_frame: DataFrame
        A dataframe of movie ratings
    groupby_column: str
        A column name in df used as a groupby column
    column_name: str
        A column name in df consisting of numeric values
         
    Returns
    --------
    ax : plotly graph object
        Axes object of movie ratings distribution 
    """
    
    # Check for movies with 100 or more views
    viewing_counter = data_frame.groupby(groupby_column).count()[column_name]
    # Filter and get movies with 100 or more viewers
    filtered_counter = viewing_counter[viewing_counter >= 10]

    # Check for movies in the ratings table that are in the filtered_counter
    filtered_df = data_frame[data_frame[groupby_column].isin(filtered_counter.index)]

    avg_rating = filtered_df.groupby(groupby_column)[column_name].mean()

    fig = go.Figure(
        data=[
            go.Histogram(
            x=avg_rating,
            nbinsx=10
            )
        ],
        layout=go.Layout(
            title='Average ratings of movies',
            title_x=0.5,
            xaxis={'title': 'Movie ratings', 'range': [0.5, 5.5]},
            yaxis={'title': 'Frequency'},
            template='none'
        )        
    )

    return fig