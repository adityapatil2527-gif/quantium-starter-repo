@echo off

echo Activating virtual environment...

call venv\Scripts\activate

echo Running test suite...

pytest

if %errorlevel%==0 (
    echo All tests passed
    exit /b 0
) else (
    echo Tests failed
    exit /b 1
)