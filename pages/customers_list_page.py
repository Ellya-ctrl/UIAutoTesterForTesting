import time
from pages.base_page import BasePage
from selectorsAndGenerating import *
import allure


#Сам класс страницы
class CustomersListPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.selectors = selectorsAndGenerating()

    def open(self):
        with allure.step('Открывает - "Customer List page"'):
            self.open_url(self.selectors.getCustomerListUrl())
            time.sleep(5)

    def checkElement(self, idElement):
        with allure.step('Ищет покупателя в списке'):
            elementSize = len(self.browser.find_elements(By.XPATH,
                                                    "/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[" + idElement + "]"))
        with allure.step('Передаёт нашёлся ли покупатель'):
            return elementSize > 0
