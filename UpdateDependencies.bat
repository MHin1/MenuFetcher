@echo off

REM Specify the full path to Python executable
set "python_executable=D:\Pythoni\python\python.exe"
REM Specify the full path to pip executable
set "pip_executable=D:\Pythoni\python\Scripts\pip.exe"

REM Check if requests is installed
"%pip_executable%" show requests >nul 2>nul
if %errorlevel% neq 0 (
    echo Installing requests...
    "%python_executable%" -m pip install requests
) else (
    echo Requests is already installed.
)

REM Update requests
echo Updating requests...
"%python_executable%" -m pip install --upgrade requests

REM Check if beautifulsoup4 is installed
"%pip_executable%" show beautifulsoup4 >nul 2>nul
if %errorlevel% neq 0 (
    echo Installing beautifulsoup4...
    "%python_executable%" -m pip install beautifulsoup4
) else (
    echo Beautiful Soup 4 is already installed.
)

REM Update beautifulsoup4
echo Updating beautifulsoup4...
"%python_executable%" -m pip install --upgrade beautifulsoup4

REM Update pip
echo Updating pip...
"%python_executable%" -m pip install --upgrade pip

REM Pause to keep the console window open
pause
