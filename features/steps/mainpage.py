from selenium import webdriver
from pages.mainpage import MainPage
from framework.browser import make_browser


@given('we are on a browser')
def step_load_browser(context):
    context.browser = make_browser(context.name)


@given('we are looking at the guinea pig website')
def step_load_site(context):
    context.browser.get(
        'https://saucelabs-sample-test-frameworks.github.io/training-test-page')
    context.page = MainPage(context.browser)


@when('we click on the uncheck box')
def step_click_uncheck(context):
    context.page.find_unchecked_checkbox().click()


@then('it should be checked')
def step_should_be_checked(context):
    assert context.page.find_unchecked_checkbox(
    ).is_selected(), "Checkbox is not selected"


@when('I populate the email field')
def step_type_email(context):
    context.page.find_email_input().send_keys('testmail-email@gmail.com')


@then('it should contain the value I entered')
def step_check_email_value(context):
    value = context.page.find_email_input().get_attribute('value')
    assert value == 'testmail-email@gmail.com', "The value is incorrect"


@given('we are on the guinea pig website')
def step_validate_location(context):
    context.browser.get(
        'https://saucelabs-sample-test-frameworks.github.io/training-test-page')
    context.page = MainPage(context.browser)


@when('I click on the link')
def step_click_on_link(context):
    context.page = MainPage(context.browser)
    context.page.find_link().click()


@then('I should see a new page')
def step_validate_redirect(context):
    print(
        "context browser title is {title}".format(
            title=context.browser.title))
    assert 'another' in context.page.get_title()
