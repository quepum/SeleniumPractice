import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.XPATH, "//label/span[2]").text)
    result = calc(x)
    input1 = browser.find_element(By.TAG_NAME, "input").send_keys(result)

    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()
