from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse_lazy

from selenium import webdriver


class TodoCreateSeleniumTestCase(StaticLiveServerTestCase):

    def tearDown(self):
        self.browser.quit()

    def setUp(self):
        user = User.objects.create_user("todo_man", "todo@man.com", "ThiSk4Zu")
        user.is_active = True
        user.save()
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.get(self.live_server_url)

    def login(self):
        self.browser.get('%s%s' % (self.live_server_url, reverse_lazy("accounts:login")))
        self.browser.find_element_by_id("id_username").send_keys("todo_man")
        self.browser.find_element_by_id("id_password").send_keys("ThiSk4Zu")
        self.browser.find_element_by_id("user-login-submit").click()

    def test_create_todo(self):
        self.login()
        self.browser.find_element_by_id("add-todo-input").send_keys("Call Batman!")
        self.browser.find_element_by_id("add-todo-form-submit").click()
        active_todo_count = self.browser.find_element_by_id("id_todos_count").text
        self.assertEqual(int(active_todo_count), 1)
