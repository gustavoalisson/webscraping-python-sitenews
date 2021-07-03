from Utilities.Utilities import Utilities
from selectors import selectors
import pandas as pd


class Parvi:
    __slots__ = 'robot', 'SELECTORS'
    links = []
    titles = []

    def __init__(self, SELECTORS):
        self.robot = Utilities()
        self.SELECTORS = SELECTORS

    def start_browser(self):
        self.robot.open_chrome()

    def select_url(self, url):
        self.robot.browser.get(url)

    def extract_notices(self):
        noticia = self.SELECTORS['LINK']['NOTICE']
        for noticia in self.robot.find(noticia)[:10]:
            print(noticia.get_attribute('title'))
            print(" ")
            print(noticia.get_attribute('href'))
            self.titles.append(noticia.get_attribute('title'))
            self.links.append(noticia.get_attribute('href'))

    def save_as_csv(self):
        linksDF = pd.DataFrame()
        linksDF['Titulos'] = self.titles
        linksDF['Links'] = self.links
        linksDF.to_csv('index.csv')
        print(linksDF.to_dict())


parvi = Parvi(selectors)

parvi.start_browser()
parvi.select_url('https://www.globo.com/')
parvi.extract_notices()
parvi.save_as_csv()
