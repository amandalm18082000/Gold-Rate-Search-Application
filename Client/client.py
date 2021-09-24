#FOR SOCKET
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

import sys
#LOAD INFORMATION RECEIVE FROM SERVER
import pickle
#FOR HTTP
import requests
#RETRIEVE INFORMATION ABOUT THE PLATFORM ON WHICH THE PROGRAMMING IS BEING EXECUTED
import platform

# GUI FILE

# IMPORT / GUI, SETTINGS AND WIDGETS
# ///////////////////////////////////////////////////////////////
# Packages
from app.packages.pyside_or_pyqt import * # Qt
from app.packages.widgets import * # Widgets
from app_modules import *

# GUIs
from app.uis.login.ui_login import Ui_Login # Login / Splash Screen
from app.uis.login.ui_IP import Ui_IPAddress
from app.uis.login.ui_signup import Ui_Signup
from ui_main import Ui_MainWindow
from ui_main import TableGolds

# Modules
import app.modules.ui_functions.functions as ui_functions
import app.modules.app_settings.settings as app_settings


# GLOBALS
# ///////////////////////////////////////////////////////////////
counter = 0
checkIP = False
FORMAT = "utf-8"
client = {}
client = socket(AF_INET,SOCK_STREAM)

#import pandas as pd

#IP
class IPWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        # GET WIDGETS FROM "ui_login.py"
        # Load widgets inside LoginWindow
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_IPAddress()
        self.ui.setupUi(self)
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # IMPORT CIRCULAR PROGRESS
        # ///////////////////////////////////////////////////////////////
        self.progress = CircularProgress()
        self.progress.width = 240
        self.progress.height = 240
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.font_size = 20
        self.progress.add_shadow(True)
        self.progress.progress_width = 4
        self.progress.progress_color = QColor("#bdff00")
        self.progress.text_color = QColor("#E6E6E6")
        self.progress.bg_color = QColor("#222222")
        self.progress.setParent(self.ui.preloader)
        self.progress.show()

        # ADD DROP SHADOW
        # ///////////////////////////////////////////////////////////////
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.bg.setGraphicsEffect(self.shadow)

        # QTIMER
        # ///////////////////////////////////////////////////////////////
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

        # KEY PRESS EVENT
        # ///////////////////////////////////////////////////////////////
        self.ui.enterIP.keyReleaseEvent = self.check_IP

        self.show()


    def receive(self, client):
        while True:
            try:
                rcv = Thread(target=self.control(client))
                rcv.start()
                check = client.recv(1024).decode("utf-8")
                if check == "Exit":
                    messagebox.showinfo("", "Client rời khỏi dịch vụ")
                    client.close()
                    break

            except:
                print("An error occured!")
                client.close()
                break

    # CHECK LOGIN
    # ///////////////////////////////////////////////////////////////
    def check_IP(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            HOST = self.ui.enterIP.text()

            def open_login(client):
                # SHOW MAIN WINDOW
                self.main = LoginWindow()
                self.main.show()                
                self.close()

            global client
            
            try: 
                client.connect((HOST, 5656))
                client.send(bytes("Success", 'utf-8'))
                self.ui.user_description.setText(f"Xin chào!")
                self.ui.user_description.setStyleSheet("#user_description { color: #bdff00 }")
                self.ui.enterIP.setStyleSheet("#enterIP:focus { border: 3px solid #bdff00; }")
                #QTimer.singleShot(1200, lambda: open_login(client))
                rcv = Thread(target=open_login(client))
                rcv.start()
            except:
                self.ui.enterIP.setStyleSheet("#enterIP:focus { border: 3px solid rgb(255, 0, 127); }")
                self.shacke_window()

    def shacke_window(self):
        # SHACKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))

    # UPDATE PROGRESS BAR
    # ///////////////////////////////////////////////////////////////
    def update(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.progress.set_value(counter)

        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter >= 100:
            # STOP TIMER
            self.timer.stop()
            self.animation_login()

        # INCREASE COUNTER
        counter += 1

    # START ANIMATION TO LOGIN
    # ///////////////////////////////////////////////////////////////
    def animation_login(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(0, 70, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(QRect(0, -325, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

class SignupWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        # GET WIDGETS FROM "ui_login.py"
        # Load widgets inside LoginWindow
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_Signup()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # IMPORT CIRCULAR PROGRESS
        # ///////////////////////////////////////////////////////////////
        '''self.progress = CircularProgress()
        self.progress.width = 240
        self.progress.height = 240
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.font_size = 20
        self.progress.add_shadow(True)
        self.progress.progress_width = 4
        self.progress.progress_color = QColor("#bdff00")
        self.progress.text_color = QColor("#E6E6E6")
        self.progress.bg_color = QColor("#222222")
        self.progress.setParent(self.ui.preloader)
        self.progress.show()'''

        # ADD DROP SHADOW
        # ///////////////////////////////////////////////////////////////
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.bg.setGraphicsEffect(self.shadow)

        # QTIMER
        # ///////////////////////////////////////////////////////////////
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)
        def open_login():
            # SHOW MAIN WINDOW
            self.login = LoginWindow()
            self.login.show()                
            self.close()

        # KEY PRESS EVENT
        # ///////////////////////////////////////////////////////////////
        self.ui.username.keyReleaseEvent = self.check_signup
        self.ui.password.keyReleaseEvent = self.check_signup
        self.ui.pushButton_Login.clicked.connect(lambda: open_login())

        self.show()



    # CHECK SIGNUP
    # ///////////////////////////////////////////////////////////////
    def check_signup(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            username = self.ui.username.text()
            password = self.ui.password.text()
            User = "Up"+"Username="+ str(username) + "&" + "Password=" + str(password)
            client.sendall(bytes(User, "utf-8"))
            check = client.recv(1024).decode("utf-8")

            def open_main():
                # SHOW MAIN WINDOW
                self.main = MainWindow()
                self.main.show()                
                self.close()

            if check == "signupsuccess":
                self.ui.user_description.setText(f"Thành công rồi nha! Chào mừng {username}!")
                self.ui.user_description.setStyleSheet("#user_description { color: #bdff00 }")
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid #bdff00; }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid #bdff00; }")
                QTimer.singleShot(1200, lambda: open_main())
            if check =="nosignupsuccess":
                # SET STYLESHEET
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid rgb(255, 0, 127); }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid rgb(255, 0, 127); }")
                self.shacke_window()
            if check == "Exit":
                self.shacke_window()
            

    def shacke_window(self):
        # SHACKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))

    # UPDATE PROGRESS BAR
    # ///////////////////////////////////////////////////////////////
    def update(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        #self.progress.set_value(counter)

        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter >= 100:
            # STOP TIMER
            self.timer.stop()
            self.animation_login()

        # INCREASE COUNTER
        counter += 10

    # START ANIMATION TO LOGIN
    # ///////////////////////////////////////////////////////////////
    def animation_login(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(0, 70, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(QRect(0, -325, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

# LOGIN
# ///////////////////////////////////////////////////////////////
class LoginWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        # GET WIDGETS FROM "ui_login.py"
        # Load widgets inside LoginWindow
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # IMPORT CIRCULAR PROGRESS
        # ///////////////////////////////////////////////////////////////
        '''self.progress = CircularProgress()
        self.progress.width = 240
        self.progress.height = 240
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.font_size = 20
        self.progress.add_shadow(True)
        self.progress.progress_width = 4
        self.progress.progress_color = QColor("#bdff00")
        self.progress.text_color = QColor("#E6E6E6")
        self.progress.bg_color = QColor("#222222")
        self.progress.setParent(self.ui.preloader)
        self.progress.show()'''

        # ADD DROP SHADOW
        # ///////////////////////////////////////////////////////////////
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.bg.setGraphicsEffect(self.shadow)

        # QTIMER
        # ///////////////////////////////////////////////////////////////
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

        def open_signup():
            # SHOW MAIN WINDOW
            self.signup = SignupWindow()
            self.signup.show()                
            self.close()
        # KEY PRESS EVENT
        # ///////////////////////////////////////////////////////////////
        self.ui.username.keyReleaseEvent = self.check_login
        self.ui.password.keyReleaseEvent = self.check_login
        self.ui.pushButton_Signup.clicked.connect(lambda: open_signup())

        self.show()

    

    # CHECK LOGIN
    # ///////////////////////////////////////////////////////////////
    def check_login(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            username = self.ui.username.text()
            password = self.ui.password.text()
            User = "In"+"Username="+ str(username) + "&" + "Password=" + str(password)
            #self.sendRequest(client, User)
            client.sendall(bytes(User, "utf-8"))
            check = client.recv(1024).decode("utf-8")
            def open_main():
                # SHOW MAIN WINDOW
                self.main = MainWindow()
                self.main.show()                
                self.close()

            if check == "usernamecorrect":
                self.ui.user_description.setText(f"Thành công rồi nha! Chào mừng {username}!")
                self.ui.user_description.setStyleSheet("#user_description { color: #bdff00 }")
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid #bdff00; }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid #bdff00; }")
                QTimer.singleShot(1200, lambda: open_main())
            if check == "usernameincorrect":
                # SET STYLESHEET  
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid rgb(255, 0, 127); }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid rgb(255, 0, 127); }")
                self.shacke_window()
            if check == "Exit":
                self.shacke_window()
            

    def shacke_window(self):
        # SHACKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))

    # UPDATE PROGRESS BAR
    # ///////////////////////////////////////////////////////////////
    def update(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        #self.progress.set_value(counter)

        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter >= 100:
            # STOP TIMER
            self.timer.stop()
            self.animation_login()

        # INCREASE COUNTER
        counter += 10

    # START ANIMATION TO LOGIN
    # ///////////////////////////////////////////////////////////////
    def animation_login(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(0, 70, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(QRect(0, -325, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()



# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    
    def __init__(self):

        QMainWindow.__init__(self)
        from PySide6 import QtCore, QtGui, QtWidgets
        from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
        from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
        from PySide6.QtWidgets import (QAbstractScrollArea, QWidget)
        from PySide6.QtGui import QPalette
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        client.sendall(bytes("Main", FORMAT))
        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

       
        ## START - WINDOW ATTRIBUTES

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Main Window - Gold Rate Search')
        UIFunctions.labelTitle(self, '  Gold Mouse - Tra cứu tỷ giá vàng')
        UIFunctions.labelDescription(self, 'Trang')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Home", "btn_home", "url(:/icons_svg/images/icons_svg/icon_emoticons.svg)", True)
        UIFunctions.addNewMenu(self, "Mục tra cứu", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "USER", "", True)
        ## ==> END ##


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                p = event.globalPosition()
                globalPos = p.toPoint()
                self.dragPos = globalPos
                #self.move(self.pos() + p - self.dragPos)
    
                event.accept()

        # WIDGET TO MOVE

        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

       
        ## END - WINDOW ATTRIBUTES

       
        ## START -------------- TABLEWIDGETS FUNCTIONS/PARAMETERS ----------- ##
        
        self.ui.lineEdit.keyReleaseEvent = self.sendSearch
        self.ui.comboBox.keyReleaseEvent = self.sendSearch

        self.ui.btn_close.clicked.connect(lambda: self.closeButton())
    

        TableGolds(self.ui.frame_3, self.ui.tableWidget)
        
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##

        ## SHOW ==> MAIN WINDOW
        self.show()
        ## ==> END ##
    ## CLOSE WINDOW
    def closeButton(self):
        try:
            client.sendall(bytes("Exit", FORMAT))
            self.close()
        except: 
            self.close()

    ## SHOW TABLE SEARCH
    def sendSearch(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter or event.type() == QEvent.MouseButtonDblClick:
            self.combo = self.ui.comboBox.currentText()
            print(self.combo)
            if (self.combo == "Loại vàng"):
                client.sendall(bytes("Type", "utf-8"))
                self.check = client.recv(1024).decode('utf-8')
            elif (self.combo == "Năm tháng ngày"):
                client.sendall(bytes("Day", "utf-8"))
                self.check = client.recv(1024).decode('utf-8')
            elif (self.combo == "Công ty"):
                client.sendall(bytes("Company", "utf-8"))
                self.check = client.recv(1024).decode('utf-8')
            elif (self.combo == "Thương hiệu"):
                client.sendall(bytes("Brands", "utf-8"))
                self.check = client.recv(1024).decode('utf-8')

            self.search = ""
            self.search = self.ui.lineEdit.text()
            print(self.search)
            if (self.combo == "Năm tháng ngày"):
                str(self.search)
                self.new_search = self.search
                if (self.search[2] == '/') or (self.search[5] == '/'): 
                    self.new_day = self.search[0:2]
                    print(self.new_day)
                    self.new_month = self.search[3:5]
                    print(self.new_month)
                    self.new_year = self.search[6:11]
                    print(self.new_year)
                    self.new_search = self.new_year + self.new_month + self.new_day
                self. dayUpdate = self.new_search.replace('/','')
                print(self.dayUpdate)
                client.sendall(bytes(self.dayUpdate, "utf-8"))
            else:
                client.sendall(bytes(self.search, "utf-8"))
            self.length = client.recv(1024).decode("utf-8")
            self.length = int(self.length)

            self.dict = client.recv(40960000)
            self.Gold = pickle.loads(self.dict)
            self.ui.tableWidget.setRowCount(self.length)
            __sortingEnabled = self.ui.tableWidget.isSortingEnabled()
            self.ui.tableWidget.setSortingEnabled(False)
            self.x = 0
            for i in self.Gold:
                self.header = self.ui.tableWidget.horizontalHeader()
                self.header.setSectionResizeMode(0, QHeaderView.Stretch)
                self.header.setSectionResizeMode(1, QHeaderView.Stretch)
                self.header.setSectionResizeMode(2, QHeaderView.Stretch)
                self.header.setSectionResizeMode(3, QHeaderView.Stretch)
                self.header.setSectionResizeMode(4, QHeaderView.Stretch)
                self.ui.tableWidget.setItem(self.x, 0, QTableWidgetItem(i['type']))
                self.ui.tableWidget.setItem(self.x, 1, QTableWidgetItem(i['updated']))
                self.ui.tableWidget.setItem(self.x, 2, QTableWidgetItem(i['brand']))
                self.ui.tableWidget.setItem(self.x, 3, QTableWidgetItem(i['buy']))
                self.ui.tableWidget.setItem(self.x, 4, QTableWidgetItem(i['sell']))
                self.x += 1
            self.ui.tableWidget.setSortingEnabled(__sortingEnabled)

    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "TRA CỨU TỶ GIÁ VÀNG")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##
    

    ## START ==> APP EVENTS

    ## EVENT ==> MOUSE DOUBLE CLICK
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MiddleButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT

    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##


    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################
    ## SHOW ==> CLOSE APPLICATION
    

# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # LOAD AND SETUP APP SETTINHS FROM JSON FILE
    setup = app_settings.Settings()
    setup.deserialize()

    # APPLICATION
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = IPWindow()
    sys.exit(app.exec())