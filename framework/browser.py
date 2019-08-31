import os
import time
from selenium import webdriver

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
is_remote = os.environ.get('IS_REMOTE')
is_hedless = os.environ.get('RUN_HEADLESS', 'FALSE').upper() == 'FALSE'

build = int(time.time())


def __make_remote_browser(name):
    assert username, "Unable to pull username from environment variables"
    assert access_key, "Unable to pull access_key from environment variables"

    desired_cap = {
        "name": name,
        "platform": os.environ.get('SAUCE_PLATFORM'),
        "browser_name": os.environ.get('SAUCE_BROWSER'),
        "version": os.environ.get('SAUCE_BROWSER_VERSION'),
        "build": build,
    }

    return webdriver.Remote(
        command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (
            username, access_key),
        desired_capabilities=desired_cap)


def __make_local_browser(name):
    options = webdriver.ChromeOptions()
    options.set_headless(headless=is_hedless)
    options.add_argument('--no-sandbox')

    # TODO: Fix options issue
    return webdriver.Chrome()


def make_browser(name):
    if is_remote:
        return __make_remote_browser(name)

    return __make_local_browser(name)
