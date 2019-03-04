import unittest
import pytest
from pages.common.LoginPage import LoginPage
from pages.common.HomePage import HomePage
from pages.customer.Customer import Customer
from pages.customer.RootCustomer import RootCustomer
from pages.accounts.Accounts import Accounts
from pages.customer.Company import Company
from pages.users.Users import Users
from Utilities.teststatus import TestStatus
from inputTestData import inputUserTest
import Utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures( "oneTimeSetUp", "SetUp" )
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

    @pytest.mark.run( order=1 )
    def test_CreateBankUser(self):
        self.login.loginToApplication()
        # self.status.mark()
        self.home.verifyWelcomeMessage()
        self.home.navigateToAdmin()
        self.UsersABO = self.bankUser.createUsers( inputUserTest.updateUsersABO )
        self.bankUser.searchUser( self.UsersABO )
        result = self.bankUser.verifyUserDetails( self.UsersABO )
        self.login.loginToApplication( self.UsersABO.get( 'UserId' ), self.UsersABO.get( 'Password' ) )
        self.status.markFinal( "test_CreateBankUser", result, "Verification is Successful" )
