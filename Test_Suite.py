Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
... from selenium.webdriver.common.by import By
... import time
... import os
... 
... if not os.path.exists("screenshots"):
...     os.makedirs("screenshots")
... 
... driver = webdriver.Chrome()
... driver.maximize_window()
... 
... URL = "https://www.saucedemo.com/"
... PASSWORD = "secret_sauce"
... 
... positive_users = [
...     "standard_user",
...     "problem_user",
...     "performance_glitch_user",
...     "error_user",
...     "visual_user"
... ]
... 
... negative_users = [
...     "locked_out_user"
... ]
... 
... print("\n===== POSITIVE LOGIN TESTS =====")
... 
... for user in positive_users:
...     driver.get(URL)
...     time.sleep(2)
... 
...     driver.find_element(By.ID, "user-name").clear()
...     driver.find_element(By.ID, "password").clear()
... 
...     driver.find_element(By.ID, "user-name").send_keys(user)
...     driver.find_element(By.ID, "password").send_keys(PASSWORD)
...     driver.find_element(By.ID, "login-button").click()
...     time.sleep(3)
... 
...     if "inventory" in driver.current_url:
...         print(f"✅ Login successful for {user}")
...         driver.save_screenshot(f"screenshots/{user}_positive.png")
... 
...         # Logout
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(2)
    else:
        print(f"⚠ Unexpected issue for {user}")
        driver.save_screenshot(f"screenshots/{user}_issue.png")

print("\n===== NEGATIVE LOGIN TEST (LOCKED USER) =====")

driver.get(URL)
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
print("❌ Locked User Error:", error)
driver.save_screenshot("screenshots/locked_user.png")


print("\n===== NEGATIVE LOGIN TEST (WRONG PASSWORD) =====")

driver.get(URL)
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("wrong_password")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
print("❌ Wrong Password Error:", error)
driver.save_screenshot("screenshots/wrong_password.png")


print("\n===== NEGATIVE LOGIN TEST (EMPTY FIELDS) =====")

driver.get(URL)
time.sleep(2)

driver.find_element(By.ID, "user-name").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
print("❌ Empty Fields Error:", error)
driver.save_screenshot("screenshots/empty_fields.png")

driver.quit()
