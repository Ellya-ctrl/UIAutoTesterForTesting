from selenium.webdriver.common.by import By
import selenium
import allure
import random


class selectorsAndGenerating:

    def __init__(self):
        self.addPageUrl = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust"
        self.customerListUrl = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list"

        self.firstNameSelector = (By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input')
        self.lastNameSelector = (By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input')
        self.postCodeSelector = (By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input')
        self.addCustomerButtonSelector = (By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button')

    @staticmethod
    def getGeneratingData():
        forNames = ""
        pCode = ""
        for i in range(10):
            pCode += str(random.randint(0, 10))
        listNumbers = [pCode[0] + pCode[1], pCode[2] + pCode[3], pCode[4] + pCode[5],
                       pCode[6] + pCode[7], pCode[8] + pCode[9]]
        for i in range(5):
            forNames += chr(97 + (int(listNumbers[i]) % 26))
        fName = forNames
        lName = forNames
        return [fName, lName, pCode]

    def getAddPageUrl(self):
        return self.addPageUrl

    def getCustomerListUrl(self):
        return self.customerListUrl

    def getFirstNameSelector(self):
        return self.firstNameSelector

    def getLastNameSelector(self):
        return self.lastNameSelector

    def getPostCodeSelector(self):
        return self.postCodeSelector

    def getAddCustomerButtonSelector(self):
        return self.addCustomerButtonSelector
