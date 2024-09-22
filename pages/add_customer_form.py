import time
from pages.base_page import BasePage
from selenium.webdriver.common.alert import Alert
from selectorsAndGenerating import *
import allure

#Сам класс страницы
class AddFormPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.selectors = selectorsAndGenerating()

    def open(self):
        with allure.step('Открывает - "Add page"'):
            self.open_url(self.selectors.getAddPageUrl())
            time.sleep(5)

    @property
    def firstName(self):
        return self.find(self.selectors.getFirstNameSelector())

    def sendFirstName(self, firsTName):
        with allure.step('Вводит -"First Name"'):
            self.firstName.clear()
            self.firstName.send_keys(firsTName)

    @property
    def lastName(self):
        return self.find(self.selectors.getLastNameSelector())

    def sendLastName(self, lasTName):
        with allure.step('Вводит -"Last Name"'):
            self.lastName.clear()
            self.lastName.send_keys(lasTName)

    @property
    def postCode(self):
        return self.find(self.selectors.getPostCodeSelector())

    def sendPostCode(self, posTCode):
        with allure.step('Вводит -"Post Code"'):
            self.postCode.clear()
            self.postCode.send_keys(posTCode)

    @property
    def addCustomerButton(self):
        return self.find(self.selectors.getAddCustomerButtonSelector())

    def addCustomer(self):
        with allure.step('Генерация данных'):
            generatedData = self.selectors.getGeneratingData()
            firstName, lastName, postCode = generatedData[0], generatedData[1], generatedData[2]
        with allure.step('Ввод сгенерированных данных'):
            self.sendFirstName(firstName)
            self.sendLastName(lastName)
            self.sendPostCode(postCode)
        with allure.step('Отправка сгенерированных данных'):
            self.addCustomerButton.click()
            time.sleep(1)
        with allure.step('Подтверждение оповещения и сохранения айди покупателя'):
            alert = Alert(self.browser)
            alertText = alert.text
            idCustomer = alertText[alertText.index(":") + 1:]
            alert.accept()
        return idCustomer
