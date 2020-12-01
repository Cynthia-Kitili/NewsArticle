import unittest
from models import Newssources

class SourcesTest(unittest.TestCase):
    '''
    test class to test behaviour of news article class
    '''
    def  setUp(self):
        '''
        set up method that will rub
        before every test
        '''

        self.new_source = Newssource('The Wall Street Journal',
        'Rebecca Ballhaus',
        'Trump to Promote U.S. as Open for Business in Davos Speech',
        '"Donald Trump is expected to promote the U.S. as “open for business,” while highlighting the nation’s commitment to global trade in an address to foreign leaders and business executives at the World Economic Forum.'
        ,'https://www.wsj.com/articles/trump-to-promote-u-s-as-open-for-business-in-davos-speech-1516962420','https://si.wsj.net/public/resources/images/BN-XE643_3nQuF_TOP_20180126053039.jpg'
        ,'2018-01-26T11:04:48Z')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Newssource))
if __name__ == '__main__':
    unittest.main()