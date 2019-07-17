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


def verify_bankupdateUser_not_able_to_create_bankusers(self):
    try:
        HomePage.navigateToAdmin(self)
        # self.home.navigateToAdmin()
        self.verify(self.users.verifyAddUserButtonNotDisplayed())
    except Exception as e:
        result = False
        self.log.error("Exception occurred while doing search users ::")
