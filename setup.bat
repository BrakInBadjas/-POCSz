@echo off
echo Trying to upgrade pip/wheel/setuptools if update is available
pip install --upgrade pip wheel setuptools

echo.
echo Installing pyserial
pip install pyserial

echo.
echo Installing PyMySQL
pip install pymysql

echo.
echo Installing Dependencies for Kivy
pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

echo.
echo Installing Kivy
pip install kivy

PAUSE