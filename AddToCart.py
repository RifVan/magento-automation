
from selenium import webdriver  # Importing the Selenium WebDriver module
import time  # Importing the time module for sleep functionality
from selenium.webdriver.common.keys import Keys  # Importing Keys for keyboard actions
from selenium.webdriver.common.by import By  # Importing By to locate elements


# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://magento.softwaretestingboard.com/")

# Maximize the window
driver.maximize_window()

# Get the title of the webpage and print it
title = driver.title
print(title)

# Click on the "Sign In" link
log_in = driver.find_element(By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]")
log_in.click()
time.sleep(2)

# Enter email address
email_input = driver.find_element(By.CSS_SELECTOR, "#email").send_keys("saiful@gmail.com")

# Enter password
password_input = driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//input[@id='pass']").send_keys("rifat786_123@3#$%667e6P")
time.sleep(2)
# Click on the "Sign In" button
sign_in = driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]")
sign_in.click()
time.sleep(3)
# Click on the "Men" product category
men_product = driver.find_element(By.XPATH, "//span[normalize-space()='Men']")
men_product.click()
time.sleep(2)  # Wait for 2 seconds

# Enter search term "Hero Hoodie" in the search input field
search_input = driver.find_element(By.XPATH, "(//input[@id='search'])[1]")
search_input.send_keys("Hero Hoodie")

# Click on the search button
search_button = driver.find_element(By.XPATH, "//button[@class='action search']")
search_button.click()
time.sleep(3)  # Wait for 3 seconds

# Go to the "Hero Hoodie" product page
driver.get("https://magento.softwaretestingboard.com/hero-hoodie.html")
time.sleep(3)  # Wait for 3 seconds

# Select hoodie size
hoodie_size = driver.find_element(By.XPATH, "(//div[@id='option-label-size-143-item-169'])[1]")
hoodie_size.click()
time.sleep(3)  # Wait for 3 seconds

# Select hoodie color
hoodie_color = driver.find_element(By.XPATH, "(//div[@id='option-label-color-93-item-53'])[1]")
hoodie_color.click()
time.sleep(3)  # Wait for 3 seconds

# Click on the "Add to Cart" button
add_cart = driver.find_element(By.XPATH, "(//span[normalize-space()='Add to Cart'])[1]")
add_cart.click()
time.sleep(3)  # Wait for 3 seconds

# Print success message
print("Product added to cart successfully!")

# Wait for 10 seconds before closing the browser
time.sleep(5)
driver.quit()