import streamlit as st
import plotly.graph_objs as go
import pandas as pd 

# Release year
def release_year(movies_df):
    """
    Returns a line plot of number of movies released by year

    Parameters
    -----------
    movies_df: DataFrame
        A Datarame consisting of movie title with year released

    Returns
    --------
    ax : plotly graph object
        Axes object of number of movies released by year 
    """

    # Storing the years from the titles separately:
    # We specify the parantheses so we don’t conflict with movies that have years in their titles
    movies_df["year"] = movies_df.title.str.extract("(\(\d\d\d\d\))",expand=False)
    # Removing the parentheses
    movies_df["year"] = movies_df.year.str.extract("(\d\d\d\d)",expand=False)
    # Removing the years from the ‘title’ column
    movies_df["title"] = movies_df.title.str.replace("(\(\d\d\d\d\))", "")
    # Applying the strip function to get rid of any ending whitespace characters that may have appeared
    movies_df["title"] = movies_df["title"].apply(lambda x: x.strip())

    release_year_counter = movies_df.groupby('year')['year'].count()

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