import time

from Login.baseClass import base
from Login.maintain import demo
from Login.readSheet import read
import pytest


def test_login():
    b = base()
    driver = b.getDriver()
    driver.get("https://www.flipkart.com/")
    time.sleep(4)
    d = demo(driver)
    b.type(d.username_xpath, read(1, 2))
    time.sleep(4)
    b.type(d.password_xpath, read(2, 2))
    time.sleep(4)
    b.clk(d.get_login_xpath())
    time.sleep(4)

