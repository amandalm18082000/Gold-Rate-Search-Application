#GUI IP Address
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_IPAddress(object):
    def setupUi(self, IPAddress):
        if not IPAddress.objectName():
            IPAddress.setObjectName(u"IPAddress")
        IPAddress.resize(300, 420)
        IPAddress.setMinimumSize(QSize(300, 420))
        IPAddress.setMaximumSize(QSize(300, 420))
        IPAddress.setStyleSheet(u"#bg {\n"
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
        self.centralwidget = QWidget(IPAddress)
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

        self.user_description = QLabel(self.frame_widgets)
        self.user_description.setObjectName(u"user_description")
        self.user_description.setStyleSheet(u"background: transparent;")

        self.verticalLayout_2.addWidget(self.user_description)

        self.enterIP = QLineEdit(self.frame_widgets)
        self.enterIP.setObjectName(u"enterIP")
        self.enterIP.setMinimumSize(QSize(0, 30))
        self.enterIP.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_2.addWidget(self.enterIP)


        self.verticalLayout.addWidget(self.bg)

        IPAddress.setCentralWidget(self.centralwidget)

        self.retranslateUi(IPAddress)

        QMetaObject.connectSlotsByName(IPAddress)
    # setupUi

    def retranslateUi(self, IPAddress):
        IPAddress.setWindowTitle(QCoreApplication.translate("IPAddress", u"IPAddress. MouseGold", None))
        self.user_description.setText(QCoreApplication.translate("IPAddress", u"Nhập địa chỉ IP:", None))
        self.enterIP.setPlaceholderText(QCoreApplication.translate("IPAddress", u"IP Address", None))
    # retranslateUi
