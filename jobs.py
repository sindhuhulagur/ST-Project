from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    username.send_keys("*********")
    password.send_keys("*********")
    print_and_flush("Entered login credentials")

    # Submit the login form
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print_and_flush("Submitted the login form")

    # Wait for the homepage to load
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-global-typeahead__input")))
    print_and_flush("Homepage loaded")

    # Click on the Jobs icon
    jobs_icon = WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.global-nav__primary-item:nth-child(3) > a:nth-child(1)")))
    jobs_icon.click()
    print_and_flush("Clicked on the Jobs icon")

    # Wait for the Jobs page to load
    WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jobs-search-box__input--keyword")))
    print_and_flush("Jobs page loaded")

    # Click on the first job link available on the page
    first_job_link = WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".job-card-container__link")))
    first_job_link.click()
    print_and_flush("Clicked on the first job link available on the page")

    # Wait for the job details page to load
    WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jobs-save-button")))
    print_and_flush("Job details page loaded")

    # Click the save button
    save_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button:nth-child(3)")
    save_button.click()
    print_and_flush("Clicked the save button")

finally:
    # Close the WebDriver
    driver.quit()
    print_and_flush("Closed the WebDriver")