from selenium import webdriver
from pynput.keyboard import Key, Controller
import time
import config
# fetch facebook password from separate file in the same directory
pw = config.secret['pw']
keyboard = Controller()

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--disable-notifications')

# navigate to facebook url
driver.get('https://facebook.com')
# driver.get('https://youtube.com')

# input email address
email_input = driver.find_element_by_xpath('//*[@id="email"]')
email_input.send_keys('joshua.c.yap@gmail.com')
# input pw
password_input = driver.find_element_by_xpath('//*[@id="pass"]')
password_input.send_keys(pw)
# click login button element
login_button = driver.find_element_by_xpath('//*[@id="u_0_b"]')
login_button.click()


home_button = driver.find_element_by_xpath('//*[@id="u_0_c"]/a')
# wait 8 seconds for browser popup before pressing esc to get out
time.sleep(8)
keyboard.press(Key.esc)


# actual actions go here


# close browser window after actions are complete
time.sleep(5)
driver.close()
