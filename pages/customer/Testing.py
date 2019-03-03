# # from ABO.customer.CustomerABO import CustomerABO
# # from Utilities.util import Util
# # from base.BasePage import BasePage
# # import Utilities.custom_logger as cl
# # import logging
# # from pages.customer.Customer import Customer
# # import time
from ctypes import c_bool

from inputTestData import inputCustomerTest
from inputTestData import inputAccountCashManagementTest

#
# # class Company(Customer):
# #     log = cl.customLogger(logging.DEBUG)
# #
# #     def __init__(self, driver):
# #         super().__init__( driver )
# #         self.driver = driver
# #
# #     # Locators
# #     lnkCustomerName = "//span[contains(text(),'{0}')]"
# #     addChildCustomer = "//span[text()='{0}']/following-sibling::div[@class='level-item-actions ng-star-inserted']]"
# #
# #     btnPlusIcon = "//app-icon[@iconname='plus']"
#
company = inputCustomerTest.companyList

# def createCustomerHierarchy():
# keyvalue=''
# def recurssive(company,keyvalue):
#     if type(company) is dict:
#         for key,value in company.items():
#             fill = inputCustomerTest.rootCustomer
#             fill['Name'] = str( key )
#             print( fill )
#             keyvalue = key
#             recurssive(value,keyvalue)
#     elif type(company) is str:
#         fill = inputCustomerTest.rootCustomer
#         fill['Name'] = str( company )
#         print( fill )
#     elif type(company) is list:
#         for item in company:
#             print( keyvalue )
#             recurssive(item,keyvalue)
#
# recurssive(company,keyvalue)

Account = inputAccountCashManagementTest.AccountList


def SelectAccountType(company):
    # print(company)
    if ('RootAccount' in str( company )):
        fill = inputAccountCashManagementTest.RootAccount
        print( fill )
    elif ('ShadowAccount' in str( company )):
        fill = inputAccountCashManagementTest.ShadowAccount
        print( fill )
    elif ('SummaryAccount' in str( company )):
        fill = inputAccountCashManagementTest.SummaryAccount
        print( fill )
    elif ('Transaction' in str( company )):
        fill = inputAccountCashManagementTest.Transaction
        print( fill )


keyvalue = ''


def recurssive1(company, keyvalue):
    if type( company ) is dict:
        for key, value in company.items():
            keyvalue = key
            SelectAccountType( key )

            # print(keyvalue)
            recurssive1( value, keyvalue )
    elif type( company ) is str:
        # print( keyvalue )
        SelectAccountType( company )
    elif type( company ) is list:
        for item in company:
            print( keyvalue )
            recurssive1( item, keyvalue )


recurssive1( Account, keyvalue )
