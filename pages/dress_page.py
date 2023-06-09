from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class DressPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    size_button = "//label[@class='j-size sizes-list__button']"
    cart_button = "//button[@class='btn-main']"
    to_cart_button = "//a[@class='btn-base j-go-to-basket']"
    dress_title_in_cart = "//span[@class='good-info__good-name']"
    dress_price_in_cart = "//span[@class='b-right']"
    dress_title_in_card_dress = "//h1[@data-link='text{:selectedNomenclature^goodsName}']"
    dress_price_in_card_dress = "//ins[@class='price-block__final-price']"

    # Getters

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.cart_button)))

    def get_size_button(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.size_button)))

    def get_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.to_cart_button)))

    def get_dress_title_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dress_title_in_cart)))
    
    def get_dress_price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dress_price_in_cart)))

    def get_dress_title_in_card_dress(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dress_title_in_card_dress)))

    def get_dress_price_in_card_dress(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.dress_price_in_card_dress)))

    # Actions

    def click_size_button(self):
        self.get_size_button()[0].click()
        print("Click size button")

    def click_cart_button(self):
        self.get_cart_button()[1].click()
        print("Click cart button")

    def click_to_cart_button(self):
        self.get_to_cart_button()[1].click()
        print("Click to cart button")

    # Methods

    def add_dress_to_cart(self):
        self.get_current_url()
        self.click_size_button()
        self.click_cart_button()
        self.assert_word(self.get_to_cart_button()[1], 'Перейти в корзину')
        self.dress_name_in_card = self.get_dress_title_in_card_dress().text
        self.dress_cost_in_card = self.get_dress_price_in_card_dress()[1].text
        self.click_to_cart_button()
        self.assert_url('https://www.wildberries.ru/lk/basket')
        self.assert_word(self.get_dress_title_in_cart(), self.dress_name_in_card)
        self.assert_word(self.get_dress_price_in_cart(), self.dress_cost_in_card)
