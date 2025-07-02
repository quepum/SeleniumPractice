import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[1]").send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[2]").send_keys("Ivanovich")
    input3 = browser.find_element(By.XPATH, "//input[3]").send_keys("iVan@gmail.com")

    current_dir = os.path.abspath(os.path.dirname("file.txt"))
    file_path = os.path.join(current_dir, "file.txt")

    input_file = browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
