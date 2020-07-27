introduction = """
    ## Introduction

    **Some introductory markdown**
"""

ratings_countplot_markdown = """
    There are high quality movies in the database with majority of the movies
    have a rating of 4, followed by 3 and then 5. 
"""

avg_ratings_markdown = """
    The above distribution is of average movie ratings in the database, 
    to avoid the case whereby a movie has one viewer with a rating of 5 
    for example, the data was filtered such that the movies considered 
    were those with 10 or more viewers.  
"""

#################################### Overview Page ######################################

introduction_overview = """
    Recommendation Engines are the programs that try to determine the similarities
    bewteen two entities. We have deployed Machine Learning models which are recommender systems.
    These systems are useful in the prediction of the "rating" or "preference" 
    that a user would give to an item. They are very popular among major tech 
    companies such as Amazon who use it to suggest products to customers, Netflix 
    who use it to recommend movies/TvShows to the users as well as YouTube who use 
    it to decide which video to play next on autoplay. These are also popular in 
    social media platform such as Facebook uses it to recommend pages to like and 
    people to follow.

    Broadly, recommender systems can be classified into 3 types:

    Simple recommenders: These are offer generalized recommendations to every user, 
    based on movie popularity and/or genre. Content-based recommenders: These suggest 
    similar items based on a particular item. This system uses item metadata, such as 
    genre, director, description, actors, etc. for movies, to make these recommendations.
    Collaborative filtering engines: These systems are widely used, and they try to predict 
    the rating or preference that a user would give an item-based on past ratings and 
    preferences of other users. 
"""
systems = """
    ### Content-based Engine
    To achieve a Content-based engine, we considered pairwise cosine similarity scores, 
    which is is a metric used to measure how similar the documents are irrespective of 
    their size for all movies based on their plot descriptions and the provided 
    recommendations based on that similarity score threshold.
    
    ### The algorithm summary:
    - Get the index of the movie given its title.
    - Get the list of cosine similarity scores for that particular movie with all movies,  
    Convert it into a list of tuples with the first element is its position, and the 
    second is the similarity score.
    - Sort the aforementioned list based on the similarity scores.
    - Get the top 10 elements of this list. 
    - Ignore the first element as it refers to self.

    The quality of any recommender would be increased with the usage of better metadata 
    and by capturing more of the finer details. We thus built a recommender system based 
    on the following metadata: the 3 top actors, the director, related genres, and the 
    movie plot keywords. The metadatada can also provide similarity score threshold 
    which as seen as above is very handy in recommendations.    
"""

Collaborative = """
    ### Collaborative filtering Engine
    Collaborative filters can further be classified into two types:
    User-based Filtering: These are systems that recommend products to a user that 
    similar users have liked. Item-based Filtering: These systems are extremely similar 
    to the content recommendation engine that you built. These systems identify similar 
    items based on how people have rated it in the past.
"""

content_based_intro = """
    Content based filtering uses attributes to recommend similar content.
    These recommendations can be based on movies with similar genres, actors and 
    directors.
"""