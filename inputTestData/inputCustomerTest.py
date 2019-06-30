import pandas as pd
import os
import xlrd
from Utilities.util import Util
from resources import config

# df_cus = pd.read_csv(os.environ.get('myHome') + 'inputTestData/customerheirarchy.csv')
parentPath = os.environ.get('myHome')
df_customer = pd.read_excel(open(parentPath + 'inputTestData/customerheirarchy.xlsx', 'rb'),
                            sheet_name='customerheirarchy', encoding='utf-8-sig')

df_Singlecustomer = pd.read_excel(open(parentPath + 'inputTestData/customerheirarchy.xlsx', 'rb'),
                                  sheet_name='SingleCustomer', encoding='utf-8-sig')

df_accounts = pd.read_excel(open(parentPath + 'inputTestData/Accounts.xlsx', 'rb'),
                            sheet_name='AccountHeirarchy', encoding='utf-8-sig')

df_users = pd.read_excel(open(parentPath + 'inputTestData/Accounts.xlsx', 'rb'),
                            sheet_name='Users', encoding='utf-8-sig')

df_Template = pd.read_excel(open(parentPath + 'inputTestData/Accounts.xlsx', 'rb'),
                            sheet_name='Template', encoding='utf-8-sig')

df_users.fillna('',inplace=True)
df_Singlecustomer.fillna('',inplace=True)
df_accounts.fillna('',inplace=True)
df_customer.fillna('',inplace=True)
df_Template.fillna('', inplace=True)


def customerDetails(df):
    newName = df_Singlecustomer['Customer Id'] + Util.get_unique_number(10)
    df_Singlecustomer['Customer Id'] = newName
    df_Singlecustomer['Name'] = df_Singlecustomer['Name'] + newName
    df_Singlecustomer['PreferredName'] = df_Singlecustomer['PreferredName'] + newName
    return df_Singlecustomer


customerDetails(df_Singlecustomer)

nameofCustomer = df_Singlecustomer['Name'][0]


def customerDetails(df):
    for i, row in df.iterrows():
        newName = df_customer['Customer Id'] + Util.get_unique_number(10)
        df_customer['Customer Id'][i] = newName
        return df_customer


customerDetails(df_customer)
print(df_customer)

print(nameofCustomer)


def accountsDetails(df):
    for name in range(len(df['Name of the account'])):
        newName = df['Name of the account'][name] + Util.get_unique_number(10)
        for parent in range(len(df['Parent'])):
            if df['Parent'][parent] == df['Name of the account'][name]:
                df['Parent'][parent] = newName
        df['Name of the account'][name] = newName
    return df


accountsDetails(df_accounts)

def createDuplicate(row):
    df = df_accounts[df_accounts['Parent'] == row]
    df = df.reset_index()
    del df['index']
    df.loc[0]['Name of the account'] = 'VTA' + Util.get_unique_number(10)
    return df


nameofAggregationAccounts = list(df_accounts[df_accounts['Account type'] == 'Internal Aggregation Account']
                                 ['Name of the account'])

ShadowAccountNumber = list(df_accounts[df_accounts['Account type'] == 'External Shadow']['Account number'])

camtinput = {
    'txsSummry': 'No',
    'txs_Credit': 0,
    'txs_Debit': 0,
    'multipleTxn': 'Yes',
    'ntry_Credit': 2,
    'ntry_Debit': 0,
    'ntry_Credit_Amt': 1.00,
    'ntry_Debit_Amt': 20000.00
}

parentPath = os.environ.get('myHome')
sheet = 'Smoke'


def checkRunMode(testName):
    df_ModuleExecution = pd.read_excel(open(parentPath + 'inputTestData/ModuleExecution.xlsx', 'rb'),
                                       sheet_name=sheet, encoding='utf-8-sig')
    temp_ModuleExecution = df_ModuleExecution[df_ModuleExecution['TestCases'] == testName]
    temp_ModuleExecution = temp_ModuleExecution.reset_index()
    del temp_ModuleExecution['index']
    if str(temp_ModuleExecution['Runmode'][0]).lower() == 'yes':
        return True
    else:
        return False

# print(df_accounts)
