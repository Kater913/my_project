from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class PageWithDresses(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    filters = "//button[@class='dropdown-filter__btn dropdown-filter__btn--all']"
    header_filters = "//h3[@class='filters-desktop__title']"
    checkbox = "//span[@class='checkbox-with-text__text']"
    radiobutton = "//span[@class='radio-with-text__text']"
    add_filter_button = "//button[@class='filters-desktop__btn-main btn-main']"
    added_filter_button = "//button[@class='your-choice__btn']"
    sorted_filter = "//button[@class='dropdown-filter__btn dropdown-filter__btn--sorter']"
    dress = "//a[@class='product-card__link j-card-link j-open-full-product-card']"
    dress_title = "//span[@class='product-card__name']"
    dress_title_on_new_page = "//h1[@data-link='text{:selectedNomenclature^goodsName}']"

    # Getters

    def get_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filters)))

    def get_header_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.header_filters)))

    def get_checkboxes(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.checkbox)))

    def get_radiobuttons(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.radiobutton)))

    def get_add_filter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_filter_button)))

    def get_added_filter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.added_filter_button)))

    def get_sorted_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorted_filter)))

    def get_dresses(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.dress)))

    def get_dress_title_in_minicard(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dress_title)))

    def get_dress_title_on_new_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dress_title_on_new_page)))

    # Actions

    def click_filters(self):
        self.get_filters().click()
        print("Click filters")

    def click_checkbox(self):
        self.get_checkboxes()[0].click()
        print("Choose checkbox dress")

    def click_radiobutton_delivery(self):
        self.get_radiobuttons()[1].click()
        print("Choose 1 days delivery")

    def click_add_filter_button(self):
        self.get_add_filter_button().click()
        print("Added filters")

    def click_sorted_filter(self):
        self.get_sorted_filter().click()
        print("Added filters")

    def click_radiobutton_sorted(self):
        self.get_radiobuttons()[3].click()
        print("Sorted most expensive")

    def click_first_dress(self):
        self.get_dresses()[0].click()
        print("Choose first dress")

    # Methods

    def choose_dresses(self):
        self.get_current_url()
        sleep(1)
        self.click_filters()
        sleep(2)
        self.assert_url('https://www.wildberries.ru/catalog/zhenshchinam/odezhda/platya')
        self.assert_word(self.get_header_filters(), 'Фильтры')
        self.click_checkbox()
        self.click_radiobutton_delivery()
        self.click_add_filter_button()
        self.assert_word(self.get_added_filter_button(), 'Сбросить все')
        # self.click_sorted_filter()
        # self.click_radiobutton_sorted()
        sleep(1)
        # проверка для случая, когда применили сортировку по цене
        # self.assert_url('https://www.wildberries.ru/catalog/zhenshchinam/odezhda/platya?sort=pricedown&page=1&xsubject=69&fdlvr=24')
        # проверка для случая, когда НЕ применили сортировку по цене
        self.assert_url('https://www.wildberries.ru/catalog/zhenshchinam/odezhda/platya?sort=popular&page=1&xsubject=69&fdlvr=24')
        self.dress_title_in_minicard = self.get_dress_title_in_minicard().text[2:]
        self.click_first_dress()
        self.assert_word(self.get_dress_title_on_new_page(), self.dress_title_in_minicard)
