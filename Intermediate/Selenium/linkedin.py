from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

chrome_driver_path = "C:/Users\henri.peters/Downloads/chromedriver_win32/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20)
driver.get(URL)

documentation_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cta-modal__primary-btn.btn-md.btn-primary.inline-block.w-full.mt-3")))
documentation_link.click()

input_element = driver.find_element("id","username")

# Use send_keys to write into the element
input_element.send_keys("Hello, world!")

input_element = driver.find_element("id","password")

# Use send_keys to write into the element
input_element.send_keys("Hello, world!")
documentation_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn__primary--large.from__button--floating")))
documentation_link.click()

time.sleep(5)

driver.close()
driver.quit()