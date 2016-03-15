from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class UserRegistrationSeleniumTestCase(StaticLiveServerTestCase):

    def setUp(self):
        super(UserRegistrationSeleniumTestCase, self).setUp()
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

    def tearDown(self):
        self.browser.quit()

    def test_user_registration(self):
        self.browser.find_element_by_id("id-register").click()
        self.browser.find_element_by_id("id_username").send_keys("erdem12")
        self.browser.find_element_by_id("id_email").send_keys("erdem12@erdem.com")
        self.browser.find_element_by_id("id_password1").send_keys("cd89c9270")
        self.browser.find_element_by_id("id_password2").send_keys("cd89c9270")
        self.browser.find_element_by_id("user-registration-submit").click()
