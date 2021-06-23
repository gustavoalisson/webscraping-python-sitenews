from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class Utilities:
    __slots__ = 'browser'

    def __init__(self):

        self.browser = ''

    def open_chrome(self):
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(
            r'C:\tools\selenium\chromedriver', chrome_options=options)
        self.browser.maximize_window()

    def _verify_type_selector(self, selector):
        is_xpath = '/' or '//' in selector
        print(selector, ">>>", is_xpath)
        by = By.XPATH if (is_xpath) else By.CSS_SELECTOR
        return by

    def find(self, selector, by=By.CSS_SELECTOR):
        wait = WebDriverWait(self.browser, 100)
        by = self._verify_type_selector(selector)
        return wait.until(EC.presence_of_all_elements_located((by, selector)))

    def find_class(self, selector, by=By.CLASS_NAME):
        wait = WebDriverWait(self.browser, 100)
        return wait.until(EC.presence_of_all_elements_located((by, selector)))

    def get_attribute(self, selector, attribute):
        element = self.find_class(selector, By.CLASS_NAME)
        return element.get_attribute(attribute)

    def click(self, selector):
        self.find(selector).click()
