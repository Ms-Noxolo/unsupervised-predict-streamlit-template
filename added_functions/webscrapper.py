# Text handling library
import re

# Web scrapping libraries
import requests
from scrapy.http import HtmlResponse

# Image handling library
from io import BytesIO
from PIL import Image

def poster(reference):
    """Returns a movie poster for the selected movie

    Parameters:
    -----------
    reference: str
        A tmdb identification number

    Returns
    --------
    image
        A movie poster
    """

    url = 'https://www.imdb.com/title/tt0' + str(reference)
    html = requests.get(url).content
    response = HtmlResponse(url=url, body=html)

    pic_url = response.css('div.poster img::attr(src)').get()
    # From the url, get pictures
    pic = requests.get(pic_url)

    img = Image.open(BytesIO(pic.content))

    return img