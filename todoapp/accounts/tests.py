from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class UserRegistrationSeleniumTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(UserRegistrationSeleniumTestCase, cls).setUpClass()
        cls.browser = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(UserRegistrationSeleniumTestCase, cls).tearDownClass()

    def setUp(self):
        super(UserRegistrationSeleniumTestCase, self).setUp()

    def test_registration(self):
        self.browser.find_element_by_id("id-sign-up")
        # self.driver.type_in('input#id_query', 'search something')