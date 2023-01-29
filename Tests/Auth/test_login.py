from playwright.sync_api import Page
from pages import HomePage
import allure
from Tests import AUTH_CONSTANTS
import pytest


@allure.description("Verify login fails for incorrect password")
def test_login_fail(page: Page):
    homePage = HomePage(page)
    assert homePage.openURL(
        AUTH_CONSTANTS.PAGE_URL).subHeader.text_content() == 'Login Page'
    homePage.enterUsernameAndPassword('abcd', 'wrongPassword@1')

    assert homePage.isVisible(homePage.flashBanner) == False

    homePage.clickElement(homePage.submitButton)

    assert homePage.isVisible(homePage.flashBanner) == True
    assert 'Your username is invalid!' in homePage.getText(
        homePage.flashBanner)


@allure.description("Verify login fails for incorrect password")
def test_login_success(page: Page):
    homePage = HomePage(page)
    assert homePage.openURL(
        AUTH_CONSTANTS.PAGE_URL).subHeader.text_content() == 'Login Page'
    homePage.enterUsernameAndPassword('tomsmith', 'SuperSecretPassword!')
    homePage.clickElement(homePage.submitButton)

    assert homePage.isVisible(homePage.flashBanner) == True
    assert 'You logged into a secure area!' in homePage.getText(
        homePage.flashBanner)
