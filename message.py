from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def print_and_flush(message):
    print(message)
    sys.stdout.flush()

# Initialize the WebDriver
driver = webdriver.Chrome()
print_and_flush("Initialized WebDriver")

# Open LinkedIn
driver.get("https://www.linkedin.com/login")
print_and_flush("Opened LinkedIn login page")

# Log in to LinkedIn
username = driver.find_element(By.CSS_SELECTOR, "#username")
password = driver.find_element(By.CSS_SELECTOR, "#password")
print_and_flush("Located login fields")

# Replace with your LinkedIn credentials
username.send_keys("*******************")
password.send_keys("*******************")
print_and_flush("Entered login credentials")

# Submit the login form
driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
print_and_flush("Submitted the login form")

# Wait for the homepage to load
WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-global-typeahead__input")))
print_and_flush("Homepage loaded")

# Click on the messaging icon
messaging_icon = WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[4]/a")))
messaging_icon.click()
print_and_flush("Clicked on the messaging icon")

# Wait for the messaging window to load
WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".msg-overlay-bubble-header")))
print_and_flush("Messaging window loaded")


# Type the message
message_box = WebDriverWait(driver, 190).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".msg-form__contenteditable")))
message_box.send_keys("Hello, this is a test message.")
print_and_flush("Typed the message")

# Send the message
send_button = WebDriverWait(driver, 190).until(EC.element_to_be_clickable((By.ID, "ember364")))
send_button.click()
print_and_flush("Sent the message")

# Close the WebDriver
driver.quit()
print_and_flush("Closed the WebDriver")