from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from base.TestParams import TestParams
from inputTestData import inputAccountCashManagementTest
from Utilities.util import Util
from datetime import date


class Reports(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    btnNewTemplate = "//span[text()[normalize-space() = '{0}']]/.."
    templateAccessFilter = "(//div[@class='btn btn-link dropdown dropdown-toggle']//span)[1]"
    templateTypeFilter = "(//div[@class='btn btn-link dropdown dropdown-toggle']//span)[2]"
    templateAccessFilterValue = "//div[@class='dropdown-menu show']//div[text()[normalize-space()='{0}']]"

    def clickOnButton(self):
        try:
            self.waitForElement(self.btnNewTemplate, 4)
            self.executeJavaScript(self.btnNewTemplate.format(self.navigationMap['btnNewTemplate']),
                                   locatorType="xpath")
            self.wait_for_page_load(3)
        except Exception as e:
            self.log.error("Unable to click on button :: ")

    def setAccessFilter(self, templateinfo):
        try:
            self.wait_for_page_load(3)
            self.elementClick(self.templateAccessFilter, locatorType="xpath")
            self.elementClick(self.templateAccessFilterValue.format(templateinfo.loc[0].get('Access')),
                              locatorType="xpath")
            self.elementClick(self.templateTypeFilter, locatorType="xpath")
            self.elementClick(self.templateAccessFilterValue.format(templateinfo.loc[0].get('Report Type')),
                              locatorType="xpath")
            self.wait_for_page_load(3)
        except Exception as e:
            self.log.error("Unable to click on button :: ")
