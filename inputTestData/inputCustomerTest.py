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


def enterDetails(df):
    for name in range(len(df['Name of the account'])):
        newName = df['Name of the account'][name] + Util.get_unique_number(10)
        for parent in range(len(df['Parent'])):
            if df['Parent'][parent] == df['Name of the account'][name]:
                df['Parent'][parent] = newName
        df['Name of the account'][name] = newName
    return df


enterDetails(df_accounts)


def createDuplicate(row):
    df = df_accounts[df_accounts['Parent'] == row]
    df = df.reset_index()
    del df['index']
    df.loc[0]['Name of the account'] = 'VTA' + Util.get_unique_number(10)
    return df.loc[0]


nameofAccounts = list(df_accounts[df_accounts['Account type'] == 'Internal Aggregation Account']['Name of the account'])

print(df_accounts)
