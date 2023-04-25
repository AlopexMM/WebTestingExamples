from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from core import settings
from core.TestObject import WebTestObject


class TestIndex:
    # Before test
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    driver = webdriver.Chrome(settings.CHROME_DRIVER, options=options)
    wait = WebDriverWait(driver, float(5))

    # Tests
    def test_get_index(self):
        """
        W1 - Should get access to wikipedia page
        """
        self.driver.get(settings.INIT_PAGE)

        assert self.driver.title == "Wikipedia"

    def test_check_languages(self):
        """
        W2 - Should find the words English and Español
        """
        english = WebTestObject(xpath='//div/a/strong[text()="English"]')
        spanish = WebTestObject(xpath='//div/a/strong[text()="Español"]')

        find_english = self.driver.find_element(By.XPATH, english.xpath)
        find_spanish = self.driver.find_element(By.XPATH, spanish.xpath)
        assert find_english.text == 'English'

        assert find_spanish.text == 'Español'

    def test_search_box(self):
        """
        W3 - Should find input search box
        """
        pass

    def test_search_work(self):
        """
        W4 - Input the word pc and be redirected to the results page
        """
        pass