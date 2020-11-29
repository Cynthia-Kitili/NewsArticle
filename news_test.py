import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News (1234,'Best News Source','All Articles are Available','http://newsapi.org/v2/everything?q=bitcoin&from=2020-10-29&sortBy=publishedAt&apiKey=98cbe32074334e28b2b2499159d3bc32')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))  

if __name__=='__main__':
    unittest.main()
              




