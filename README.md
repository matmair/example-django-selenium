## Percy Django Selenium Example App

An example Django project with selenium tests which are integrated with Percy.

### Install

    pip install -r requirements.txt
    brew install chromedriver

### Usage

    cd todoapp/
    PERCY_TOKEN=X python manage.py test

### Test Case Scenarios
* Verifies user registration.
* Verifies user login.
* Creates active todo object with an authenticated user.
* Changes the status of todo objects from active to completed
* Changes the status of todo objects from completed to active.

Takes screenshots if any test case fail.

### Demo
![selenium-demo](https://github.com/erdem/django-selenium-example/blob/master/demo.gif?raw=true)

### Development of client

```
pip uninstall percy
```

And then when you `import percy`, add the path to your local copy of the client like so:

```python
import sys
sys.path.append('path/to/python-percy-client')
import percy
```
