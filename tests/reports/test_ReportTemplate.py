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
from pages.reports.Template import Template
from pages.reports.Reports import Reports
from Utilities.teststatus import TestStatus
from inputTestData import inputCustomerTest
from resources.config import ApplicationConfig
import Utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "SetUp")
class ReportsTest(unittest.TestCase):
    log = cl.customLogger(logging.INFO)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.login = LoginPage(self.driver)
        self.rootCustomer = RootCustomer(self.driver)
        self.home = HomePage(self.driver)
        self.account = Accounts(self.driver)
        self.company = Company(self.driver)
        self.reports = Reports(self.driver)
        self.template = Template(self.driver)
        self.status = TestStatus(self.driver)

    @pytest.mark.smoke
    def test_CreateReportTemplate(self):
        self.login.loginToApplication(ApplicationConfig.get('UserId'), ApplicationConfig.get('Password'))
        # self.home.verifyWelcomeMessage( ApplicationConfig.get( 'UserId' ) )
        self.home.navigateToReports()
        self.template.navigateToTemplate()
        # self.reports.clickOnButton()
        templateinfo = inputCustomerTest.df_Template
        # self.template.createReportTemplate(templateinfo)
        self.reports.setAccessFilter(templateinfo)
        self.home.userLogout()
        print('TTTTTTTT')
