import unittest
from models import news,sources
News = news.News
Sources=sources.Sources

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News (1234,'Best News Source','Joanna Weiss','Politics','Time to shine','Be the best version of yourself')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))  

class SorcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Sources (1669,'Best News Source','Economics','Different Direction','Economics','"https://abcnews.go.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))          

if __name__=='__main__':
    unittest.main()
              




