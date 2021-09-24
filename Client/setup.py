import sys
import os
from cx_Freeze import setup, Executable
# Packages
from app.packages.pyside_or_pyqt import * # Qt
from app.packages.widgets import * # Widgets
# GUIs
from app.uis.login.ui_login import Ui_Login # Login / Splash Screen
from app.uis.login.ui_IP import Ui_IPAddress
from app.uis.login.ui_signup import Ui_Signup
from app_modules import *
from iu_main import *
# Modules
import app.modules.ui_functions.functions as ui_functions
import app.modules.app_settings.settings as app_settings

# ADD FILES/FOLDERS
files = ['settings.json','images/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
)

# SETUP CX FREEZE
setup(
    name = "Golds",
    version = "1.0",
    description = "Modern search for users",
    author = "20127082_20127084",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]    
)
