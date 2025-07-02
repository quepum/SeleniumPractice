import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, "button").click()

    confirm = browser.switch_to.alert.accept()

    x = int(browser.find_element(By.XPATH, "//label/span[2]").text)
    result = calc(x)
    input1 = browser.find_element(By.TAG_NAME, "input").send_keys(result)

    button2 = browser.find_element(By.CSS_SELECTOR, "button").click()
finally:
    time.sleep(10)
    browser.quit()
