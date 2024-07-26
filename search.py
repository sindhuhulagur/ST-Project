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

try:
    # Open LinkedIn
    driver.get("https://www.linkedin.com/login")
    print_and_flush("Opened LinkedIn login page")

    # Log in to LinkedIn
    username = driver.find_element(By.CSS_SELECTOR, "#username")
    password = driver.find_element(By.CSS_SELECTOR, "#password")
    print_and_flush("Located login fields")

    # Replace with your LinkedIn credentials
    username.send_keys("***********************")
    password.send_keys("*************************")
    print_and_flush("Entered login credentials")

    # Submit the login form
    driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button").click()
    print_and_flush("Submitted the login form")

    # Wait for the homepage to load
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-global-typeahead__input")))
    print_and_flush("Homepage loaded")

    # Search for the company
    search_box = driver.find_element(By.CSS_SELECTOR, ".search-global-typeahead__input")
    search_box.send_keys("jio")
    search_box.send_keys(Keys.RETURN)
    print_and_flush("Performed search for the company")

    # Wait for the search results to load
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'search-results__list')]")))
    print_and_flush("Search results loaded")

    # Click on the company page link
    company_link = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Jio')]/ancestor::a"))
    )
    company_link.click()
    print_and_flush("Clicked on the company page link")

    # Wait for the company page to load
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".org-top-card-primary-actions__inner button")))
    print_and_flush("Company page loaded")

    # Click the follow button
    follow_button = driver.find_element(By.CSS_SELECTOR, ".org-top-card-primary-actions__inner button")
    follow_button.click()
    print_and_flush("Clicked the follow button")

    # Wait for a moment to ensure the click is processed
    time.sleep(5)
    print_and_flush("Waited for follow action to be processed")

finally:
    # Close the browser
    driver.quit()
    print_and_flush("Closed the browser")
