#This script automates removal of gwx and install of our basic application package (This choco soltion will be replaced with ninite)
#This is executed by a usb rubber ducky for quick "plug and play" computer setups
#
#
#Written by Philip Bove - 2016

$apps = @("unchecky","googlechrome","flashplayerplugin","adobereader","adobeshockwaveplayer","7zip","silverlight","jre8")
$updates = @("3035583","2976978")
Import-Module PSWindowsUpdate
if(Test-Path c:\windows\system32\gwx){
	"Removing GWX..."
	Stop-Process -processname gwx
	$Acl = Get-Acl "c:\windows\system32\gwx"
	#not entirely sure if I need this stuff
	#$addUsr = New-Object system.security.accesscontrol.filesystemaccessrule("pylon","FullControl","ContainerInherit, ObjectInherit","Allow")
	takeown /F "c:\windows\system32\gwx" /R /D Y
	#needs testing
	$rmTrusted = New-Object system.security.accesscontrol.filesystemaccessrule("TrustedInstaller","Read","Allow")
    $Acl.REmoveAccessRuleAll($rmTrusted)
    Set-Acl -Path "C:\Window\system32\gwx" -AclObject $Acl
	
	#TODO: Remove GWX folder
	Remove-Item c:\windows\system32\gwx -recurse
	#TODO: Check for and remove specific updates
	"Uninstalling updates..."
	foreach($update in $updates){
	wusa /uninstall /kb:$update /quiet /norestart
	}
	
	#Possible: Turn off windows update, install choclatey, and grab our usual set of programs
	"Hiding Updates..."
	foreach($update in $updates){
		#need to get pswindwosupdate module
		Hide-WUUpdate -KB $update
	}
	"Turning off Windows update..."

}
"Checking for Chocolatey..."
if(Test-Path c:\programdata\chocolatey){
	"Chocolatey is already installed. Exiting..."
    Remove-Item c:\programdata\chocolatey -recurse
	Remove-Item Env:\ChocolateyInstall
	exit
}
else{
	"Installing Chocolatey..."
    #replace with choclatey install script (this is a security risk)
	iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))
	"Installing programs..."
	foreach($choco in $apps){
		choco install $choco
	}
    "Removing Chocolatey..."
    Remove-Item c:\programdata\chocolatey -recurse -force
	Remove-Item Env:\ChocolateyInstall
    }
	"Apps installed..."
	"Program finished!"
	
