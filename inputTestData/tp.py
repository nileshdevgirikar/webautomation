import pandas as pd
import os
import xlrd
from resources import config

parentPath = os.environ.get('myHome')
df_customer = pd.read_excel(open(parentPath + 'inputTestData/customerheirarchy1.xlsx', 'rb'),
                            sheet_name='customerheirarchy')
print(df_customer.loc[0]['Customer catergory'])

# for i in range(len(df_cus)):
#     print(df_cus.loc[i]['Subentity'])
