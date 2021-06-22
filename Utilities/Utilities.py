from selenium import webdriver
from selenium.webdriver import Chrome


class Utilities:
    def __init__(self):
        __slots__ = 'browser'

        self.brower = ''

    def open_chrome(self):
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(
            r'C:\tools\selenium\chromedriver', chrome_options=options)
        self.browser.maximize_window()
