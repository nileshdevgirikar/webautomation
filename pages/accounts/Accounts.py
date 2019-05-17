from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from base.TestParams import TestParams
from inputTestData import inputAccountCashManagementTest, inputCustomerTest
from Utilities.util import Util
import time


class Accounts(BasePage):
    log = cl.customLogger( logging.DEBUG )

    def __init__(self, driver):
        super().__init__( driver )
        self.driver = driver

    # Locators
    btnAddRootAccount = "//a[@class='btn btn-primary mt-3 ng-star-inserted']"
    btnAddSuccessAccount = "//button[@class='btn btn-lg btn-success']"

    # Select boxes
    ddlAccountType = "//span[@class='ng-arrow']"
    ddlAccountSubType = "//div[@class='ng-option ng-star-inserted marked']" \
                        "//span[@class='ng-option-label ng-star-inserted'][contains(text(),'{0}')]"
    # "//div[span[h6[contains(text(),'{0}')]]]/following-sibling::div[@class='ng-option ng-star-inserted']/span[text()='{0}']"
    ddlAccountHeaderType = "//div[span[h6[contains(text(),'{0}')]]]"
    ddlRootAccountType = "//span[@class='ng-option-label ng-star-inserted'][text()='{0}']"
    ddlHierarchysubtype = "//select[@id='hierarchySubType']"
    ddlCurrency = "//select[@id='currency']"
    ddlCountrylist = "//select[@id='country']"
    ddlReferencetype = "//table[@class='table table-sm']/tbody/tr[@ng-reflect-name='{0}']" \
                       "/td/label[text()='Reference Type']/following-sibling::div"
    ddlParentAccount = "//select[@id='parentAccount']"
    ddlNewParentAccount = "//select[@id='newParentId']"
    ddlOwner = "//select[@id='owner']"
    chkboxChooseBranchForApproval = "//label/div/strong[text()='{0}']"

    # TextBoxes
    txtNameOfTheaccount = "//input[@id='accountName']"
    txtAccountNumber = "//input[@id='accountNumber']"
    txtReferenceNumber = "//table[@class='table table-sm']/tbody/tr[@ng-reflect-name='0']/td/input"
    # txtManRefNumber = ""

    lnkCustomerName = "//span[text()[normalize-space() = '{0}']]"
    addChildCustomer = "//span[text()[normalize-space() = '{0}']]/ancestor::li//app-icon[@iconclass='icon-sm']"

    arrow = "//*[@class='icon icon-chevron-left icon-lg']"
    folder = "//*[@class='icon icon-folder']"

    btnSendForActivation = "//button[@class='btn btn-primary']"
    btnSend = "//button[@class='btn btn-lg btn-success']"

    def clickOnAddRootAccountButton(self):
        try:
            self.waitForElement(self.btnAddRootAccount,4)
            self.executeJavaScript(self.btnAddRootAccount, locatorType="xpath")
            #self.elementClick( self.btnAddRootAccount, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Unable to click add root account button :: " )

    def selectAccountType(self,Account):
        try:
            self.waitForElement( self.ddlAccountType )
            self.elementClick( self.ddlAccountType, locatorType="xpath" )
            self.waitForElement(self.ddlRootAccountType)
            self.elementClick( self.ddlRootAccountType.format(Account), locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while click on AccountType. :: " )

    def selectHierarchyoffering(self, Hierarchyoffering):
        try:
            self.selectvaluefromDropdown(Hierarchyoffering, self.ddlHierarchysubtype, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while selecting Hierarchyoffering. :: " )

    def selectSubAccountType(self):
        try:
            #self.waitForElement(self.ddlAccountType )
            self.elementClick( self.ddlAccountType, locatorType="xpath" )
            #self.waitForElement( self.ddlAccountSubType )
            #self.elementClick( self.ddlAccountSubType, locatorType="xpath" )
        except Exception as e:
            self.log.error("Error occurred while click on AccountType. :: ")

    def clickOnSuccessAccountButton(self):
        try:
            self.elementClick( self.btnAddSuccessAccount, locatorType="xpath" )
        except Exception as e:
            self.log.error("Error occurred while click on AccountType. :: ")

    def selectCurrency(self,currency):
        try:
            self.waitForElement(self.ddlCurrency)
            self.selectvaluefromDropdown(currency, self.ddlCurrency, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while filling address details. :: " )

    def enterAccountName(self,accountName):
        try:
            accountName = accountName  #+ Util.get_unique_number( 5 )
            self.sendKeys(accountName, self.txtNameOfTheaccount, locatorType="xpath")
        except Exception as e:
            self.log.error( "Error occurred while filling address details. :: " )
        return accountName

    def enterAccountNumber(self, AccountNumber):
        try:
            AccountNumber = AccountNumber + Util.get_unique_number( 14 )
            self.sendKeys(AccountNumber, self.txtAccountNumber, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while filling address details. :: " )
        return AccountNumber

    def selectCountry(self, country):
        try:
            self.selectvaluefromDropdown(country, self.ddlCountrylist, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while filling address details. :: " )

    def fill_Account_Details(self, accountDetail,i):
        self.selectHierarchyoffering(accountDetail.loc[i]['Hierarchy offering'])
        self.selectAccountType(accountDetail.loc[i].get('Account type'))
        self.selectCurrency(accountDetail.loc[i].get('Currency'))
        accountDetail['Name of the account'][i] = self.enterAccountName(accountDetail.loc[i].get('Name of the account'))
        # accountDetail.loc[i]['Name of the account'] = Accountname
        accountDetail['Account number'][i] = self.enterAccountNumber(accountDetail.loc[i].get('Account number'))
        # accountDetail.loc[i]['Account number'] = Accountnumber
        self.selectCountry(accountDetail.loc[i].get('Country'))
        # inputCustomerTest.df_accounts = accountDetail
        return accountDetail

    def clickOnParentAccountToAddChild(self, parent):
        try:
            self.wait_for_page_load(5)
            self.elementClick(self.folder, locatorType="xpath" )
            self.elementClick(self.lnkCustomerName.format(parent),
                               locatorType="xpath" )
            self.waitForElement(self.addChildCustomer.format(parent))
            self.elementClick( self.addChildCustomer.format(parent),
                               locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while filling address details. :: " )

    def createAccountHierarchy(self, Accountlists):
        try:
            # toReturn = ''
            # for key, value in Accountlists.items():
            #     if type( value ) is list:
            #         count = len( value )
            #         i = 0
            #         while count > 0:
            #             toReturn = key
            #             self.clickOnParentAccountToAddChild(key)
            #             self.createAccount(value[i])
            #             i += 1
            #             count -= 1
            # self.wait_for_page_load(4)

            #Below code is for Excel sheet
            for i in range(len(Accountlists)):
                if Accountlists.loc[i]['Parent'] != '':
                    self.clickOnParentAccountToAddChild(Accountlists.loc[i]['Parent'])
                data = self.createAccount(Accountlists,i)
        except Exception as e:
            self.log.error("Error occurred while creating AccountHierarchy. :: ")
        return data

    def createAccount(self, accountDetails, i):
        try:
            data = self.fill_Account_Details(accountDetails, i)
            self.clickOnSuccessAccountButton()
        except Exception as e:
            self.log.error("Error occurred while in the createAccount. :: ")
        return data

    def activateAccount(self, accountDetails):
        try:
            self.elementClick( self.btnSendForActivation, locatorType="xpath" )
            self.waitForElement( self.chkboxChooseBranchForApproval,format(accountDetails))
            self.elementClick( self.chkboxChooseBranchForApproval.format(accountDetails),
                               locatorType="xpath" )
            self.elementClick( self.btnSend, locatorType="xpath" )
        except Exception as e:
            self.log.error("Unable to activate account :: ")
