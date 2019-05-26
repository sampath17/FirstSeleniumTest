from selenium import webdriver

driver = webdriver.Chrome("C:\\Python Selenium drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("facebook.png")
driver.quit()

