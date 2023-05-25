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

documentation_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view")))
documentation_link.click()

time.sleep(5)

driver.close()
driver.quit()