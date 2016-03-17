from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os
from selenium import webdriver

SCREENSHOT_DUMP_LOCATION = os.path.join(settings.BASE_DIR, 'screendumps')


class UserRegistrationSeleniumTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

    def tearDown(self):
        self.browser.quit()

    def take_screenshot(self):
        filename = self.get_filename()
        self.browser.get_screenshot_as_file(filename)

    def get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        return '{folder}/{classname}.{method}-{timestamp}.png'.format(
            folder=SCREENSHOT_DUMP_LOCATION,
            classname=self.__class__.__name__,
            method=self._testMethodName,
            timestamp=timestamp
        )

    def test_user_registration(self):
        self.browser.find_element_by_id("id-register").click()
        self.take_screenshot()
        username = "newuser"
        self.browser.find_element_by_id("id_username").send_keys(username)
        self.browser.find_element_by_id("id_email").send_keys("newuser@email.com")
        self.browser.find_element_by_id("id_password1").send_keys("Psiph5sK")
        self.browser.find_element_by_id("id_password2").send_keys("Psiph5sK")
        self.browser.find_element_by_id("user-registration-submit").click()
        self.assertEqual(username, self.browser.find_element_by_id("username-text").text)
        self.take_screenshot()


class UserLoginSeleniumTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        self.create_user()

    def tearDown(self):
        self.browser.quit()

    def create_user(self):
        self.user = User.objects.create_user(username="newuser", password="NiGiw3Ch", email="erdem2@erdem.com")

    def test_user_login(self):
        self.browser.find_element_by_id("id-login").click()
        self.browser.find_element_by_id("id_username").send_keys("newuser")
        self.browser.find_element_by_id("id_password").send_keys("NiGiw3Ch")
        self.browser.find_element_by_id("user-login-submit").click()
        self.assertEqual(self.user.username, self.browser.find_element_by_id("username-text").text)
