<img>https://travis-ci.org/bandit145/PCsetup.svg?branch=master</img>
# PCsetup
A little script to help setup pcs at my office.

PCsetup is a program that is intended for desktop support techs to assist with configuring computers.

Program structure:

  quickdeploy.py is the executable
  
  iniclass.py contains the ini methods
  
  ftpclass.py contains the ftp related methods
  
  config.ini contains the ip address and username of the server (note: there is no password because this was for internal network use only)
  
  scriptpackages.ini contains the "packages" (not exactly but close enough) of scripts that will be run in order of the numbers the user
  enters, if they are on the ftp server they will be downloaded and run sequentially
  
  help.txt is the help message for the program.
  
  Stuff todo (eventually):
  
    Make program an .exe for windows using pytoexe
    
    Add FTP_TLS for external network use
