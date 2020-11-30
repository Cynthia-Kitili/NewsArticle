from app import app
import urllib.request,json
from .models import news,sources

News = news.News
Sources=sources.Sources
# Getting api key
api_key = app.config ['NEWS_API_KEY']


# Getting the movie base url
base_url = app.config["ARTICLES_API_BASE_URL"]
source_url=app.config["NEWS_API_SOURCE_URL"]


def get_news_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title=news_item.get('title')
        name = news_item.get('name')
        description = news_item.get('description')
        category = news_item.get('category')
        url = news_item.get('url')

        if url:
            source_object = Sources(id, name, description, category, url)
            news_results.append(source_object)

    return news_results    
