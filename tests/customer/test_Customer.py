import unittest
import pytest
from pages.common.LoginPage import LoginPage
from pages.common.HomePage import HomePage
from pages.customer.Customer import Customer
from pages.customer.RootCustomer import RootCustomer
from pages.accounts.Accounts import Accounts
from pages.customer.Company import Company
from inputTestData import inputCustomerTest
from pages.globalSearch.GlobalSearch import GlobalSearch
from resources.config import ApplicationConfig
import time
import xlrd
from resources import config
import os
import pandas as pd


@pytest.mark.usefixtures("oneTimeSetUp")
class TestCustomer(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.login = LoginPage( self.driver )
        self.rootCustomer = RootCustomer( self.driver )
        self.home = HomePage( self.driver )
        self.ct = Customer( self.driver )
        self.account = Accounts( self.driver )
        self.company = Company( self.driver )
        self.globalSearch = GlobalSearch(self.driver)

    @pytest.mark.Smoke
    @pytest.mark.run(order=1)
    def test_navigation(self):
        # if inputCustomerTest.checkRunMode('test_navigation') == True:
        # TestCustomer.classSetup()
        self.login.loginToApplication(ApplicationConfig['UserId'], ApplicationConfig['Password'])
        self.home.verifyWelcomeMessage(ApplicationConfig['UserId'])
        self.home.navigateToRootCustomers()
        self.rootCustomer.verifyTextonRootCustomer()

    @pytest.mark.run(order=2)
    def test_CreateSingleRootCustomer(self):
        # if inputCustomerTest.checkRunMode('test_CreateSingleRootCustomer') == True:
        # TestCustomer.classSetup()
        self.login.loginToApplication(ApplicationConfig['UserId'], ApplicationConfig['Password'])
        self.home.verifyWelcomeMessage(ApplicationConfig['UserId'])
        self.home.navigateToRootCustomers()
        self.rootCustomer.clickOnAddRootCustomerButton()
        companyList = inputCustomerTest.df_Singlecustomer
        self.company.createCustomerHierarchy(companyList)
        self.company.activateCustomer(inputCustomerTest.nameofCustomer )

    @pytest.mark.Smoke
    @pytest.mark.run(order=3)
    def test_createCustomerHierarchy(self):
        # if inputCustomerTest.checkRunMode('test_createCustomerHierarchy') == True:
        # self.classSetup()
        self.login.loginToApplication(ApplicationConfig['UserId'], ApplicationConfig['Password'])
        # self.home.verifyWelcomeMessage( ApplicationConfig.get( 'UserId' ) )
        self.home.navigateToRootCustomers()
        self.rootCustomer.clickOnAddRootCustomerButton()
        companyList = inputCustomerTest.df_customer
        self.company.createCustomerHierarchy(companyList)
        self.company.activateCustomer(companyList.loc[0]['Subentity'])
