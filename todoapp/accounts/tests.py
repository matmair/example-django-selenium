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

    def test_login(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_xpath('//input[@type="text"]').click()
        self.browser.find_element_by_xpath('//a').click()

