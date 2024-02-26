# Import necessary libraries
import q as q
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the Magento website
driver.get("https://magento.softwaretestingboard.com/")

# Maximize the window
driver.maximize_window()

# Find and click on the "Create Account" link
create_account_link = driver.find_element(By.CSS_SELECTOR, "a[href*='customer/account/create/']")
create_account_link.click()

# Find the first name input field and enter first name
first_name_input = driver.find_element(By.ID, "firstname")
first_name_input.send_keys("Saiful")

# Find the last name input field and enter last name
last_name_input = driver.find_element(By.ID, "lastname")
last_name_input.send_keys(" Islam Rifat")

# Find the email input field and enter email address
email_input = driver.find_element(By.ID, "email_address")
email_input.send_keys("saiful@gmail.com")

# Find the password input field and enter password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("rifat786_123@3#$%667e6P")

# Find the confirm password input field and enter password again
confirm_password = driver.find_element(By.ID, "password-confirmation")
confirm_password.send_keys("rifat786_123@3#$%667e6P")

# Find and click on the "Create an Account" button
submit_button = driver.find_element(By.CSS_SELECTOR, ("button[title='Create an Account'] span"))
submit_button.click()

# Get the title of the current page and print it
title = driver.title
print(title)

# Wait for 10 seconds (you might want to replace this with an explicit wait)
time.sleep(10)
