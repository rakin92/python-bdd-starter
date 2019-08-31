import os
# from sauceclient import SauceClient
from framework.browser import username, access_key


def before_scenario(context, scenario):
    context.name = scenario.name


def after_scenario(context, scenario):
    if hasattr(context, 'browser'):
        context.browser.delete_all_cookies()
        context.browser.quit()
        if username and access_key:
            pass
            # sauce_client = SauceClient(username, access_key)
            # passed = scenario.status == 'passed'
            # sauce_client.jobs.update_job(context.browser.session_id, passed = passed)
