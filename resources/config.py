ApplicationConfig = {
    'APP_URL': 'http://10.254.187.37:9181/vam-ui/#/',
    'UserId': 'banksup',
    'Password': 'Password@123',
    'BICOrBEI': 'NDEANOKKXXX',
    'SERVERIPADDR': '10.254.187.172',
    'FTP_USERID': 'vamtest',
    'FTP_PASSWORD': 'vamtest',
    'INCOMINGFILEPATH': '/VAM2.0_1/incoming',
    'SERVER_TYPE': 'SFTP'
}
import os

os.environ['myHome'] = 'C:/workspace/webautomation/'
print(os.environ.get('myHome'))
