import os


"""
Here goes general environment variables and search for secret variables in env file.
If the project has some user info that is private please use the env file. REMEMBER add the file to .gitignore file.
"""

# Base folder path
BASE_PATH = os.path.abspath("")

# Drivers
CHROME_DRIVER = "/home/mario/web_drivers/chromedriver"
FIREFOX_DRIVER = ""
SAFARI_DRIVER = ""

INIT_PAGE = "https://wikipedia.org"