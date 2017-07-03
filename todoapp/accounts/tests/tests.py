from accounts.tests.mixins import SeleniumScreenShotMixin
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os
import sys

from selenium import webdriver
from IPython import embed

# Uncomment for local development testing
# sys.path.append('/Users/djones/Code/python-percy-client')
import percy

class UserRegistrationSeleniumTestCase(SeleniumScreenShotMixin, StaticLiveServerTestCase):

    def setUp(self):
        self.webdriver = webdriver.Chrome()
        self.webdriver.get(self.live_server_url)

        root_static_dir = os.path.join(os.path.dirname(__file__), '../../', 'static')

        loader = percy.ResourceLoader(
          root_dir=root_static_dir,
          # Prepend `/assets` to all of the files in the static directory, to match production assets.
          # This is only needed if your static assets are served from a nested directory.
          base_url='/static/',

          webdriver=self.webdriver,
        )

        self.percy_runner = percy.Runner(loader=loader)
        self.percy_runner.initialize_build()

    def test_user_registration(self):
        self.webdriver.find_element_by_id("id-register").click()

        username = "newuser"
        self.webdriver.find_element_by_id("id_username").send_keys(username)
        self.webdriver.find_element_by_id("id_email").send_keys("newuser@email.com")
        self.webdriver.find_element_by_id("id_password1").send_keys("Psiph5sK")
        self.webdriver.find_element_by_id("id_password2").send_keys("Psiph5sK")

        self.webdriver.find_element_by_id("user-registration-submit").click()
        self.assertEqual(username, self.webdriver.find_element_by_id("username-text").text)

        
        self.percy_runner.snapshot()

    def tearDown(self):
        if sys.exc_info()[0]:  # Returns the info of exception being handled
            self.take_screenshot()
        self.webdriver.quit()

        self.percy_runner.finalize_build()


class UserLoginSeleniumTestCase(SeleniumScreenShotMixin, StaticLiveServerTestCase):

    def setUp(self):
        self.webdriver = webdriver.Chrome()
        self.webdriver.get(self.live_server_url)
        self.user = User.objects.create_user(username="newuser", password="NiGiw3Ch", email="todo@todoapp.com")

    def tearDown(self):
        self.webdriver.quit()

    def test_user_login(self):
        self.webdriver.find_element_by_id("id-login").click()
        self.webdriver.find_element_by_id("id_username").send_keys("newuser")
        self.webdriver.find_element_by_id("id_password").send_keys("NiGiw3Ch")
        self.webdriver.find_element_by_id("user-login-submit").click()
        self.assertEqual(self.user.username, self.webdriver.find_element_by_id("username-text").text)
