# -*- coding:utf-8 -*-
# main.py
# zhengyinloong
# 2023/06/30 17:42

from PyQt5.QtCore import QTimer, QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFontDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from socket import *
import numpy as np
from users import *
import struct
import sys
import cv2


def recvall(sock, length):
    data = b''
    while len(data) < length:
        packet = sock.recv(length - len(data))
        if not packet:
            break
        data += packet
    return data


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        # ============ ADD ====================
        self.PrepOpen()  # 初始化参数和控件状态
        self.CallBackFunctions()  # 各个控件的功能函数集

    def PrepOpen(self):
        # self.camera = cv2.VideoCapture(0)
        self.setStyleSheet("#MainWindow{background-color:#123456;}")

        self.textBrowser_message.clear()
        self.textBrowser_message.append('welcome!')
        self.statusbar.showMessage("Ready")
        # self.groupBox_car.setFont(self.font)

        self.PrepParameters()  # 定义并初始化程序运行过程中会用到的变量
        self.PrepWidgets()  # 初始化各个控件
        # self.textBrowser_message.clear()
        # self.textBrowser_message.append(str(e))

    def PrepParameters(self):
        """
        定义并初始化程序运行过程中会用到的变量
        :return:
        """
        # 参数
        self.serverIP = '192.168.217.219'
        self.serverPort = '1500'

        self.clientIP = ''
        self.clientPort = ''
        self.BUFLEN = 60000

        self.carX = ''
        self.carY = ''
        self.carYaw = ''
        self.carAngularV = ''
        self.carLinearV = ''
        self.carStatus = '未连接'

        self.gwX = '0.70'
        self.gwY = '2.35'
        self.grX = '3.75'
        self.grY = '4.74'
        self.guX = '7.05'
        self.guY = '0.42'

        self.font = QtGui.QFont()
        self.font.setFamily("等线 Light")
        self.font.setPointSize(10)

        # 显示
        self.lineEdit_serverIP.setText(self.serverIP)
        self.lineEdit_serverport.setText(self.serverPort)

        self.lineEdit_clientIP.setText(self.clientIP)
        self.lineEdit_clientport.setText(self.clientPort)

        self.lineEdit_carX.setText(self.carX)
        self.lineEdit_carY.setText(self.carY)
        self.lineEdit_carYaw.setText(self.carYaw)
        self.lineEdit_carAngularV.setText(self.carAngularV)
        self.lineEdit_carLinearV.setText(self.carLinearV)
        self.lineEdit_carStatus.setText(self.carStatus)

        self.lineEdit_gwX.setText(self.gwX)
        self.lineEdit_gwY.setText(self.gwY)
        self.lineEdit_grX.setText(self.grX)
        self.lineEdit_grY.setText(self.grY)
        self.lineEdit_guX.setText(self.guX)
        self.lineEdit_guY.setText(self.guY)

    def PrepWidgets(self):
        """
        设置刚开启时控件的状态
        :return: none
        """
        self.pushButton_closeserver.setEnabled(False)
        self.SetWidgetsEnable(False)
        self.lineEdit_gwY.setStyleSheet("color:red")
        self.lineEdit_grX.setStyleSheet("color:red")
        self.lineEdit_guX.setStyleSheet("color:red")

    def SetWidgetsEnable(self, isEnable):
        """
        设置后三块组合(客户端、小车状态、发送)中控件的状态
        :return: none
        """
        self.groupBox_client.setEnabled(isEnable)
        self.groupBox_car.setEnabled(isEnable)
        self.groupBox_go.setEnabled(isEnable)

    def CallBackFunctions(self):
        """
        各个控件的回调函数
        :return: none
        """
        # 菜单动作
        self.actionQuit.triggered.connect(self.QuitApp)
        # self.actionMsgFont.triggered.connect(lambda: self.SetFonts(self.textBrowser_message))
        self.actionMsgFont.triggered.connect(lambda: self.SetFonts(self.textBrowser_message))

        self.actionAbout.triggered.connect(self.ShowAbout)

        # 按键
        self.pushButton_quit.clicked.connect(self.QuitApp)

        self.pushButton_openserver.clicked.connect(self.OpenServer)
        self.pushButton_closeserver.clicked.connect(self.CloseServer)

        self.pushButton_run.clicked.connect(lambda: self.CarControl(cmd=0x01))
        self.pushButton_stop.clicked.connect(lambda: self.CarControl(cmd=0x02))
        self.pushButton_restart.clicked.connect(lambda: self.CarControl(cmd=0x03))

        self.pushButton_gowait.clicked.connect(lambda: self.CarControl(cmd=0x04))
        self.pushButton_goreceive.clicked.connect(lambda: self.CarControl(cmd=0x05))
        self.pushButton_gounload.clicked.connect(lambda: self.CarControl(cmd=0x06))

        # 文本框

        # self.lineEdit_serverIP.changeEvent()

        # 计时器的定义和调用
        # 它定义了一个定时器，执行计时器开始的代码后，该计时器就开始计时
        # 每次计时结束都会调用一次函数TimerOutFun
        self.receiveMessageTimer = QTimer()
        self.receiveMessageTimer.timeout.connect(self.ReceiveMessage)

        # 定义一个线程
        # self.receiveThread_car = ReceiveThread('receiveThread_car',self)

    def OpenServer(self):
        self.textBrowser_message.append('正在尝试连接...')
        # =========== ADD ==========
        self.serverIP = self.lineEdit_serverIP.text()
        self.serverPort = self.lineEdit_serverport.text()
        # self.textBrowser_message.append(self.serverIP)
        try:
            self.dataSocket = self.ConnectServer()
            self.receiveMessageTimer.start(10)

            self.clientIP = self.dataSocket.getsockname()[0]
            self.clientPort = str(self.dataSocket.getsockname()[1])
            # 显示
            self.lineEdit_clientIP.setText(self.clientIP)
            self.lineEdit_clientport.setText(self.clientPort)
            self.textBrowser_message.append(f'IP{self.clientIP}[{self.clientPort}] 连接成功!')

            # 设置控件可用
            self.SetWidgetsEnable(True)
            self.pushButton_closeserver.setEnabled(True)
            self.pushButton_openserver.setEnabled(False)

        except Exception as e:
            # self.textBrowser_message.clear()
            self.textBrowser_message.append(f'connect failed:{str(e)}')

    def ConnectServer(self):
        # 实例化一个socket对象，并指明协议
        dataSocket = socket(AF_INET, SOCK_STREAM)

        # 连接服务端socket
        dataSocket.connect((self.serverIP, int(self.serverPort)))

        return dataSocket

    def CloseServer(self):
        self.textBrowser_message.append('正在断开连接...')
        # =========== ADD ==========
        self.dataSocket.close()
        # self.receiveThread_car.stop()
        self.receiveMessageTimer.stop()
        # self.Timer_carStatus.stop()
        self.textBrowser_message.append('连接断开')
        self.pushButton_closeserver.setEnabled(False)
        self.pushButton_openserver.setEnabled(True)
        self.SetWidgetsEnable(False)

    def CarControl(self, cmd):

        if cmd == 0x01:
            self.toSend = '继续前进'
            self.SendMessage()

            self.textBrowser_message.append(f'客户端:{self.toSend}')
        elif cmd == 0x02:
            self.toSend = '停止前进'
            self.SendMessage()

            self.textBrowser_message.append(f'客户端:{self.toSend}')
        elif cmd == 0x03:
            self.toSend = '重启'
            self.SendMessage()

            self.textBrowser_message.append(f'客户端:{self.toSend}')
        elif cmd == 0x04:
            # self.toSend = '3'
            self.gwY = self.lineEdit_gwY.text()
            self.toSend = self.lineEdit_gwY.text()
            self.SendMessage()
            self.textBrowser_message.append(f'客户端:等待区{self.toSend}')
        elif cmd == 0x05:
            # self.toSend = '1'
            self.grX = self.lineEdit_grX.text()
            self.toSend = self.lineEdit_grX.text()
            self.SendMessage()
            self.textBrowser_message.append(f'客户端:装货区{self.toSend}')
        elif cmd == 0x06:
            # self.toSend = '2'
            self.guX = self.lineEdit_guX.text()
            self.toSend = self.lineEdit_guX.text()
            self.SendMessage()
            self.textBrowser_message.append(f'客户端:卸货区{self.toSend}')
    def SendMessage(self):
        self.dataSocket.send(self.toSend.encode())

    def ReceiveMessage(self):
        # self.recved = self.dataSocket.recv(self.BUFLEN)
        try:
            # self.recved = self.dataSocket.recv(8)
            self.recved = recvall(self.dataSocket, 8)

            header, length = struct.unpack('!4sI', self.recved)
            start_flag = b'\x02\x20\x02\x20'
            # self.textBrowser_message.append(f'客户接收到消息头{header, length}')
            self.statusbar.showMessage(f'客户接收到消息头{header, length}')
            if header == start_flag:
                self.recved = recvall(self.dataSocket, length)
                self.recvedMsgLength = len(self.recved)
                if self.recvedMsgLength == length:
                    # self.statusbar.showMessage(f'{self.recvedMsgLength, len(self.recved)}')
                    self.ParsingMessage()

        except Exception as e:
            self.textBrowser_message.append(f'connect failed:{str(e)}')

    def ParsingMessage(self):
        """
        解析收到的信息，得到小车状态和摄像机图像
        :return: none
        """
        try:
            if self.recvedMsgLength > 1000:
                nparr = np.frombuffer(self.recved, dtype=np.uint8)
                img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                # img2 = np.frombuffer(self.recved,dtype=np.uint8).reshape((360,480))
                img2 = cv2.cvtColor(img_decode, cv2.COLOR_BGR2RGB)
                # img2 = cv2.cvtColor(nparr, cv2.COLOR_BGR2RGB)
                # img2=nparr
                camera_img = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                                    QImage.Format_RGB888)
                self.camera_img = QPixmap.fromImage(camera_img)

                self.ShowCamera()
                # self.textBrowser_message.append(f'客户端接收到img{img2.shape}')  # {self.recved.decode()}
                self.statusbar.showMessage(f'客户端接收到img{img2.shape}')  # {self.recved.decode()}
                # # 解决同步问题
                # self.toSend = 'get camera'
                # self.SendMessage()
            else:
                # try:
                str0 = self.recved.decode()

                self.carInfo = str0
                self.carInfoList = self.carInfo.split(' ')
                self.Show_carInfo()
                # self.textBrowser_message.append(f'客户端接收到小车状态{self.carInfo}')  # {self.recved.decode()}
                self.statusbar.showMessage(f'客户端接收到小车状态{self.carInfo}')  # {self.recved.decode()}
                # except Exception as e:
                #     self.textBrowser_message.append(f'解析失败:{str(e)}')
        except Exception as e:
            self.textBrowser_message.append(f'解析失败:{str(e)}')

    def Show_carInfo(self):
        self.carX = self.carInfoList[0][:4]
        self.carY = self.carInfoList[1][:4]
        self.carYaw = self.carInfoList[2][:4]
        self.carAngularV = self.carInfoList[3][:4]
        self.carLinearV = self.carInfoList[4][:4]
        self.carStatus = self.carInfoList[5]
        M = {'1': '初始化',
             '2': '前往装货',
             '3': '红绿灯',
             '4': '坡路',
             '5': '前往卸货',
             '6': '避障',
             '7': 'S路',
             '8': '倒车',
             '9': '前往初始区'
             }

        self.lineEdit_carX.setText(self.carX)
        self.lineEdit_carY.setText(self.carY)
        self.lineEdit_carYaw.setText(self.carYaw)
        self.lineEdit_carAngularV.setText(self.carAngularV)
        self.lineEdit_carLinearV.setText(self.carLinearV)
        self.lineEdit_carStatus.setText(M[self.carStatus])
        # self.textBrowser_message.append(self.carStatus)

    def ShowCamera(self):
        # 在 label 中显示
        ratio1 = self.camera_img.width() / self.label_video.width()  # (label 宽度)
        ratio2 = self.camera_img.height() / self.label_video.height()  # (label高度)
        ration = max(ratio1, ratio2)
        self.camera_img.setDevicePixelRatio(ration)

        self.label_video.setPixmap(self.camera_img)

    def SetFonts(self, widget):
        font, ok = QFontDialog.getFont()
        if ok:
            # for widget_ in widget.findChildren():
            widget.setFont(font)
            self.textBrowser_message.append(f'设置消息框字体为:'
                                            f'{widget.font().family(), widget.font().pointSize(), "Bold" if widget.font().bold() else ""}')

    def ShowAbout(self):
        about_text = """
        <html>
            <head>
                <style>
                    p { color:#FF23CC; }
                    body{font-family: "方正喵呜"; }
                </style>
            </head>
            <body>
                <h2>智能车调度软件 v1.0</h2>
                <p>参赛队伍: 风驰电掣</p>
                <p>所属学校: 华北电力大学(保定)</p>
                <p>要了解更多信息，请访问<a href="https://github.com/zhengyinloong/qingzhou_shangweiji">https://github.com/zhengyinloong</a></p>
            </body>
        </html>
        """

        QMessageBox.about(self, "关于", about_text)

    def QuitApp(self):
        # self.Timer.Stop()
        # ============ ADD ===========
        self.textBrowser_message.append('Exiting the application..')

        # QCoreApplication.quit()
        QCoreApplication.exit(0)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 设置其窗口尺寸显示正常
    app = QApplication(sys.argv)
    # app.setStyle('fusion')  # 设置 fusion 风格
    # app.setStyle('windows')  # 设置 windows 风格
    app.setStyle('windowsvista')  # 设置 windowsvista 风格
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
