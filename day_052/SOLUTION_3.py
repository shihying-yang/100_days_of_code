#Additional Imports
from selenium.webdriver.common.keys import Keys
import time

def login(self):
    self.driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    username = self.driver.find_element_by_name("username")
    password = self.driver.find_element_by_name("password")

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)

    time.sleep(2)
    password.send_keys(Keys.ENTER)
