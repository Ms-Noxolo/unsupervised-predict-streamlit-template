import streamlit as st
import plotly.graph_objs as go
import pandas as pd 


def counting_plot(df, column_name, orientation='vertical'):
    """
    Returns a bar graph of the number movies in each rating category.
    
    Parameters
    -----------
    df: dataframe
        A list of movie ratings
    column_name: str
        A column name in df consisting of categorical values
    orientation: str, {'vertical', 'horizontal'} default='vertical'
        The orientation of the bar graph
         
    Returns
    --------
    ax : plotly graph object
        Axes object for number of movies in each rating category 
    """



def distribution_plot(df, column_name):

    """
    Returns a histogram of the movie ratings distribution.
    
    Parameters
    -----------
    df: dataframe
        A dataframe of movie ratings
    column_name: str
        A column name in df consisting of numeric values
         
    Returns
    --------
    ax : plotly graph object
        Axes object of movie ratings distribution 
    """

    fig = go.Figure()
