#This will be typed in by rubber ducky alonmg with the ftp script to deploy the setup scripts
while(Test-Path \pylon\desktop\pcsetup.ps1 -eq false){
	ftp -s:ftp.txt}
cd \pylon\desktop
./pcsetup.ps1