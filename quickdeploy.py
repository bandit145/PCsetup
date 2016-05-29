import sys
from iniclass import INI
from ftpclass import FTPclass
import getpass
import logging
import datetime
import ftplib
import os
import platform

#TODO set up FTP_TLS support for external network use
def main():
    ini = INI()
    sections = ini.CollectScripts()
    sections = sections
    directorylinx = '//home//'+ getpass.getuser()+'//Desktop'
    directorywin = 'C:\\Users\\' + getpass.getuser() + '\\desktop'
    UserAns = input("Hello, what do you need? > ")
    check(UserAns, directorywin, sections,ini,directorylinx)


def check(UserAns, directorywin, sections,ini,directorylinx):
    if UserAns in sections:
        ftp = FTPclass()
        package = UserAns  # package of scripts
        scripts = ini.Package(package)
        scripts = dict(scripts) #passes it to dict to be searched easier
        if platform.system() == 'Windows':
            if '.exe' or '.ps1' or '.msi': #Check for compatability
                ftp.DLWS(scripts, directorywin)
            else:
                print('This package contains Linux executables and will not run on Windows')
        elif platform.system() =='Linux':
            if '.exe' or '.ps1' or '.msi' not in scripts.values():
                ftp.DLLN(scripts,directorylinx)
            else:
                print('This package contains Windows executables and will not run on Linux')

        main()

    elif UserAns.lower() == 'list':
        print('Available packages: ' + str(sections))
        main()
    elif UserAns.lower() == 'exit':
        sys.exit()
    elif UserAns.lower() == 'help':
        f = open("help.txt")
        print(f.read())
        main()
    else:
        print('Unrecognized input, try "help"')
        main()

if __name__ == '__main__':
    logging.basicConfig(filename='log.txt', level=logging.ERROR)
    try:
        main()
    except ftplib.all_errors :
        currentTime = datetime.datetime.now()
        logging.exception('Error at ' + str(currentTime))
        print('There was an FTP related error, most likely the ip address of the server is wrong. Please check that in "conifg.ini"')
        print('Exiting...')
        sys.exit()
    except os.error:
        currentTime = datetime.datetime.now()
        logging.exception('Error at ' + str(currentTime))
        print('There was a file related error')
        print('Exiting...')
        sys.exit()
