#CHANGE FTP VERIFY TO MORE MODULAR THING, THE PWRSHELL SCRIPT NEEDS DPENEDNCIES BUT IT DOESNT NEED TO BE RUN
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
		self.ini = INI()
		self.ftp = FTP('10.1.10.161')
		self.user = getpass.getuser()
		#except:
		#print('Could not connect to FTP server')
	
	def ftpverifyPS(self,scripts,directory): #verifies download and runs app/scripts that are Powershell
		self.ftp.login('tech')
		os.chdir(directory)
		count =0
		access = 0
		for v in scripts.values(): #iterates through number of dependencies needed
			access = access+1
			value =scripts[str(access)] #dls them based of of order in ini file
			size = self.ftp.size(value)
			self.ftp.retrbinary('RETR ' + value, open(value, 'wb').write)
			if os.path.exists(directory+'\\' +value):
				while os.path.getsize(directory+'\\'+value) != size: #checks to make sure file size is correct, if it is not correct this would indicate a bad download
					continue
					
				sp.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe','-ExecutionPolicy','Unrestricted',''+directory+'\\'+value]) #works now
				while os.path.exists('done.txt') != True:
					continue
			else:
				print('Download did not start for '+ value)
				self.main()
			count = count+1
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
		elif UserAns.lower() == 'help':
			f = open("help.txt")
			print(f.read())
			self.main()
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
		
		
