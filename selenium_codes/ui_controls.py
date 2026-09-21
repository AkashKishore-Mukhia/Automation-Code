from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = 'https://rahulshettyacademy.com/AutomationPractice/'
driver = webdriver.Chrome()

driver.get(url)

checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxs:
    checkbox_value = checkbox.get_attribute('value') 
    if checkbox_value == 'option2':
        checkbox.click()
        # check assertion
        assert checkbox.is_selected()

time.sleep(2)

driver.close()

