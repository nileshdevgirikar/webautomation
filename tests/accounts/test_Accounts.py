import unittest
import pytest
from pages.common.LoginPage import LoginPage
from pages.common.HomePage import HomePage
from pages.customer.Customer import Customer
from pages.customer.RootCustomer import RootCustomer
from pages.customer.Company import Company
from pages.accounts.Accounts import Accounts
from pages.accounts.Transactions import Transactions
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
        self.transaction = Transactions(self.driver)

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
        self.account.createAccountHierarchy(accountList)
        self.account.activateAccount(accountList.loc[0]['Name of the account'])
        self.home.userLogout()


    @pytest.mark.Smoke
    def test_CAMT053CreditDebitProcessingWithCorrectPrtrycodeAndPublishedVA(self):
        self.login.loginToApplication( ApplicationConfig.get( 'UserId' ), ApplicationConfig.get( 'Password' ) )
        # self.home.verifyWelcomeMessage(ApplicationConfig.get('firstname'))

        self.home.navigateToRootCustomers()
        self.rootCustomer.clickOnAddRootCustomerButton()
        companyList = inputCustomerTest.df_Singlecustomer
        self.company.createCustomerHierarchy(companyList)
        self.company.activateCustomer(companyList.loc[0]['Subentity'])
        self.home.navigateToAccounts()
        self.account.clickOnAddRootAccountButton()
        accountList = inputCustomerTest.df_accounts
        data = self.account.createAccountHierarchy(accountList)
        self.account.activateAccount(accountList.loc[0]['Name of the account'])

        shadowAccount = ""
        for i in range(len(accountList)):

            if accountList.loc[i]['TransactionPosting'] == 'RealAccount':
                shadowAccount = accountList.loc[i].get('Account number')
            if shadowAccount !='' and accountList.loc[i]['TransactionPosting'] != '' \
                    and accountList.loc[i]['TransactionPosting'] != 'RealAccount':
                transactionAccount = accountList.loc[i].get('Account number')
                self.camtFile.generateCAMT053(shadowAccount,
                                      accountList.loc[i].get('Account number'),
                                      inputAccountCashManagementTest.camtinput)
                self.camtFile.ftpCAMT053Files()
                self.camtFile.generateCAMT053(shadowAccount,
                                      accountList.loc[i].get('Account number'),
                                      inputAccountCashManagementTest.camtinput)
                self.camtFile.ftpCAMT053Files()

                self.transaction.navigateToTransactions()

                self.nonExceptionCount = self.transaction.verifyTransationsOnUI(inputAccountCashManagementTest.camtinput,
                                                                   accountList.loc[i].get('Account number'))

        print("Successfully")
        self.home.userLogout()
