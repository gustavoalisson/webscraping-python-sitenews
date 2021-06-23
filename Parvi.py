from Utilities.Utilities import Utilities
from selectors import selectors


class Parvi:
    __slots__ = 'robot', 'SELECTORS'

    def __init__(self, SELECTORS):
        self.robot = Utilities()
        self.SELECTORS = SELECTORS

    def start_browser(self):
        self.robot.open_chrome()

    def select_url(self, url):
        self.robot.browser.get(url)

    def cookies_confirm(self):
        button_ok = self.SELECTORS['BUTTONS']['COOKIES']
        if(self.robot.find(button_ok)):
            self.robot.click(button_ok)
            return self.robot.click(button_ok)

    def extract_notices(self):
        noticia = self.SELECTORS['LINK']['NOTICE']
        for noticia in self.robot.find_class(noticia):
            print(noticia.get_attribute('title'))
            print(noticia.get_attribute('href'))


parvi = Parvi(selectors)

parvi.start_browser()
parvi.select_url('https://www.globo.com/')
# parvi.cookies_confirm()
parvi.extract_notices()
