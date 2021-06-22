from Utilities.Utilities import Utilities


class Parvi:
    def __init__(self):
        __slots__ = 'robot'

    def __init__(self):
        self.robot = Utilities()

    def select_url(self):
        self.robot.open_chrome()


parvi = Parvi()

parvi.select_url()
