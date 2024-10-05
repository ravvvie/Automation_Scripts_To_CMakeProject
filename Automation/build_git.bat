@echo off

REM check if python is installed
python --version >nul 2>&1
if %errorlevel% NEQ 0 (
    echo "Python is not installed. Please install Python to continue."
    exit /b 1
)

REM check args
if "%~1"=="" (
    echo "Usage: build_git.bat full_default_build"
    exit /b 1
)

python Automation/automation_git.py %~1

pause