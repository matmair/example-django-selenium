from datetime import datetime
from accounts.tests.constants import SCREENSHOT_DUMP_LOCATION
import os


class SeleniumScreenShotMixin():

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

    @property
    def failureException(self):
        class MyFailureException(AssertionError):
            def __init__(self_, *args, **kwargs):
                screenshot_dir = 'reports/screenshots'
                if not os.path.exists(screenshot_dir):
                    os.makedirs(screenshot_dir)
                self.take_screenshot()
                return super(MyFailureException, self_).__init__(*args, **kwargs)
        MyFailureException.__name__ = AssertionError.__name__
        return MyFailureException