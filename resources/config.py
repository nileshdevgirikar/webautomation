ApplicationConfig = {
    'APP_URL': 'http://10.254.187.37:9181/vam-ui/#/',
    'BANKADMIN_USERID': 'nbank',
    'BANKADMIN_PASSWORD' : 'Tieto@123',
    'UserId': 'banksup',
    'Password': 'Password@123',
    'BICOrBEI': 'TIEEGB22XXX',
    'SERVERIPADDR': '10.254.187.37',
    'FTP_USERID': 'vamtest',
    'FTP_PASSWORD': 'vamtest',
    'INCOMINGFILEPATH': '/VAM2.0_2/incoming',
    'SERVER_TYPE': 'SFTP'
}
import os

os.environ['myHome'] = 'C:/workspace/webautomation/'
print(os.environ.get('myHome'))
