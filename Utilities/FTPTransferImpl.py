import pysftp  # as sftp
import ftplib
import paramiko, sys
import Utilities.custom_logger as cl
import logging
import os


class FTPTransferImpl():
    log = cl.customLogger(logging.INFO)
    PORT = 21
    SFTPPORT = 22

    def sendFileToSFTPServer(self, serverIp, userName, password, localPath, destinationPath):
        try:
            cnopts = pysftp.CnOpts()
            cnopts.hostkeys = None
            with pysftp.Connection(host=serverIp, username=userName,
                                   password=password, cnopts=cnopts, log=True) as sftp:
                print("Connection succesfully established ... ")
                sftp.put(localPath, destinationPath)
            sftp.close()
        except Exception:
            print(Exception)

    def sendFileToFTPServer(self, serverIp, userName, password, localPath, destinationPath):
        try:
            session = ftplib.FTP(serverIp, FTPTransferImpl.PORT, userName, password)
            file = open('kitten.jpg', 'rb')
            # ftp.login(user=userName, passwd=password)

            # connect = ftp.Connection(serverIp, userName, password)
            localFile = localPath  # + "\\" + localFileName
            # remotepath = destinationPath
            # connect.put(localFile,remotepath)
            # connect.close()
        except Exception:
            print(Exception)
