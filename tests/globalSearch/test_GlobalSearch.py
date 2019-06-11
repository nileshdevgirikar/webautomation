import unittest
import pytest
from resources import config
from base.TestParams import TestParams
from pages.common.LoginPage import LoginPage
from pages.common.HomePage import HomePage
from pages.customer.Customer import Customer
from pages.customer.RootCustomer import RootCustomer
from pages.accounts.Accounts import Accounts
from pages.customer.Company import Company
from pages.globalSearch.GlobalSearch import GlobalSearch
from Utilities.teststatus import TestStatus
from inputTestData import inputCustomerTest
from resources.config import ApplicationConfig
import Utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "SetUp")
class GlobalSearchTest(unittest.TestCase):
    log = cl.customLogger(logging.INFO)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.login = LoginPage(self.driver)
        self.rootCustomer = RootCustomer(self.driver)
        self.home = HomePage(self.driver)
        self.account = Accounts(self.driver)
        self.company = Company(self.driver)
        self.globalSearch = GlobalSearch(self.driver)
        self.status = TestStatus(self.driver)

    @pytest.mark.smoke
    def test_searchCustomerAndClick(self):
        result = False
        self.login.loginToApplication(ApplicationConfig.get('UserId'), ApplicationConfig.get('Password'))
        # self.home.verifyWelcomeMessage( ApplicationConfig.get( 'UserId' ) )
        # self.status.mark(result, "Incorrect match")
        self.home.navigateToRootCustomers()
        # self.rootCustomer.clickOnAddRootCustomerButton()
        companyList = inputCustomerTest.df_Singlecustomer
        # self.company.createCustomerHierarchy(companyList)
        # self.home.navigateToRootCustomers()
        customerName = companyList['Subentity'][0]
        customerName = '01PKTESTCUST'
        self.globalSearch.searchAccountOrCustomerAndClick(self.home.labelsOnUI['GlobalSearchType_Company'],
                                                          customerName)
        self.home.verifyRootCustomerLabelOnCompanyPage(customerName)
        self.overview.verifyCustomerDetails(companyList)
        print('TTTTTTTT')
