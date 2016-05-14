import configparser


class INI:
    def __init__(self):
        self.config = configparser.ConfigParser()

    # config.read(['scriptpackages.ini'])
    def CollectScripts(self):
        self.config.read(['scriptpackages.ini'])
        sections = self.config.sections()  # Used to pull a list of availble scripts into the main program, updated by sysadmin
        return sections

    def Package(self, ScriptSel):  # Get  scripts of setup
        self.config.read(['scriptpackages.ini'])
        scripts = self.config.items(ScriptSel)
        return scripts

    def Config(self, check):  # pull ip address and username from config.ini
        try:
            self.config.read(['config.ini'])
            setup = self.config.items('FTPserver')
            setup = dict(setup)
            if check == 'ip':
                return setup['ip']
            elif check == 'name':
                return setup['name']
        except:
            print('No ip address in config.ini')
