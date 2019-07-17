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
from pages.customer.CustomerOverview import CustomerOverview
from resources.config import ApplicationConfig
from Utilities.teststatus import TestStatus
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
        self.customer = Customer(self.driver)
        self.account = Accounts( self.driver )
        self.company = Company( self.driver )
        self.globalSearch = GlobalSearch(self.driver)
        self.overview = CustomerOverview(self.driver)

    # @pytest.mark.Smoke
    # @pytest.mark.run(order=1)
    # def test_navigation(self):
    #     # if inputCustomerTest.checkRunMode('test_navigation') == True:
    #     # TestCustomer.classSetup()
    #     self.login.loginToApplication(ApplicationConfig['UserId'], ApplicationConfig['Password'])
    #     self.home.verifyWelcomeMessage(ApplicationConfig['UserId'])
    #     self.home.navigateToRootCustomers()
    #     self.rootCustomer.verifyTextonRootCustomer()

    @pytest.mark.run(order=2)
    def test_CreateSingleRootCustomer(self):
        self.status = TestStatus(self.driver)
        # if inputCustomerTest.checkRunMode('test_CreateSingleRootCustomer') == True:
        # TestCustomer.classSetup()
        self.login.loginToApplication(ApplicationConfig['UserId'], ApplicationConfig['Password'])
        self.home.verifyWelcomeMessage(ApplicationConfig['UserId'])
        self.home.navigateToRootCustomers()
        self.rootCustomer.clickOnAddRootCustomerButton()
        companyList = inputCustomerTest.df_Singlecustomer
        self.company.createCustomerHierarchy(companyList)
        self.company.activateCustomer(inputCustomerTest.nameofCustomer )
        # self.globalSearch.searchAccountOrCustomerAndClick("RC2932065044",
        #                                                   self.home.labelsOnUI['GlobalSearchType_Company'])
        result = self.overview.verifyCustomerDetails(inputCustomerTest.df_Singlecustomer)
        self.status.markFinal("test_CreateSingleRootCustomer", result, "Verification is Successful")

    # @pytest.mark.Smoke
    # @pytest.mark.run(order=3)
    # def test_createCustomerHierarchy(self):
    #     # if inputCustomerTest.checkRunMode('test_createCustomerHierarchy') == True:
    #     # self.classSetup()
    #     self.login.loginToApplication(ApplicationConfig['UserId'], ApplicationConfig['Password'])
    #     # self.home.verifyWelcomeMessage( ApplicationConfig.get( 'UserId' ) )
    #     self.home.navigateToRootCustomers()
    #     self.rootCustomer.clickOnAddRootCustomerButton()
    #     companyList = inputCustomerTest.df_customer
    #     self.company.createCustomerHierarchy(companyList)
    #     self.company.activateCustomer(companyList.loc[0]['Subentity'])

    def test_editCorporateCustomerHappyFlow(self):
        self.status = TestStatus(self.driver)
        self.login.loginToApplication(ApplicationConfig['UserId'], ApplicationConfig['Password'])
        # self.home.verifyWelcomeMessage( ApplicationConfig.get( 'UserId' ) )
        self.globalSearch.searchAccountOrCustomerAndClick(inputCustomerTest.nameofCustomer,
                                                          self.home.labelsOnUI['GlobalSearchType_Company'])
        # self.globalSearch.searchAccountOrCustomerAndClick("RC2932065044",
        #                                                   self.home.labelsOnUI['GlobalSearchType_Company'])
        inputCustomerTest.set_details_for_customer_edit(inputCustomerTest.df_Editcustomer)
        self.overview.clickOnEditCustomerLink()
        self.customer.fillEditCustomerInformation(inputCustomerTest.df_Singlecustomer)
        self.customer.clickOnSaveChangesButton()
        # self.verifyMessageOnProgressBar()
        # inputCustomerTest.df_Singlecustomer.loc[:, 'Status'] = self.labelsOnUI['CustomerStatusValueToVarify']
        result = self.overview.verifyCustomerDetails(inputCustomerTest.df_Singlecustomer)
        self.status.mark(result, "Incorrect match")
        self.status.markFinal("test_editCorporateCustomerHappyFlow", result, "Verification is Successful")

    def test_verifyUnableToAddCustomerClientAllowCheckOn(self):
        self.status = TestStatus(self.driver)
        self.login.loginToApplication(ApplicationConfig['UserId'], ApplicationConfig['Password'])
        # self.home.verifyWelcomeMessage( ApplicationConfig.get( 'UserId' ) )
        # self.globalSearch.searchAccountOrCustomerAndClick(inputCustomerTest.nameofCustomer,
        #                                                       self.home.labelsOnUI['GlobalSearchType_Company'])
        self.globalSearch.searchAccountOrCustomerAndClick("TAutoCustomer953995",
                                                          self.home.labelsOnUI['GlobalSearchType_Company'])
        self.overview.clickOnEditCustomerLink()
        self.customer.disabledClientsallowed()
        self.customer.clickOnSaveChangesButton()
        self.customer.clickOnParentCustomerToAddChild("TAutoCustomer953995")
        self.customer.verifyElementIsEnabledOrDisabled()
