@echo off
python setup.py install
ECHO "COMPILE COMPLETE!"
PAUSE
python setup.py py2exe
ECHO "BUILD COMPLETE!"
PAUSE
QUIT