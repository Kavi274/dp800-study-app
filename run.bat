@echo off
title DP-800 Study Application
echo ==========================================
echo   DP-800: SQL AI Developer Study App
echo ==========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt -q
echo.
echo Starting application...
echo App will open in your browser automatically.
echo Press Ctrl+C to stop.
echo.
python app.py
pause
