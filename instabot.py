from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# To automatically configure the right version of chromeDriver based on the local chrome verions
driver = webdriver.Chrome(ChromeDriverManager().install())

class InstaBot:
    
    def __init__(self, username, password): 
        
        self.opts = webdriver.ChromeOptions() 
        self.opts.add_experimental_option("detach", True) 
        self.driver  = driver

        self.username = username
        self.password = password
        
          
        # Open Instagram
        self.driver.get("https://instagram.com") 
        time.sleep(3) # 3 Second Wait 
          
        # Insert username and password in their respective text fields
        self.driver.find_element_by_xpath("//input[@name = 'username']").send_keys(self.username) 
        self.driver.find_element_by_xpath("//input[@name = 'password']").send_keys(self.password) 
          
        # Locate login button and click
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click() 
        time.sleep(3) # 3 Second Wait 
  
        # Click on 'Not Now' when Instagram asks to save login info
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click() 
        time.sleep(3) # 3 Second Wait 

        #Click on 'Not Now' when Instagram asks to send notifications
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        time.sleep(3) # 3 Second Wait 
        search_box = self.driver.find_element_by_xpath('//input[@placeholder="Search"]')
        #Add your username here
        self.driver.find_element_by_xpath('//a[@href="/<username>/"]').click()
        time.sleep(3)
        prevFollowing = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').text
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[text()='Follow']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        time.sleep(3)
        newFollowing = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').text

        # check whether the following count has changed
        if(prevFollowing!=newFollowing):
            print("Follow successfull")
        else:
            print("Could not follow the profile")





# Testing Your Code by instantiating the class
p = InstaBot('<username>','<password>') 
