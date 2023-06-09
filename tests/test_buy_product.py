from selenium import webdriver

from pages.cart_page import CartPage
from pages.dress_page import DressPage
from pages.main_page import MainPage
from pages.page_with_categories import PageWithWomanCategories
from pages.page_with_dresses import PageWithDresses


def test_buy_product():

    driver = webdriver.Chrome("/home/e.glushanina/PycharmProjects/resource/chromedriver")

    print('Start test')

    mp = MainPage(driver)
    mp.choose_category_for_woman()

    pwp = PageWithWomanCategories(driver)
    pwp.select_dresses()

    pwd = PageWithDresses(driver)
    pwd.choose_dresses()

    dp = DressPage(driver)
    dp.add_dress_to_cart()

    cp = CartPage(driver)
    cp.choose_delivery()

    driver.quit()
