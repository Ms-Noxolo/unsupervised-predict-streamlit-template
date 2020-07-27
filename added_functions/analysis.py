import plotly.graph_objs as go
# CONTENT BASED FILTERING


# COLLABORATIVE FILTERING

def plot_results(data_frame):
    """
    Returns the average rmse surprise models.

    Parameters
    -----------
    data_frame: DataFrame
        Dataframe containing model prediction rmse scores

    Returns
    --------
    ax : plotly graph object
        Axes object showing average rmse scores.
    """
    colors = ['#1f77b4'] * 6
    colors[0] = 'red'
    fig = go.Figure(
        data=[
            go.Bar(
                x=data_frame['Algorithm'],
                y=data_frame['test_rmse'],
                marker_color=colors
            )
        ],
        layout=go.Layout(
            title='Model performance',
            title_x=0.5,
            xaxis={'title':'Model'},
            yaxis={'title':'Root Mean Square Error'},
            template='none'
        )
    )

    return fig