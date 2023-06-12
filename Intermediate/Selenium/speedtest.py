from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

URL = "https://www.speedtest.net"

chrome_driver_path = "/Users/henri.peters/Downloads/chromedriver_win32/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20)
driver.get(URL)

documentation_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-text")))
documentation_link.click()
time.sleep(120)
print([my_elem.get_attribute("textContent") for my_elem in driver.find_elements(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.download-speed")])
print([my_elem.get_attribute("textContent") for my_elem in driver.find_elements(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.upload-speed")])



time.sleep(5)

driver.close()
driver.quit()