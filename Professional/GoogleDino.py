from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# Open the Google Chrome Dino game
driver.get('chrome://dino')

# Wait for the game to load
time.sleep(2)

# Find the game container
container = driver.find_element_by_class_name('offline')

# Send SPACE key to start the game
container.send_keys(Keys.SPACE)

# Play the game for 30 seconds
time_end = time.time() + 30
while time.time() < time_end:
    # Send the UP arrow key to jump
    container.send_keys(Keys.ARROW_UP)
    time.sleep(0.1)

# Close the browser window
driver.quit()
