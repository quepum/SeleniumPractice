import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    def test_registration1_should_pass(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.first_class input.form-control")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.second_class input.form-control")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.third_class input.form-control")
        input3.send_keys("iVan@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()

    def test_registration2_should_pass(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.first_class input.form-control")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.second_class input.form-control")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.third_class input.form-control")
        input3.send_keys("iVan@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        browser.quit()


if __name__ == "__main__":
    unittest.main()
