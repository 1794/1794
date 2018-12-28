@echo off
SETLOCAL ENABLEEXTENSIONS
SETLOCAL ENABLEDELAYEDEXPANSION

:init

set CD="!CD!"

:: setup our python and specify what folders are included in the search path for scripts
set PATH=!CD:~1,-1!\Builder\Python
set PYTHONPATH=%PYTHONPATH%;!CD:~1,-1!\ID;!CD:~1,-1!\Header;!CD:~1,-1!\Process;!CD:~1,-1!

python -B Lav/compile.py

echo ______________________________
echo Script processing has ended.
echo Press any key to restart. . .
pause>nul
goto :init
