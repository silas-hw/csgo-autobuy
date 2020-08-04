@echo off
cd source
pyinstaller --onefile -w csgo-autobuy.py
cd dist
MOVE csgo-autobuy.exe "D:\silas\python\csgo autobuy"
cd ..
@RD /S /Q dist
@RD /S /Q build