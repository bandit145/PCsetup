#This script automates removal of gwx and install of our basic application package (This choco soltion will be replaced with ninite)
#This is executed by a usb rubber ducky for quick "plug and play" computer setups
#
#
#Written by Philip Bove - 2016
#From ben armstrong's virtulaization blog https://blogs.msdn.microsoft.com/virtual_pc_guy/2010/09/23/a-self-elevating-powershell-script/
# Get the ID and security principal of the current user account
$myWindowsID=[System.Security.Principal.WindowsIdentity]::GetCurrent()
$myWindowsPrincipal=new-object System.Security.Principal.WindowsPrincipal($myWindowsID)
 
# Get the security principal for the Administrator role
$adminRole=[System.Security.Principal.WindowsBuiltInRole]::Administrator
 
# Check to see if we are currently running "as Administrator"
if ($myWindowsPrincipal.IsInRole($adminRole))
   {
   # We are running "as Administrator" - so change the title and background color to indicate this
   $Host.UI.RawUI.WindowTitle = $myInvocation.MyCommand.Definition + "(Elevated)"
   $Host.UI.RawUI.BackgroundColor = "DarkBlue"
   clear-host
   }
else
   {
   # We are not running "as Administrator" - so relaunch as administrator
   
   # Create a new process object that starts PowerShell
   $newProcess = new-object System.Diagnostics.ProcessStartInfo "PowerShell";
   
   # Specify the current script path and name as a parameter
   $newProcess.Arguments = $myInvocation.MyCommand.Definition;
   
   # Indicate that the process should be elevated
   $newProcess.Verb = "runas";
   
   # Start the new process
   [System.Diagnostics.Process]::Start($newProcess);
   
   # Exit from the current, unelevated, process
   }
Write-Host -NoNewLine "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
 
# Run your code that needs to be elevated here
#From here on is my code 
$apps = @("unchecky","googlechrome","flashplayerplugin","adobereader","adobeshockwaveplayer","7zip","silverlight","jre8")
$updates = @("3035583","2976978")
if(Test-Path c:\windows\system32\gwx){
	"Removing GWX..."
	Stop-Process -processname gwx
	$Acl = Get-Acl "c:\windows\system32\gwx"
	#not entirely sure if I need this stuff
	#$addUsr = New-Object system.security.accesscontrol.filesystemaccessrule("User name","FullControl","ContainerInherit, ObjectInherit","Allow")
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
    #replace with choclatey install script (this is currently a security risk)
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
	
