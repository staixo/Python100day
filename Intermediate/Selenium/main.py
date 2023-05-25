from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


chrome_driver_path = "C:/Users\henri.peters/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
wait = WebDriverWait(driver, 20)
driver.get("https://www.python.org")
print([my_elem.get_attribute("textContent") for my_elem in driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last time")])
print([my_elem.get_attribute("textContent") for my_elem in driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last a")])

wait.until(driver.find_elements(By.CSS_SELECTOR, "Documentation")).click()

time.sleep(5)

driver.close()
driver.quit()