from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.browser = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def setUp(self):
        super(MySeleniumTests, self).setUp()
