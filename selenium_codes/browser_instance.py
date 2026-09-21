from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# chrome driver service selenium driver.
# service_obj = Service('path/of/chrome-driver')
# driver = webdriver.Chrome(Service=service_obj)

# chrome driver intialization
driver = webdriver.Chrome()
driver.get('https://selenium-python.readthedocs.io/getting-started.html')
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(2)

