import sys
import time

sys.path.insert(0, "../..")

from personal_config import my_info
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

PROMISED_DOWN = 750
PROMISED_UP = 700

SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/i/flow/login"
twitter_login = my_info["twitter_login"]
twitter_password = my_info["twitter_password"]
twitter_phone = my_info["twitter_phone"]

chrome_driver_path = r"D:\myStuff\bin\chromedriver.exe"


class InternetSpeedTwitterBot:
    """Internet Speed Twitter Bot"""

    def __init__(self):
        """initialize the bot"""
        self.service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.download_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):
        """check the internet speed"""
        self.driver.get(SPEEDTEST_URL)
        time.sleep(2)
        # begin testing speed
        # #container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a
        go_btn = self.driver.find_element(By.CSS_SELECTOR, "div.start-button > a")
        go_btn.click()

        # give 300 seconds to test
        for _ in range(30):
            time.sleep(10)
            try:
                # if the test is done, we will get the correct result for the float casting
                self.download_speed = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
                self.upload_speed = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
                break
            except ValueError:
                pass
            except NoSuchElementException:
                pass

    def tweet_at_provider(self):
        """Login and tweet the provider"""
        # only do that if the speed is lower than the promised speed
        if self.download_speed < PROMISED_DOWN or self.upload_speed < PROMISED_UP:
            self.driver.get(TWITTER_URL)

            time.sleep(2)

            # putting user name
            # #layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input
            login_email = self.driver.find_element(By.CSS_SELECTOR, "label > div > div > div > input")
            login_email.send_keys(twitter_login)
            login_email.send_keys(Keys.ENTER)
            # #layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div:nth-child(6) > div

            time.sleep(1)

            # if twitter complains that the login is suspicious, we will need to put in the phone number
            try:
                # #layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div:nth-child(1) > div > div.css-901oao.r-37j5jr.r-1yjpyg1.r-b88u0q.r-ueyrd6.r-bcqeeo.r-qvutc0 > span > span
                ask_email = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#layers > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div:nth-child(1) > div > div > span > span",
                ).text
                if ask_email.startswith("Enter your"):
                    login_phone = self.driver.find_element(
                        By.CSS_SELECTOR, "label > div > div > div > input"
                    )
                    login_phone.send_keys(twitter_phone)
                    login_phone.send_keys(Keys.ENTER)
                time.sleep(1)
            except NoSuchElementException:
                pass

            # putting password
            # #layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-13qz1uu > div > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div.css-901oao.r-1awozwy.r-6koalj.r-37j5jr.r-1inkyih.r-16dba41.r-135wba7.r-bcqeeo.r-13qz1uu.r-qvutc0 > input
            password_field = self.driver.find_element(
                By.CSS_SELECTOR,
                "#layers > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > label > div > div > div > input",
            )

            password_field.send_keys(twitter_password)
            password_field.send_keys(Keys.ENTER)

            time.sleep(5)

            # start the twit
            # #react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div
            twit_field = self.driver.find_element(
                By.CSS_SELECTOR,
                "div > div > label > div > div > div > div > div > div > div > div > div > div",
            )
            twit_field.send_keys(
                f"Hey internet provider, why is my internet speed {self.download_speed} down/{self.upload_speed} up when I pay for gigabit down and up?"
            )
            twit_field.send_keys(Keys.ENTER)


if __name__ == "__main__":
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    time.sleep(3)
    bot.tweet_at_provider()
