import copy

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

AccountName = 'Name of Accoount';

ipID = {
    'name': 'Sarah',
    'age': '23'
}

Old = ipID
Old[AccountName] = 'Debit Account'

new = copy.deepcopy( ipID )
new[AccountName] = 'Credit Account'

print( Old )
print( new )
