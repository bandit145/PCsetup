$newProcess = new-object System.Diagnostics.ProcessStartInfo "PowerShell";  
$newProcess.Arguments = $myInvocation.MyCommand.Definition;  
$newProcess.Verb = "runas";
[System.Diagnostics.Process]::Start($newProcess);
$path = "c:\Windows\System32\consent.exe"
while(get-process | ?{$_.path -eq $path}){
}
New-Item done.txt -type file
exit