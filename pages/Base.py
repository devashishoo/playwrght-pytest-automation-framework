from playwright.sync_api import Page
import allure


class Base:
    def __init__(self, page: Page):
        self.page = page
        self.subHeader = page.locator('h2')
        self.submitButton = page.locator("//button[@type='submit']")

    @allure.step("Opening page - {url}")
    def openURL(self, url):
        self.page.goto(url)
        return self

    @allure.step("Clicking on element")
    def clickElement(self, locator: Page.locator):
        locator.click()
        return self

    @allure.step("Verify if element is visible")
    def isVisible(self, locator: Page.locator):
        return locator.is_visible()

    @allure.step("Entering text - '{text}' in text field")
    def enterText(self, locator: Page.locator, text):
        locator.click()
        locator.fill(text)
        return self

    @allure.step("Get text of element")
    def getText(self, locator: Page.locator):
        return locator.text_content()
