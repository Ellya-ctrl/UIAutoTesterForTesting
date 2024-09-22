from selenium import webdriver
import pytest
import allure


@pytest.fixture(scope="session")
def browser():
    chromeBrowser = webdriver.Edge()
    yield chromeBrowser
    chromeBrowser.quit()