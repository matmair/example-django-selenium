from datetime import datetime
from accounts.tests.constants import SCREENSHOT_DUMP_LOCATION


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