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

    def test(self):
        teste = self.SELECTORS['LINK']['TESTE']
        extraiu = self.robot.find(teste)
        inserido = extraiu.text
        print(inserido)


parvi = Parvi(selectors)

parvi.start_browser()
parvi.select_url('https://www.bbc.com/portuguese')
parvi.cookies_confirm()
parvi.test()
