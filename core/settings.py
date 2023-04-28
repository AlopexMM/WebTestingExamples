import os
import environ


"""
Here goes general environment variables and search for secret variables in env file.
If the project has some user info that is private please use the env file. REMEMBER add the file to .gitignore file.
"""
env = environ.Env()

# Base folder path
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_PATH, ".env"))

# Drivers
CHROME_DRIVER = "C:\\Users\\mario\\webDrivers\\chromedriver.exe"
FIREFOX_DRIVER = ""
SAFARI_DRIVER = ""
