#CHANGE FTP VERIFY TO MORE MODULAR THING, THE PWRSHELL SCRIPT NEED DPENEDNCIES BUT IT DOESNT NEED OT BE RUN
	#PROBABLY A FOR LOOP FOR LENGTH OF NEW LIST THAT I WILL CREATE
	#
	#
#TODO ADD ERROR HANDLING FOR FTP/EVERYTHING! 
#TODO EVERY TIME DOWNLAOD STARTS INITATE FTP SESSION SO TIMEOUT DOES NOT OCCUR
import configparser
import sys
import getpass
import os
from ftplib import FTP
import subprocess as sp
from iniclass import INI
class Class01:
	def __init__(self):
		#try:
		#config = ConfigParser.RawConfigParser() Modularize with ini files
		#config.read('quickconfig.ini')
		self.ini = INI()
		self.ftp = FTP('192.168.1.9')
		self.ftp.login('tech')
		self.user = getpass.getuser()
		#except:
		#print('Could not connect to FTP server')
	
	def ftpverifyPS(self,scripts,directory): #verifies download and runs app/scripts that are Powershell
		os.chdir(directory)
		for v in scripts.values():
			size = self.ftp.size(v)
			self.ftp.retrbinary('RETR ' + v, open(v, 'wb').write)
			if os.path.exists(directory+'\\' +v):
				while os.path.getsize(directory+'\\'+v) != size: #checks to make sure file size is correct, if it is not correct this would indicate a bad download
					continue
					
				sp.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe','-ExecutionPolicy','Unrestricted',''+directory+'\\'+v]) #works now
				while os.path.exists('done.txt') != True:
					continue
			else:
				print('Download did not start for '+ v)
				self.main()
	#keep track of data in list
		
	def check(self,UserAns,directory,sections):
		if UserAns in sections:
			package = UserAns#package of scripts
			scripts = self.ini.Package(package)
			scripts = dict(scripts)
			print(scripts)
			self.ftpverifyPS(scripts,directory)
			
		elif UserAns.lower() == 'list':
			print('Available packages: '+str(sections))
			self.main()
		elif UserAns.lower() == 'exit':
			sys.exit()
		else:
			print('Unrecognized input, try list')
			self.main()
	#Begins program
	def main(self):
		sections = self.ini.CollectScripts()
		sections = sections
		directory = 'C:\\Users\\'+self.user+'\\desktop'
		UserAns =input("Hello, what do you need? > ")
		self.check(UserAns,directory,sections)
		
if __name__ == '__main__':
	quick = Class01()
	quick.main()
		
		
