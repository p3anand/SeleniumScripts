#Open an Url and print the Url's page source
from selenium import webdriver

def test_open_vmo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")  # Navigate to URL
    page_source_data = driver.page_source
    print(page_source_data)
