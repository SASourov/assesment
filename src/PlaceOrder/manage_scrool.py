class LayoutScrool:
    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self):
        return self.driver.swipe(512, 1496, 521, 787, 570)
