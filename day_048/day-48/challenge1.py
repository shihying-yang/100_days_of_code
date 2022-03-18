from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

chrome_driver_path = r"D:\myStuff\bin\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(URL)

event_dates = driver.find_elements(
    By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > time"
)
# for date in event_dates:
#     print(date.get_attribute("datetime").split("T")[0])

event_names = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > a")
# for name in event_names:
#     print(name.text)
events = {}
for ind in range(len(event_dates)):
    events[ind] = {
        "time": event_dates[ind].get_attribute("datetime").split("T")[0],
        "name": event_names[ind].text,
    }

print(events)

driver.quit()
