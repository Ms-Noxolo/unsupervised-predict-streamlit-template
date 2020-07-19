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

    url = 'https://www.themoviedb.org/movie/' + str(reference)
    html = requests.get(url).content
    response = HtmlResponse(url=url, body=html)

    pic_url = response.css('div.image_content img::attr(data-srcset)').get()
    # From the url, get pictures
    first_url = re.findall('https?\S+', pic_url)[0]
    pic = requests.get(first_url)

    img = Image.open(BytesIO(pic.content))

    return img