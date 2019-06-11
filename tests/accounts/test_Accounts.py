import unittest
import pytest
from pages.common.LoginPage import LoginPage
from pages.common.HomePage import HomePage
from pages.customer.Customer import Customer
from pages.customer.RootCustomer import RootCustomer
from pages.customer.Company import Company
from pages.accounts.Accounts import Accounts
from pages.accounts.Transactions import Transactions
from pages.globalSearch.GlobalSearch import GlobalSearch
from pages.accounts.AccountOverview import AccountOverview
from inputTestData import inputCustomerTest
from inputTestData import inputAccountCashManagementTest
from Utilities.filegenerator.CAMT053FileProcessing import CAMT053FileProcessing
from resources.config import ApplicationConfig
from Utilities.teststatus import TestStatus


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
        self.globalSearch = GlobalSearch(self.driver)
        self.overview = AccountOverview(self.driver)
        self.status = TestStatus(self.driver)

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

    def test_create_account_hierarchy(self):
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

    def test_closed_account_in_hierarchy(self):
        self.login.loginToApplication(ApplicationConfig.get('UserId'), ApplicationConfig.get('Password'))
        # self.home.verifyWelcomeMessage(ApplicationConfig.get('firstname'))
        self.home.navigateToRootCustomers()
        self.rootCustomer.clickOnAddRootCustomerButton()
        companyList = inputCustomerTest.df_Singlecustomer
        self.company.createCustomerHierarchy(companyList)
        self.company.activateCustomer(companyList['Subentity'][0])
        self.home.navigateToAccounts()
        self.account.clickOnAddRootAccountButton()
        accountList = inputCustomerTest.df_accounts
        self.account.createAccountHierarchy(accountList)
        self.account.activateAccount(accountList[self.home.labelsOnUI['NameOfTheAccount']][0])
        self.globalSearch.searchAccountOrCustomerAndClick(inputCustomerTest.nameofAccounts[0])
        self.account.clickOnParentAccountToAddChild(inputCustomerTest.nameofAccounts[0])
        newAccountDetails = inputCustomerTest.createDuplicate(inputCustomerTest.nameofAccounts[0])
        self.account.fill_Account_Details(newAccountDetails, 0)
        self.account.clickOnSuccessAccountButton()
        self.account.activateAccount(newAccountDetails[self.home.labelsOnUI['NameOfTheAccount']][0])
        self.globalSearch.searchAccountOrCustomerAndClick(
            newAccountDetails[self.home.labelsOnUI['NameOfTheAccount']][0])
        self.overview.clickOnOptionsInActionTab(self.home.labelsOnUI['btnCloseAccount'])
        self.status.mark(self.overview.verifyClosedAccountFunctionality(), "Incorrect match")
        self.status.mark(self.account.verifyAccountStatus(self.home.labelsOnUI['custStatus_Closed']),
                         "Incorrect match")

        # self.camtFile.generateCAMT053(shadowAccount, newAccountDetails[self.home.labelsOnUI['NameOfTheAccount']][0],
        #                               inputAccountCashManagementTest.camtinput)
        # self.camtFile.ftpCAMT053Files()
        # self.camtFile.generateCAMT053(shadowAccount,
        #                               newAccountDetails[self.home.labelsOnUI['NameOfTheAccount']][0],
        #                               inputAccountCashManagementTest.camtinput)
        # self.camtFile.ftpCAMT053Files()

        self.home.userLogout()

    def test_delete_account_in_hierarchy(self):
        self.login.loginToApplication(ApplicationConfig.get('UserId'), ApplicationConfig.get('Password'))
        # self.home.verifyWelcomeMessage(ApplicationConfig.get('firstname'))
        self.home.navigateToRootCustomers()
        self.rootCustomer.clickOnAddRootCustomerButton()
        companyList = inputCustomerTest.df_Singlecustomer
        self.company.createCustomerHierarchy(companyList)
        self.company.activateCustomer(companyList['Subentity'][0])
        self.home.navigateToAccounts()
        self.account.clickOnAddRootAccountButton()
        accountList = inputCustomerTest.df_accounts
        self.account.createAccountHierarchy(accountList)
        self.account.activateAccount(accountList[self.home.labelsOnUI['NameOfTheAccount']][0])
        self.globalSearch.searchAccountOrCustomerAndClick(inputCustomerTest.nameofAccounts[0])
        self.account.clickOnParentAccountToAddChild(inputCustomerTest.nameofAccounts[0])
        newAccountDetails = inputCustomerTest.createDuplicate(inputCustomerTest.nameofAccounts[0])
        self.account.fill_Account_Details(newAccountDetails, 0)
        self.account.clickOnSuccessAccountButton()
        self.account.activateAccount(newAccountDetails[self.home.labelsOnUI['NameOfTheAccount']][0])
        self.globalSearch.searchAccountOrCustomerAndClick(
            newAccountDetails[self.home.labelsOnUI['NameOfTheAccount']][0])
        self.overview.clickOnOptionsInActionTab(self.home.labelsOnUI['btnDeleteAccount'])
        self.status.mark(self.overview.verifyDeleteAccountFunctionality(), "Incorrect match")
        self.globalSearch.searchAccountOrCustomerAndClick(
            newAccountDetails[self.home.labelsOnUI['NameOfTheAccount']][0])
        self.status.mark(self.home.is_text_present(self.home.labelsOnUI['NotMatchingMessage']), "Incorrect match")
        self.home.userLogout()

    def test_blocked_account_in_hierarchy(self):
        self.login.loginToApplication(ApplicationConfig.get('UserId'), ApplicationConfig.get('Password'))
        # self.home.verifyWelcomeMessage(ApplicationConfig.get('firstname'))
        self.home.navigateToRootCustomers()
        # self.rootCustomer.clickOnAddRootCustomerButton()
        # companyList = inputCustomerTest.df_Singlecustomer
        # self.company.createCustomerHierarchy(companyList)
        # self.company.activateCustomer(companyList['Subentity'][0])
        # self.home.navigateToAccounts()
        # self.account.clickOnAddRootAccountButton()
        # accountList = inputCustomerTest.df_accounts
        # self.account.createAccountHierarchy(accountList)
        # self.account.activateAccount(accountList[self.home.labelsOnUI['NameOfTheAccount']][0])
        # self.globalSearch.searchAccountOrCustomerAndClick(inputCustomerTest.nameofAccounts[0])
        # self.account.clickOnParentAccountToAddChild(inputCustomerTest.nameofAccounts[0])
        # newAccountDetails = inputCustomerTest.createDuplicate(inputCustomerTest.nameofAccounts[0])
        # self.account.fill_Account_Details(newAccountDetails,0)
        # self.account.clickOnSuccessAccountButton()
        # self.account.activateAccount(newAccountDetails[self.home.labelsOnUI['NameOfTheAccount']][0])
        self.globalSearch.searchAccountOrCustomerAndClick("VTA31604596088")
        self.overview.clickOnOptionsInActionTab(self.home.labelsOnUI['lblBlockAccountPopUp'])
        self.status.mark(self.overview.verifyAccountBlockedBasedOnInput(self.overview.blockedRadio),
                         "Incorrect match")
        self.overview.clickOnOptionsInActionTab(self.home.labelsOnUI['lblBlockAccountPopUp'])
        self.status.mark(self.overview.verifyAccountBlockedBasedOnInput(self.overview.blockedCreditRadio),
                         "Incorrect match")
        self.overview.clickOnOptionsInActionTab(self.home.labelsOnUI['lblBlockAccountPopUp'])
        self.status.mark(self.overview.verifyAccountBlockedBasedOnInput(self.overview.blockedDebitRadio),
                         "Incorrect match")
        self.overview.clickOnOptionsInActionTab(self.home.labelsOnUI['lblBlockAccountPopUp'])
        self.status.mark(self.overview.verifyAccountBlockedBasedOnInput(self.overview.notBlockedRadio),
                         "Incorrect match")
        result = self.account.verifyAccountStatus(self.home.labelsOnUI['custStatus_Blocked'])
        self.home.userLogout()

    def test_trialclosed_account_in_hierarchy(self):
        self.login.loginToApplication(ApplicationConfig.get('UserId'), ApplicationConfig.get('Password'))
        # self.home.verifyWelcomeMessage(ApplicationConfig.get('firstname'))
        self.home.navigateToRootCustomers()
        accountList = inputCustomerTest.df_accounts
        newAccountDetails = inputCustomerTest.createDuplicate(inputCustomerTest.nameofAccounts[0])
        self.globalSearch.searchAccountOrCustomerAndClick("Agg One7396800991")
        self.account.clickOnParentAccountToAddChild("Agg One7396800991")
        newAccountDetails = inputCustomerTest.createDuplicate(inputCustomerTest.nameofAccounts[0])
        self.account.fill_Account_Details(newAccountDetails, 0)
        self.account.clickOnSuccessAccountButton()
        self.account.activateAccount(newAccountDetails[self.home.labelsOnUI['NameOfTheAccount']][0])
        self.globalSearch.searchAccountOrCustomerAndClick(
            newAccountDetails[self.home.labelsOnUI['NameOfTheAccount']][0])
        self.overview.clickOnOptionsInActionTab(self.home.labelsOnUI['lblBlockAccountPopUp'])
        self.status.mark(self.overview.verifyAccountBlockedBasedOnInput(self.overview.blockedCreditRadio),
                         "Incorrect match")
        self.status.mark(self.account.verifyAccountStatus(self.home.labelsOnUI['custStatus_Blocked']),
                         "Incorrect match")

        self.camtFile.generateCAMT053("SHA60356703911796",
                                      newAccountDetails[self.home.labelsOnUI['NameOfTheAccount']][0],
                                      inputAccountCashManagementTest.camtinput)
        self.camtFile.ftpCAMT053Files()
        self.camtFile.generateCAMT053("SHA60356703911796",
                                      newAccountDetails[self.home.labelsOnUI['NameOfTheAccount']][0],
                                      inputAccountCashManagementTest.camtinput)
        self.camtFile.ftpCAMT053Files()

        self.home.userLogout()
