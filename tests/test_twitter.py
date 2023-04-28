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
        T2 - Log in into Twitter using second factor that is a manual step
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
