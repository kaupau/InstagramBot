import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InstaBot:
    def __init__(self, usernameLogin, passwordLogin):
        self.username = usernameLogin
        self.password = passwordLogin

        self.driver = webdriver.Safari()
        self.driver.implicitly_wait(60) # wait timeout sht
        self.driver.get("https://www.instagram.com/accounts/login/?hl=en")

        # type username
        loginInput = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input') #login
        loginInput.send_keys(self.username)
        time.sleep(1)

        # type password
        loginInput = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        loginInput.send_keys(self.password)
        time.sleep(1)

        # log in by pressing button
        loginInput = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
        loginInput.click()
        time.sleep(1)

    def like(self):
        self.driver.find_element_by_class_name("_9AhH0").click() #????

    def harvest(self):
        self.driver.find_element_by_class_name("sXUSN").click()
        self.driver          
    #    class ="sXUSN" for the more button to load hashtags
    #    <a class href="/explore/tags/colorful/"> hashtag here </a> hashtag
    #    class="_8Rm4L M9sTE  L_LMM SgTZ1" for posts
    #    class="_9AhH0" for images in posts

    def delay(self):
        time.sleep(random.randint(10,100)) # are these numbers good enough? can you speed this up anyhow?


thotbot = InstaBot("username","password")
# 2 modes: 
#           like mode
#           harvest hashtag mode

