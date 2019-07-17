"""
@package base

base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.SeleniumDriver import SeleniumDriver
from traceback import print_stack
from Utilities.util import Util
from base.TestParams import TestParams
import os
class BasePage(SeleniumDriver):
    resourcePropertyPath = os.environ.get('myHome') + "resources/captionBundle.properties"
    labelsOnUI = TestParams.load_properties(resourcePropertyPath)

    progressBarlocator = "//div[@class='simple-notification success ng-trigger ng-trigger-enterLeave']//div[contains(text(),'{0}')]"

    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def verifyMessageOnProgressBar(self, expectedMessageToVerify):
        """
        Verify the message on progress bar

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getText(self.progressBarlocator.format(expectedMessageToVerify),
                                       locatorType="xpath")
            # self.wait_for_page_load(5)
            self.waitForElementInVisible(self.progressBarlocator.format(expectedMessageToVerify),
                                         locatorType="xpath")
            # self.elementClick(self.progressBarlocator.format(expectedMessageToVerify),
            #                            locatorType="xpath")
            return self.util.verifyTextMatch(actualTitle, expectedMessageToVerify)
        except:
            self.log.error("Failed to verify message on progress bar")
            print_stack()
            return False

    def is_text_present(self, text):
        return str(text) in self.driver.page_source

    def verify(self, lbltargetDetails, expectedText):
        result = False
        try:
            actualText = self.getText(lbltargetDetails, locatorType="xpath")
            actualResult = str(actualText)
            expectedResult = str(expectedText)
            result = self.util.verifyTextMatch(actualResult, expectedResult)
            self.log.info("Successfully verify detail of::" + expectedResult)
        except:
            self.log.info("Error in verifying detail of::" + expectedText)
        return result
