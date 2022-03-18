from telnetlib import SE
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# URL = "https://en.wikipedia.org/wiki/Main_Page"
URL = "http://secure-retreat-92358.herokuapp.com/"

chrome_driver_path = r"D:\myStuff\bin\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(URL)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Sean")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Yang")
email = driver.find_element(By.NAME, "email")
email.send_keys("ysying888@gmail.com")
btn = driver.find_element(By.CLASS_NAME, "btn")
btn.click()

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # print(article_count.text)

# # article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# # all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


driver.quit()
