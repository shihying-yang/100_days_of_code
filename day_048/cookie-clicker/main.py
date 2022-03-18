import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "http://orteil.dashnet.org/experiments/cookie/"

MIN = 0.5

chrome_driver_path = r"D:\myStuff\bin\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(URL)

helpers_str = [
    "buyTime machine",
    "buyPortal",
    "buyAlchemy lab",
    "buyShipment",
    "buyMine",
    "buyFactory",
    "buyGrandma",
    "buyCursor",
]

cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")


def find_helper():
    helpers = [driver.find_element(By.ID, helper) for helper in helpers_str]
    for helper in helpers:
        if helper.get_attribute("class") == "":
            helper.click()
            break
    del helpers


current_time = time.time()
timeout = current_time + 60 * MIN
test_time = current_time + 5

while True:
    # cookie = driver.find_element(By.ID, "cookie")
    # money = driver.find_element(By.ID, "money")
    if time.time() > timeout:
        break
    elif time.time() > test_time:
        find_helper()
        test_time = time.time() + 5

    cookie.click()

    # print(money.text)

clicks_count_tag = driver.find_element(By.ID, "cps")
# click_count = clicks_count_tag.text.split(":")[1].strip()
print(f"{clicks_count_tag.text}")

# driver.quit()
