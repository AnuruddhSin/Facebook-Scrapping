from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
#Set the email id and password environment
email_id=os.environ.get('EMAIL_ID')
lk_pass = os.environ.get('PASSWORD')
# Define chrome path for executing the program
chrome_driver_path = Service("D:\Python\Python course udemy\Software\chromedriver_"
                             "win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
#Handling the window execution for cancelling the opened window after executing program automatically
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#Tinder website path/address
driver.get("https://tinder.com/")
#Time dealy at every action is must because of this shows the website can't be run through the robots that's run
#by user if there is no delay the end up the program without executing next command
time.sleep(4)
#Path for clicking login button and step by step actions are perform to open the account using eamil id and password
log_in=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
time.sleep(3)
log_in.click()
time.sleep(2)
more_option=driver.find_element(By.CSS_SELECTOR,".Mt(a) ")
time.sleep(2)
more_option.click()
time.sleep(3)
facebook_login=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
time.sleep(2)
facebook_login.click()
time.sleep(3)
#These command handle the next new window open through links using indexes to one path to another window opens
fb_login_window=driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(4)
emailing=driver.find_element(By.XPATH,'//*[@id="email"]')
emailing.send_keys(email_id)
time.sleep(3)
password=driver.find_element(By.NAME,"pass")
time.sleep(3)
password.click()
password.send_keys(lk_pass)
time.sleep(2)
login=driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]')
login.click()
time.sleep(3)
# These commands are used for getback on the original windows using indexes to one path to another
tinder__window=driver.window_handles[0]
driver.switch_to.window(tinder__window)
print(driver.title)
time.sleep(5)
#Share Your Location
location=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
time.sleep(3)
location.click()
time.sleep(3)
#Enable Notification on Tinder
enable_noti=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
time.sleep(3)
enable_noti.click()
time.sleep(3)
#Accept privacy and cookies
accept=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
time.sleep(3)
accept.click()
time.sleep(3)
# Like the photos by actionchain module which is imported from
while True:
    # Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change
    for n in range(100):
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.send_keys(Keys.ARROW_RIGHT)
            actions.perform()
        except:
            print("error")
            driver.quit()

