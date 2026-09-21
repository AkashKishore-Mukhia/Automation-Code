from selenium import webdriver
from selenium.webdriver.common.by import By
import time

name = 'Akash'
url = 'https://rahulshettyacademy.com/AutomationPractice/'
driver = webdriver.Chrome()

driver.get(url)

driver.find_element(By.NAME, 'enter-name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()

alert_popup = driver.switch_to.alert
alert_msg = alert_popup.text

print(alert_msg)
assert name in alert_msg

alert_popup.accept()
# alert_popup.dismiss

driver.switch_to
driver.find_element(By.ID, 'confirmbtn').click()
confimation_popup = driver.switch_to.alert
confimation_popup.dismiss()

time.sleep(2)