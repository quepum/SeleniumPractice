import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math

link = "https://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    price_element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    browser.execute_script("window.scrollTo(0, 100);")
    x = int(browser.find_element(By.XPATH, "//label/span[2]").text)
    result = calc(x)
    input1 = browser.find_element(By.TAG_NAME, "input").send_keys(result)

    button2 = browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(10)
    browser.quit()
