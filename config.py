import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    EVERYTHING_SOURCE_BASE_URL = 'https://newsapi.org/v2/everythingNews?sources={}&pageSize={}&apiKey={}'
    HEADLINES_BASE_URL = 'https://newsapi.org/v2/headlines?language=en&pageSize={}&apiKey={}'
    EVERYTHINGNEWS_BASE_URL = 'https://newsapi.org/v2/everythingNews?sources=bbc-news,al-jazeera-english,cnn,independent,google-news,the-telegraph,mashable,the-lad-bible,buzzfeed,bloomberg,engadget,espn,fortune&sortBy=publishedAt&pageSize={}&apiKey={}'
    SEARCH_API_BASE_URL = 'https://newsapi.org/v2/everythingNews?language=en&q={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}
