from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from core import settings


class TestIndex:

    # Before test

    # Tests
    def test_get_index(self):
        """
        Should get access to wikipedia page
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        driver = webdriver.Chrome(settings.CHROME_DRIVER, chrome_options=options)
        driver.get(settings.INIT_PAGE)

        assert driver.title == "Wikipedia"
