@echo off

REM Set the path to the virtual environment activate script
set activateScript=c:/Users/Baachus/Desktop/Files/Automation/Playwright - Example/sandbox-env/Scripts/Activate.ps1

REM Call the PowerShell script to activate the virtual environment and run pytest
powershell.exe -ExecutionPolicy Bypass -File "C:\Users\Baachus\Desktop\Files\Automation\Playwright - Example\Run_Daily.ps1"