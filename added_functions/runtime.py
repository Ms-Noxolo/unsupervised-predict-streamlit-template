import plotly.graph_objs as go

def movie_duration(data_frame, duration):
    """
    Returns a distribution of the runtime of movies in the database
    that are not more than the specified duration.
    
    Parameters
    -----------
    data_frame: DataFrame
        A data frame of movies metadata
    duration: int, float
        The max duration of the movie
         
    Returns
    --------
    ax : plotly graph object
        Axes object for distribution of movie runtime 
    """

    # Filter by maximum duration
    filtered_df = data_frame[data_frame['runtime'] <= duration]

    fig = go.Figure(
        data=[
            go.Histogram(
                x=filtered_df['runtime']
            )
        ],
        layout=go.Layout(
            title='Distribution of movies runtime',
            title_x=0.5,
            xaxis={'title': 'Movie runtime'},
            yaxis={'title': 'Frequency'},
            template='none'
        )   
    )

    return fig