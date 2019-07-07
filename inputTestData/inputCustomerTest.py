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

df_Editcustomer = pd.read_excel(open(parentPath + 'inputTestData/customerheirarchy.xlsx', 'rb'),
                                sheet_name='EditCustomer', encoding='utf-8-sig')

df_accounts = pd.read_excel(open(parentPath + 'inputTestData/Accounts.xlsx', 'rb'),
                            sheet_name='AccountHeirarchy', encoding='utf-8-sig')

df_BankUsers = pd.read_excel(open(parentPath + 'inputTestData/Users.xlsx', 'rb'),
                             sheet_name='BankUsers', encoding='utf-8-sig')

df_CustUsers = pd.read_excel(open(parentPath + 'inputTestData/Users.xlsx', 'rb'),
                             sheet_name='CustUsers', encoding='utf-8-sig')

df_TransactionTemplate = pd.read_excel(open(parentPath + 'inputTestData/Template.xlsx', 'rb'),
                                       sheet_name='Transaction', encoding='utf-8-sig')

df_BalanceTemplate = pd.read_excel(open(parentPath + 'inputTestData/Template.xlsx', 'rb'),
                                   sheet_name='Balance', encoding='utf-8-sig')

df_BankUsers.fillna('', inplace=True)
df_CustUsers.fillna('', inplace=True)
df_customer.fillna('', inplace=True)
df_Singlecustomer.fillna('',inplace=True)
df_accounts.fillna('',inplace=True)
df_TransactionTemplate.fillna('', inplace=True)
df_BalanceTemplate.fillna('', inplace=True)


def singlecustomerDetails(df):
    newName = df['Customer Id'] + Util.get_unique_number(10)
    df['Customer Id'] = newName
    df['Name'] = df['Name'] + newName
    df['Preferred name'] = df['Preferred name'] + newName
    return df


singlecustomerDetails(df_Singlecustomer)
singlecustomerDetails(df_Editcustomer)

nameofCustomer = df_Singlecustomer['Name'][0]

def customerDetails(df):
    for i in range(len(df['Customer Id'])):
        newName = df['Customer Id'][i] + Util.get_unique_number(10)
        df_customer['Customer Id'][i] = newName
    return df

customerDetails(df_customer)

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


def set_details_for_customer_edit(df_duplicate):
    df_Singlecustomer['Name'] = df_duplicate['Name']
    df_Singlecustomer['Preferred name'] = df_duplicate['Preferred name']
    df_Singlecustomer['Customer Id'] = 'RC2932065044'
    df_Singlecustomer['Line 1'] = df_duplicate['Line 1']
    df_Singlecustomer['Line 2'] = df_duplicate['Line 2']
    df_Singlecustomer['Line 3'] = df_duplicate['Line 3']
    df_Singlecustomer['Line 4'] = df_duplicate['Line 4']
    df_Singlecustomer['Value'] = df_duplicate['Value']
    df_Singlecustomer['Reference number'] = 'RN324693'
    df_Singlecustomer['Description'] = df_duplicate['Description']
    return df_Singlecustomer


def set_status_of_customer(df_Singlecustomer, status):
    df_Singlecustomer.loc[:, 'Status'] = status
    print(df_Singlecustomer)

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
