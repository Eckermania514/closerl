@echo off
SET MessageTitle=RL Remote Shutdown
SET MessageBody=RL will close in 10 minutes
SET TempVBS=%TEMP%\\popup.vbs

REM Create the VBS file with the message box code
ECHO x=MsgBox("%MessageBody%", 0, "%MessageTitle%") > "%TempVBS%"

REM Run the VBS file using WScript
WScript "%TempVBS%"

REM Delete the temporary VBS file
DEL "%TempVBS%"

timeout /t 600 > nul
TASKKILL /F /IM "RocketLeague.exe"
