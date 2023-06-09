from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    delivery = "//div[@class='basket-delivery__choose-address j-btn-choose-address']"
    delivery_address = "//span[@class='address-item__name-text']"
    delivery_address_in_information = "//span[@class='details-self__name-text']"
    add_address_button = "//button[@class='details-self__btn btn-main']"
    address_in_cart = "//p[@class='b-delivery__address']"
    order_button = "//button[@class='b-btn-do-order btn-main j-btn-confirm-order']"
    autorization_warn = "//p[@class='basket-section__text-msg']"

    # Getters

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_delivery_address(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.delivery_address)))

    def get_delivery_address_in_information(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_address_in_information)))

    def get_add_address_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_address_button)))

    def get_address_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_in_cart)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    def get_autorization_warn(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.autorization_warn)))

    # Actions

    def click_delivery(self):
        self.get_delivery().click()
        print("Open delivery")

    def click_delivery_address(self):
        self.get_delivery_address()[0].click()
        print("Click first delivery address")

    def click_add_address_button(self):
        self.get_add_address_button().click()
        print("Click add address button")

    def click_order_button(self):
        self.get_order_button().click()
        print("Click order button")

    # Methods

    def choose_delivery(self):
        self.get_current_url()
        self.click_delivery()
        self.delivery_address_text = self.get_delivery_address()[0].text
        self.click_delivery_address()
        self.assert_word(self.get_delivery_address_in_information(), self.delivery_address_text)
        self.click_add_address_button()
        self.assert_word_in_str(self.get_address_in_cart(), self.delivery_address_text)
        self.get_screenshot()
        self.click_order_button()
        self.assert_word(self.get_autorization_warn()[1], 'Войти или зарегистрироваться, чтобы оформить заказ')
