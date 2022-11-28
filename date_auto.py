import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#######################
#Please set dates for date fields here.
datefield1date = "01/02/2022"
datefield2date = "01/11/2022"
datefield3date = "05/11/2022"
#######################


os.environ['PATH'] += 'D:\Selenium\ChromeDriver'
driver = webdriver.Chrome()

driver.get('https://demo.seleniumeasy.com/bootstrap-date-picker-demo.html')
driver.implicitly_wait(3)

###
#Today button automation
###

#Wait for dropdown button to be clickable then click
try:
    dropdbtn = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(By.CLASS_NAME,"input-group-addon")
        )
        
except:
    print('Dropdown button could not found')

finally:
    dropdbtn.click()

#Wait for Today button to be clickable then click
try:
    todaybtn = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(By.CLASS_NAME,"today")
    )
   
except:
    print("Today button could not found")

finally:
    todaybtn.click()

###
#Clear Button automation
###

#Wait for dropdown button to be clickable then click
try:    
    dropdbtn = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(By.CLASS_NAME,"input-group-addon")
        )
except:
    print("Date dropdown button could not be found")
finally:
    dropdbtn.click()

#Wait for today button to be located then click
try:
    todaybtn = WebDriverWait(driver,10).until(
        EC.element_located_to_be_selected(By.CLASS_NAME,'clear')
    )
    todaybtn.click()
except:
    print("Clear button could not be found")

###
#Date field 1 automation
###

#Wait for Date field 1 to be located then send date data
try:
    datefield1=WebDriverWait(driver,10).until(
        EC.presence_of_element_located(By.XPATH,"//input[@placeholder='dd/mm/yyyy']")
    )
except: 
    print("Could not send date data")
finally:
    datefield1.click()
    datefield1.send_keys(datefield1date)

###
#Date field 2 and 3 automation
###

#Wait for date field 2 to be located then send date data
try:
    datefield2=WebDriverWait(driver,10).until(
        EC.presence_of_element_located(By.XPATH,"//input[@placeholder='Start date']"
    ))
except:
    print("Date fild can not be found")
finally:
    datefield2.send_keys(datefield2date)
    time.sleep(1)
    ###date2 = driver.find_element(By.XPATH,"//input[@placeholder='End date']")
    ###date2.send_keys(datefield3date)
    ###time.sleep(1)
    driver.quit()

