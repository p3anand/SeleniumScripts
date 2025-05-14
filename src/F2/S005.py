#Understanding Chrome Options

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def test_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=900,600")
    chrome_options.add_argument("--headless") #No UI - test will run
    # chrome_options.add_argument("--disable-infobars") #this removes the bar with message Chrome is being controlled by automated test software.

    driver = webdriver.Chrome(chrome_options)  # Create the Session | 62c075633fd0b0727c5c3f6eae5665ab
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # Navigate to URL
    # Chrome - incognito mode ->

    assert True == False #Code made to fail on purpose

    # Stop the Python int for 10 secs
    time.sleep(10)