function getIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}
function getDate {
    (Get-Date)
    }
function getVers {
    (Get-Host).Version | Select-String "5*"
    }

$IP = getIP
$DATE = getDate
$VERS = getVers
$USER = $env:USERNAME
$NAME = $env:COMPUTERNAME
$BODY = "This machine's IP is $IP. User is $User. Hostname is $NAME. PowerShell Version $VERS. Todays Date is $DATE"

Send-MailMessage -To "meyer2rn@mail.uc.edu" -From "rnm0128@gmail.com" -Subject "IT3038C" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)