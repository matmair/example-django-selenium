from django.core.urlresolvers import reverse_lazy

from todos.models import Todo
from todos.tests.utils import UserBaseSeleniumTestCase


class CreateActiveTodoSeleniumTestCase(UserBaseSeleniumTestCase):

    def test_create_todo(self):
        self.login()
        self.webdriver.find_element_by_id("add-todo-input").send_keys("Call Batman!")
        self.webdriver.find_element_by_id("add-todo-form-submit").click()
        active_todo_count = self.webdriver.find_element_by_id("id_todos_count").text
        self.assertEqual(int(active_todo_count), 1)


class TodoActionSeleniumTestCase(UserBaseSeleniumTestCase):

    def setUp(self):
        super(TodoActionSeleniumTestCase, self).setUp()
        self.active_todo_1 = Todo.objects.create(user=self.user, text="Call Superman")
        self.active_todo_2 = Todo.objects.create(user=self.user, text="Call Batman")

    def test_complete_todo_action(self):
        self.login()
        active_todo_count = self.webdriver.find_element_by_id("id_todos_count").text
        self.assertEqual(int(active_todo_count), 2)

        self.webdriver.find_element_by_id("todo-complete-action-%s" % self.active_todo_1.id).click()

        self.webdriver.get('%s%s' % (self.live_server_url, reverse_lazy("todos:completed_list")))
        user_completed_todo_count = Todo.objects.filter(user=self.user, done=True).count()
        todo_count_in_html_elem = self.webdriver.find_element_by_id("id_todos_count").text
        self.assertEqual(int(todo_count_in_html_elem), user_completed_todo_count)

        user_completed_todo = Todo.objects.filter(user=self.user, done=True).first()
        self.webdriver.find_element_by_id("todo-active-action-%s" % user_completed_todo.id).click()
        self.webdriver.get('%s%s' % (self.live_server_url, reverse_lazy("todos:active_list")))
        user_active_todo_count = Todo.objects.filter(user=self.user, done=False).count()
        todo_count_in_html_elem = self.webdriver.find_element_by_id("id_todos_count").text
        self.assertEqual(int(todo_count_in_html_elem), user_active_todo_count)
