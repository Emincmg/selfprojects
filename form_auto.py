
import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

#########################
####### Variables #######

#########################

### Driver implementation ###
os.environ['PATH'] += "D:\Selenium\ChromeDriver"
driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(3)
### Driver implementation ###


##########################
####### Test Cases #######

### Case : Login with valid username and valid password.



##########################




