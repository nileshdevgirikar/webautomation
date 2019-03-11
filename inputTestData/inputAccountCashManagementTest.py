import random
import copy

AccountDetails = {
    'Owner': '',
    'Hierarchy offering': 'Virtual Account Management',
    'Account type': 'Root Account',
    'Currency': '',
    'Name of the account': '',
    'Account number': 'NO' + str( random.randint( 0, 99999999999999 ) ),
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
    'Name of the account': '',
    'Country': 'NORWAY',
    'Reference type': '',
    'Reference number': '',
    'Funds check': 'false',
    'Hierarchy activation date': ''
}

ShadowAccount = {
    'Owner': '',
    'Account type': 'Shadow Account',
    'Currency': 'NOK',
    'Name of the account': '',
    'Account number': 'NO',
    'Country': 'NORWAY',
    'Reference type': '',
    'Reference number': '',
    'Funds check': 'false',
    'Hierarchy activation date': ''
}

SummaryAccount = {
    'Owner': '',
    'Account type': 'Summary Account',
    'Currency': 'NOK',
    'Name of the account': '',
    'Account number': '',
    'Country': 'NORWAY',
    'Reference type': '',
    'Reference number': '',
    'Funds check': 'false',
    'Hierarchy activation date': ''
}

TransactionAccount = {
    'Owner': '',
    'Account type': 'Virtual Account',
    'Currency': 'NOK',
    'Name of the account': '',
    'Account number': 'NO',
    'Country': 'NORWAY',
    'Reference type': '',
    'Reference number': '',
    'Funds check': 'false',
    'Settlement mark': '',
    'Hierarchy activation date': ''
}

RootAccount['Name of the account'] = 'TopAcc1'
TopAcc1 = RootAccount

ShadowAccount['Name of the account'] = 'Shadow'
Shadow = ShadowAccount

AggAcc3 = copy.deepcopy( SummaryAccount )
AggAcc3['Name of the account'] = 'AggAcc3'

AggAcc4 = copy.deepcopy( SummaryAccount )
AggAcc4['Name of the account'] = 'AggAcc4'

TranAcc1 = copy.deepcopy( TransactionAccount )
TranAcc1['Name of the account'] = 'TranAcc1'
TranAcc2 = copy.deepcopy( TransactionAccount )
TranAcc2['Name of the account'] = 'TranAcc2'
TranAcc3 = copy.deepcopy( TransactionAccount )
TranAcc3['Name of the account'] = 'TranAcc3'
TranAcc4 = copy.deepcopy( TransactionAccount )
TranAcc4['Name of the account'] = 'TranAcc4'
TranAcc5 = copy.deepcopy( TransactionAccount )
TranAcc5['Name of the account'] = 'TranAcc5'
TranAcc6 = copy.deepcopy( TransactionAccount )
TranAcc6['Name of the account'] = 'TranAcc6'

print( AggAcc3 )

Accountlists = {
    "TopAcc1": [
        Shadow
    ],
    "Shadow": [
        AggAcc3,
        AggAcc4,
        TranAcc1,
        TranAcc2
    ],
    "AggAcc3": [
        TranAcc3,
        TranAcc4
    ],
    "AggAcc4": [
        TranAcc5,
        TranAcc6
    ]
}


def getKey(Accountlists):
    toReturn = ''
    for key, value in Accountlists.items():
        if type( value ) is list:
            count = len( value )
            i = 0
            while count > 0:
                toReturn = key
                print( key )
                print( value[i] )
                i += 1
                count -= 1
    # return toReturn


# getKey(item,Accountlists)
getKey( Accountlists )
