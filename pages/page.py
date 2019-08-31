from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import By


class Page(object):
    """
    Base class that all page models can inherit from
    """

    def __init__(self, selenium_driver):
        self.driver = selenium_driver

    def get_title(self):
        return self.driver.title

    def visible_by_id(element_id):
        return EC.visibility_of_element_located((By.ID, element_id))

    def visible_by_css(css_selector):
        return EC.visibility_of_element_located(
            (By.CSS_SELECTOR, css_selector))

    def visible_by_class(element_class):
        return EC.visibility_of_element_located((By.CLASS_NAME, element_class))

    def visible_by_name(name):
        return EC.visibility_of_element_located((By.NAME, name))

    def visible_by_text(text):
        x_path = "//*[contains(text(), '{value}')]".format(value=text)
        return EC.visibility_of_element_located((By.XPATH, x_path))

    def clickable_by_name(name):
        return EC.element_to_be_clickable((By.NAME, name))

    def clickable_by_class(element_class):
        return EC.element_to_be_clickable((By.CLASS_NAME, element_class))

    def clickable_by_text(text):
        x_path = "//*[contains(text(), '{value}')]".format(value=text)
        return EC.element_to_be_clickable((By.XPATH, x_path))

    def clickable_by_id(element_id):
        return EC.element_to_be_clickable((By.ID, element_id))

    def not_visible_by_id(element_id):
        return EC.invisibility_of_element_located((By.ID, element_id))

    def not_visible_by_css(css_selector):
        return EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, css_selector))

    def not_visible_by_class(element_class):
        return EC.invisibility_of_element_located(
            (By.CLASS_NAME, element_class))

    def select_by_value(value):
        x_path = "//option[@value='{value}']".format(value=value)
        return self.driver.find_element_by_xpath(x_path).click()

    def click_with_text_contains(value):
        x_path = "//*[contains(text(), '{value}')]".format(value=value)
        return self.driver.find_element_by_xpath(x_path).click()

    def click_button_with_name(value):
        x_path = "//button[@name='{value}']".format(value=value)
        return self.driver.find_element_by_xpath(x_path).click()

    def click_button_with_name(value):
        x_path = "//button[@name='{value}']".format(value=value)
        return self.driver.find_element_by_xpath(x_path).click()

    def click_on_label_for(value):
        x_path = "//label[@for='{value}']".format(value=value)
        return self.driver.find_element_by_xpath(x_path).click()

    def visible_by_name_has_text(element, text):
        return EC.text_to_be_present_in_element((By.NAME, element), text)

    def visible_by_id_has_text(element, text):
        return EC.text_to_be_present_in_element((By.ID, element), text)
