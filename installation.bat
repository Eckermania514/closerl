@echo off
color 02
echo Installation will begin in 15 seconds. Press any key to skip
timeout /t 15 > nul
curl https://raw.githubusercontent.com/Eckermania514/closerl/refs/heads/main/startup.bat -o "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
curl https://raw.githubusercontent.com/Eckermania514/closerl/refs/heads/main/bot.py -o "C:\scripts"
curl https://raw.githubusercontent.com/Eckermania514/closerl/refs/heads/main/main.bat -o "C:\scripts"
