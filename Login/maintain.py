from selenium.webdriver.common.by import By

from Login import Locators


class demo:
    def __init__(self, driver):
        self.driver = driver
        self.username_xpath = driver.find_element(By.XPATH, Locators.txt_username_xpath)
        self.password_xpath = driver.find_element(By.XPATH, Locators.txt_password_xpath)
        self.login_xpath = driver.find_element(By.XPATH, Locators.btn_login_xpath)

    def get_username_xpath(self):
        return self.username_xpath

    def get_password_xpath(self):
        return self.password_xpath

    def get_login_xpath(self):
        return self.login_xpath
