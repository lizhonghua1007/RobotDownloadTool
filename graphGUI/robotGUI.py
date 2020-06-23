# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robotGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.version = 'V2.0'
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 335)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 2, 5)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 6, 1, 1, 5)
        self.sourceHost = QtWidgets.QLineEdit(self.centralwidget)
        self.sourceHost.setObjectName("sourceHost")
        self.sourceHost.setReadOnly(True)
        self.gridLayout.addWidget(self.sourceHost, 2, 3, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.selectFile = QtWidgets.QPushButton(self.widget)
        self.selectFile.setGeometry(QtCore.QRect(40, 0, 81, 21))
        self.selectFile.setObjectName("selectFile")
        self.gridLayout.addWidget(self.widget, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(50, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 2, 1, 1)
        self.dstSSHTest = QtWidgets.QPushButton(self.centralwidget)
        self.dstSSHTest.setObjectName("dstSSHTest")
        self.gridLayout.addWidget(self.dstSSHTest, 3, 4, 1, 1)
        self.logView = QtWidgets.QTextEdit(self.centralwidget)
        self.logView.setObjectName("logView")
        self.gridLayout.addWidget(self.logView, 7, 0, 1, 6)
        spacerItem1 = QtWidgets.QSpacerItem(44, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(44, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 5, 2, 1)
        self.filePath = QtWidgets.QLineEdit(self.centralwidget)
        self.filePath.setMinimumSize(QtCore.QSize(0, 20))
        self.filePath.setObjectName("filePath")
        self.gridLayout.addWidget(self.filePath, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(44, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 2, 1)
        spacerItem4 = QtWidgets.QSpacerItem(50, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 2)
        self.dstHost = QtWidgets.QLineEdit(self.centralwidget)
        self.dstHost.setMinimumSize(QtCore.QSize(0, 20))
        self.dstHost.setObjectName("dstHost")
        self.gridLayout.addWidget(self.dstHost, 3, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(44, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 4, 5, 1, 1)
        self.branch = QtWidgets.QComboBox(self.centralwidget)
        self.branch.setObjectName("branch")
        self.gridLayout.addWidget(self.branch, 4, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(44, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 5, 1, 1)
        self.sourceSSHTest = QtWidgets.QPushButton(self.centralwidget)
        self.sourceSSHTest.setObjectName("sourceSSHTest")
        self.gridLayout.addWidget(self.sourceSSHTest, 2, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(50, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 0, 1, 2)
        self.commit = QtWidgets.QPushButton(self.centralwidget)
        self.commit.setObjectName("commit")
        self.gridLayout.addWidget(self.commit, 5, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "机器人软件安装及升级 " + self.version))
        self.selectFile.setText(_translate("MainWindow", "选择备份路径"))
        self.label_3.setText(_translate("MainWindow", "请选择分支:"))
        self.dstSSHTest.setText(_translate("MainWindow", "测试连接"))
        self.filePath.setText(_translate("MainWindow", "未选择路径"))
        self.label.setText(_translate("MainWindow", "源地址主机host:"))
        self.label_9.setText(_translate("MainWindow", "机器人主机host:"))
        self.sourceSSHTest.setText(_translate("MainWindow", "测试连接"))
        self.commit.setText(_translate("MainWindow", "下载"))

    def flush(self):
        return QtCore.QCoreApplication.processEvents()

    # 提醒消息弹框
    def messageBoxTip(self):
        messageBox = QtWidgets.QMessageBox()
        messageBox.information(self, '注意', '请先源地址测试连接，用以获取分支', messageBox.Yes)

    # 升级消息框
    def messageBoxinstall(self, brunch,hostname):
        messageBox = QtWidgets.QMessageBox()
        information = messageBox.question(self, '升级确认', '确定升级 ' + brunch + '分支到' + '<font size="5" color="red">' + hostname + '</font>' + '？', messageBox.Yes | messageBox.No,
                                              messageBox.No)
        return information

    def dirName(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(caption='选择备份路径',directory='/')
        return filename

    # sucess download
    def messageSuccessDownload(self):
        messageBox = QtWidgets.QMessageBox()
        information = messageBox.information(self,'结果','安装/升级成功',messageBox.Yes)

    def messageBoxDst(self):
        messageBox = QtWidgets.QMessageBox()
        information = messageBox.information(self,'提示','请对robot机器人测试连接',messageBox.Yes)


