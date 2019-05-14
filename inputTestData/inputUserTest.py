import random

updateUsersABO = {
    "UserId": "BN" + str(random.randint(0, 9999999)),
    "profile": "Bank Admin",
    "firstName": "AdminName",
    "lastName": "AdminLastName",
    "email": "acb@gmail.com",
    "phone": '1234567789',
    "BANKID": 'NBNO',
    "Password": "Test@12345",
    "repeatPassword": "Test@12345",
    "userStatus": "Active"
}

print( updateUsersABO )
