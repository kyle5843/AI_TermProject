# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from AI_GUI import *
from Robot import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        # robot
        self.robot = Robot()
        self.move_distance = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move)

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
        self.robot.getPath()
        self.timer.start(30)

    def move(self):
        if self.move_distance < len(self.robot.path_log):
            if (self.move_distance-1) >= 0:
                pre_step = self.robot.path_log[self.move_distance-1]
                self.drawMap(pre_step[0], pre_step[1], "background-color: darkcyan")
            step = self.robot.path_log[self.move_distance]
            self.drawMap(step[0], step[1], "background-color: deeppink")
            self.move_distance = self.move_distance + 1
            self.updateStatus(step)

        else:
            self.timer.stop()

    def updateStatus(self, step):
        # update Status
        self.Distance.setText(str(self.move_distance))
        if step not in self.robot.clearArea:
            self.robot.clearArea.append(step)
            self.CleanArea.setText(str(len(self.robot.clearArea)))
        self.GoalProbability.setText(str("%.0f%%" % (100 * self.robot.cleanSensor.getCleanAreaPercentage(self.robot))))
        self.NowX.setText(str(step[0]))
        self.NowY.setText(str(step[1]))
        self.NowZ.setText(str(0))
        self.NowA.setText(str(self.robot.coordinate_data[step[0]][step[1]]['a']))
        self.NowB.setText(str(self.robot.coordinate_data[step[0]][step[1]]['b']))
        self.NowC.setText(str(self.robot.coordinate_data[step[0]][step[1]]['c']))

    def drawMap(self, posX, posY, color):
        self.lableX = QtWidgets.QLabel(self.layoutWidget)
        self.lableX.setGeometry(QtCore.QRect(60 + 14*posX, 70 + 14*posY, 14, 14))
        self.lableX.setStyleSheet(color)
        self.layout().addWidget(self.lableX)

    def clearMap(self):
        for coordinate in self.robot.coordinate_list:
            if coordinate not in self.robot.impassable_coordinate_list:
                x,y = coordinate
                self.drawMap(x, y, "background-color: white")
        self.Distance.setText("")
        self.CleanArea.setText("")
        self.GoalProbability.setText("")
        self.NowX.setText(str(self.robot.current_coordinate[0]))
        self.NowY.setText(str(self.robot.current_coordinate[1]))
        self.NowZ.setText("")
        self.NowA.setText("")
        self.NowB.setText("")
        self.NowC.setText("")
        self.move_distance = 0
        self.drawMap(self.robot.current_coordinate[0], self.robot.current_coordinate[1], "background-color: deeppink")
        self.robot.reset()

    def GetFile(self):
        for impassable in self.robot.impassable_coordinate_list:
            self.drawMap(impassable[0], impassable[1], "background-color: black")
        for coordinate in self.robot.coordinate_list:
            if coordinate not in self.robot.impassable_coordinate_list:
                if self.robot.coordinate_data[coordinate[0]][coordinate[1]]['a'] == 2:#毛毯
                    self.drawMap(coordinate[0], coordinate[1], "background-color: blue")
                elif self.robot.coordinate_data[coordinate[0]][coordinate[1]]['a'] == 3:#灰塵
                    self.drawMap(coordinate[0], coordinate[1], "background-color: yellow")
                elif self.robot.coordinate_data[coordinate[0]][coordinate[1]]['a'] == 4:#毛髮
                    self.drawMap(coordinate[0], coordinate[1], "background-color: pink")

        x, y = self.robot.start_coordinate
        self.drawMap(x, y, "background-color: deeppink")
        self.NowX.setText(str(x))
        self.NowY.setText(str(y))
        self.NowZ.setText(str(self.robot.coordinate_data[x][y]['z']))
        self.NowA.setText(str(self.robot.coordinate_data[x][y]['a']))
        self.NowB.setText(str(self.robot.coordinate_data[x][y]['b']))
        self.NowC.setText(str(self.robot.coordinate_data[x][y]['c']))
        self.repaint()

    def moveStartPoint(self):
        x = int(self.NowX.text())
        y = int(self.NowY.text())
        self.NowZ.setText(str(self.robot.coordinate_data[x][y]['z']))
        self.NowA.setText(str(self.robot.coordinate_data[x][y]['a']))
        self.NowB.setText(str(self.robot.coordinate_data[x][y]['b']))
        self.NowC.setText(str(self.robot.coordinate_data[x][y]['c']))
        self.drawMap(x, y, "background-color: deeppink")
        self.robot.start_coordinate = (x,y)
        self.robot.current_coordinate = (x,y)

#取出RenowXYZABC的數值，回傳給NowX.Y.Z.A.B.C
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
            self.drawMap(int(self.NowX.text()), int(self.NowY.text()), "background-color: white")
            YValue=self.NowY.text()
            YValue=int(YValue)-1
            YValue=str(YValue)
            self.NowY.setText(YValue)
            self.moveStartPoint()
            self.repaint()

    def Down(self):
        if self.robot.check_down():
            self.drawMap(int(self.NowX.text()), int(self.NowY.text()), "background-color: white")
            YValue=self.NowY.text()
            YValue=int(YValue)+1
            YValue=str(YValue)
            self.NowY.setText(YValue)
            self.moveStartPoint()
            self.repaint()

    def Right(self):
        if self.robot.check_right():
            self.drawMap(int(self.NowX.text()), int(self.NowY.text()), "background-color: white")
            XValue=self.NowX.text()
            XValue=int(XValue)+1
            XValue=str(XValue)
            self.NowX.setText(XValue)
            self.moveStartPoint()
            self.repaint()

    def Left(self):
        if self.robot.check_left():
            self.drawMap(int(self.NowX.text()), int(self.NowY.text()), "background-color: white")
            XValue=self.NowX.text()
            XValue=int(XValue)-1
            XValue=str(XValue)
            self.NowX.setText(XValue)
            self.moveStartPoint()
            self.repaint()

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
    # '''
    
    
#在地圖上面顯示掃地的路徑，並回傳到GUI的Map參數上面
#目前有這個功能，但是在另一個視窗= ="
class Drawing(QWidget):
    def paintEvent(self, e):
        Map = QPainter()
        Map.begin(self)
        self.drawLines(Map)
        Map.end()

    def drawLines(self, Map):
        brush = QBrush(Qt.SolidPattern)
        Map.setBrush(brush)  # 設定畫筆風格
        Map.drawRect(10, 15, 20, 40)  # 畫矩形(x,y,w,h)


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()

    print(myWin.robot.coordinate_data[0][1])
    print(myWin.robot.coordinate_data[0][1]['b'])

    sys.exit(app.exec_())  

