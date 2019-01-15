from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from base.TestParams import TestParams
import time

class RootCustomer(BasePage):
    log = cl.customLogger( logging.DEBUG )
    navigationMap = TestParams.load_properties( "../resources/captionBundle.properties" )

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    #Button
    btnAddRootCustomer = "//span[(text()='{0}')]/ancestor::button[@class='btn btn-primary ng-star-inserted']"
    title = "//h3[contains(.,'{0}')]"

    # Links
    lnkDifferentStatus = "//ul[@class='nav nav-pills ng-star-inserted']/li/a/span[(text()='{0}')]"
    tblRootCustomersDataRows = "//div/table/tbody/tr"
    custStatus = "//div/table/tbody/tr/td[4]", "customer Status"
    columnheader = "//span[contains(text(),'{0}')]"

    customerLink = "//div[@title='%s']/../following-sibling::td/span[1]/a"
    accountLink = "//div[@title='%s']/../following-sibling::td/span[2]/a"
    msgScrollDown = "//div[contains(.,'Please scroll down to see more records')]"


    def verifyTextonRootCustomer(self):
        self.verifyRootCustomersTitle()
        self.verifyAddRootCustomerButtonIsPresent()
        self.verifyRootCustomersStatusLinks()


    def verifyRootCustomersTitle(self):
        ExpectedText = self.navigationMap['RootCustomers']
        ActualText = self.getText( self.title.format(ExpectedText), locatorType="xpath")

    def verifyAddRootCustomerButtonIsPresent(self):
        try:
            self.isElementPresent( self.btnAddRootCustomer.format(self.navigationMap['btn_AddRootCustomer']),
                                   locatorType="xpath")
            self.log.info( "Element is present :: " + self.navigationMap['btn_AddRootCustomer'] )
        except:
            self.log.info("Error while finding element :: " + self.navigationMap['btn_AddRootCustomer'])

    def verifyRootCustomersStatusLinks(self):
        statusElements = self.navigationMap['lnk_Diff_status']
        self.list = []
        self.list = statusElements.split('|')
        for elementText in self.list:
            self.isElementPresent(self.lnkDifferentStatus.format(elementText.title()), locatorType="xpath")
            self.verifyColumnText()
            self.navigateToOthersCustomerTab(elementText.title())

    def verifyColumnText(self):
        self.isElementPresent( self.columnheader.format(self.navigationMap['lbl_tblcolumn_Name'].title() ),
                               locatorType="xpath" )
        self.isElementPresent( self.columnheader.format(self.navigationMap['lbl_tblcolumn_CustomerId'].title() ),
                               locatorType="xpath" )
        self.isElementPresent( self.columnheader.format(self.navigationMap['lbl_tblcolumn_BankId'].title() ),
                               locatorType="xpath" )
        self.isElementPresent( self.columnheader.format(self.navigationMap['lbl_tblcolumn_Status'].title() ),
                               locatorType="xpath" )
        self.isElementPresent( self.columnheader.format(self.navigationMap['lbl_tblcolumn_Sector'].title() ),
                               locatorType="xpath" )
        self.isElementPresent( self.columnheader.format(self.navigationMap['lbl_tblcolumn_MarketSegment'].title() ),
                               locatorType="xpath" )

    def navigateToOthersCustomerTab(self, tabHeader):
        try:
            self.elementClick(self.lnkDifferentStatus.format(tabHeader),
                                               locatorType="xpath")
            self.log.info("Successfully navigated to :: " + tabHeader.upper())
        except:
            self.log.info("Error while navigating to :: " + tabHeader.upper())

    def clickOnAddRootCustomerButton(self):
        self.elementClick(self.btnAddRootCustomer.format(self.navigationMap['btn_AddRootCustomer']),
                                   locatorType="xpath")
