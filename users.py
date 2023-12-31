# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'users.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 420)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("swj.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_server = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_server.setGeometry(QtCore.QRect(290, 10, 160, 100))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.groupBox_server.setFont(font)
        self.groupBox_server.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.groupBox_server.setObjectName("groupBox_server")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_server)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 141, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_serverport = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.lineEdit_serverport.setFont(font)
        self.lineEdit_serverport.setStyleSheet("")
        self.lineEdit_serverport.setText("")
        self.lineEdit_serverport.setObjectName("lineEdit_serverport")
        self.gridLayout.addWidget(self.lineEdit_serverport, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_serverIP = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.lineEdit_serverIP.setFont(font)
        self.lineEdit_serverIP.setStyleSheet("")
        self.lineEdit_serverIP.setText("")
        self.lineEdit_serverIP.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit_serverIP.setObjectName("lineEdit_serverIP")
        self.gridLayout.addWidget(self.lineEdit_serverIP, 0, 1, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_server)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 70, 141, 21))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_openserver = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_openserver.sizePolicy().hasHeightForWidth())
        self.pushButton_openserver.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.pushButton_openserver.setFont(font)
        self.pushButton_openserver.setObjectName("pushButton_openserver")
        self.horizontalLayout.addWidget(self.pushButton_openserver)
        self.pushButton_closeserver = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_closeserver.sizePolicy().hasHeightForWidth())
        self.pushButton_closeserver.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.pushButton_closeserver.setFont(font)
        self.pushButton_closeserver.setObjectName("pushButton_closeserver")
        self.horizontalLayout.addWidget(self.pushButton_closeserver)
        self.groupBox_client = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_client.setGeometry(QtCore.QRect(460, 10, 151, 101))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.groupBox_client.setFont(font)
        self.groupBox_client.setObjectName("groupBox_client")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_client)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 131, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_clientIP = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.lineEdit_clientIP.setFont(font)
        self.lineEdit_clientIP.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_clientIP.setText("")
        self.lineEdit_clientIP.setReadOnly(True)
        self.lineEdit_clientIP.setObjectName("lineEdit_clientIP")
        self.gridLayout_2.addWidget(self.lineEdit_clientIP, 0, 1, 1, 1)
        self.lineEdit_clientport = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.lineEdit_clientport.setFont(font)
        self.lineEdit_clientport.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_clientport.setText("")
        self.lineEdit_clientport.setReadOnly(True)
        self.lineEdit_clientport.setObjectName("lineEdit_clientport")
        self.gridLayout_2.addWidget(self.lineEdit_clientport, 1, 1, 1, 1)
        self.groupBox_car = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_car.setGeometry(QtCore.QRect(290, 130, 320, 100))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.groupBox_car.setFont(font)
        self.groupBox_car.setObjectName("groupBox_car")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_car)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 221, 71))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_carX = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.lineEdit_carX.setFont(font)
        self.lineEdit_carX.setText("")
        self.lineEdit_carX.setReadOnly(True)
        self.lineEdit_carX.setObjectName("lineEdit_carX")
        self.gridLayout_3.addWidget(self.lineEdit_carX, 0, 1, 1, 1)
        self.lineEdit_carLinearV = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.lineEdit_carLinearV.setFont(font)
        self.lineEdit_carLinearV.setText("")
        self.lineEdit_carLinearV.setReadOnly(True)
        self.lineEdit_carLinearV.setObjectName("lineEdit_carLinearV")
        self.gridLayout_3.addWidget(self.lineEdit_carLinearV, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 2, 1, 1)
        self.lineEdit_carY = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.lineEdit_carY.setFont(font)
        self.lineEdit_carY.setText("")
        self.lineEdit_carY.setReadOnly(True)
        self.lineEdit_carY.setObjectName("lineEdit_carY")
        self.gridLayout_3.addWidget(self.lineEdit_carY, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 2, 1, 1)
        self.lineEdit_carAngularV = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.lineEdit_carAngularV.setFont(font)
        self.lineEdit_carAngularV.setText("")
        self.lineEdit_carAngularV.setReadOnly(True)
        self.lineEdit_carAngularV.setObjectName("lineEdit_carAngularV")
        self.gridLayout_3.addWidget(self.lineEdit_carAngularV, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 2, 1, 1)
        self.lineEdit_carStatus = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.lineEdit_carStatus.setFont(font)
        self.lineEdit_carStatus.setReadOnly(True)
        self.lineEdit_carStatus.setObjectName("lineEdit_carStatus")
        self.gridLayout_3.addWidget(self.lineEdit_carStatus, 2, 3, 1, 1)
        self.lineEdit_carYaw = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.lineEdit_carYaw.setFont(font)
        self.lineEdit_carYaw.setText("")
        self.lineEdit_carYaw.setReadOnly(True)
        self.lineEdit_carYaw.setObjectName("lineEdit_carYaw")
        self.gridLayout_3.addWidget(self.lineEdit_carYaw, 2, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_car)
        self.layoutWidget1.setGeometry(QtCore.QRect(240, 20, 71, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_run = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.pushButton_run.setFont(font)
        self.pushButton_run.setObjectName("pushButton_run")
        self.verticalLayout.addWidget(self.pushButton_run)
        self.pushButton_stop = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout.addWidget(self.pushButton_stop)
        self.pushButton_restart = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.pushButton_restart.setFont(font)
        self.pushButton_restart.setObjectName("pushButton_restart")
        self.verticalLayout.addWidget(self.pushButton_restart)
        self.groupBox_go = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_go.setGeometry(QtCore.QRect(290, 250, 200, 130))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.groupBox_go.setFont(font)
        self.groupBox_go.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.groupBox_go.setObjectName("groupBox_go")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_go)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 181, 101))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_gowait = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_gowait.setObjectName("pushButton_gowait")
        self.gridLayout_4.addWidget(self.pushButton_gowait, 1, 0, 1, 1)
        self.lineEdit_grX = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_grX.setObjectName("lineEdit_grX")
        self.gridLayout_4.addWidget(self.lineEdit_grX, 2, 1, 1, 1)
        self.lineEdit_guX = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_guX.setObjectName("lineEdit_guX")
        self.gridLayout_4.addWidget(self.lineEdit_guX, 3, 1, 1, 1)
        self.lineEdit_guY = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_guY.setObjectName("lineEdit_guY")
        self.gridLayout_4.addWidget(self.lineEdit_guY, 3, 2, 1, 1)
        self.lineEdit_grY = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_grY.setObjectName("lineEdit_grY")
        self.gridLayout_4.addWidget(self.lineEdit_grY, 2, 2, 1, 1)
        self.pushButton_gounload = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_gounload.setObjectName("pushButton_gounload")
        self.gridLayout_4.addWidget(self.pushButton_gounload, 3, 0, 1, 1)
        self.pushButton_goreceive = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_goreceive.setObjectName("pushButton_goreceive")
        self.gridLayout_4.addWidget(self.pushButton_goreceive, 2, 0, 1, 1)
        self.lineEdit_gwX = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_gwX.setObjectName("lineEdit_gwX")
        self.gridLayout_4.addWidget(self.lineEdit_gwX, 1, 1, 1, 1)
        self.lineEdit_gwY = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_gwY.setObjectName("lineEdit_gwY")
        self.gridLayout_4.addWidget(self.lineEdit_gwY, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)
        self.groupBox_message = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_message.setGeometry(QtCore.QRect(10, 10, 260, 150))
        self.groupBox_message.setObjectName("groupBox_message")
        self.textBrowser_message = QtWidgets.QTextBrowser(self.groupBox_message)
        self.textBrowser_message.setGeometry(QtCore.QRect(10, 20, 240, 120))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(6)
        self.textBrowser_message.setFont(font)
        self.textBrowser_message.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser_message.setObjectName("textBrowser_message")
        self.groupBox_video = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_video.setGeometry(QtCore.QRect(10, 170, 260, 210))
        self.groupBox_video.setObjectName("groupBox_video")
        self.label_video = QtWidgets.QLabel(self.groupBox_video)
        self.label_video.setGeometry(QtCore.QRect(10, 20, 240, 180))
        self.label_video.setStyleSheet("background-color: rgb(105, 170, 255);")
        self.label_video.setAlignment(QtCore.Qt.AlignCenter)
        self.label_video.setObjectName("label_video")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(560, 360, 41, 20))
        self.pushButton_quit.setObjectName("pushButton_quit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 20))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuSet = QtWidgets.QMenu(self.menubar)
        self.menuSet.setObjectName("menuSet")
        self.menuFonts = QtWidgets.QMenu(self.menuSet)
        self.menuFonts.setObjectName("menuFonts")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        self.actionAbout.setFont(font)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionMsgFont = QtWidgets.QAction(MainWindow)
        self.actionMsgFont.setObjectName("actionMsgFont")
        self.menu.addAction(self.actionQuit)
        self.menuFonts.addAction(self.actionMsgFont)
        self.menuSet.addAction(self.menuFonts.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuSet.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智能车调度软件-风驰电掣"))
        self.groupBox_server.setTitle(_translate("MainWindow", "服务端"))
        self.label.setText(_translate("MainWindow", "IP地址"))
        self.label_2.setText(_translate("MainWindow", "端口号"))
        self.pushButton_openserver.setText(_translate("MainWindow", "连接"))
        self.pushButton_closeserver.setText(_translate("MainWindow", "断开"))
        self.groupBox_client.setTitle(_translate("MainWindow", "客户端"))
        self.label_4.setText(_translate("MainWindow", "端口号"))
        self.label_3.setText(_translate("MainWindow", "IP地址"))
        self.groupBox_car.setTitle(_translate("MainWindow", "小车参数"))
        self.label_8.setText(_translate("MainWindow", "角速度"))
        self.label_5.setText(_translate("MainWindow", "X"))
        self.label_6.setText(_translate("MainWindow", "Y"))
        self.label_9.setText(_translate("MainWindow", "线速度"))
        self.label_7.setText(_translate("MainWindow", "偏航角"))
        self.label_10.setText(_translate("MainWindow", "状态"))
        self.pushButton_run.setText(_translate("MainWindow", "通行"))
        self.pushButton_stop.setText(_translate("MainWindow", "禁行"))
        self.pushButton_restart.setText(_translate("MainWindow", "重启"))
        self.groupBox_go.setTitle(_translate("MainWindow", "发送目标"))
        self.pushButton_gowait.setText(_translate("MainWindow", "初始等待区"))
        self.pushButton_gounload.setText(_translate("MainWindow", "卸货区"))
        self.pushButton_goreceive.setText(_translate("MainWindow", "接货区"))
        self.label_11.setText(_translate("MainWindow", "X"))
        self.label_12.setText(_translate("MainWindow", "Y"))
        self.label_13.setText(_translate("MainWindow", "位置\\坐标"))
        self.groupBox_message.setTitle(_translate("MainWindow", "消息历史"))
        self.groupBox_video.setTitle(_translate("MainWindow", "实时图像"))
        self.label_video.setText(_translate("MainWindow", "camera"))
        self.pushButton_quit.setText(_translate("MainWindow", "退出"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menuSet.setTitle(_translate("MainWindow", "设置"))
        self.menuFonts.setTitle(_translate("MainWindow", "字体"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionQuit.setText(_translate("MainWindow", "退出"))
        self.actionMsgFont.setText(_translate("MainWindow", "消息框"))
