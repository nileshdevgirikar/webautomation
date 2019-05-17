ApplicationConfig = {
    'APP_URL': 'http://10.254.187.172:9081/vam-ui/#/',
    'BANKADMIN_USERID' : 'jbankupdate',
    'BANKADMIN_PASSWORD' : 'Tieto@123',
    'UserId': '130503',
    'Password': 'Tieto@123',
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
