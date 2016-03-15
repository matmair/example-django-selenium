from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class UserRegistrationSeleniumTestCase(StaticLiveServerTestCase):

    def setUp(self):
        super(UserRegistrationSeleniumTestCase, self).setUp()
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

    def tearDown(self):
        self.browser.quit()

    def test_registration(self):
        self.browser.find_element_by_id("id-register").click()
        self.browser.stop_client()
        # self.driver.type_in('input#id_query', 'search something')
