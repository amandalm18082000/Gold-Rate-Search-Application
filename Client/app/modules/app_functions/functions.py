# IMPORT
# ///////////////////////////////////////////////////////////////
# Packages
from app.packages.pyside_or_pyqt import *
from app.packages.widgets import *
# Modules
import app.modules.app_settings.settings as app_settings

# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
class AppFunctions:
    def __init__(self):
        # GET WIDGETS FROM "ui_main.py"
        # Load widgets inside App Functions
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def change_placeholder(self):
        self.ui.search_line_edit.setPlaceholderText("teste")