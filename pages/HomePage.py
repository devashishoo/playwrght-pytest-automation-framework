from playwright.sync_api import Page
from .Base import Base
import allure


class HomePage(Base):
    def __init__(self, page: Page):
        Base.__init__(self, page)
        self.usernameField = page.get_by_label("Username")
        self.passwordField = page.get_by_label("Password")
        self.flashBanner = page.locator("//div[@id='flash']")
        self.dsds = 'dsds'

    @allure.step("Enter username - {username} and password - {password}")
    def enterUsernameAndPassword(self, username, password):
        self.enterText(self.usernameField, username).enterText(
            self.passwordField, password)
