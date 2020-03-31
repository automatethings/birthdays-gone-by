from selenium import webdriver
import config
# fetch facebook password from separate file in the same directory
pw = config.secret['pw']


driver = webdriver.Chrome()
driver.get('https://facebook.com')
# driver.get('https://youtube.com')

email_input = driver.find_element_by_xpath('//*[@id="email"]')
email_input.send_keys('joshua.c.yap@gmail.com')

password_input = driver.find_element_by_xpath('//*[@id="pass"]')
password_input.send_keys(pw)

login_button = driver.find_element_by_xpath('//*[@id="u_0_b"]')
login_button.click()


# driver.until()
# driver.close()
