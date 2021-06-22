from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        is_xpath = '//' in selector
        print(selector, ">>>", is_xpath)
        by = By.XPATH if (is_xpath) else By.CSS_SELECTOR
        return by

    def find(self, selector, by=By.CSS_SELECTOR):
        wait = WebDriverWait(self.browser, 100)
        by = self._verify_type_selector(selector)
        return wait.until(EC.presence_of_element_located((by, selector)))

    def click(self, selector):
        self.find(selector).click()
