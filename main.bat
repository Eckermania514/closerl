@echo off
echo Closing RL in 5 minutes... (space to skip)
timeout /t 600 > nul
TASKKILL /F /IM "RocketLeague.exe"
