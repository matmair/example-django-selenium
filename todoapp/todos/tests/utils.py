from accounts.tests.mixins import SeleniumScreenShotMixin
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse_lazy

from selenium import webdriver


class UserBaseSeleniumTestCase(SeleniumScreenShotMixin, StaticLiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create_user("todo_man", "todo@man.com", "ThiSk4Zu")
        self.user.is_active = True
        self.user.save()
        self.webdriver = webdriver.Chrome()
        self.webdriver.get(self.live_server_url)

    def login(self):
        self.webdriver.get('%s%s' % (self.live_server_url, reverse_lazy("accounts:login")))
        self.webdriver.find_element_by_id("id_username").send_keys("todo_man")
        self.webdriver.find_element_by_id("id_password").send_keys("ThiSk4Zu")
        self.webdriver.find_element_by_id("user-login-submit").click()
