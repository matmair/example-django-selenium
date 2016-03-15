from datetime import datetime
from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os
from selenium import webdriver

SCREENSHOT_DUMP_LOCATION = os.path.join(settings.BASE_DIR, 'screendumps')


class UserRegistrationSeleniumTestCase(StaticLiveServerTestCase):

    def setUp(self):
        super(UserRegistrationSeleniumTestCase, self).setUp()
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
        self.browser.find_element_by_id("id_username").send_keys("erdem12")
        self.browser.find_element_by_id("id_email").send_keys("erdem12@erdem.com")
        self.browser.find_element_by_id("id_password1").send_keys("cd89c9270")
        self.browser.find_element_by_id("id_password2").send_keys("cd89c9270")
        self.browser.find_element_by_id("user-registration-submit").click()
