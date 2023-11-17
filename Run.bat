@echo off
set script_path=D:\pythoni\menusver1.0.py

REM Check if the script file exists
if not exist "%script_path%" (
    echo Script not detected.
    pause
    exit /b
)

REM Run the Python script
D:\pythoni\python\python.exe "%script_path%"

REM Pause to keep the console window open
pause