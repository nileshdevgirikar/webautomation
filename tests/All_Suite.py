import unittest
import pytest
import HtmlTestRunner
import os
from inputTestData import inputCustomerTest
from tests.customer.test_Customer import TestCustomer
from tests.accounts.test_Accounts import TestAccounts

reportpath = os.environ.get('myHome') + 'executionReport'

suite = unittest.TestSuite()
suite.addTest(TestAccounts("test_trialclosed_account_in_hierarchy"))
suite.addTest(TestCustomer("test_CreateSingleRootCustomer"))
# unittest.TextTestRunner().run(suite)

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# testNames = ["TestCustomer.test_CreateSingleRootCustomer"]
#
# loader = unittest.TestLoader()
# suite = loader.loadTestsFromNames( testNames , TestCustomer)
#
#
# runner = unittest.TextTestRunner(verbosity=2)
# results = runner.run( suite )


# class MyTest( unittest.TestCase ):
#
#     suite = unittest.TestSuite()
#     suite.addTest(TestAccounts('test_trialclosed_account_in_hierarchy'))
#     suite.addTest(TestCustomer('test_CreateSingleRootCustomer'))
#     # unittest.TextTestRunner().run(suite)
#
#     runner = unittest.TextTestRunner()
#     runner.run(suite)

# test_cases = ('test_CreateSingleRootCustomer')
#
# def load_tests(loader, tests, pattern):
#     suite = unittest.TestSuite()
#     for test_class in test_cases:
#         tests = loader.loadTestsFromTestCase(test_class)
#         suite.addTests(tests)
#     return suite


# import sys
# from tests.customer.test_Customer import TestCustomer
#
# PACKAGE_ROOT_DIRECTORY = os.path.dirname( os.path.realpath( __file__ ) )
# start_dir = os.path.join( PACKAGE_ROOT_DIRECTORY, 'testing' )
#
#
# testNames = ["TestCustomer.test_CreateSingleRootCustomer"]
#
# loader = unittest.TestLoader()
# # suite = unittest.TestSuite()
# # suite.addTest(TestCustomer("test_CreateSingleRootCustomer"))
# suite = loader.loadTestsFromNames( testNames )
#
# runner = unittest.TextTestRunner(verbosity=2)
# results = runner.run( load_tests )
