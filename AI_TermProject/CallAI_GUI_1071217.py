# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from AI_GUI_1071216 import *
from Robot import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.robot = Robot()

#以下為自定義的函數及新增內容
        self.BtnInputMap.clicked.connect(self.GetFile)
        self.BtnRenew.clicked.connect(self.GetValue)
        self.BtnUp.clicked.connect(self.Up)
        self.BtnDown.clicked.connect(self.Down)
        self.BtnRight.clicked.connect(self.Right)
        self.BtnLeft.clicked.connect(self.Left)
        self.BtnStart.clicked.connect(self.Start)
#        self.BtnAddTime.clicked.connect(self.AddTimeList)

# 跑路徑
    def Start(self):
        self.robot.getPath()
        print(len(self.robot.path_log))
        
#輸入圖片，設定檔案格式及開啟C槽根目錄下的檔案
#Map=Qlabel  (因為QWidget與QGraphicView沒有支援QPixmap)
#但是下面要畫矩形需要QWidget...
#不知道有沒有東西是支援兩種的
    def GetFile(self):
        fname,_=QFileDialog.getOpenFileName(self, 'Open file', 'C:\\',"Image files (*.jpg *.gif)")
        self.Map.setPixmap(QPixmap(fname))

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
#按鍵上下左右控制掃地機器人(尚未完成)==========================
    def Up(self):
        YValue=self.NowY.text()
        YValue=int(YValue)+1
        YValue=str(YValue)
        self.NowY.setText(YValue)
    def Down(self):
        YValue=self.NowY.text()
        YValue=int(YValue)-1
        YValue=str(YValue)
        self.NowY.setText(YValue)
    def Right(self):
        XValue=self.NowX.text()
        XValue=int(XValue)+1
        XValue=str(XValue)
        self.NowX.setText(XValue)
    def Left(self):
        XValue=self.NowX.text()
        XValue=int(XValue)-1
        XValue=str(XValue)
        self.NowX.setText(XValue)
#        YValue=int(YValue+1)      #這個是要怎麼加??????
 #       int (YValue, 10)=int(YValue, 10)+1
 #       a=int (YValue)
 #       YValue=int(a+1)
#===========================================================

#預約清掃功能(還在研究中)
#   def AddTimeList(self):
#        Time=text(dateTimeEdit)
#        self.TimeList.setPlaintext(Time)
    
    
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
    # demo = Drawing()
    # myWin.layout().addWidget(demo)

    sys.exit(app.exec_())  

