@echo off

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Installing Python...
    choco install python -y
)

:: Create and activate virtual environment
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

echo Activating virtual environment...
call .venv\Scripts\activate

:: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

:: Go in the app directory
cd vark_quiz

:: Apply migrations
echo Applying migrations...
python manage.py migrate

:: Run the development server
echo Starting the development server...
python manage.py runserver