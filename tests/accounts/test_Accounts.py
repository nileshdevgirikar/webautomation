import unittest
import pytest
from pages.common.LoginPage import LoginPage
from pages.common.HomePage import HomePage
from pages.customer.Customer import Customer
from pages.customer.RootCustomer import RootCustomer
from pages.accounts.Accounts import Accounts
from pages.customer.Company import Company
from inputTestData import inputCustomerTest
from inputTestData import inputAccountCashManagementTest
from Utilities.filegenerator.CAMT053FileProcessing import CAMT053FileProcessing
from resources.config import ApplicationConfig


@pytest.mark.usefixtures( "oneTimeSetUp", "SetUp" )
class TestAccounts( unittest.TestCase ):

    @pytest.fixture( autouse=True )
    def classSetup(self, oneTimeSetUp):
        self.login = LoginPage( self.driver )
        self.rootCustomer = RootCustomer( self.driver )
        self.home = HomePage( self.driver )
        self.ct = Customer( self.driver )
        self.account = Accounts( self.driver )
        self.company = Company( self.driver )
        self.camtFile = CAMT053FileProcessing()

    @pytest.mark.Smoke
    # def test_CreateAccountHierarchy(self):
    #     self.login.loginToApplication(ApplicationConfig.get('UserId'), ApplicationConfig.get('Password'))
    #     # self.home.verifyWelcomeMessage(ApplicationConfig.get('firstname'))
    #     self.home.navigateToRootCustomers()
    #     self.rootCustomer.clickOnAddRootCustomerButton()
    #     companyList = inputCustomerTest.rootCustomer1
    #     self.company.createCustomerHierarchy(companyList, keyvalue='')
    #     self.company.activateCustomer(companyList)
    #     self.home.navigateToAccounts()
    #     self.account.clickOnAddRootAccountButton()
    #     AccountList = inputAccountCashManagementTest.Accountlists
    #     self.account.createAccount(inputAccountCashManagementTest.TopAcc1)
    #     self.account.createAccountHierarchy(AccountList)
    #     self.account.activateAccount(inputAccountCashManagementTest.TopAcc1)
    #     self.home.userLogout()

    def test_CreateAccountHierarchy(self):
        self.login.loginToApplication(ApplicationConfig.get('UserId'), ApplicationConfig.get('Password'))
        # self.home.verifyWelcomeMessage(ApplicationConfig.get('firstname'))
        self.home.navigateToRootCustomers()
        self.rootCustomer.clickOnAddRootCustomerButton()
        companyList = inputCustomerTest.df_Singlecustomer
        self.company.createCustomerHierarchy(companyList)
        self.company.activateCustomer(companyList.loc[0]['Subentity'])
        self.home.navigateToAccounts()
        self.account.clickOnAddRootAccountButton()
        accountList = inputCustomerTest.df_accounts
        # self.account.createAccount(inputAccountCashManagementTest.TopAcc1)
        self.account.createAccountHierarchy(accountList)
        # self.account.activateAccount(inputAccountCashManagementTest.TopAcc1)
        self.home.userLogout()


    @pytest.mark.Smoke
    def test_CAMT053CreditDebitProcessingWithCorrectPrtrycodeAndPublishedVA(self):
        self.login.loginToApplication( ApplicationConfig.get( 'UserId' ), ApplicationConfig.get( 'Password' ) )
        # self.home.verifyWelcomeMessage(ApplicationConfig.get('firstname'))
        self.home.navigateToRootCustomers()
        self.rootCustomer.clickOnAddRootCustomerButton()
        companyList = inputCustomerTest.rootCustomer1
        self.company.createCustomerHierarchy( companyList, keyvalue='' )
        self.company.activateCustomer( companyList )
        self.home.navigateToAccounts()
        self.account.clickOnAddRootAccountButton()
        AccountList = inputAccountCashManagementTest.Accountlistsforposting
        self.account.createAccount( inputAccountCashManagementTest.TopAcc1 )
        self.account.createAccountHierarchy( AccountList )
        self.account.activateAccount( inputAccountCashManagementTest.TopAcc1 )
        self.camtFile.generateCAMT053(inputAccountCashManagementTest.Shadow.get('Account number'),
                                      inputAccountCashManagementTest.TranAcc1.get('Account number'),
                                      inputAccountCashManagementTest.camtinput)
        self.camtFile.ftpCAMT053Files()
        self.camtFile.generateCAMT053(inputAccountCashManagementTest.Shadow.get('Account number'),
                                      inputAccountCashManagementTest.TranAcc1.get('Account number'),
                                      inputAccountCashManagementTest.camtinput)
        self.camtFile.ftpCAMT053Files()
        print("Successfully")
        self.home.userLogout()
