from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse_lazy

from selenium import webdriver
from todos.models import Todo


class CreateActiveTodoSeleniumTestCase(StaticLiveServerTestCase):

    def setUp(self):
        user = User.objects.create_user("todo_man", "todo@man.com", "ThiSk4Zu")
        user.is_active = True
        user.save()
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

    def tearDown(self):
        self.browser.quit()

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


class CompleteTodoSeleniumTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create_user("todo_man", "todo@man.com", "ThiSk4Zu")
        self.user.is_active = True
        self.user.save()
        self.active_todo_1 = Todo.objects.create(user=self.user, text="Call Superman")
        self.active_todo_2 = Todo.objects.create(user=self.user, text="Call Batman")
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

    def tearDown(self):
        self.browser.quit()

    def login(self):
        self.browser.get('%s%s' % (self.live_server_url, reverse_lazy("accounts:login")))
        self.browser.find_element_by_id("id_username").send_keys("todo_man")
        self.browser.find_element_by_id("id_password").send_keys("ThiSk4Zu")
        self.browser.find_element_by_id("user-login-submit").click()

    def test_complete_todo_action(self):
        self.login()
        active_todo_count = self.browser.find_element_by_id("id_todos_count").text
        self.assertEqual(int(active_todo_count), 2)

        self.browser.find_element_by_id("todo-complete-action-%s" % self.active_todo_1.id).click()

        self.browser.get('%s%s' % (self.live_server_url, reverse_lazy("todos:completed_list")))
        user_completed_todo_count = Todo.objects.filter(user=self.user, done=True).count()
        todo_count_in_html_elem = self.browser.find_element_by_id("id_todos_count").text
        self.assertEqual(int(todo_count_in_html_elem), user_completed_todo_count)
