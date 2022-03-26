import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

sys.path.insert(0, "../..")
from personal_config import my_info

instagram_login = my_info["instagram_login"]
instagram_password = my_info["instagram_password"]
instagram_base_url = "https://www.instagram.com"

similar_user = "woodpeckers_tools"

chrome_driver_path = r"D:\myStuff\bin\chromedriver.exe"


class InstaFollower:
    def __init__(self):
        self.service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.get(f"{instagram_base_url}/accounts/login/")
        time.sleep(2)
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(instagram_login)

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(instagram_password)

        time.sleep(1)
        password_field.send_keys(Keys.ENTER)

        time.sleep(2)

        try:
            # body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm
            no_notif_btn = self.driver.find_element(By.CSS_SELECTOR, "button.aOOlW.HoLwm")
            no_notif_btn.click()

            time.sleep(2)
        except NoSuchElementException:
            pass

    def find_followers(self):
        self.driver.get(f"{instagram_base_url}/{similar_user}/")
        # followers = self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > section > main > div > header > section > ul > li:nth-child(2) > a > div")
        followers = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div'
        )
        followers.click()
        time.sleep(2)

        modal = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]")

        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.CSS_SELECTOR, "button.aOOlW.HoLwm")
                cancel.click()


if __name__ == "__main__":
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow()
