from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def print_and_flush(message):
    print(message)
    sys.stdout.flush()

def initialize_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")
    return driver

def login(driver, email, password):
    try:
        username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
        password_field = driver.find_element(By.CSS_SELECTOR, "#password")
        print_and_flush("Located login fields")

        username.send_keys(email)
        password_field.send_keys(password)
        print_and_flush("Entered login credentials")

        driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
        print_and_flush("Submitted the login form")

        return True
    except Exception as e:
        print_and_flush(f"Login failed with exception: {e}")
        return False

def test_login_success(driver):
    print_and_flush("Testing successful login...")
    success = login(driver, "************", "******************")
    if success:
        try:
            WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-global-typeahead__input")))
            print_and_flush("Login successful, homepage loaded")
        except Exception as e:
            print_and_flush(f"Failed to load homepage after successful login: {e}")
    else:
        print_and_flush("Login unsuccessful with valid credentials.")

def test_login_failure(driver):
    print_and_flush("Testing failed login...")
    success = login(driver, "****************", "invalidpassword")
    if not success:
        try:
            error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "error-for-password")))
            print_and_flush("Login failed as expected with invalid credentials")
        except Exception as e:
            print_and_flush(f"Failed to find error message after failed login: {e}")
    else:
        print_and_flush("Unexpectedly logged in with invalid credentials.")

def main():
    driver = initialize_driver()
    
    test_login_success(driver)
    
    driver.quit()
    print_and_flush("Closed the WebDriver after successful login test")

    driver = initialize_driver()
    
    test_login_failure(driver)
    
    driver.quit()
    print_and_flush("Closed the WebDriver after failed login test")

if __name__ == "__main__":
    main()
