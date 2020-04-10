# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showqa.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys 
import resource_rc
import math
import random
from PyQt5 import QtCore , QtGui , QtWidgets 
from PyQt5.QtWidgets import QDialog , QMainWindow , QWidget , QLCDNumber , QMessageBox ,QTableWidget, QHBoxLayout, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap, QIntValidator, QFont


class ShowQa(QDialog):
    def __init__(self, just_fun,problems,answers,problemsnum,answersnum,numall,sigforqa,ordernum,problems2,answers2,problemsnum2,answersnum2,numall2,sigforqa2,ordernum2):
        super().__init__()
        # 题库显示的信息
        self.problemstr = problems[:]
        self.answerstr = answers[:]
        self.numofproblem = problemsnum
        self.numofanswer = answersnum
        self.numforall = numall
        self.sigforall = sigforqa[:]
        self.order = ordernum[:]
        self.problemstr2 = problems2[:]
        self.answerstr2 = answers2[:]
        self.numofproblem2 = problemsnum2
        self.numofanswer2 = answersnum2
        self.numforall2 = numall2
        self.sigforall2 = sigforqa2[:]
        self.order2 = ordernum2[:]
        self.setupUi(just_fun) #界面绘制交给InitUi方法
    
    #建立起数值与符号图片之间的映射，便于显示图片
    def numtopicture(self,inputnum):
        temnum = inputnum
        if temnum == 0:
            str = "./emp.png" #空图
        elif temnum == 1:
            str = "./plus.png" #加号
        elif temnum == 2:
            str = "./min.png" #减号
        elif temnum == 3:
            str = "./mul.png" #乘号
        elif temnum == 4:
            str = "./equ.png" #等号
        else:
            str = "./emp.png"
        return str
    
    #显示问题与答案的等式
    def dispalyqa(self):
        tabnum = self.tabWidget.currentIndex()
        if tabnum == 0:
            item = self.displaytable.selectedItems()
            rownum = item[0].row()
            numinorigin = self.order[rownum]
            numten1 = self.numofproblem[numinorigin][1] // 10
            numone1 = self.numofproblem[numinorigin][1] % 10
            numten2 = self.numofproblem[numinorigin][2] // 10
            numone2 = self.numofproblem[numinorigin][2] % 10
            numten3 = self.numofproblem[numinorigin][3] // 10
            numone3 = self.numofproblem[numinorigin][3] % 10
            if numten1 == 0:
                self.show1num1.display('')
            else:
                self.show1num1.display(numten1)
            if numten2 == 0:
                self.show2num1.display('')
            else:
                self.show2num1.display(numten2)
            if numten3 == 0:
                self.show3num1.display('')
            else:
                self.show3num1.display(numten3)
            self.show1num2.display(numone1)
            self.show2num2.display(numone2)
            self.show3num2.display(numone3)
            temppix1 = QPixmap(self.numtopicture(self.numofproblem[numinorigin][0] + 1))
            self.showsign1.setPixmap(temppix1)
            temppix2 = QPixmap("./equ.png")
            self.showsign2.setPixmap(temppix2)
            
            rnumten1 = self.numofanswer[numinorigin][1] // 10
            rnumone1 = self.numofanswer[numinorigin][1] % 10
            rnumten2 = self.numofanswer[numinorigin][2] // 10
            rnumone2 = self.numofanswer[numinorigin][2] % 10
            rnumten3 = self.numofanswer[numinorigin][3] // 10
            rnumone3 = self.numofanswer[numinorigin][3] % 10
            if rnumten1 == 0:
                self.result1num1.display('')
            else:
                self.result1num1.display(rnumten1)
            if rnumten2 == 0:
                self.result2num1.display('')
            else:
                self.result2num1.display(rnumten2)
            if rnumten3 == 0:
                self.result3num1.display('')
            else:
                self.result3num1.display(rnumten3)
            self.result1num2.display(rnumone1)
            self.result2num2.display(rnumone2)
            self.result3num2.display(rnumone3)
            temppix1 = QPixmap(self.numtopicture(self.numofanswer[numinorigin][0] + 1))
            self.resultsign1.setPixmap(temppix1)
            temppix2 = QPixmap("./equ.png")
            self.resultsign2.setPixmap(temppix2)
        else:
            item = self.displaytable2.selectedItems()
            rownum = item[0].row()
            numinorigin = self.order2[rownum]
            numten1 = self.numofproblem2[numinorigin][1] // 10
            numone1 = self.numofproblem2[numinorigin][1] % 10
            numten2 = self.numofproblem2[numinorigin][2] // 10
            numone2 = self.numofproblem2[numinorigin][2] % 10
            numten3 = self.numofproblem2[numinorigin][3] // 10
            numone3 = self.numofproblem2[numinorigin][3] % 10
            if numten1 == 0:
                self.show1num1.display('')
            else:
                self.show1num1.display(numten1)
            if numten2 == 0:
                self.show2num1.display('')
            else:
                self.show2num1.display(numten2)
            if numten3 == 0:
                self.show3num1.display('')
            else:
                self.show3num1.display(numten3)
            self.show1num2.display(numone1)
            self.show2num2.display(numone2)
            self.show3num2.display(numone3)
            temppix1 = QPixmap(self.numtopicture(self.numofproblem2[numinorigin][0] + 1))
            self.showsign1.setPixmap(temppix1)
            temppix2 = QPixmap("./equ.png")
            self.showsign2.setPixmap(temppix2)
            
            rnumten1 = self.numofanswer2[numinorigin][1] // 10
            rnumone1 = self.numofanswer2[numinorigin][1] % 10
            rnumten2 = self.numofanswer2[numinorigin][2] // 10
            rnumone2 = self.numofanswer2[numinorigin][2] % 10
            rnumten3 = self.numofanswer2[numinorigin][3] // 10
            rnumone3 = self.numofanswer2[numinorigin][3] % 10
            if rnumten1 == 0:
                self.result1num1.display('')
            else:
                self.result1num1.display(rnumten1)
            if rnumten2 == 0:
                self.result2num1.display('')
            else:
                self.result2num1.display(rnumten2)
            if rnumten3 == 0:
                self.result3num1.display('')
            else:
                self.result3num1.display(rnumten3)
            self.result1num2.display(rnumone1)
            self.result2num2.display(rnumone2)
            self.result3num2.display(rnumone3)
            temppix1 = QPixmap(self.numtopicture(self.numofanswer2[numinorigin][0] + 1))
            self.resultsign1.setPixmap(temppix1)
            temppix2 = QPixmap("./equ.png")
            self.resultsign2.setPixmap(temppix2)
                
    #清空显示
    def dispalyclear(self):
        #数字置零
        self.show1num2.display(0)
        self.show2num2.display(0)
        self.show3num2.display(0)
        self.show1num1.display(0)
        self.show2num1.display(0)
        self.show3num1.display(0)
        self.result1num2.display(0)
        self.result2num2.display(0)
        self.result3num2.display(0)
        self.result1num1.display(0)
        self.result2num1.display(0)
        self.result3num1.display(0)
        #符号置空
        temppix = QPixmap("./emp.png")
        self.resultsign1.setPixmap(temppix)
        self.resultsign2.setPixmap(temppix)
        self.showsign1.setPixmap(temppix)
        self.showsign2.setPixmap(temppix)
    
    #初始化
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(622, 641)
        self.show1num1 = QtWidgets.QLCDNumber(Dialog)
        self.show1num1.setGeometry(QtCore.QRect(20, 380, 51, 91))
        self.show1num1.setDigitCount(1)
        self.show1num1.setObjectName("show1num1")
        self.show1num2 = QtWidgets.QLCDNumber(Dialog)
        self.show1num2.setGeometry(QtCore.QRect(80, 380, 51, 91))
        self.show1num2.setDigitCount(1)
        self.show1num2.setObjectName("show1num2")
        self.show2num1 = QtWidgets.QLCDNumber(Dialog)
        self.show2num1.setGeometry(QtCore.QRect(250, 380, 51, 91))
        self.show2num1.setDigitCount(1)
        self.show2num1.setObjectName("show2num1")
        self.show2num2 = QtWidgets.QLCDNumber(Dialog)
        self.show2num2.setGeometry(QtCore.QRect(310, 380, 51, 91))
        self.show2num2.setDigitCount(1)
        self.show2num2.setObjectName("show2num2")
        self.show3num1 = QtWidgets.QLCDNumber(Dialog)
        self.show3num1.setGeometry(QtCore.QRect(480, 380, 51, 91))
        self.show3num1.setDigitCount(1)
        self.show3num1.setObjectName("show3num1")
        self.show3num2 = QtWidgets.QLCDNumber(Dialog)
        self.show3num2.setGeometry(QtCore.QRect(540, 380, 51, 91))
        self.show3num2.setDigitCount(1)
        self.show3num2.setObjectName("show3num2")
        self.showsign1 = QtWidgets.QLabel(Dialog)
        self.showsign1.setGeometry(QtCore.QRect(170, 400, 41, 51))
        self.showsign1.setScaledContents(True)
        self.showsign1.setObjectName("showsign1")
        self.showsign2 = QtWidgets.QLabel(Dialog)
        self.showsign2.setGeometry(QtCore.QRect(410, 400, 41, 51))
        self.showsign2.setScaledContents(True)
        self.showsign2.setObjectName("showsign2")
        self.resultsign1 = QtWidgets.QLabel(Dialog)
        self.resultsign1.setGeometry(QtCore.QRect(170, 540, 41, 51))
        self.resultsign1.setScaledContents(True)
        self.resultsign1.setObjectName("resultsign1")
        self.result1num1 = QtWidgets.QLCDNumber(Dialog)
        self.result1num1.setGeometry(QtCore.QRect(20, 520, 51, 91))
        self.result1num1.setDigitCount(1)
        self.result1num1.setObjectName("result1num1")
        self.result3num1 = QtWidgets.QLCDNumber(Dialog)
        self.result3num1.setGeometry(QtCore.QRect(480, 520, 51, 91))
        self.result3num1.setDigitCount(1)
        self.result3num1.setObjectName("result3num1")
        self.result3num2 = QtWidgets.QLCDNumber(Dialog)
        self.result3num2.setGeometry(QtCore.QRect(540, 520, 51, 91))
        self.result3num2.setDigitCount(1)
        self.result3num2.setObjectName("result3num2")
        self.result2num2 = QtWidgets.QLCDNumber(Dialog)
        self.result2num2.setGeometry(QtCore.QRect(310, 520, 51, 91))
        self.result2num2.setDigitCount(1)
        self.result2num2.setObjectName("result2num2")
        self.result1num2 = QtWidgets.QLCDNumber(Dialog)
        self.result1num2.setGeometry(QtCore.QRect(80, 520, 51, 91))
        self.result1num2.setDigitCount(1)
        self.result1num2.setObjectName("result1num2")
        self.result2num1 = QtWidgets.QLCDNumber(Dialog)
        self.result2num1.setGeometry(QtCore.QRect(250, 520, 51, 91))
        self.result2num1.setDigitCount(1)
        self.result2num1.setObjectName("result2num1")
        self.resultsign2 = QtWidgets.QLabel(Dialog)
        self.resultsign2.setGeometry(QtCore.QRect(410, 540, 41, 51))
        self.resultsign2.setScaledContents(True)
        self.resultsign2.setObjectName("resultsign2")
        self.problem = QtWidgets.QLabel(Dialog)
        self.problem.setGeometry(QtCore.QRect(30, 350, 71, 21))
        self.problem.setScaledContents(False)
        self.problem.setObjectName("problem")
        self.answer = QtWidgets.QLabel(Dialog)
        self.answer.setGeometry(QtCore.QRect(30, 490, 71, 21))
        self.answer.setScaledContents(False)
        self.answer.setObjectName("answer")
        self.confirm = QtWidgets.QPushButton(Dialog)
        self.confirm.setGeometry(QtCore.QRect(160, 310, 93, 28))
        self.confirm.setObjectName("confirm")
        self.clearall = QtWidgets.QPushButton(Dialog)
        self.clearall.setGeometry(QtCore.QRect(350, 310, 93, 28))
        self.clearall.setObjectName("clearall")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(70, 10, 471, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.displaytable = QtWidgets.QTableWidget(self.tab)
        self.displaytable.setGeometry(QtCore.QRect(100, 10, 280, 241))
        self.displaytable.setObjectName("displaytable")
        self.displaytable.setColumnCount(2)
        self.displaytable.setRowCount(self.numforall)
        item = QtWidgets.QTableWidgetItem()
        self.displaytable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.displaytable.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.displaytable2 = QtWidgets.QTableWidget(self.tab_2)
        self.displaytable2.setGeometry(QtCore.QRect(100, 10, 280, 241))
        self.displaytable2.setObjectName("displaytable2")
        self.displaytable2.setColumnCount(2)
        self.displaytable2.setRowCount(self.numforall2)
        item = QtWidgets.QTableWidgetItem()
        self.displaytable2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.displaytable2.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.tab_2, "")
        #样式变化
        self.confirm.setStyleSheet("QPushButton{border-image: url(button.png)}"
         "QPushButton:hover{border-image: url(buttonon.png)}"
         "QPushButton:pressed{border-image: url(buttonpre.png)}")
        self.confirm.setFont(QFont("方正经黑简体", 12))
        self.clearall.setStyleSheet("QPushButton{border-image: url(button.png)}"
         "QPushButton:hover{border-image: url(buttonon.png)}"
         "QPushButton:pressed{border-image: url(buttonpre.png)}")
        self.clearall.setFont(QFont("方正经黑简体", 12))
        self.problem.setFont(QFont("方正清刻本悦宋简体",13))
        self.answer.setFont(QFont("方正清刻本悦宋简体",13))
        self.show1num1.setSegmentStyle(QLCDNumber.Flat)
        self.show1num1.setStyleSheet("border: 1px #ead273; color: #cb2d2d;")
        self.show2num1.setSegmentStyle(QLCDNumber.Flat)
        self.show2num1.setStyleSheet("border: 1px #ead273; color: #cb2d2d;")
        self.show3num1.setSegmentStyle(QLCDNumber.Flat)
        self.show3num1.setStyleSheet("border: 1px #ead273; color: #cb2d2d;")
        self.show1num2.setSegmentStyle(QLCDNumber.Flat)
        self.show1num2.setStyleSheet("border: 1px #ead273; color: #030000;")
        self.show2num2.setSegmentStyle(QLCDNumber.Flat)
        self.show2num2.setStyleSheet("border: 1px #ead273; color: #030000;")
        self.show3num2.setSegmentStyle(QLCDNumber.Flat)
        self.show3num2.setStyleSheet("border: 1px #ead273; color: #030000;")
        self.result1num1.setSegmentStyle(QLCDNumber.Flat)
        self.result1num1.setStyleSheet("border: 1px #ead273; color: #cb2d2d;")
        self.result2num1.setSegmentStyle(QLCDNumber.Flat)
        self.result2num1.setStyleSheet("border: 1px #ead273; color: #cb2d2d;")
        self.result3num1.setSegmentStyle(QLCDNumber.Flat)
        self.result3num1.setStyleSheet("border: 1px #ead273; color: #cb2d2d;")
        self.result1num2.setSegmentStyle(QLCDNumber.Flat)
        self.result1num2.setStyleSheet("border: 1px #ead273; color: #030000;")
        self.result2num2.setSegmentStyle(QLCDNumber.Flat)
        self.result2num2.setStyleSheet("border: 1px #ead273; color: #030000;")
        self.result3num2.setSegmentStyle(QLCDNumber.Flat)
        self.result3num2.setStyleSheet("border: 1px #ead273; color: #030000;")
        self.tabWidget.setStyleSheet("QTabWidget::pane{border: 1px;background:transparent;}"
                                     "QTabWidget::tab-bar{background:transparent;subcontrol-position:center;}"
                                     "QTabBar::tab{min-width:30px;min-height:10px;background:transparent;}"
                                     "QTabBar::tab:selected{color: rgb(16,3,3);background:rgb(192,108,34);}"
                                     "QTabBar::tab:!selected{color: rgb(16,3,3);background:rgb(217,159,68);}"
                                     "QTabBar::tab:hover{color: rgb(16,3,3);background:rgb(209,206,81);}")
        self.displaytable.setStyleSheet("QTableWidget{border:none;background-color:#FFFFFF;}"
                                        "QTableWidget::item{border-bottom:1px solid #DEE1E4;}"
                                        "QTableWidget::item:selected{background-color:#F4F4F4;color:#444444;}")
        self.displaytable.horizontalScrollBar().setStyleSheet("QScrollBar{background:transparent; height:10px;}"
                                                        "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
                                                        "QScrollBar::handle:hover{background:gray;}"
                                                        "QScrollBar::sub-line{background:transparent;}"
                                                        "QScrollBar::add-line{background:transparent;}");
        self.displaytable.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}"
                                                     "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
                                                    "QScrollBar::handle:hover{background:gray;}"
                                                    "QScrollBar::sub-line{background:transparent;}"
                                                    "QScrollBar::add-line{background:transparent;}");
        self.displaytable.setShowGrid(False)
        self.displaytable.setFrameShape(QFrame.NoFrame)
        self.displaytable2.setStyleSheet("QTableWidget{border:none;background-color:#FFFFFF;}"
                                        "QTableWidget::item{border-bottom:1px solid #DEE1E4;}"
                                        "QTableWidget::item:selected{background-color:#F4F4F4;color:#444444;}")
        self.displaytable2.horizontalScrollBar().setStyleSheet("QScrollBar{background:transparent; height:10px;}"
                                                        "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
                                                        "QScrollBar::handle:hover{background:gray;}"
                                                        "QScrollBar::sub-line{background:transparent;}"
                                                        "QScrollBar::add-line{background:transparent;}");
        self.displaytable2.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}"
                                                     "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
                                                    "QScrollBar::handle:hover{background:gray;}"
                                                    "QScrollBar::sub-line{background:transparent;}"
                                                    "QScrollBar::add-line{background:transparent;}");
        self.displaytable2.setShowGrid(False)
        self.displaytable2.setFrameShape(QFrame.NoFrame)
        self.displaytable.horizontalHeader().setFont(QFont("方正经黑简体",12))
        self.displaytable2.horizontalHeader().setFont(QFont("方正经黑简体",12))
        self.displaytable2.verticalHeader().setFont(QFont("方正经黑简体",10))
        self.displaytable.verticalHeader().setFont(QFont("方正经黑简体",10))
        self.tabWidget.setFont(QFont("方正经黑简体",12))
        self.displaytable.setFont(QFont("方正经黑简体",10))
        self.displaytable2.setFont(QFont("方正经黑简体",10))
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.confirm.clicked.connect(self.dispalyqa)
        self.clearall.clicked.connect(self.dispalyclear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.showsign1.setText(_translate("Dialog", " "))
        self.showsign2.setText(_translate("Dialog", " "))
        self.resultsign1.setText(_translate("Dialog", " "))
        self.resultsign2.setText(_translate("Dialog", " "))
        self.problem.setText(_translate("Dialog", "题目："))
        self.answer.setText(_translate("Dialog", "答案："))
        self.confirm.setText(_translate("Dialog", "确定"))
        self.clearall.setText(_translate("Dialog", "清空"))
        item = self.displaytable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "题目"))
        item = self.displaytable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "答案"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "移动一根火柴棍"))
        item = self.displaytable2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "题目"))
        item = self.displaytable2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "答案"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "移动两根火柴棍"))
        for i in range(self.numforall):
                    newItem1 = QTableWidgetItem(self.problemstr[i])
                    newItem2 = QTableWidgetItem(self.answerstr[i])
                    newItem1.setTextAlignment(QtCore.Qt.AlignCenter)
                    newItem2.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.displaytable.setItem(i,0,newItem1)
                    self.displaytable.setItem(i,1,newItem2)
        for i in range(self.numforall2):
                    newItem1 = QTableWidgetItem(self.problemstr2[i])
                    newItem2 = QTableWidgetItem(self.answerstr2[i])
                    newItem1.setTextAlignment(QtCore.Qt.AlignCenter)
                    newItem2.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.displaytable2.setItem(i,0,newItem1)
                    self.displaytable2.setItem(i,1,newItem2)
