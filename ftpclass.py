from ftplib import FTP
from iniclass import INI
import subprocess as sp
import os
class FTPclass():
    def __init__(self):
        self.ini = INI()

    def DLWS(self, scripts, directory):  # downloads for windows execution
        ip = self.ini.Config('ip')
        name = self.ini.Config('name')
        ftp = FTP(ip)
        ftp.login(name)
        os.chdir(directory)
        count = 0
        access = 0
        for v in scripts.values():  # iterates through number of dependencies needed
            access = access + 1
            value = scripts[str(access)]  # dls them based off of the order in ini file
            size = ftp.size(value)
            ftp.retrbinary('RETR ' + value, open(value, 'wb').write)
            if os.path.exists(directory + '\\' + value):
                while os.path.getsize(directory + '\\' + value) != size:  # checks to make sure file size is correct, if it is not correct this would indicate a bad download
                    continue
                if '.ps1' in value:
                    powershell = sp.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe', '-ExecutionPolicy', 'Unrestricted','' + directory + '\\' + value])  #currently works, issue with powershell admin elevation but that is more of an issue with my powrshell script than this program
                    powershell.wait()
                elif '.exe' in value:
                     sp.Popen([directory+'\\'+value])

            else:
                print('Download did not start for ' + value)
            count = count + 1
            # keep track of data in list
