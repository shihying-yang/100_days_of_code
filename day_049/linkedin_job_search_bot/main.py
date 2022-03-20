import time
import sys


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

sys.path.insert(0, "../..")

from personal_config import my_info

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
user_name = my_info["linkedin_login"]
password = my_info["linkedin_password"]

chrome_driver_path = r"D:\myStuff\bin\chromedriver.exe"

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(URL)

signin_btn = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
signin_btn.click()

time.sleep(2)

id = driver.find_element(By.ID, "username")
id.send_keys(user_name)

pswd = driver.find_element(By.ID, "password")
pswd.send_keys(password)

signin_btn2 = driver.find_element(By.CLASS_NAME, "btn__primary--large")
signin_btn2.click()

time.sleep(2)

all_jobs = driver.find_elements(By.CLASS_NAME, "job-card-list__title")

for job in all_jobs:
    # print(job.text)
    job.click()
    time.sleep(2)

    job_save_btn = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    job_save_btn.click()

driver.quit()
