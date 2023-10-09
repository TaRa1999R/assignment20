# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Palam_Pulum_Plish.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(429, 563)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(167, 167, 167);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.back1 = QPushButton(self.centralwidget)
        self.back1.setObjectName(u"back1")
        self.back1.setGeometry(QRect(200, 420, 91, 91))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(25)
        self.back1.setFont(font)
        self.back1.setStyleSheet(u"background-color: rgb(255, 88, 124);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.front1 = QPushButton(self.centralwidget)
        self.front1.setObjectName(u"front1")
        self.front1.setGeometry(QRect(310, 420, 91, 91))
        self.front1.setFont(font)
        self.front1.setStyleSheet(u"background-color: rgb(255, 88, 124);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.player_choice = QLineEdit(self.centralwidget)
        self.player_choice.setObjectName(u"player_choice")
        self.player_choice.setGeometry(QRect(200, 300, 201, 111))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(60)
        font1.setBold(False)
        self.player_choice.setFont(font1)
        self.player_choice.setStyleSheet(u"background-color: rgb(255, 119, 148);\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.player_choice.setMaxLength(2)
        self.player_choice.setAlignment(Qt.AlignCenter)
        self.computer_choice = QLineEdit(self.centralwidget)
        self.computer_choice.setObjectName(u"computer_choice")
        self.computer_choice.setGeometry(QRect(200, 120, 201, 111))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(60)
        self.computer_choice.setFont(font2)
        self.computer_choice.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.computer_choice.setMaxLength(2)
        self.computer_choice.setAlignment(Qt.AlignCenter)
        self.main = QLineEdit(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(10, 210, 151, 111))
        self.main.setFont(font2)
        self.main.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.main.setMaxLength(2)
        self.main.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.back2 = QPushButton(self.centralwidget)
        self.back2.setObjectName(u"back2")
        self.back2.setGeometry(QRect(200, 20, 91, 91))
        self.back2.setFont(font)
        self.back2.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.front2 = QPushButton(self.centralwidget)
        self.front2.setObjectName(u"front2")
        self.front2.setGeometry(QRect(310, 20, 91, 91))
        self.front2.setFont(font)
        self.front2.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.player_score = QLineEdit(self.centralwidget)
        self.player_score.setObjectName(u"player_score")
        self.player_score.setGeometry(QRect(40, 330, 91, 61))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setUnderline(True)
        self.player_score.setFont(font3)
        self.player_score.setStyleSheet(u"color: rgb(255, 88, 124);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.player_score.setMaxLength(1)
        self.player_score.setAlignment(Qt.AlignCenter)
        self.computer_score = QLineEdit(self.centralwidget)
        self.computer_score.setObjectName(u"computer_score")
        self.computer_score.setGeometry(QRect(40, 130, 91, 61))
        self.computer_score.setFont(font3)
        self.computer_score.setStyleSheet(u"color: rgb(85, 255, 255);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.computer_score.setMaxLength(1)
        self.computer_score.setAlignment(Qt.AlignCenter)
        self.computer = QRadioButton(self.centralwidget)
        self.computer.setObjectName(u"computer")
        self.computer.setGeometry(QRect(20, 30, 161, 20))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.computer.setFont(font4)
        self.player = QRadioButton(self.centralwidget)
        self.player.setObjectName(u"player")
        self.player.setGeometry(QRect(20, 60, 161, 20))
        self.player.setFont(font4)
        self.win = QLineEdit(self.centralwidget)
        self.win.setObjectName(u"win")
        self.win.setGeometry(QRect(170, 250, 251, 31))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(13)
        font5.setBold(True)
        self.win.setFont(font5)
        self.win.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.win.setMaxLength(13)
        self.win.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 429, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Palam Pulum Plish", None))
        self.back1.setText("")
        self.front1.setText("")
        self.player_choice.setText("")
        self.computer_choice.setText("")
        self.main.setText("")
        self.back2.setText("")
        self.front2.setText("")
        self.player_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.computer_score.setInputMask("")
        self.computer_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.computer.setText(QCoreApplication.translate("MainWindow", u"Player vs. Computer", None))
        self.player.setText(QCoreApplication.translate("MainWindow", u"2 Player", None))
        self.win.setText("")
    # retranslateUi

