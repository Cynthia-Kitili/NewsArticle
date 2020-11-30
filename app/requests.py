from app import app
import urllib.request,json
from .models import news,sources

News = news.News
Sources=sources.Sources
# Getting api key
api_key = app.config ['NEWS_API_KEY']


# Getting the movie base url
base_url = app.config["NEWS_API_SOURCE_URL"]
article_url=app.config["ARTICLES_API_BASE_URL"]


def get_news_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
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
            source_object = Sources(id, title,name, description, category, url)
            news_results.append(source_object)

    return news_results    

def get_news(category):
    '''
    Function that gets the json response to url request
    '''

    get_news_url = article_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_article_results(news_results_list)

    return news_results

def process_article_results(article_list):

    article_results = []

    for item in article_list:
        id = item.get('id')
        name = item.get('name')
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        content = item.get('content')
        
        

        if url:
            article_object = News(id,name,author,title,description,content)
            article_results.append(article_object)

    return article_results
