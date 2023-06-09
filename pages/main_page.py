from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):

    url = 'https://www.wildberries.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    product_category_btn = "//button[@aria-label='Навигация по сайту']"
    category_for_woman = "//a[@class='menu-burger__main-list-link menu-burger__main-list-link--306']"
    header = "//h1[@class='catalog-title']"

    # Getters

    def get_product_category_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_category_btn)))

    def get_category_for_woman(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_for_woman)))

    def get_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.header)))

    # Actions

    def click_product_category_btn(self):
        self.get_product_category_btn().click()
        print("Open product category")

    def click_category_for_woman(self):
        self.get_category_for_woman().click()
        print("Choose category for woman")

    # Methods

    def choose_category_for_woman(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(1)
        self.click_product_category_btn()
        self.click_category_for_woman()
        self.assert_url('https://www.wildberries.ru/catalog/zhenshchinam')
        self.assert_word(self.get_header(), 'Женщинам')
