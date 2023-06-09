from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class PageWithWomanCategories(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    woman_categories = "//a[@class='j-menu-item']"
    header = "//h1[@class='catalog-title']"

    # Getters

    def get_woman_categories(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.woman_categories)))

    def get_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.header)))

    # Actions

    def click_woman_categories(self):
        self.get_woman_categories()[9].click()
        print("Click dresses")

    # Methods

    def select_dresses(self):
        self.get_current_url()
        sleep(1)
        self.click_woman_categories()
        sleep(2)
        self.assert_url('https://www.wildberries.ru/catalog/zhenshchinam/odezhda/platya')
        self.assert_word(self.get_header(), 'Женские платья')
