# -*- coding: utf-8 -*-

import sys
import datetime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from AI_GUI import *
from Robot import *

BG_White = "background-color: white"
BG_Black = "background-color: black"
BG_BLUE = "background-color: blue"
BG_GRAY = "background-color: gray"
BG_BROWN = "background-color: brown"
BG_PURPLE = "background-color: purple"
BG_DirtyL3 = "background-color: darkgreen"
BG_DirtyL2 = "background-color: green"
BG_DirtyL1 = "background-color: darkcyan"
BG_Passed = "background-color: darkcyan"
BG_Robot = "background-color: deeppink"

class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        # robot
        self.robot = Robot()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move)
        self.clearTimes = 0
        self.startTime = 0

        # 以下為自定義的函數及新增內容
        self.BtnInputMap.clicked.connect(self.GetFile)
        self.BtnClearMap.clicked.connect(self.clearMap)
        self.BtnRenew.clicked.connect(self.GetValue)
        self.BtnUp.clicked.connect(self.Up)
        self.BtnDown.clicked.connect(self.Down)
        self.BtnRight.clicked.connect(self.Right)
        self.BtnLeft.clicked.connect(self.Left)
        self.BtnStart.clicked.connect(self.Start)
        self.BtnAddTime.clicked.connect(self.AddTimeList)
        self.BtnDelTime.clicked.connect(self.DelTimeList)

    # 跑路徑
    def Start(self):
        self.clearTimes = self.clearTimes + 1
        self.CleanFrequency.setText(str(self.clearTimes))
        self.startTime = datetime.datetime.now()
        self.robot.getPath()
        self.timer.start(100)

    def move(self):
        distance = self.robot.cleanSensor.distance
        if distance < len(self.robot.path_log):
            if (distance - 1) >= 0:
                pre_step = self.robot.path_log[distance - 1]
                self.drawMap(pre_step[0], pre_step[1], BG_Passed)
            step = self.robot.path_log[distance]
            self.updateStatus(step)

            x, y = step
            dirtyLevel = self.robot.cleanSensor.checkDirtyLevel(x, y)
            if dirtyLevel == 3:
                self.drawMap(x, y, BG_DirtyL3)
                self.robot.clean(x, y)
            elif dirtyLevel == 2:
                self.drawMap(x, y, BG_DirtyL2)
                self.robot.clean(x, y)
            elif dirtyLevel == 1:
                self.drawMap(x, y, BG_DirtyL1)
                self.robot.clean(x, y)
            else:
                self.drawMap(x, y, BG_Robot)
                self.robot.move()
        else:
            self.timer.stop()

    def updateStatus(self, step):
        # update Status
        self.Distance.setText(str(self.robot.cleanSensor.distance))
        x, y = step
        if step not in self.robot.clearArea:
            self.robot.clearArea.append(step)
            self.CleanArea.setText(str(len(self.robot.clearArea)))
        now = datetime.datetime.now()
        diffSeconds = (now - self.startTime).total_seconds()
        self.CleanTime.setText("{:.2f}".format(diffSeconds)+"秒")
        self.lcdNumber.display("{:.2f}".format(diffSeconds)+"秒")
        self.Power.setText("{:.2f}".format(self.robot.power)+"%")
        self.progressBar.setValue(self.robot.power)
        self.CleanProbability.setText("{:.2f}".format(100 * self.robot.cleanSensor.getTotalDirtyCleanPercentage()) + "%")
        self.GoalProbability.setText("{:.2f}".format(100 * self.robot.cleanSensor.getCleanAreaPercentage()) + "%")
        self.NowX.setText(str(x))
        self.NowY.setText(str(y))
        self.NowZ.setText(str(0))
        self.NowA.setText(str(self.robot.detectObstructionType(x, y)))
        self.NowB.setText(str(self.robot.cleanSensor.checkDirtyLevel(x, y)))
        self.NowC.setText(str(0))

    def drawMap(self, posX, posY, color):
        self.lableX = QtWidgets.QLabel(self.layoutWidget)
        self.lableX.setGeometry(QtCore.QRect(60 + 14*posX, 70 + 14*posY, 14, 14))
        self.lableX.setStyleSheet(color)
        self.layout().addWidget(self.lableX)

    def clearMap(self):
        for coordinate in self.robot.coordinate_list:
            if coordinate not in self.robot.impassable_coordinate_list:
                x, y = coordinate
                self.drawMap(x, y, BG_White)
        x, y = self.robot.current_coordinate
        self.Distance.setText("")
        self.CleanArea.setText("")
        self.GoalProbability.setText("")
        self.NowX.setText(str(x))
        self.NowY.setText(str(y))
        self.NowZ.setText("")
        self.NowA.setText("")
        self.NowB.setText("")
        self.NowC.setText("")
        self.drawMap(x, y, BG_Robot)
        self.robot.reset()

    def GetFile(self):
        for coordinate in self.robot.coordinate_list:
            self.drawMapWithColor(coordinate[0], coordinate[1])

        x, y = self.robot.start_coordinate
        self.drawMap(x, y, BG_Robot)
        self.NowX.setText(str(x))
        self.NowY.setText(str(y))
        self.NowZ.setText(str(0))
        self.NowA.setText(str(self.robot.detectObstructionType(x, y)))
        self.NowB.setText(str(self.robot.coordinate_data[x][y]['b']))
        self.NowC.setText(str(0))
        self.Power.setText("100%")
        self.CleanTime.setText("")
        self.lcdNumber.display("")
        self.CleanProbability.setText("")
        self.GoalProbability.setText("")
        self.repaint()

    def drawMapWithColor(self, x, y):
        obstructionType = self.robot.detectObstructionType(x, y)
        if obstructionType == 2: #毛毯
            self.drawMap(x, y, BG_BLUE)
        elif obstructionType == 3: #灰塵
            self.drawMap(x, y, BG_GRAY)
        elif obstructionType == 4: #毛髮
            self.drawMap(x, y, BG_PURPLE)
        elif obstructionType == 6: #家具
            self.drawMap(x, y, BG_BROWN)
        elif (x, y) in self.robot.impassable_coordinate_list: #牆壁
            self.drawMap(x, y, BG_Black)
        else:
            self.drawMap(x, y, BG_White)

    # 更新位置
    def GetValue(self):
        XValue=self.RenewX.text()
        self.NowX.setText(XValue)
        
        YValue=self.RenewY.text()
        self.NowY.setText(YValue)
        
        ZValue=self.RenewZ.text()
        self.NowZ.setText(ZValue)
        
        AValue=self.RenewA.text()
        self.NowA.setText(AValue)
        
        BValue=self.RenewB.text()
        self.NowB.setText(BValue)
        
        CValue=self.RenewC.text()
        self.NowC.setText(CValue)

        self.robot.start_coordinate = (int(XValue), int(YValue))
        self.robot.current_coordinate = (int(XValue), int(YValue))
        self.clearMap()

    # 按鍵上下左右控制掃地機器人
    def Up(self):
        if self.robot.check_up():
            self.drawMapWithColor(int(self.NowX.text()), int(self.NowY.text()))
            YValue=self.NowY.text()
            YValue=int(YValue)-1
            YValue=str(YValue)
            self.NowY.setText(YValue)
            self.moveStartPoint()
            self.repaint()

    def Down(self):
        if self.robot.check_down():
            self.drawMapWithColor(int(self.NowX.text()), int(self.NowY.text()))
            YValue=self.NowY.text()
            YValue=int(YValue)+1
            YValue=str(YValue)
            self.NowY.setText(YValue)
            self.moveStartPoint()
            self.repaint()

    def Right(self):
        if self.robot.check_right():
            self.drawMapWithColor(int(self.NowX.text()), int(self.NowY.text()))
            XValue=self.NowX.text()
            XValue=int(XValue)+1
            XValue=str(XValue)
            self.NowX.setText(XValue)
            self.moveStartPoint()
            self.repaint()

    def Left(self):
        if self.robot.check_left():
            self.drawMapWithColor(int(self.NowX.text()), int(self.NowY.text()))
            XValue=self.NowX.text()
            XValue=int(XValue)-1
            XValue=str(XValue)
            self.NowX.setText(XValue)
            self.moveStartPoint()
            self.repaint()

    def moveStartPoint(self):
        x = int(self.NowX.text())
        y = int(self.NowY.text())
        self.NowZ.setText(str(0))
        self.NowA.setText(str(self.robot.detectObstructionType(x, y)))
        self.NowB.setText(str(self.robot.cleanSensor.checkDirtyLevel(x, y)))
        self.NowC.setText(str(0))
        self.drawMap(x, y, BG_Robot)
        self.robot.start_coordinate = (x, y)
        self.robot.current_coordinate = (x, y)

    # 預約清掃功能(還沒有做鬧鐘功能)
    def AddTimeList(self):
        Year = self.dateTimeEdit.date().year()
        Month = self.dateTimeEdit.date().month()
        Day = self.dateTimeEdit.date().day()
        Hour = self.dateTimeEdit.time().hour()
        Minute = self.dateTimeEdit.time().minute()
        print(Year, '年', Month, '月', Day, '日', Hour, '時', Minute, '分')
        alarm = "%s年%s月%s日%s時%s分"%(Year, Month, Day, Hour, Minute)
        self.listWidget.addItem(str(alarm))
        # 要順便把加入的時間放到list或是array，方便之後做鬧鐘的功能
        '''
        #請參考https://blog.csdn.net/lmhuanying1012/article/details/78112907
        QStringList data;
        data << "Letter A" << "Letter B" << "Letter C";
        model = new QStringListModel(this);
        model->setStringList(data);
        '''
        # ===========================================================
    def DelTimeList(self):
        NowRow=self.listWidget.currentRow()
        self.listWidget.takeItem(NowRow)


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()

    sys.exit(app.exec_())  

