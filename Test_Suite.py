Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
... from selenium.webdriver.common.by import By
... import time
... import os
... 
... # Create screenshots folder if not exists
... if not os.path.exists("screenshots"):
...     os.makedirs("screenshots")
... 
... driver = webdriver.Chrome()
... driver.maximize_window()
... 
... # SauceDemo URL
... url = "https://www.saucedemo.com/"
... 
... # User list from image
... users = [
...     "standard_user",
...     "locked_out_user",
...     "problem_user",
...     "performance_glitch_user",
...     "error_user",
...     "visual_user"
... ]
... 
... password = "secret_sauce"
... 
... for user in users:
...     driver.get(url)
...     time.sleep(2)
... 
...     # Enter username & password
...     driver.find_element(By.ID, "user-name").clear()
...     driver.find_element(By.ID, "password").clear()
... 
...     driver.find_element(By.ID, "user-name").send_keys(user)
...     driver.find_element(By.ID, "password").send_keys(password)
...     driver.find_element(By.ID, "login-button").click()
...     time.sleep(3)
... 
...     print(f"\n🔍 Testing user: {user}")
... 
...     # Locked user validation
...     if user == "locked_out_user":
...         error_msg = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        print("❌ Login Failed as Expected:", error_msg)
        driver.save_screenshot(f"screenshots/{user}_error.png")

    # Successful login users
    else:
        if "inventory" in driver.current_url:
            print("✅ Login Successful")

            # Screenshot after login
            driver.save_screenshot(f"screenshots/{user}_login.png")

            # Logout
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            time.sleep(1)
            driver.find_element(By.ID, "logout_sidebar_link").click()
            time.sleep(2)
        else:
            print("⚠ Unexpected behavior observed")
            driver.save_screenshot(f"screenshots/{user}_issue.png")

driver.quit()
