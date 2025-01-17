@echo off
setlocal

REM Check if .env already exists
if exist .env (
    echo Warning: .env file already exists
    set /p REPLY="Do you want to overwrite it? (y/n) "
    if /i not "%REPLY%"=="y" (
        echo Setup cancelled
        exit /b 1
    )
)

REM Copy .env.example to .env if it doesn't exist or user agreed to overwrite
copy .env.example .env >nul

echo Created .env file from template
echo Please edit .env and add your API keys
echo The following environment variables need to be configured:
echo.

REM List variables from .env (excluding comments)
for /f "tokens=1 delims==" %%a in ('type .env ^| findstr /v "^#" ^| findstr "="') do (
    echo - %%a
)

echo.
echo Setup complete! Edit .env to configure your environment
pause
