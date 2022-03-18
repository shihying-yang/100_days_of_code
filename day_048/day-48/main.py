from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://www.amazon.com/gp/product/B07YYYFJ1D"

chrome_driver_path = r"D:\myStuff\bin\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(URL)

# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.text)

price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print("Check", price.tag_name)
print(price.get_attribute('innerHTML'))



# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get(URL)

# price = driver.find_element_by_id("priceblock-ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)



# driver.close()
driver.quit()

