from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from core import settings
from test_objects.wikipedia import Wikipedia
import re


class TestIndex:
    # Before test
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    driver = webdriver.Chrome(settings.CHROME_DRIVER, options=options)
    wait = WebDriverWait(driver, float(5))
    wiki = Wikipedia()

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
        find_english = self.driver.find_element(By.XPATH, self.wiki.strong_english)
        find_spanish = self.driver.find_element(By.XPATH, self.wiki.strong_spanish)
        assert find_english.text == 'English'

        assert find_spanish.text == 'Español'

    def test_search_box(self):
        """
        W3 - Should find input search box
        """
        input_search_box = self.driver.find_element(By.XPATH, self.wiki.input_search_box)
        assert input_search_box.is_displayed() == True

    def test_search_word(self):
        """
        W4 - Input the word pc and be redirected to the results page
        """
        input_search_box = self.driver.find_element(By.XPATH, self.wiki.input_search_box)
        input_search_box.send_keys('pc')
        input_search_box.send_keys(Keys.ENTER)
        # We wait to load the page
        self.wait.until(self.driver.find_element(By.TAG_NAME, 'title').is_displayed())

        assert re.search('PC', self.driver.title) == True


