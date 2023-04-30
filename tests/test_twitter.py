from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from test_objects.twitter import Twitter
from core import settings
from time import sleep
import re

# Before test
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(settings.CHROME_DRIVER, options=options)
wait = WebDriverWait(driver, timeout=10)
twitter = Twitter()

class TestTwitter:

    def test_get_to_index(self):
        """
        T1 - Access to Twitter init page in spanish
        """

        # Go to Twitter page
        driver.get(twitter.INIT_PAGE)

        # Wait until title tag is present
        sleep(5)
        assert driver.title == 'Explorar / Twitter'

    def test_login(self):
        """
        T2 - Log in into Twitter, I have to use second factor and that is a manual step
        """

        # Click on Log in button (Iniciar sesión)
        driver.find_element(By.XPATH, twitter.LOGIN_BUTTON).click()

        # Input the user
        sleep(5)
        input_user = driver.find_element(By.XPATH, twitter.LOGIN_MODAL_USER_INPUT)
        input_user.click()
        input_user.send_keys(twitter.USER)

        # Click on next (siguiente)
        driver.find_element(By.XPATH, twitter.LOGIN_MODAL_NEXT_BUTTON).click()

        # Input the password
        sleep(5)
        input_password = driver.find_element(By.XPATH, twitter.LOGIN_MODAL_PASSWORD_INPUT)
        input_password.send_keys(twitter.PASSWORD)

        # Click on Log in (iniciar sesión)
        driver.find_element(By.XPATH, twitter.LOGIN_MODAL_LOGIN_BUTTON).click()

        # Find user portal load
        sleep(10)
        driver.find_element(By.XPATH, twitter.USER_PORTAL)

    def test_search_box(self):
        """
        T3 - Input in search box Selenium
        """

        # Input the word selenium in the search box
        search_box = driver.find_element(By.XPATH, twitter.SEARCH_BOX)
        search_box.click()
        search_box.send_keys("selenium")

        # Find selenium user
        sleep(3)
        driver.find_element(By.XPATH, twitter.SELENIUM_USER).click()

        # Check if is in Selenium portal
        sleep(5)
        assert driver.find_element(By.XPATH, twitter.SELENIUM_USER).is_displayed() == True
        assert driver.find_element(By.XPATH, twitter.SELENIUM_ABOUT).is_displayed() == True

    def test_tweet_something(self):
        """
        T4 - Make a tweet
        """
        # Go to you portal and search the tweet
        driver.get(twitter.TWEETER_HOME_LINK)

        # Click Tweet button
        sleep(3)
        driver.find_element(By.XPATH, twitter.TWEET_BUTTON).click()

        # Write some text in the modal
        sleep(5)
        text_to_tweet = 'Hello this tweet was made using #python #pytest and #selenium.'
        driver.find_element(By.XPATH, twitter.TWEET_MODAL_TEXTAREA).send_keys(text_to_tweet)

        # Click Tweet button in modal
        driver.find_element(By.XPATH, twitter.TWEET_MODAL_TWEET_BUTTON).click()

        # Check for the tweet
        sleep(5)
        tweet_finded = False
        section = driver.find_element(By.XPATH, twitter.TWEET_SECTION)
        articles = section.find_elements(By.TAG_NAME, 'article')
        for article in articles:
            text_of_tweet = article.find_element(By.XPATH, '//div[@data-testid="tweetText"]').text
            if text_of_tweet == text_to_tweet:
                tweet_finded = True
                break
        assert tweet_finded == True