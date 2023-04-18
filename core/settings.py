import os
import re


"""
Here goes general environment variables and search for secret variables in env file.
If the project has some user info that is private please use the env file. REMEMBER add the file to .gitignore file.
"""

# Base folder path
BASE_PATH = os.path.abspath("")

# Drivers folder
DRIVERS_FOLDER = os.path.join(BASE_PATH, "dirvers")

# Searching for drivers
CHROME_DRIVER = ""
FIREFOX_DRIVER = ""
SAFARI_DRIVER = ""

for (root, dirs, files) in os.walk(os.path.join(DRIVERS_FOLDER)):
    for file in files:
        if re.search('chrome+'):
            CHROME_DRIVER = os.path.join(DRIVERS_FOLDER, file)
        if re.search('firefox+'):
            FIREFOX_DRIVER = os.path.join(DRIVERS_FOLDER, file)
        if re.search('safari+'):
            SAFARI_DRIVER = os.path.join(DRIVERS_FOLDER, file)

INIT_PAGE = "https://wikipedia.org"