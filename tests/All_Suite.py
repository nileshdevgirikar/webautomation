from unittest import TestLoader, TestSuite, TextTestRunner
import pytest
import HtmlTestRunner
import os
from inputTestData import inputCustomerTest
from tests.customer.test_Customer import TestCustomer
from tests.accounts.test_Accounts import TestAccounts
from tests.reports.test_ReportTemplate import ReportsTest

reportpath = os.environ.get('myHome') + 'executionReport'

if __name__ == '__main__':
    loader = TestLoader()
    suite = TestSuite()

    # suite = unittest.TestSuite()
    suite.addTest(TestAccounts("test_trialclosed_account_in_hierarchy"))
    suite.addTest(TestCustomer("test_CreateSingleRootCustomer"))
    suite.addTest(ReportsTest('test_create_transaction_template_and_report'))
    # unittest.TextTestRunner().run(suite)

    runner = TextTestRunner(verbosity=2)
    result = runner.run(suite)
