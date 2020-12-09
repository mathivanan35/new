from selenium.webdriver.common.by import By

from placeOrder.Locators import buyNow_locators


class buy:
    def __init__(self, driver):
        self.driver = driver
        self.close_btn = driver.find_element(By.XPATH, buyNow_locators.btn_closePopup_xpath)
        self.search_txt = driver.find_element(By.XPATH, buyNow_locators.txt_search_xpath)
        self.searchIcon_btn = driver.find_element(By.XPATH, buyNow_locators.btn_searchicon_xpath)
        self.selectproduct_link = driver.find_element(By.XPATH, buyNow_locators.link_selectProduct_xpath)
        # self.buyNow_btn = driver.find_element(By.XPATH, buyNow_locators.btn_buyNow_xpath)

    def get_close_btn(self):
        return self.close_btn

    def get_search_txt(self):
        return self.search_txt

    def get_searchIcon_btn(self):
        return self.searchIcon_btn

    def get_selectproduct_link(self):
        return self.selectproduct_link

    def get_buyNow_btn(self):
        return self.buyNow_btn

