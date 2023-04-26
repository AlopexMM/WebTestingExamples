from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from core import settings
from test_objects.wikipedia import Wikipedia
import re

# Before test
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(settings.CHROME_DRIVER, options=options)
wait = WebDriverWait(driver, timeout=10)
wiki = Wikipedia()


class TestIndex:

    # Tests
    def test_get_index(self):
        """
        W1 - Should get access to wikipedia page
        """
        driver.get(settings.INIT_PAGE)

        assert driver.title == "Wikipedia"

    def test_check_languages(self):
        """
        W2 - Should find the words English and Español
        """
        find_spanish = driver.find_element(By.XPATH, wiki.strong_spanish)
        assert find_spanish.text == 'Español'

        find_english = driver.find_element(By.XPATH, wiki.strong_english)
        assert find_english.text == 'English'

    def test_search_box(self):
        """
        W3 - Should find input search box
        """
        input_search_box = driver.find_element(By.XPATH, wiki.input_search_box)
        assert input_search_box.is_displayed() == True

    def test_search_word(self):
        """
        W4 - Input the word pc and be redirected to the results page
        """
        input_search_box = driver.find_element(By.XPATH, wiki.input_search_box)
        input_search_box.send_keys('pc')
        input_search_box.send_keys(Keys.ENTER)
        result = True if re.search('PC', driver.title) else False
        assert result == True
