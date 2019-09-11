import unittest
from app.modelsmodels import Article
# from models import article
# Article = article.Article

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News Source Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("CNN News","Inside Apple's big September event: Live updates","See the $699 iPhone 11's new features", "https://edition.cnn.com/tech/live-news/apple-event-september-2019/index.html","https://ichef.bbci.co.uk/news/1024/branded_news/8AC7/production/",_"https://dynaimage.cdn.cnn.com/cnn/digital-images/org/8ec76204-2531-4fc1-bb12-e80d70fe49ff.jpg","2019-09-11T06:50:40Z")

    def test_instance(self):
        '''
        test case to test if object instance is created
        '''
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        '''
        Test case to test if object is initialized properly
        '''
        self.assertEqual(self.new_article.author,"CNN News")
        self.assertEqual(self.new_article.title,"Inside Apple's big September event: Live updates")
        self.assertEqual(self.new_article.description,"See the $699 iPhone 11's new features")
        self.assertEqual(self.new_article.url,"https://edition.cnn.com/tech/live-news/apple-event-september-2019/index.html")
        self.assertEqual(self.new_article.urlToImage,"https://dynaimage.cdn.cnn.com/cnn/digital-images/org/8ec76204-2531-4fc1-bb12-e80d70fe49ff.jpg")
        self.assertEqual(self.new_article.publishedAt,"2019-09-11T06:50:40Z")
