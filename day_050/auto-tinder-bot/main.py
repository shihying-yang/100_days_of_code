import sys
import time

sys.path.insert(0, "../..")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

from personal_config import my_info

fb_user = my_info["fb_login"]
fb_pass = my_info["fb_password"]

URL = "https://tinder.com/"


chrome_driver_path = r"D:\myStuff\bin\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(URL)

time.sleep(2)

# click login button
login_btn = driver.find_element(
    By.CSS_SELECTOR, "header > div > div:nth-child(2) > div.H\(40px\).Px\(28px\) > a"
)
login_btn.click()

time.sleep(2)

# click facebook login button

fb_btn = driver.find_element(By.CSS_SELECTOR, "div > div:nth-child(4) > span > div:nth-child(2) > button")
fb_btn.click()

# find all new facebook login window, and switch to it
tinder_window, fb_window = driver.window_handles
# fb_windows = driver.window_handles[1]
driver.switch_to.window(fb_window)
# print(driver.title)

# login facebook
fb_user_field = driver.find_element(By.ID, "email")
fb_user_field.send_keys(fb_user)
fb_pass_field = driver.find_element(By.ID, "pass")
fb_pass_field.send_keys(fb_pass)
# fb_login_btn = driver.find_element(By.ID, "u_0_0_CR")
# fb_login_btn.click()
fb_pass_field.send_keys(Keys.ENTER)

time.sleep(5)

# return to tinder window
driver.switch_to.window(tinder_window)
# print(driver.title)

# disable all notification popups
try:
    # #t492665908 > div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Pos\(r\).Ov\(h\).C\(\#fff\).Bg\(\$c-pink\)\:h\:\:b.Bg\(\$c-pink\)\:f\:\:b.Bg\(\$c-pink\)\:a\:\:b.Trsdu\(\$fast\).Trsp\(\$background\).Bg\(\$g-ds-brand\).button--primary-shadow.StyledButton.Bxsh\(\$bxsh-btn\).Fw\(\$semibold\).focus-button-style.W\(225px\).W\(a\)
    location_btn = driver.find_element(
        By.CSS_SELECTOR,
        "div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Pos\(r\).Ov\(h\).C\(\#fff\).Bg\(\$c-pink\)\:h\:\:b.Bg\(\$c-pink\)\:f\:\:b.Bg\(\$c-pink\)\:a\:\:b.Trsdu\(\$fast\).Trsp\(\$background\).Bg\(\$g-ds-brand\).button--primary-shadow.StyledButton.Bxsh\(\$bxsh-btn\).Fw\(\$semibold\).focus-button-style.W\(225px\).W\(a\)",
    )
    location_btn.click()
    time.sleep(1)
except NoSuchElementException as e:
    print(e)

try:
    # #t492665908 > div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Pos\(r\).Ov\(h\).C\(\#fff\).Bg\(\$c-pink\)\:h\:\:b.Bg\(\$c-pink\)\:f\:\:b.Bg\(\$c-pink\)\:a\:\:b.Trsdu\(\$fast\).Trsp\(\$background\).Bg\(\$g-ds-brand\).button--primary-shadow.StyledButton.Bxsh\(\$bxsh-btn\).Fw\(\$semibold\).focus-button-style.W\(225px\).W\(a\)
    notif_btn = driver.find_element(
        By.CSS_SELECTOR,
        "div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Pos\(r\).Ov\(h\).C\(\#fff\).Bg\(\$c-pink\)\:h\:\:b.Bg\(\$c-pink\)\:f\:\:b.Bg\(\$c-pink\)\:a\:\:b.Trsdu\(\$fast\).Trsp\(\$background\).Bg\(\$g-ds-brand\).button--primary-shadow.StyledButton.Bxsh\(\$bxsh-btn\).Fw\(\$semibold\).focus-button-style.W\(225px\).W\(a\)",
    )
    notif_btn.click()
    time.sleep(1)
except NoSuchElementException as e:
    print(e)

try:
    # #t-2073920312 > div > div.Pos\(f\).Start\(0\).End\(0\).Z\(2\).Bxsh\(\$bxsh-4-way-spread\).B\(0\).Bgc\(\#fff\).C\(\$c-secondary\) > div > div > div.D\(f\)--ml > div:nth-child(1) > button
    cookies_btn = driver.find_element(
        By.CSS_SELECTOR,
        "div > div.Pos\(f\).Start\(0\).End\(0\).Z\(2\).Bxsh\(\$bxsh-4-way-spread\).B\(0\).Bgc\(\#fff\).C\(\$c-secondary\) > div > div > div.D\(f\)--ml > div:nth-child(1) > button",
    )
    cookies_btn.click()
    time.sleep(1)
except NoSuchElementException as e:
    print(e)

try:
    # #t492665908 > div > div > div.Ta\(c\).Expand.Mx\(a\) > div.Ta\(c\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).C\(\$c-secondary\).C\(\$c-base\)\:h.Fw\(\$semibold\).focus-button-style.D\(b\).Mt\(24px\).W\(100\%\).Fz\(\$s\).Cur\(p\).Maw\(315px\)
    email_notif_btn = driver.find_element(
        By.CSS_SELECTOR,
        "div.Ta\(c\).Expand.Mx\(a\) > div.Ta\(c\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).C\(\$c-secondary\).C\(\$c-base\)\:h.Fw\(\$semibold\).focus-button-style.D\(b\).Mt\(24px\).W\(100\%\).Fz\(\$s\).Cur\(p\).Maw\(315px\)",
    )
    email_notif_btn.click()
    time.sleep(1)
except NoSuchElementException as e:
    print(e)

for i in range(50):
    # #t-2073920312 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml.Mah\(fc\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Isolate.W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-pink\) > button
    try:
        dislike_btn = driver.find_element(
            By.CSS_SELECTOR,
            "main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml.Mah\(fc\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Isolate.W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-pink\) > button",
        )
        dislike_btn.click()
        time.sleep(1)
    except NoSuchElementException as e:
        print(e)
        time.sleep(2)
    except ElementClickInterceptedException as e:
        # this is when the "add to home screen" shows up. Click not interested to move forward
        try:
            # #t492665908 > div > div > div.Pt\(12px\).Pb\(8px\).Px\(36px\).Px\(24px\)--s > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(42px\)--s.Mih\(50px\)--ml.C\(\$c-secondary\).C\(\$c-base\)\:h.Fw\(\$semibold\).focus-button-style.D\(b\).Mx\(a\)
            not_interested_btn = driver.find_element(
                By.CSS_SELECTOR,
                "div > div > div.Pt\(12px\).Pb\(8px\).Px\(36px\).Px\(24px\)--s > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(42px\)--s.Mih\(50px\)--ml.C\(\$c-secondary\).C\(\$c-base\)\:h.Fw\(\$semibold\).focus-button-style.D\(b\).Mx\(a\)",
            )
            not_interested_btn.click()
        except NoSuchElementException as e:
            print(e)
        time.sleep(2)

driver.quit()
