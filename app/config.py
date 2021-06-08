class Config:
    '''
    General configuration parent class
    '''
    SOURCE_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    NEWS_API_KEY = 'd1ec0f636be94766b9ae8b1995f9ca44'

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True