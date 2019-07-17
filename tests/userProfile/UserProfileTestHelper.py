import unittest
import pytest
from pages.common.LoginPage import LoginPage
from pages.common.HomePage import HomePage
from pages.customer.Customer import Customer
from pages.customer.RootCustomer import RootCustomer
from pages.accounts.Accounts import Accounts
from pages.customer.Company import Company
from inputTestData import userProfileTestData
from pages.globalSearch.GlobalSearch import GlobalSearch
from pages.customer.CustomerOverview import CustomerOverview
from resources.config import ApplicationConfig
from pages.users.Users import Users
from Utilities.teststatus import TestStatus
from inputTestData import inputCustomerTest


@pytest.mark.usefixtures("oneTimeSetUp")
class UserProfile(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.login = LoginPage(self.driver)
        self.rootCustomer = RootCustomer(self.driver)
        self.home = HomePage(self.driver)
        self.customer = Customer(self.driver)
        self.account = Accounts(self.driver)
        self.company = Company(self.driver)
        self.globalSearch = GlobalSearch(self.driver)
        self.overview = CustomerOverview(self.driver)
        self.bankUser = Users(self.driver)
        self.status = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_createAllBankUsers(self):
        self.login.loginToApplication(ApplicationConfig.get('BANKADMIN_USERID'),
                                      ApplicationConfig.get('BANKADMIN_PASSWORD'))
        self.home.verifyWelcomeMessage(ApplicationConfig.get('BANKADMIN_USERID'))
        self.home.navigateToAdmin()
        self.bankUser.createUsers(userProfileTestData.df_BankAdmin)
        self.bankUser.searchUser(userProfileTestData.df_BankAdmin[self.home.labelsOnUI['UserID']][0])
        result = self.bankUser.verifyDetails(userProfileTestData.df_BankAdmin)
        self.status.mark(result, "Incorrect Match")

    @pytest.mark.run(order=1)
    def test_bank_admin_user_able_to_create_all_bankusers(self):
        self.login.loginToApplication(ApplicationConfig.get('BANKADMIN_USERID'),
                                      ApplicationConfig.get('BANKADMIN_PASSWORD'))
        self.home.verifyWelcomeMessage(ApplicationConfig.get('BANKADMIN_USERID'))
        self.home.navigateToAdmin()
        self.status.mark(self.bankUser.verifyAddUserButtonNotDisplayed(), "Incorrect Match")

        self.bankUser.createUsers(userProfileTestData.df_BankRead)
        self.bankUser.searchUser(userProfileTestData.df_BankRead[self.home.labelsOnUI['UserID']][0])
        result = self.bankUser.verifyDetails(userProfileTestData.df_BankRead)
        self.status.mark(result, "Incorrect Match")

        self.bankUser.createUsers(userProfileTestData.df_BankUpdate)
        self.bankUser.searchUser(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0])
        result = self.bankUser.verifyDetails(userProfileTestData.df_BankUpdate)
        self.status.mark(result, "Incorrect Match")
        self.home.userLogout()
        self.status.markFinal("test_bank_admin_user_able_to_create_all_bankusers", result, "Verification is Successful")

    @pytest.mark.run(order=2)
    def test_bank_update_user_not_able_to_create_bankusers(self):
        self.login.loginToApplication(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0],
                                      userProfileTestData.df_BankUpdate[self.home.labelsOnUI['Password']][0])
        self.home.verifyWelcomeMessage(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0])
        self.home.navigateToAdmin()
        result = self.bankUser.verifyAddUserButtonNotDisplayed()
        self.status.mark(result, "Incorrect Match")
        self.status.markFinal("test_bank_update_user_not_able_to_create_all_bankusers", result,
                              "Verification is Successful")

    @pytest.mark.run(order=2)
    def test_bank_update_user_able_to_view_all_bankusers_details(self):
        self.login.loginToApplication(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0],
                                      userProfileTestData.df_BankUpdate[self.home.labelsOnUI['Password']][0])
        self.home.verifyWelcomeMessage(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0])
        self.home.navigateToAdmin()
        # For Bank admin user
        self.bankUser.searchUser(userProfileTestData.df_BankAdmin[self.home.labelsOnUI['UserID']][0])
        self.bankUser.clickOnViewUserlink(userProfileTestData.df_BankAdmin[self.home.labelsOnUI['UserID']][0])
        result = self.bankUser.verifyDetails(userProfileTestData.df_BankAdmin)
        self.status.mark(result, "Incorrect Match")
        # For Bank Update user
        self.bankUser.searchUser(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0])
        self.bankUser.clickOnViewUserlink(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0])
        result = self.bankUser.verifyDetails(userProfileTestData.df_BankUpdate)
        self.status.mark(result, "Incorrect Match")
        # For Bank Read user
        self.bankUser.searchUser(userProfileTestData.df_BankRead[self.home.labelsOnUI['UserID']][0])
        self.bankUser.clickOnViewUserlink(userProfileTestData.df_BankRead[self.home.labelsOnUI['UserID']][0])
        result = self.bankUser.verifyDetails(userProfileTestData.df_BankRead)
        self.status.mark(result, "Incorrect Match")
        self.status.markFinal("test_bank_update_user_able_to_view_all_bankusers_details", result,
                              "Verification is Successful")

    @pytest.mark.run(order=2)
    def test_bank_update_user_able_to_create_root_customer(self):
        self.login.loginToApplication(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0],
                                      userProfileTestData.df_BankUpdate[self.home.labelsOnUI['Password']][0])
        self.home.verifyWelcomeMessage(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0])
        self.home.navigateToRootCustomers()
        self.rootCustomer.clickOnAddRootCustomerButton()
        self.company.createCustomerHierarchy(inputCustomerTest.df_Singlecustomer)
        self.company.activateCustomer(inputCustomerTest.nameofCustomer)
        result = self.overview.verifyCustomerDetails(inputCustomerTest.df_Singlecustomer)
        self.status.markFinal("test_bank_update_user_able_to_create_root_customer_trail", result,
                              "Verification is Successful")

    @pytest.mark.run(order=2)
    def test_bank_update_user_able_to_create_all_customer_users(self):
        # self.login.loginToApplication(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0],
        #                               userProfileTestData.df_BankUpdate[self.home.labelsOnUI['Password']][0])
        # self.home.verifyWelcomeMessage(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0])
        self.login.loginToApplication(ApplicationConfig['BANKADMIN_USERID'],
                                      ApplicationConfig['BANKADMIN_PASSWORD'])
        self.home.verifyWelcomeMessage(ApplicationConfig['BANKADMIN_USERID'])
        self.home.navigateToRootCustomers()
        self.globalSearch.searchAccountOrCustomerAndClick("TALinæRC5582478236",
                                                          self.home.labelsOnUI['GlobalSearchType_Company'])
        self.company.navigateToUser()
        # For Cust admin user
        self.bankUser.createUsers(userProfileTestData.df_CustAdmin)
        self.bankUser.searchUser(userProfileTestData.df_CustAdmin[self.home.labelsOnUI['UserID']][0])
        self.bankUser.clickOnViewUserlink(userProfileTestData.df_CustAdmin[self.home.labelsOnUI['UserID']][0])
        result = self.bankUser.verifyDetails(userProfileTestData.df_CustAdmin)
        # For Cust Update user
        self.bankUser.createUsers(userProfileTestData.df_CustAdmin)
        self.bankUser.searchUser(userProfileTestData.df_CustUpdate[self.home.labelsOnUI['UserID']][0])
        self.bankUser.clickOnViewUserlink(userProfileTestData.df_CustUpdate[self.home.labelsOnUI['UserID']][0])
        result = self.bankUser.verifyDetails(userProfileTestData.df_CustUpdate)
        # For Cust Read user
        self.bankUser.createUsers(userProfileTestData.df_CustRead)
        self.bankUser.searchUser(userProfileTestData.df_CustRead[self.home.labelsOnUI['UserID']][0])
        self.bankUser.clickOnViewUserlink(userProfileTestData.df_CustRead[self.home.labelsOnUI['UserID']][0])
        result = self.bankUser.verifyDetails(userProfileTestData.df_CustRead)

        self.status.markFinal("test_bank_update_user_able_to_create_all_customer_users", result,
                              "Verification is Successful")

    @pytest.mark.run(order=2)
    def test_bank_update_user_able_to_create_all_customer_users_trail(self):
        # self.login.loginToApplication(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0],
        #                               userProfileTestData.df_BankUpdate[self.home.labelsOnUI['Password']][0])
        # self.home.verifyWelcomeMessage(userProfileTestData.df_BankUpdate[self.home.labelsOnUI['UserID']][0])
        self.login.loginToApplication(ApplicationConfig['BANKADMIN_USERID'],
                                      ApplicationConfig['BANKADMIN_PASSWORD'])
        self.home.verifyWelcomeMessage(ApplicationConfig['BANKADMIN_USERID'])
        self.home.navigateToRootCustomers()
        self.globalSearch.searchAccountOrCustomerAndClick("TALinæRC5582478236",
                                                          self.home.labelsOnUI['GlobalSearchType_Company'])

        self.company.navigateToUser()
        # For Cust admin user
        self.bankUser.createUsers(userProfileTestData.df_CustAdmin)
        self.bankUser.searchUser(userProfileTestData.df_CustAdmin[self.home.labelsOnUI['UserID']][0])
        self.bankUser.clickOnViewUserlink(userProfileTestData.df_CustAdmin[self.home.labelsOnUI['UserID']][0])
        result = self.bankUser.verifyDetails(userProfileTestData.df_CustAdmin)
        # For Cust Update user
        self.bankUser.createUsers(userProfileTestData.df_CustUpdate)
        self.bankUser.searchUser(userProfileTestData.df_CustUpdate[self.home.labelsOnUI['UserID']][0])
        self.bankUser.clickOnViewUserlink(userProfileTestData.df_CustUpdate[self.home.labelsOnUI['UserID']][0])
        result = self.bankUser.verifyDetails(userProfileTestData.df_CustUpdate)
        # For Cust Read user
        self.bankUser.createUsers(userProfileTestData.df_CustRead)
        self.bankUser.searchUser(userProfileTestData.df_CustRead[self.home.labelsOnUI['UserID']][0])
        self.bankUser.clickOnViewUserlink(userProfileTestData.df_CustRead[self.home.labelsOnUI['UserID']][0])
        result = self.bankUser.verifyDetails(userProfileTestData.df_CustRead)

        self.status.markFinal("test_bank_update_user_able_to_create_root_customer_trail", result,
                              "Verification is Successful")
