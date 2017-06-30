## Percy Django Selenium Example App

An example Django project with selenium tests which are integrated with Percy.

### Test Case Scenarios
* Verifies user registration.
* Verifies user login.
* Creates active todo object with an authenticated user.
* Changes the status of todo objects from active to completed
* Changes the status of todo objects from completed to active.

Takes screenshots if any test case fail.

### Demo
![selenium-demo](https://github.com/erdem/django-selenium-example/blob/master/demo.gif?raw=true)

### Install 

    pip install -r requirements.txt
    brew install chromedriver

### Usage

    PERCY_TOKEN=X PERCY_PROJECT=X/X python manage.py test

