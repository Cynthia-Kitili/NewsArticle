import urllib.request,json
from .models import Newssources,Newsarticle

#getting the api key
api_key = None

#getting the sources and articles url
sources_url = None
articles_url = None

def configure_request(app):
    global api_key,sources_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_API_URL']
    articles_url = app.config['ARTICLES_API_URL']



def get_sources(category):
    '''
    function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(category, api_key)
    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        # print(get_sources_response)
        sources_results = None

        if get_sources_response['sources']:
            
            news_sources_list = get_sources_response['sources']
            news_sources = process_sources(news_sources_list)
            print(news_sources)

    return news_sources


def process_sources(sources_list):
    '''
    functin that processes the news sources result and transform them to 
    a list of objects
    args:
        sources_list- a list of dictionaries that contain
        news details
    returns:
        news_sources: a list of news objects
    '''
    news_sources = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')

    

        if url:
            sources_object = Newssources(id,name,description,url,category,language,country)
            news_sources.append(sources_object)
    return news_sources



def get_articles(sources):
    '''
    function that gets json response to
    our url request
    '''
    get_articles_url = articles_url.format(sources,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        news_articles = None

        if get_articles_response['articles']:
            news_articles_list = get_articles_response['articles']
            news_articles = process_articles(news_articles_list)
            print(news_articles)
    return news_articles

def process_articles(news_list):
    '''
    function that processes the news result and transform them to 
    a list of objects
    args:
        news_list- a list of dictionaries that contain
        news details
    returns:
        news_articles: a list of news objects
    '''
    news_articles = []
    for news_item in news_list:
        source_id = news_item.get('source.id')
        source_name = news_item.get('source.name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        if urlToImage:
            news_object = Newsarticle(source_id,source_name,author,title,description,url,urlToImage,publishedAt)
            news_articles.append(news_object)
    return news_articles


