import logging
import Utilities.custom_logger as cl
from base.SeleniumDriver import SeleniumDriver
from base.BasePage import BasePage


class Welcome( BasePage ):
    log = cl.customLogger( logging.DEBUG )

    def __init__(self, driver):
        super().__init__( driver )
        self.driver = driver

    progressBar = "//div[@class='simple-notification success ng-trigger ng-trigger-enterLeave']"
    ctlWelcomeMessage = "//div[contains(text(),'{0}')]"
    lnkCustomerAndAccount = "//span[contains(.,'Customer & Account')]"

    def verifyWelcomeMessage(self, msg):
        self.waitForElement( self.progressBar, 10 )
        result = self.isElementDisplayed( self.ctlWelcomeMessage.format() )
