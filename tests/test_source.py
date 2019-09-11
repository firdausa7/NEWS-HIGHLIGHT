import unittest
from app.models import Source
# from models import source
# Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News Source Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('abc-news','ABC News','Your trusted source for breaking news.','http://abcnews.go.com/','general','us')

    def test_instance(self):
        '''
        test case to test if object instance is created
        '''
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
        '''
        Test case to test if object is initialized properly
        '''
        self.assertEqual(self.new_source.id,'cnn-news')
        self.assertEqual(self.new_source.name,'CNN News')
        self.assertEqual(self.new_source.description,'Shawn Mendes finally admits to being in a relationship')
        self.assertEqual(self.new_source.url,'https://edition.cnn.com/2019/09/02/entertainment/shawn-mendes-relationship-trnd/index.html')
        self.assertEqual(self.new_source.category,'general')
        self.assertEqual(self.new_source.country,'us')

if __name__ == '__main__':
    unittest.main()
