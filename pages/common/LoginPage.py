import Utilities.custom_logger as cl
from pages.common.HomePage import HomePage
from base.BasePage import BasePage
import logging
from resources.config import ApplicationConfig
from base.WebDriverFactory import WebDriverFactory


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home = HomePage(driver)
        self.WebDriver = WebDriverFactory( driver )

    # Locators
    txtUserId = "userid"
    txtPassword = "password"
    btnSign_In = "//button[@type='submit']"

    def loginToApplication(self, userId="", password=""):
        if userId == "" and password == "":
            self.clearFields()
            self.enterUserId( ApplicationConfig.get( 'UserId' ) )
            self.enterPassword( ApplicationConfig.get( 'Password' ) )
            self.clickLogin()
        else:
            self.driver = self.WebDriver.getWebDriverInstance()
            self.enterUserId( userId )
            self.enterPassword( password )
            self.clickLogin()

    def enterUserId(self, userId):
        self.sendKeys(userId,self.txtUserId)

    def enterPassword(self, password):
        self.sendKeys(password, self.txtPassword)

    def clickLogin(self):
        self.elementClick(locator=self.btnSign_In, locatorType="xpath")

    def clearFields(self):
        txtUserId = self.getElement(locator=self.txtUserId)
        txtUserId.clear()
        txtPassword = self.getElement(locator=self.txtPassword)
        txtPassword.clear()