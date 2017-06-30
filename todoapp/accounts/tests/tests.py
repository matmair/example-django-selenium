from accounts.tests.mixins import SeleniumScreenShotMixin
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver


class UserRegistrationSeleniumTestCase(SeleniumScreenShotMixin, StaticLiveServerTestCase):

    def setUp(self):
        self.webdriver = webdriver.Chrome()
        self.webdriver.get(self.live_server_url)

    def test_user_registration(self):
        self.webdriver.find_element_by_id("id-register").click()

        username = "newuser"
        self.webdriver.find_element_by_id("id_username").send_keys(username)
        self.webdriver.find_element_by_id("id_email").send_keys("newuser@email.com")
        self.webdriver.find_element_by_id("id_password1").send_keys("Psiph5sK")
        self.webdriver.find_element_by_id("id_password2").send_keys("Psiph5sK")

        self.webdriver.find_element_by_id("user-registration-submit").click()
        self.assertEqual(username, self.webdriver.find_element_by_id("username-text").text)


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
