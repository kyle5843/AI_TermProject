# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\@@政大資訊科學在職\1-4-人工智慧\掃地機器人\GUI\AI_GUI_1071129.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1017, 702)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnInputMap = QtWidgets.QPushButton(self.centralwidget)
        self.BtnInputMap.setGeometry(QtCore.QRect(70, 10, 361, 31))
        self.BtnInputMap.setObjectName("BtnInputMap")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(700, 50, 297, 585))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Distance = QtWidgets.QLabel(self.formLayoutWidget)
        self.Distance.setText("")
        self.Distance.setObjectName("Distance")
        self.verticalLayout_2.addWidget(self.Distance)
        self.CleanTime = QtWidgets.QLabel(self.formLayoutWidget)
        self.CleanTime.setText("")
        self.CleanTime.setObjectName("CleanTime")
        self.verticalLayout_2.addWidget(self.CleanTime)
        self.CleanArea = QtWidgets.QLabel(self.formLayoutWidget)
        self.CleanArea.setText("")
        self.CleanArea.setObjectName("CleanArea")
        self.verticalLayout_2.addWidget(self.CleanArea)
        self.CleanFrequency = QtWidgets.QLabel(self.formLayoutWidget)
        self.CleanFrequency.setText("")
        self.CleanFrequency.setObjectName("CleanFrequency")
        self.verticalLayout_2.addWidget(self.CleanFrequency)
        self.Power = QtWidgets.QLabel(self.formLayoutWidget)
        self.Power.setText("")
        self.Power.setObjectName("Power")
        self.verticalLayout_2.addWidget(self.Power)
        self.GoalProbability = QtWidgets.QLabel(self.formLayoutWidget)
        self.GoalProbability.setText("")
        self.GoalProbability.setObjectName("GoalProbability")
        self.verticalLayout_2.addWidget(self.GoalProbability)
        self.CleanProbability = QtWidgets.QLabel(self.formLayoutWidget)
        self.CleanProbability.setText("")
        self.CleanProbability.setObjectName("CleanProbability")
        self.verticalLayout_2.addWidget(self.CleanProbability)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.dateTimeEdit.setTime(QtCore.QTime(0, 0, 0))
        self.dateTimeEdit.setMinimumDate(QtCore.QDate(2018, 12, 1))
        self.dateTimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.dateTimeEdit)
        self.BtnAddTime = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BtnAddTime.setObjectName("BtnAddTime")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.BtnAddTime)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_4.setItem(5, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.pushButton_7 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_7.setMouseTracking(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButton_8)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_4.setItem(8, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.BtnUp = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BtnUp.setObjectName("BtnUp")
        self.gridLayout.addWidget(self.BtnUp, 0, 1, 1, 1)
        self.BtnLeft = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BtnLeft.setObjectName("BtnLeft")
        self.gridLayout.addWidget(self.BtnLeft, 1, 0, 1, 1)
        self.BtnDown = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BtnDown.setObjectName("BtnDown")
        self.gridLayout.addWidget(self.BtnDown, 1, 1, 1, 1)
        self.BtnRight = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BtnRight.setObjectName("BtnRight")
        self.gridLayout.addWidget(self.BtnRight, 1, 2, 1, 1)
        self.formLayout_4.setLayout(10, QtWidgets.QFormLayout.SpanningRole, self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_4.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.TimeList = QtWidgets.QListView(self.formLayoutWidget)
        self.TimeList.setObjectName("TimeList")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.TimeList)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 560, 413, 87))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BtnRenew = QtWidgets.QPushButton(self.layoutWidget)
        self.BtnRenew.setObjectName("BtnRenew")
        self.gridLayout_2.addWidget(self.BtnRenew, 2, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 0, 6, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        self.RenewA = QtWidgets.QLineEdit(self.layoutWidget)
        self.RenewA.setObjectName("RenewA")
        self.gridLayout_2.addWidget(self.RenewA, 2, 5, 1, 1)
        self.RenewX = QtWidgets.QLineEdit(self.layoutWidget)
        self.RenewX.setObjectName("RenewX")
        self.gridLayout_2.addWidget(self.RenewX, 2, 0, 1, 1)
        self.RenewZ = QtWidgets.QLineEdit(self.layoutWidget)
        self.RenewZ.setObjectName("RenewZ")
        self.gridLayout_2.addWidget(self.RenewZ, 2, 2, 1, 1)
        self.RenewC = QtWidgets.QLineEdit(self.layoutWidget)
        self.RenewC.setObjectName("RenewC")
        self.gridLayout_2.addWidget(self.RenewC, 2, 7, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 7, 1, 1)
        self.RenewY = QtWidgets.QLineEdit(self.layoutWidget)
        self.RenewY.setObjectName("RenewY")
        self.gridLayout_2.addWidget(self.RenewY, 2, 1, 1, 1)
        self.RenewB = QtWidgets.QLineEdit(self.layoutWidget)
        self.RenewB.setObjectName("RenewB")
        self.gridLayout_2.addWidget(self.RenewB, 2, 6, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 5, 1, 1)
        self.NowX = QtWidgets.QLabel(self.layoutWidget)
        self.NowX.setText("")
        self.NowX.setObjectName("NowX")
        self.gridLayout_2.addWidget(self.NowX, 1, 0, 1, 1)
        self.NowY = QtWidgets.QLabel(self.layoutWidget)
        self.NowY.setText("")
        self.NowY.setObjectName("NowY")
        self.gridLayout_2.addWidget(self.NowY, 1, 1, 1, 1)
        self.NowZ = QtWidgets.QLabel(self.layoutWidget)
        self.NowZ.setText("")
        self.NowZ.setObjectName("NowZ")
        self.gridLayout_2.addWidget(self.NowZ, 1, 2, 1, 1)
        self.NowA = QtWidgets.QLabel(self.layoutWidget)
        self.NowA.setText("")
        self.NowA.setObjectName("NowA")
        self.gridLayout_2.addWidget(self.NowA, 1, 5, 1, 1)
        self.NowB = QtWidgets.QLabel(self.layoutWidget)
        self.NowB.setText("")
        self.NowB.setObjectName("NowB")
        self.gridLayout_2.addWidget(self.NowB, 1, 6, 1, 1)
        self.NowC = QtWidgets.QLabel(self.layoutWidget)
        self.NowC.setText("")
        self.NowC.setObjectName("NowC")
        self.gridLayout_2.addWidget(self.NowC, 1, 7, 1, 1)
        self.BtnStart = QtWidgets.QPushButton(self.centralwidget)
        self.BtnStart.setGeometry(QtCore.QRect(440, 10, 151, 31))
        self.BtnStart.setObjectName("BtnStart")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(530, 570, 101, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(530, 540, 61, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(450, 540, 71, 23))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(20, 530, 71, 23))
        self.label_19.setObjectName("label_19")
        self.Map = QtWidgets.QLabel(self.centralwidget)
        self.Map.setGeometry(QtCore.QRect(20, 70, 621, 431))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Map.setFont(font)
        self.Map.setObjectName("Map")
        self.Map.setStyleSheet("background-color: white")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1017, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_13.setBuddy(self.RenewY)
        self.label_16.setBuddy(self.RenewB)
        self.label_12.setBuddy(self.RenewX)
        self.label_17.setBuddy(self.RenewC)
        self.label_14.setBuddy(self.RenewZ)
        self.label_15.setBuddy(self.RenewA)
        self.Map.setBuddy(self.RenewA)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.BtnInputMap, self.dateTimeEdit)
        MainWindow.setTabOrder(self.dateTimeEdit, self.BtnAddTime)
        MainWindow.setTabOrder(self.BtnAddTime, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.pushButton_8)
        MainWindow.setTabOrder(self.pushButton_8, self.BtnUp)
        MainWindow.setTabOrder(self.BtnUp, self.BtnLeft)
        MainWindow.setTabOrder(self.BtnLeft, self.BtnDown)
        MainWindow.setTabOrder(self.BtnDown, self.BtnRight)
        MainWindow.setTabOrder(self.BtnRight, self.RenewX)
        MainWindow.setTabOrder(self.RenewX, self.RenewY)
        MainWindow.setTabOrder(self.RenewY, self.RenewZ)
        MainWindow.setTabOrder(self.RenewZ, self.RenewA)
        MainWindow.setTabOrder(self.RenewA, self.RenewB)
        MainWindow.setTabOrder(self.RenewB, self.RenewC)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AI_GUI"))
        self.BtnInputMap.setText(_translate("MainWindow", "輸入地圖"))
        self.label_5.setText(_translate("MainWindow", "移動距離"))
        self.label_4.setText(_translate("MainWindow", "清理時間"))
        self.label_6.setText(_translate("MainWindow", "掃地面積??"))
        self.label.setText(_translate("MainWindow", "執行掃地次數"))
        self.label_7.setText(_translate("MainWindow", "目前電量"))
        self.label_3.setText(_translate("MainWindow", "達成率"))
        self.label_2.setText(_translate("MainWindow", "清潔率"))
        self.label_10.setText(_translate("MainWindow", "預約清掃"))
        self.BtnAddTime.setText(_translate("MainWindow", "ADD"))
        self.label_11.setText(_translate("MainWindow", "禁區設置"))
        self.pushButton_7.setText(_translate("MainWindow", "掃這裡"))
        self.pushButton_8.setText(_translate("MainWindow", "不掃這裡"))
        self.label_9.setText(_translate("MainWindow", "遠程遙控"))
        self.BtnUp.setText(_translate("MainWindow", "UP"))
        self.BtnLeft.setText(_translate("MainWindow", "LEFT"))
        self.BtnDown.setText(_translate("MainWindow", "DOWN"))
        self.BtnRight.setText(_translate("MainWindow", "RIGHT"))
        self.BtnRenew.setText(_translate("MainWindow", "更新位置"))
        self.label_13.setText(_translate("MainWindow", "&y"))
        self.label_16.setText(_translate("MainWindow", "&b"))
        self.label_12.setText(_translate("MainWindow", "&x"))
        self.label_17.setText(_translate("MainWindow", "&c"))
        self.label_14.setText(_translate("MainWindow", "&z"))
        self.label_15.setText(_translate("MainWindow", "&a"))
        self.BtnStart.setText(_translate("MainWindow", "開始打掃"))
        self.label_18.setText(_translate("MainWindow", "目前時間"))
        self.label_19.setText(_translate("MainWindow", "目前位置"))
        self.Map.setText(_translate("MainWindow", "地圖在此(若檔案太小無法變大)"))

