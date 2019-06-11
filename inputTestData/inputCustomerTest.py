import pandas as pd
import os
import xlrd

from resources import config

# df_cus = pd.read_csv(os.environ.get('myHome') + 'inputTestData/customerheirarchy.csv')
parentPath = os.environ.get('myHome')
df_customer = pd.read_excel(open(parentPath + 'inputTestData/customerheirarchy1.xlsx', 'rb'),
                            sheet_name='customerheirarchy', encoding='utf-8-sig')

df_Singlecustomer = pd.read_excel(open(parentPath + 'inputTestData/customerheirarchy1.xlsx', 'rb'),
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

ddd = df_Template
values = ddd['Optional fields'][0]
x = values.split("|")
print(x)

