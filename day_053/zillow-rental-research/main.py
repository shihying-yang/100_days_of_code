import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"D:\myStuff\bin\chromedriver.exe"

zillow_search_url = "https://www.zillow.com/memphis-tn/rentals/3-_beds/1.5-_baths/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Memphis%2C%20TN%22%2C%22mapBounds%22%3A%7B%22west%22%3A-90.35118861132813%2C%22east%22%3A-89.59038538867188%2C%22south%22%3A34.892531187053365%2C%22north%22%3A35.36537822820445%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A32811%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A231211%2C%22max%22%3A365069%7D%2C%22mp%22%3A%7B%22min%22%3A950%2C%22max%22%3A1500%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22baths%22%3A%7B%22min%22%3A1.5%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
# zillow_search_url = "https://www.zillow.com/homes/for_rent/condo,apartment_duplex_type/1-_beds/paymenta_sort/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Beaverton%2C%20OR%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.98363040844727%2C%22east%22%3A-122.75738071362305%2C%22south%22%3A45.3838603720992%2C%22north%22%3A45.56129678646036%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A351747%2C%22max%22%3A502495%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22lau%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22min%22%3A1400%2C%22max%22%3A2000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22paymenta%22%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ldog%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
accepted_language = "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSddnIPT-K_KrQ5_htqNzuTXRaMiQw8omTPGq9zdS-Rl7saa4w/viewform?usp=sf_link"


class ZillowSearchBot:
    """zilloow search bot"""

    def __init__(self):
        """initilize the zillow search bot with a dict to hold properties"""
        self.properties = {}

    def search_properties(self):
        """Search zillow for properties with BeautifulSoup"""
        # Not the URL might give "buy" instead of "rent" results. Double check that
        headers = {"User-Agent": user_agent, "Accept-Language": accepted_language}
        response = requests.get(zillow_search_url, headers=headers)
        website_html = response.text
        # # work around it by saving the result to a html file
        # with open("Rental Listings in Memphis TN - 105 Rentals _ Zillow.html", "r", encoding="utf8") as f_in:
        #     website_html = f_in.read()

        # BeautifulSoup to parse the html
        soup = BeautifulSoup(website_html, "html.parser")
        prices = soup.find_all(class_="list-card-price")
        addrs = soup.find_all(class_="list-card-addr")
        urls = soup.select(selector="article div.list-card-info a")
        # save the results to the dict
        for price, addr, url in zip(prices, addrs, urls):
            self.properties[addr.getText()] = {"price": price.getText(), "url": url.get("href")}

    def get_data(self):
        """return the data in the dict"""
        return self.properties


class GoogleFormBot:
    """Google Form Bot"""

    def __init__(self, properties):
        """Initialize the Google Form Bot by passing in a dict of properties"""
        self.service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.proterties = properties

    def submit_form(self):
        """Method to submit result to the google form"""
        self.driver.get(form_url)
        time.sleep(1)
        # fill in the properties info
        for key, value in self.proterties.items():
            addr = key
            price = value["price"]
            url = value["url"]
            addr_field = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
            )
            addr_field.send_keys(addr)
            price_field = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
            )
            price_field.send_keys(price)
            url_field = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
            )
            url_field.send_keys(url)
            time.sleep(1)
            submit_btn = self.driver.find_element(
                By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
            )
            # submit is a button
            submit_btn.click()
            time.sleep(2)
            # submit again is an extra link
            again_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            again_link.click()
            time.sleep(2)


if __name__ == "__main__":
    zillow_bot = ZillowSearchBot()
    zillow_bot.search_properties()
    print(zillow_bot.get_data())
    google_form_bot = GoogleFormBot(zillow_bot.get_data())
    google_form_bot.submit_form()
