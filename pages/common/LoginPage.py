import Utilities.custom_logger as cl
from pages.common.HomePage import HomePage
from base.BasePage import BasePage
import logging


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home = HomePage(driver)

    # Locators
    txtUserId = "userid"
    txtPassword = "password"
    btnSign_In = "//button[@type='submit']"

    def loginToApplication(self, userId="", password=""):
        # self.clearFields()
        self.enterUserId(userId)
        self.enterPassword(password)
        self.clickLogin()

    def enterUserId(self, userId):
        #self.clearField()
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