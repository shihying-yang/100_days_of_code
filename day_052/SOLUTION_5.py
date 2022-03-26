from selenium.common.exceptions import ElementClickInterceptedException

def follow(self):
    all_buttons = self.driver.find_elements_by_css_selector("li button")
    for button in all_buttons:
        try:
            button.click()
            time.sleep(1)
        except ElementClickInterceptedException:
            cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            cancel_button.click()
