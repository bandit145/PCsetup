#CHANGE FTP VERIFY TO MORE MODULAR THING, THE PWRSHELL SCRIPT NEED DPENEDNCIES BUT IT DOESNT NEED OT BE RUN
	#PROBABLY A FOR LOOP FOR LENGTH OF NEW LIST THAT I WILL CREATE
	#
	#
	#verifies file integrity
import time
import sys
import getpass
import os
from ftplib import FTP
import subprocess as sp
class Class01:
	def __init__(self):
		#try:
		self.ftp = FTP('192.168.1.9')
		self.ftp.login('tech')
		self.user = getpass.getuser()
		#except:
		#print('Could not connect to FTP server')
	
	def ftpverify(self,dl,directory): #verifies download and runs app/scripts
		count = 0
		while count <= len(dl):
			size = self.ftp.size(dl[count])
			self.ftp.retrbinary('RETR ' + dl[count], open(dl[count], 'wb').write)
			if os.path.exists(directory+'\\' +dl[count]):
				while os.path.getsize(directory+'\\'+dl[count]) != size: #checks to make sure file size is correct, if it is not correct this would indicate a a bad download
					continue
					
				sp.Popen(['powershell.exe'],''+directory+'\\'+dl[count],1) #figure out bufsize
					
			else:
				print('Download did not start')
				self.main()
			count = count + 1
	#keep track of data in list
	def listcheck(self,UserAns,directory,scripts):
		if UserAns.lower() == 'new user':
			dl = [scripts[0],scripts[1]]
			self.ftpverify(dl,directory)
			
		
	#Checks user input	
	def check(self,UserAns,scripts,directory):
		if UserAns.lower() == 'new user':
			self.NewUsr(scripts,directory,UserAns)
		elif UserAns.lower() == 'exit' or 'quit':
			sys.exit()
	#Begins program
	def main(self):
		directory = 'C:\\Users\\'+self.user+'\\desktop'
		scripts = ['pcsetup.ps1','PSWindowsUpdate']
		UserAns =input("Hello, what do you need? > ")
		self.check(UserAns,scripts,directory)
	#for new user
	def NewUsr(self,scripts,directory,UserAns):
		#self.ftp.cwd('scripts')
		os.chdir(directory)
		self.listcheck(UserAns,directory,scripts)
		
if __name__ == '__main__':
	quick = Class01()
	quick.main()
		
		
