#GUI Signup
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_Signup(object):
    def setupUi(self, Signup):
        if not Signup.objectName():
            Signup.setObjectName(u"Signup")
        Signup.resize(300, 420)
        Signup.setMinimumSize(QSize(300, 420))
        Signup.setMaximumSize(QSize(300, 420))
        Signup.setStyleSheet(u"#bg {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QLabel {\n"
"	color:  rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-top: 20px;\n"
"}\n"
".QLineEdit {\n"
"	border: 3px solid rgb(47, 48, 50);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(47, 48, 50);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
".QLineEdit:hover {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(62, 63, 66);\n"
"}\n"
".QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(189, 255, 0);\n"
"	background-color: rgb(14, 14, 15);\n"
"}")
        self.centralwidget = QWidget(Signup)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.bg = QFrame(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setFrameShape(QFrame.NoFrame)
        self.bg.setFrameShadow(QFrame.Raised)
        self.frame_widgets = QFrame(self.bg)
        self.frame_widgets.setObjectName(u"frame_widgets")
        self.frame_widgets.setGeometry(QRect(0, 70, 280, 720))
        self.frame_widgets.setMinimumSize(QSize(280, 720))
        self.frame_widgets.setFrameShape(QFrame.NoFrame)
        self.frame_widgets.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_widgets)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 10, 20, 10)
        self.preloader = QFrame(self.frame_widgets)
        self.preloader.setObjectName(u"preloader")
        self.preloader.setMinimumSize(QSize(240, 240))
        self.preloader.setMaximumSize(QSize(260, 260))
        self.preloader.setFrameShape(QFrame.NoFrame)
        self.preloader.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.preloader)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.logo = QFrame(self.frame_widgets)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 260))
        self.logo.setStyleSheet(u"#logo {\n"
"	border-radius: 10px;\n"
"	background-image: url(:/users/images/users/mouse_150px.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.logo)

        self.pushButton_Login = QPushButton(self.frame_widgets)
        self.pushButton_Login.setObjectName(u"pushButton")
        self.pushButton_Login.setMinimumSize(QSize(0, 25))
        self.pushButton_Login.setMaximumSize(QSize(16777215, 40))

        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(10)
        self.pushButton_Login.setFont(font8)
        self.pushButton_Login.setStyleSheet(u"QPushButton {\n"
"   border: 2px solid rgb(52, 59, 72);\n"
"   border-radius: 5px; \n"
"   background-color: rgb(52, 59, 72);\n"
"   color: rgb(236, 236, 236);\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(57, 65, 80);\n"
"   border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {  \n"
"   background-color: rgb(35, 40, 49);\n"
"   border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons_svg/images/icons_svg/icon_settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Login.setIcon(icon3)

        self.pushButton_Login.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.pushButton_Login)

        self.user_description = QLabel(self.frame_widgets)
        self.user_description.setObjectName(u"user_description")
        self.user_description.setStyleSheet(u"background: transparent;")

        self.verticalLayout_2.addWidget(self.user_description)

        self.username = QLineEdit(self.frame_widgets)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 30))
        self.username.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_2.addWidget(self.username)

        self.password = QLineEdit(self.frame_widgets)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 30))
        self.password.setMaximumSize(QSize(16777215, 40))
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password)


        self.verticalLayout.addWidget(self.bg)

        Signup.setCentralWidget(self.centralwidget)

        self.retranslateUi(Signup)

        QMetaObject.connectSlotsByName(Signup)
    # setupUi

    def retranslateUi(self, Signup):
        Signup.setWindowTitle(QCoreApplication.translate("Signup", u"Signup. MouseGold", None))
        self.pushButton_Login.setText(QCoreApplication.translate("Signup", u"Đã có tài khoản hả ?", None))
        self.user_description.setText(QCoreApplication.translate("Signup", u"Đăng ký:", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Signup", u"Username", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Signup", u"Password", None))
    # retranslateUi

