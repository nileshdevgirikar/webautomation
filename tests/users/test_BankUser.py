import unittest
import pytest
from resources import config
from pages.common.LoginPage import LoginPage
from pages.common.HomePage import HomePage
from pages.customer.Customer import Customer
from pages.customer.RootCustomer import RootCustomer
from pages.accounts.Accounts import Accounts
from pages.customer.Company import Company
from pages.users.Users import Users
from Utilities.teststatus import TestStatus
from inputTestData import inputCustomerTest
from resources.config import ApplicationConfig
import Utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp")
class BankUserTest( unittest.TestCase ):
    log = cl.customLogger( logging.INFO )

    @pytest.fixture( autouse=True )
    def classSetup(self, oneTimeSetUp):
        self.login = LoginPage( self.driver )
        self.rootCustomer = RootCustomer( self.driver )
        self.home = HomePage( self.driver )
        self.ct = Customer( self.driver )
        self.account = Accounts( self.driver )
        self.company = Company( self.driver )
        self.bankUser = Users( self.driver )
        self.status = TestStatus( self.driver )

    @pytest.mark.smoke
    def test_CreateBankUsers_And_ViewUsers(self):
        self.login.loginToApplication(ApplicationConfig.get('BANKADMIN_USERID'),
                                      ApplicationConfig.get('BANKADMIN_PASSWORD'))
        # self.home.verifyWelcomeMessage( ApplicationConfig.get( 'UserId' ) )
        self.home.navigateToAdmin()
        userList = inputCustomerTest.df_BankUsers
        self.UsersABO = self.bankUser.createUsers(userList.loc[0])
        # print(self.UsersABO)
        self.bankUser.searchUser(self.UsersABO)
        result = self.bankUser.verifyAdminUserDetails(self.UsersABO)
        self.status.mark(result, "Incorrect Match")
        self.home.userLogout()
        self.login.loginToApplication(self.UsersABO.get('User ID'), self.UsersABO.get('Password'))
        result = self.home.verifyWelcomeMessage(self.UsersABO.get('First name'))
        self.status.mark(result, "Incorrect Match")
        self.home.userLogout()
        self.status.markFinal("test_CreateBankAdminUser_And_ViewUser", result, "Verification is Successful")

    @pytest.mark.smoke
    def test_CreateCustUsers_And_ViewUsers(self):
        self.login.loginToApplication(ApplicationConfig.get('BANKADMIN_USERID'),
                                      ApplicationConfig.get('BANKADMIN_PASSWORD'))
        #self.home.verifyWelcomeMessage( ApplicationConfig.get( 'UserId' ) )
        self.home.navigateToAdmin()
        userList = inputCustomerTest.df_CustUsers
        self.UsersABO = self.bankUser.createUsers(userList.loc[0])
        # print(self.UsersABO)
        self.bankUser.searchUser( self.UsersABO )
        result = self.bankUser.verifyAdminUserDetails( self.UsersABO )
        self.status.mark( result, "Incorrect Match" )
        self.home.userLogout()
        self.login.loginToApplication( self.UsersABO.get( 'User ID' ), self.UsersABO.get( 'Password' ) )
        result = self.home.verifyWelcomeMessage( self.UsersABO.get( 'First name' ) )
        self.status.mark(result, "Incorrect Match")
        self.home.userLogout()
        self.status.markFinal("test_CreateBankAdminUser_And_ViewUser", result, "Verification is Successful" )
