import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.XPATH, "//h2/span[2]").text)
    y = int(browser.find_element(By.XPATH, "//h2/span[4]").text)
    result = x + y

    select = Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(str(result))

    browser.find_element(By.XPATH, "//button").click()

finally:
    time.sleep(10)
    browser.quit()
