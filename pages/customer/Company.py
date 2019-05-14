from ABO.customer.CustomerABO import CustomerABO
from Utilities.util import Util
from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from pages.customer.Customer import Customer
import time

from inputTestData import inputCustomerTest
from inputTestData import inputAccountCashManagementTest


class Company( Customer ):
    log = cl.customLogger( logging.DEBUG )

    def __init__(self, driver):
        super().__init__( driver )
        self.driver = driver

    # Locators
    lnkCustomerName = "//span[contains(text(),'{0}')]"
    addChildCustomer = "//span[text()='{0}']/following-sibling::" \
                       "div[@class='level-item-actions ng-star-inserted']//app-icon[@iconclass='icon-sm']"

    btnSendForActivation = "//button[@class='btn btn-primary']"
    chkboxChooseBranchForApproval = "//label/div/strong[text()='{0}']"
    btnSend = "//button[@class='btn btn-lg btn-success']"

    def clickOnParentCustomerToAddChild(self, parent):
        try:
            self.elementClick( self.lnkCustomerName.format( parent ),
                               locatorType="xpath" )
            self.elementClick( self.addChildCustomer.format( parent ),
                               locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while filling address details. :: " )

    def createCustomerHierarchy(self, company):
        # if type( company ) is dict:
        #     for key, value in company.items():
        #         fill = inputCustomerTest.rootCustomer
        #         fill['Name'] = str( key )
        #         self.fill_customer_information( fill )
        #         self.clickOnAddCustomerButton()
        #         time.sleep( 5 )
        #         keyvalue = key
        #         self.clickOnParentCustomerToAddChild( key )
        #         self.createCustomerHierarchy( value, keyvalue )
        # elif type( company ) is str:
        #     fill = inputCustomerTest.rootCustomer
        #     fill['Name'] = str( company )
        #     self.fill_customer_information( fill )
        #     self.clickOnAddCustomerButton()
        #     time.sleep( 5 )
        # elif type( company ) is list:
        #     for item in company:
        #         print( keyvalue )
        #         self.clickOnParentCustomerToAddChild( keyvalue )
        #         self.createCustomerHierarchy( item, keyvalue )
        # if type(company) is str:
        #     fill = inputCustomerTest.rootCustomer
        #     fill['Name'] = str( company )
        #     self.fill_customer_information( fill )
        #     self.clickOnAddCustomerButton()
        #     time.sleep( 5 )
        # else:
        for i in range(len(company)):
            self.clickOnParentCustomerToAddChild(company.loc[i]['Parent'])
            fill = company.loc[i]
            self.fill_customer_information(fill)
            self.clickOnAddCustomerButton()
            time.sleep(5)

    def activateCustomer(self, companyName):
        try:
            self.waitForElement( self.btnSendForActivation )
            self.elementClick( self.btnSendForActivation, locatorType="xpath" )
            self.waitForElement( self.chkboxChooseBranchForApproval )
            self.elementClick( self.chkboxChooseBranchForApproval.format( companyName ),
                               locatorType="xpath" )
            self.elementClick( self.btnSend, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while filling address details. :: " )
