import streamlit as st
import plotly.graph_objs as go
import pandas as pd 

# Release year
def release_year(data_frame):
    """
    Returns a line plot of number of movies released by year

    Parameters
    -----------
    data_frame: DataFrame
        A Datarame consisting of movie title with year released

    Returns
    --------
    ax : plotly graph object
        Axes object of number of movies released by year 
    """

    # Storing the years from the titles separately:
    # We specify the parantheses so we don’t conflict with movies that have years in their titles
    data_frame["year"] = data_frame.title.str.extract("(\(\d\d\d\d\))",expand=False)
    # Removing the parentheses
    data_frame["year"] = data_frame.year.str.extract("(\d\d\d\d)",expand=False)
    # Removing the years from the ‘title’ column
    data_frame["title"] = data_frame.title.str.replace("(\(\d\d\d\d\))", "")
    # Applying the strip function to get rid of any ending whitespace characters that may have appeared
    data_frame["title"] = data_frame["title"].apply(lambda x: x.strip())

    release_year_counter = data_frame.groupby('year')['year'].count()

    fig = go.Figure(
        data=[
            go.Scatter(
                x=release_year_counter.index,
                y=release_year_counter.values,
                mode='lines'
            )
        ],
        layout=go.Layout(
            title='Number of movies released by year',
            title_x=0.5,
            xaxis={'title': 'Year'},
            yaxis={'title': 'Number of movies'},
            template='none'
        )
    ) 

    return fig 