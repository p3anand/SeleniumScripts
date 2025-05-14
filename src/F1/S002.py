#Sample program to understand how's is getting converted to API requests behind the picture

from selenium import webdriver

def test_open_vwo_login():
    driver = webdriver.Chrome()
    #  POST request is made here to create a New copy of Chrome
    #  New - Chrome Copy will have Session ID - example -> 6e31bb70-4809-4b20-8d87-cce289af6ce1


    driver.get("https://app.vwo.com")
    # Code makes HTTP Request - ChromeDriver is handled by (Selenium Manager) -> CHROME (SessionID)

    print(driver.title) # This is a GET Request
    assert driver.title == "Login - VWO"