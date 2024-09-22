from pages.add_customer_form import AddFormPage
from pages.customers_list_page import CustomersListPage
import pytest
import allure


@pytest.mark.AddForm
@allure.feature('Add form')
@allure.story('Add form')
def test_add_form_page(browser):
    addFormPage = AddFormPage(browser)
    addFormPage.open()
    idCustomer = addFormPage.addCustomer()
    customerListpage = CustomersListPage(browser)
    customerListpage.open()
    assert customerListpage.checkElement(idCustomer)
#Команды для старта:
#pytest -v -s --alluredir results
#allure serve result