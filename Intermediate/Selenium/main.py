from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:/Users\henri.peters/Downloads/chromedriver_win32/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20)
driver.get("https://www.python.org")

print([my_elem.get_attribute("textContent") for my_elem in driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last time")])
print([my_elem.get_attribute("textContent") for my_elem in driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last a")])

documentation_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.tier-1.element-2 > a")))
documentation_link.click()

time.sleep(5)

driver.close()
driver.quit()
