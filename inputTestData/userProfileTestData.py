import pandas as pd
import os
import xlrd
from Utilities.util import Util
from resources import config

# df_cus = pd.read_csv(os.environ.get('myHome') + 'inputTestData/customerheirarchy.csv')
parentPath = os.environ.get('myHome')
df_BankAdmin = pd.read_excel(open(parentPath + 'inputTestData/Users.xlsx', 'rb'),
                             sheet_name='BankAdmin', encoding='utf-8-sig')

df_BankUpdate = pd.read_excel(open(parentPath + 'inputTestData/Users.xlsx', 'rb'),
                              sheet_name='BankUpdate', encoding='utf-8-sig')

df_BankRead = pd.read_excel(open(parentPath + 'inputTestData/Users.xlsx', 'rb'),
                            sheet_name='BankRead', encoding='utf-8-sig')

df_CustAdmin = pd.read_excel(open(parentPath + 'inputTestData/Users.xlsx', 'rb'),
                             sheet_name='CustAdmin', encoding='utf-8-sig')

df_CustUpdate = pd.read_excel(open(parentPath + 'inputTestData/Users.xlsx', 'rb'),
                              sheet_name='CustUpdate', encoding='utf-8-sig')

df_CustRead = pd.read_excel(open(parentPath + 'inputTestData/Users.xlsx', 'rb'),
                            sheet_name='CustRead', encoding='utf-8-sig')


def generateUniqueUserId(df):
    newName = df['User ID'] + Util.get_unique_number(7)
    df['User ID'] = newName
    return df


generateUniqueUserId(df_BankAdmin)
generateUniqueUserId(df_BankUpdate)
generateUniqueUserId(df_BankRead)
generateUniqueUserId(df_CustAdmin)
generateUniqueUserId(df_CustUpdate)
generateUniqueUserId(df_BankRead)

print(df_BankAdmin)
