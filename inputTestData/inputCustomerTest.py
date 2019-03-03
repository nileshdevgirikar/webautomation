contactPerson = {
    'type': 'Email',
    'Value': 'abc.def@tieto.com',
    'Description': 'testemail'
}

customerReferences = {
    'Company Reg Number': 'CRN',
    'Reference type': {
                        'General Ledger Number': 'GL',
                        #'Additional Reference': 'AR'
                      }
}

ADDRESS = [
    {
        'value': 'Cluster D',
        'id': "//input[@id='addressLine1']",
        'name': 'Line 1'
    },
    {
        'value': 'Eon IT Park',
        'id': "//input[@id='addressLine2']",
        'name': 'Line 2'
    }
]

rootCustomer = {
    'Customer category': 'Sub-entity',
    'Bank Id': 'NBNO',
    'Customer type': 'Corporate',
    'Name': 'TestCustomer',
    'Preferred name': '',
    'Customer Id': 'TA',
    'Sector classification': 'Not Applicable',
    'Market Segment': 'Not Applicable',
    'Clients allowed': 'false',
    'ADDRESS': ADDRESS,
    'contactPerson': contactPerson,
    'customerReferences': customerReferences
}

# ADDRESS = {
#     'Line 1': 'Cluster D',
#     'Line 2': 'Eon IT Park',
#     'Line 3': 'Wing 1',
#     'Line 4': '3rd Floor',
#     "Postal code": "411012",
#     "Country": "NORWAY"
# }

rootCustomer1 = 'TestAutomation'

companyList = {
    'TataSons': [
        {
            'TataSteel': [
                'TataSteelX',
                'TataSteelY'
            ]
        },
        {
            'TataEast': [
                {
                    'TataPower': [
                        'TataPowerX',
                        'TataPowerY'
                    ]
                }
            ]
        }
    ]
}
# print(str(companyList.keys())[12:-3])
# for key in companyList:
#     print(key)
