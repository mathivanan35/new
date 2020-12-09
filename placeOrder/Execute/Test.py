import time

from placeOrder.Reuse.baseClass import base
from placeOrder.maintenance.buyNow_maintain import buy
from placeOrder.Reuse.readSheet import read


def test_buy():
    b = base()
    driver = b.getDriver()
    driver.get("https://www.flipkart.com/")
    driver.implicitly_wait(20)
    buy1 = buy(driver)
    time.sleep(10)
    b.clk(buy1.get_close_btn())
    time.sleep(10)
    b.type(buy1.get_search_txt(),read(1, 2))
    time.sleep(10)
    b.clk(buy1.get_searchIcon_btn())
    time.sleep(10)

    # b.clk(buy1.get_selectproduct_link())
    # time.sleep(10)
    #
    #
    #
    # k = driver.window_handles
    # p = driver.current_window_handle
    # for i in k:
    #     if i != p:
    #         driver.switch_to.window(i)
    #         time.sleep(10)
    # b.clk(buy1.get_buyNow_btn())