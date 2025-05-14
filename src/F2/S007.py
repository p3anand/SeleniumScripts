#Automating test steps
#1. Navigate to the URL - ﻿[katalon-demo-cura.herokuapp.com](https://katalon-demo-cura.herokuapp.com/profile.php#login)
#2. Find the **Make appointment** Button
#3. Click on the **Make appointment** Button
#4. Next Page will be loaded
#5. **Find and Enter** the details **Username and Password** and **Click** on the Login Button

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_chrome_current_url_verification():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # 1- Find the element the anchor tag
    # <a - open tag
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a> close tag

    # Find an element given a By strategy and locator.
    # 2- We need to find the unique attribute which can find the web element

    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")

    # 3- Click on it
    make_appointment_element.click()

    # 4- Verify that URL changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(10)
    driver.quit()