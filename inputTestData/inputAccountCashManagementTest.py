import random

AccountDetails = {
    'Owner': '',
    'Hierarchy offering': 'Virtual Account Management',
    'Account type': 'Root Account',
    'Currency': '',
    'Name of the account': '',
    'Account number': '',
    'Country': 'NORWAY',
    'Reference type': '',
    'Reference number': '',
    'Funds check': 'false',
    'Hierarchy activation date': ''
}

RootAccount = {
    'Owner': '',
    'Hierarchy offering': 'Virtual Account Management',
    'Account type': 'Root Account',
    'Currency': 'NOK',
    'Name of the account': 'RootAccount',
    'Country': 'NORWAY',
    'Reference type': '',
    'Reference number': '',
    'Funds check': 'false',
    'Hierarchy activation date': ''
}

ShadowAccount = {
    'Owner': '',
    'Hierarchy offering': 'Virtual Account Management',
    'Account type': 'Shadow Account',
    'Currency': 'NOK',
    'Name of the account': 'ShadowAccount',
    'Account number': '',
    'Country': 'NORWAY',
    'Reference type': '',
    'Reference number': '',
    'Funds check': 'false',
    'Hierarchy activation date': ''
}

SummaryAccount = {
    'Owner': '',
    'Hierarchy offering': 'Virtual Account Management',
    'Account type': 'Summary Account',
    'Currency': 'NOK',
    'Name of the account': 'SummaryAccount',
    'Account number': '',
    'Country': 'NORWAY',
    'Reference type': '',
    'Reference number': '',
    'Funds check': 'false',
    'Hierarchy activation date': ''
}

TransactionAccount = {
    'Owner': '',
    'Hierarchy offering': 'Virtual Account Management',
    'Account type': 'Virtual Account',
    'Currency': 'NOK',
    'Name of the account': 'VirtualAccount',
    'Account number': '',
    'Country': 'NORWAY',
    'Reference type': '',
    'Reference number': '',
    'Funds check': 'false',
    'Hierarchy activation date': ''
}

AccountList = {
    'RootAccount': [
        {
            'ShadowAccount': [
                {
                    'SummaryAccount': [
                        'Transaction',
                        'Transaction'
                    ]
                },
                {
                    'SummaryAccount1': [
                        'Transaction',
                        'Transaction'
                    ]
                },
                [
                    'Transaction',
                    'Transaction'
                ]
            ]}
    ]
}

# ShadowAcct = ShadowAccount
#
# SummaryAcct4 = {
#     'TranAcct1' : TransactionAccount,
#     'TranAcct2' : TransactionAccount,
# }
#
#
# SummaryAcct2 = {
#     'SummaryAccount': {
#         'TranAcct1': TransactionAccount,
#         'TranAcct2': TransactionAccount,
#     }
# }
#
# SummaryAcct3 = {
#     'SummaryAccount': {
#         'TranAcct1': TransactionAccount,
#         'TranAcct2': TransactionAccount,
#         'TranAcct3': TransactionAccount,
#         'SummaryAcct3': SummaryAcct4
#     }
# }
#
# SummaryAcct1 = {
#     'SummaryAccount': {
#         'TranAcct1': TransactionAccount,
#         'TranAcct2': TransactionAccount,
#         'TranAcct3': TransactionAccount,
#         'SummaryAcct3': SummaryAcct3
#     }
# }
#
#
# ShadowAcct = {
#         'ShadowAccount':[
#             SummaryAcct1,
#             SummaryAcct2
#         ]
# }
#
# hierrachyRelationship = {
#     'TopAcct1' : RootAccount,
#     'ShadowAcct' : ShadowAcct,
#     'TrancAcc' : TransactionAccount
# }
#
#
# TopAcct1 = RootAccount
#
# hierrachyRelationship1 = {
#     [TopAcct1]
# }
#
# AggreAcc1,AggreAcc2 =  SummaryAccount
#
#
# ShadowAcc = {
#     [AggreAcc1,AggreAcc2]
# }
#
# TopAcct1 = [ShadowAcc]
#
#
# print(hierrachyRelationship)

list = {
    "TopAcc1": [
        "Shadow"
    ],
    "Shadow": [
        "AggAcc3",
        "AggAcc4",
        "TranAcc1",
        "TranAcc2"
    ],
    "AggAcc3": [
        "TranAcc3",
        "TranAcc4"
    ],
    "AggAcc4": [
        "TranAcc5",
        "TranAcc6"
    ]
}

print( list )
