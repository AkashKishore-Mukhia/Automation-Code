from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

base_url = 'https://rahulshettyacademy.com/angularpractice/'
driver = webdriver.Chrome()

driver.get(base_url)

driver.find_element(By.NAME, 'name').send_keys('Akash')
driver.find_element(By.NAME, 'email').send_keys('akashkishoremukhia@gmail.com')

driver.find_element(By.ID, 'exampleInputPassword1').send_keys('Akash123@#')

driver.find_element(By.ID, 'exampleCheck1').click()
driver.find_element(By.XPATH, "//input[@value='Submit']").click()

# Static dropdown
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')
dropdown.select_by_index(0)

driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()

msg = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(msg)
assert 'successfully' in msg.strip()



# Email = driver.get_by_element(By.)


time.sleep(2)

driver.close()