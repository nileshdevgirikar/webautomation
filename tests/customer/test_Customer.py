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
import time
from resources.config import ApplicationConfig

@pytest.mark.usefixtures( "oneTimeSetUp", "SetUp" )
class TestCustomer( unittest.TestCase ):

    @pytest.fixture( autouse=True )
    def classSetup(self, oneTimeSetUp):
        self.login = LoginPage( self.driver )
        self.rootCustomer = RootCustomer( self.driver )
        self.home = HomePage( self.driver )
        self.ct = Customer( self.driver )
        self.account = Accounts( self.driver )
        self.company = Company( self.driver )

    @pytest.mark.Smoke
    def test_navigation(self):
        self.login.loginToApplication( ApplicationConfig.get( 'UserId' ), ApplicationConfig.get( 'Password' ) )
        self.home.verifyWelcomeMessage( ApplicationConfig.get( 'UserId' ) )
        self.home.navigateToRootCustomers()
        self.rootCustomer.verifyTextonRootCustomer()

    @pytest.mark.Smoke
    def test_CreateSingleRootCustomer(self):
        self.login.loginToApplication( ApplicationConfig.get( 'UserId' ), ApplicationConfig.get( 'Password' ) )
        self.home.verifyWelcomeMessage( ApplicationConfig.get( 'UserId' ) )
        self.home.navigateToRootCustomers()
        self.rootCustomer.clickOnAddRootCustomerButton()
        companyList = inputCustomerTest.rootCustomer1
        self.company.createCustomerHierarchy( companyList, keyvalue='' )
        self.company.activateCustomer( companyList )

    @pytest.mark.Smoke
    def test_createCustomerHierarchy(self):
        self.login.loginToApplication( ApplicationConfig.get( 'UserId' ), ApplicationConfig.get( 'Password' ) )
        self.home.verifyWelcomeMessage( ApplicationConfig.get( 'UserId' ) )
        self.home.navigateToRootCustomers()
        self.rootCustomer.clickOnAddRootCustomerButton()
        companyList = inputCustomerTest.companyList
        self.company.createCustomerHierarchy( companyList, keyvalue='' )
        self.company.activateCustomer( str( companyList.keys() )[12:-3] )
