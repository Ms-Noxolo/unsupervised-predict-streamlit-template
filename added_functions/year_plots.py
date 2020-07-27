import plotly.graph_objs as go

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


def genre_pct(data, year_from, year_to):
    """
    Returns a pie chart showing the percent of genres in the movies

    Parameters
    -----------
    data: DataFrame
        An imdb data frame of movies and their genres
    year_from, year_to: int, default 'None'
        A display period for the year

    Returns
    --------
    ax : plotly graph object
        Axes object of percent genre distribution 
    """

    # Remove Nan values in the year column
    data.dropna(inplace=True, subset=['year'], axis=0)
    # Convert the year column to numeric values
    data['year'] = data['year'].astype(int)
    # Filter by specified range
    filtered_data = data[(data['year'] >= year_from) & (data['year'] <= year_to)]

    # Convert the genre count into a dictionary
    count_dist = filtered_data.sum(axis=0).loc['Sci-Fi':'Mystery'].pipe(dict)
    # Filter by values greater than 0
    filtered_dict = {k: v for k, v in count_dist.items() if v > 0}  

    fig = go.Figure(
        data=[
            go.Pie(
                labels=list(filtered_dict.keys()),
                values=list(filtered_dict.values()),
                hoverinfo='label+percent'
            )
        ],
        layout=go.Layout(
            title=f'Genre distribution {year_from}-{year_to}',
            title_x=0.5,
            showlegend=False
        )
    )

    return fig       