import os

class Config:
    '''
    general configuration parent class
    '''
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SOURCES_API_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLES_API_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config:The parent configuration class with general configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config:The parent configuration class with general configuration settings
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}