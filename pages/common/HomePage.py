from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from Utilities.util import Util
from base.TestParams import TestParams
import time

class HomePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    # navigationMap = TestParams.load_properties("../resources/captionBundle.properties")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    lnkdashboard = "//a[@class='nav-link active ng-star-inserted']//*[text()='{0}']"
    lnkrootCustomer = "//span[contains(text(),'{0}')]"
    lnkreports = "//span[contains(text(),'{0}')]"
    lnkadmin = "//span[contains( text(), '{0}' )]"
    btnAccountSearch = "//button[contains(text(),'{0}')]"
    btnCompaniesSearch = "//a[contains(text(),'{0}')]"
    lnkprofile = "//a[@id='userDropdown']"
    lnksettings = "//span[contains(text(),'{0}')]"
    lnksign_out = "//span[contains(text(),'{0}')]"
    ctlWelcomeMessage = "//div[contains(text(),'{0}')]"
    login_SuccessBar = "//div[@class='simple-notification success ng-trigger ng-trigger-enterLeave']//*[text()='{0}')]"
    searchTextBox = "//input[@placeholder='{0}']"

    # Locators
    lnkAccounts = "//span[contains(text(),'{0}')]"

    def verifyTextonHomepage(self):
        self.verifyWelcomeMessage()
        self.verifyDashboardlink("Dashboard")
        self.verifyRootCustomerslink("RootCustomers")
        self.verifyRootCustomerslink("Reports")
        self.verifyRootCustomerslink("Admin")
        self.verifyAccountsSearchButtontext("GlobalSearchType_Accounts", "WaterMark_Accounts")
        self.verifyCustomerSearchButtontext("GlobalSearchType_Company", "WaterMark_Company")

    def userLogout(self):
        userSettingsElement = self.waitForElement(locator=self.lnkprofile,
                                      locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)
        self.verifySettingtext("lbl_Settings")
        self.verifySignOutMessage()

    def verifyWelcomeMessage(self, loginUser):
        # ExpectedText = self.navigationMap['AdminWelcomeMessage']
        expectedText = self.navigationMap['WelcomeMsg'] + ' ' + loginUser
        actualText = self.getText( self.ctlWelcomeMessage.format( expectedText ), locatorType="xpath" )
        self.wait_for_page_load( 10)
        # result = self.isElementDisplayed(self.ctlWelcomeMessage.format(expectedText),locatorType="xpath")
        self.util.verifyTextMatch( actualText, expectedText)

    def verifyDashboardlink(self, linkText):
        ExpectedText = self.navigationMap[linkText]
        #self.waitForElement(self.lnkdashboard.format(ExpectedDashboardtext), locatorType="xpath")
        ActualText = self.getText(self.lnkdashboard.format(ExpectedText),locatorType="xpath")

    def verifyRootCustomerslink(self, linkText):
        ExpectedText = self.navigationMap[linkText]
        ActualText = self.getText(self.lnkrootCustomer.format(ExpectedText),
                                               locatorType="xpath")

    def verifyReportslink(self, linkText):
        ExpectedText = self.navigationMap[linkText]
        ActualText = self.getText(self.lnkreports.format(ExpectedText),
                                               locatorType="xpath")

    def verifyAdminlink(self, linkText):
        ExpectedText = self.navigationMap[linkText]
        ActualText = self.getText(self.lnkadmin.format(ExpectedText),
                                               locatorType="xpath")

    def verifyTextInSearchBox(self, linkText):
        Expectedtext = self.navigationMap[linkText]
        Actualtext = self.getText(self.searchTextBox.format(Expectedtext),locatorType="xpath")


    def verifyAccountsSearchButtontext(self, linkText, Placeholder):
        Expectedtext = self.navigationMap[linkText]
        ActualText = self.getText(self.btnAccountSearch.format(Expectedtext),
                                               locatorType="xpath")
        self.verifyTextInSearchBox(Placeholder)

    def verifyCustomerSearchButtontext(self, linkText, Placeholder):
        Expectedtext = self.navigationMap['GlobalSearchType_Accounts']
        self.elementClick(locator=self.btnAccountSearch.format(Expectedtext), locatorType="xpath")
        Expectedtext = self.navigationMap[linkText]
        #self.waitForElement(self.btnCompaniesSearch.format(Expectedtext), locatorType="xpath" )
        #self.elementClick(locator=self.btnCompaniesSearch.format(Expectedtext), locatorType="xpath")
        self.executeJavaScript(self.btnCompaniesSearch.format(Expectedtext),locatorType="xpath")
        self.verifyTextInSearchBox(Placeholder)

    def verifySettingtext(self, linkText):
        Expectedtext = self.navigationMap[linkText]
        ActualText = self.getText(self.lnksettings.format(Expectedtext),
                                               locatorType="xpath")

    def verifySignOuttext(self, linkText):
        expectedText = self.navigationMap[linkText]
        actualText = self.getText( self.lnksign_out.format( expectedText),
                                   locatorType="xpath" )
        self.elementClick( locator=self.lnksign_out.format( expectedText ), locatorType="xpath" )
        result = self.isElementPresent( self.ctlWelcomeMessage.format( self.navigationMap['LogOutMessage'] ),
                                        locatorType="xpath" )
        self.util.verifyTextMatch( actualText, expectedText )

    def verifySignOutMessage(self):
        expectedText = self.navigationMap['LogOutMessage']
        self.elementClick( locator=self.lnksign_out.format( self.navigationMap['lbl_SignOut'] ),
                           locatorType="xpath" )
        self.wait_for_page_load( 7 )
        result = self.isElementPresent( self.ctlWelcomeMessage.format( self.navigationMap['LogOutMessage'] ),
                                        locatorType="xpath" )
        actualText = self.getText( self.ctlWelcomeMessage.format( expectedText ),
                                   locatorType="xpath" )
        self.util.verifyTextMatch( actualText, expectedText)

    def navigateToRootCustomers(self):
        try:
            self.elementClick(self.lnkrootCustomer.format(self.navigationMap['RootCustomers']),
                                               locatorType="xpath")
            self.log.info("Successfully navigated to "+self.navigationMap['RootCustomers'])
        except:
            self.log.info("Error while navigating to" + self.navigationMap['RootCustomers'])

    def navigateToAccounts(self):
        try:
            self.elementClick( self.lnkAccounts.format( self.navigationMap['Accounts'] ),
                               locatorType="xpath" )
            self.log.info( "Successfully navigated to " + self.navigationMap['Accounts'] )
        except:
            self.log.info( "Error while navigating to" + self.navigationMap['Accounts'] )

    def navigateToAdmin(self):
        try:
            self.waitForElement( self.lnkadmin)
            self.elementClick( self.lnkadmin.format( self.navigationMap['Admin']),
                               locatorType="xpath" )
            self.log.info( "Successfully navigated to " + self.navigationMap['Accounts'] )
        except:
            self.log.info( "Error while navigating to" + self.navigationMap['Accounts'])
