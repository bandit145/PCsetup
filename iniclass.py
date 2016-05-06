import configparser
class INI:
	def __init__(self):
		self.config = configparser.ConfigParser()
		#config.read(['scriptpackages.ini'])
	def CollectScripts(self):
		self.config.read(['scriptpackages.ini'])
		sections = self.config.sections() # Used to pull a list of availble scripts into the main program, updated by sysadmin
		return sections
	def Package(self,ScriptSel): #Get  scripts of setup
		self.config.read(['scriptpackages.ini'])
		scripts = self.config.items(ScriptSel)
		return scripts
		
		