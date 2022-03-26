def find_followers(self):
    time.sleep(5)
    self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

    time.sleep(2)
    followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    followers.click()

    time.sleep(2)
    modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
    for i in range(10):
        #In this case we're executing some Javascript, that's what the execute_script() method does. 
        #The method can accept the script as well as a HTML element. 
        #The modal in this case, becomes the arguments[0] in the script.
        #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)
