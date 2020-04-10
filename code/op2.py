# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operation.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys 
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import resource_rc
import math
import random
import showqa
from showqa import ShowQa
from PyQt5 import QtCore , QtGui , QtWidgets 
from PyQt5.QtWidgets import QDialog , QMainWindow , QWidget , QLCDNumber , QMessageBox
from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap, QIntValidator, QIcon, QFont, QPalette, QBrush

problem = []
answer = []
problemnum = []
answernum = []
num = []
sigforqa = []
order = []

problem2 = []
answer2 = []
problemnum2 = []
answernum2 = []
num2 = []
sigforqa2 = []
order2 = []
class Ui_just_fun(QWidget):
    #初始化
    def __init__(self, just_fun):
        super().__init__()
        #输入等式的数字与符号
        inputnum1 = 0
        inputnum2 = 0
        inputnum3 = 0
        inputsign1 = 0
        inputsign2 = 0
        #输出等式的数字与符号
        resultnum1 = 0
        resultnum2 = 0
        resultnum3 = 0
        resultsign1 = 0
        resultsign2 = 0
        #随机生成等式的来源
        self.randequ = []
        #0-13的数字分别对应0-9，+，-，×，=
        information = [[9,9,9,9,9,9,0,9,1,0,9,9,9,9],
                       [9,9,9,9,9,9,9,1,9,9,9,9,9,9],
                       [9,9,9,0,9,9,9,9,9,9,9,9,9,9],
                       [9,9,0,9,9,0,9,9,9,1,9,9,9,9],
                       [9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                       [9,9,9,0,9,9,1,9,9,1,9,9,9,9],
                       [0,9,9,9,9,-1,9,9,1,0,9,9,9,9],
                       [9,-1,9,9,9,9,9,9,9,9,9,9,9,9],
                       [-1,9,9,9,9,9,-1,9,9,-1,9,9,9,9],
                       [0,9,9,-1,9,-1,0,9,1,9,9,9,9,9],
                       [9,9,9,9,9,9,9,9,9,9,9,-1,9,0],
                       [9,9,9,9,9,9,9,9,9,9,1,9,9,1],
                       [9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                       [9,9,9,9,9,9,9,9,9,9,0,-1,9,9]]
        information2 = [[9,9,-1,-1,9,-1,0,9,1,0,9,9,9,9],
                        [9,9,9,9,2,9,9,9,9,9,9,9,9,9],
                        [1,9,9,0,9,0,1,9,2,1,9,9,9,9],
                        [1,9,0,9,-1,0,1,-2,2,1,9,9,9,9],
                        [9,-2,9,1,9,1,9,-1,9,2,9,9,9,9],
                        [1,9,0,0,-1,9,1,9,2,1,9,9,9,9],
                        [0,9,-1,-1,9,-1,9,9,1,0,9,9,9,9],
                        [9,-1,9,2,1,9,9,9,9,9,9,9,9,9],
                        [-1,9,-2,-2,9,-2,-1,9,9,-1,9,9,9,9],
                        [0,9,-1,-1,-2,-1,0,9,1,9,9,9,9,9],
                        [9,9,9,9,9,9,9,9,9,9,9,-1,0,0],
                        [9,9,9,9,9,9,9,9,9,9,1,9,9,9],
                        [9,9,9,9,9,9,9,9,9,9,0,-1,9,0],
                        [9,9,9,9,9,9,9,9,9,9,0,-1,0,9]] #移动两根火柴棍时数字变化情况的信息存储列表
        numofinfor = [3,1,1,3,0,3,4,1,3,5,2,2,0,2]
        numofinfor2 = [6,1,6,8,5,7,6,3,6,7,3,1,3,3] #每个数字可以变化的情况数量
        #以下均为移动一根火柴
        glaxy = [] #随机等式，100个
        glaxychange = [] #随机题目，100个
        sigforglaxy = [] #题目可解与否的标志
        strformula = [] #题目字符串
        stranswer = [] #答案字符串
        numstr = 0 #可解题目的个数
        ordernum = [] #可解题目在glaxychange中对应的序号
        #以下均为移动两根火柴
        glaxy2 = [] #随机等式，100个
        glaxychange2 = [] #随机题目，100个
        sigforglaxy2 = [] #题目可解与否的标志
        strformula2 = [] #题目字符串
        stranswer2 = [] #答案字符串
        numstr2 = 0 #可解题目的个数
        ordernum2 = [] #可解题目在glaxychange中对应的序号
        self.searesult = []
        self.searesultnum = 0
        self.exchangemes = []
        self.currentnum = 0
        self.evaluedifficulty = []
        #题目的生成，采用随机的方式生成题库，对应移动一根火柴
        for i in range(100):
            glaxy.append([])
            signforstr = random.randint(0,2) #0-2对应加减乘
            if signforstr == 0:
                sign = 1
                while sign == 1:
                    firstnum = random.randint(0,99)
                    secondnum = random.randint(0,99)
                    resultnum = firstnum + secondnum
                    if resultnum <= 99:
                        sign = 0
                glaxy[i].append(signforstr)
                glaxy[i].append(firstnum)
                glaxy[i].append(secondnum)
                glaxy[i].append(resultnum)
            elif signforstr == 1:
                sign = 1
                while sign == 1:
                    firstnum = random.randint(0,99)
                    secondnum = random.randint(0,99)
                    if firstnum >= secondnum:
                        sign = 0
                resultnum = firstnum - secondnum
                glaxy[i].append(signforstr)
                glaxy[i].append(firstnum)
                glaxy[i].append(secondnum)
                glaxy[i].append(resultnum)
            elif signforstr == 2:
                sign = 1
                while sign == 1:
                    firstnum = random.randint(0,99)
                    secondnum = random.randint(0,99)
                    resultnum = firstnum * secondnum
                    if resultnum <= 99:
                        sign = 0
                glaxy[i].append(signforstr)
                glaxy[i].append(firstnum)
                glaxy[i].append(secondnum)
                glaxy[i].append(resultnum)
        for i in range(100):
            glaxychange.append([])
            glaxychange[i].append(glaxy[i][0])
            glaxychange[i].append(glaxy[i][1])
            glaxychange[i].append(glaxy[i][2])
            glaxychange[i].append(glaxy[i][3])
        for i in range(100):
            numarr = [0,0,0,0,0,0,0,0]
            position0 = []
            nump0 = 0
            position1 = []
            nump1 = 0
            positionm1 = []
            numpm1 = 0
            numarr[2] = glaxychange[i][0] + 10
            numarr[0] = glaxychange[i][1] // 10
            numarr[1] = glaxychange[i][1] % 10
            numarr[3] = glaxychange[i][2] // 10
            numarr[4] = glaxychange[i][2] % 10
            numarr[5] = 13
            numarr[6] = glaxychange[i][3] // 10
            numarr[7] = glaxychange[i][3] % 10
            if numarr[0] == 0:
                numarr[0] = -1
            if numarr[3] == 0:
                numarr[3] = -1
            if numarr[6] == 0:
                numarr[6] = -1
            for j in range(8):
                if numarr[j] != -1:
                    for k in range(14):
                        if information[numarr[j]][k] == 1:
                            position1.append([j,k])
                            nump1 = nump1 + 1
            for j in range(8):
                if numarr[j] != -1:
                    for k in range(14):
                        if information[numarr[j]][k] == 0:
                            position0.append([j,k])
                            nump0 = nump0 + 1
            for j in range(8):
                if numarr[j] != -1:
                    for k in range(14):
                        if information[numarr[j]][k] == -1:
                            positionm1.append([j,k])
                            numpm1 = numpm1 + 1
                            
            flagforchange = 0
            chooseway = random.randint(0,1)
            if chooseway == 0 and nump0 != 0:
                chone = random.randint(0,nump0-1)
                numarr[position0[chone][0]] = position0[chone][1]
            elif chooseway == 1 and nump1 != 0 and numpm1 != 0:
                chone1 = random.randint(0,nump1-1)
                chonem1 = random.randint(0,numpm1-1)
                numarr[position1[chone1][0]] = position1[chone1][1]
                numarr[positionm1[chonem1][0]] = positionm1[chonem1][1]
            else:
                flagforchange = -1
            if numarr[5] != 13 or numarr[2] == 13:
                flagforchange = -1
            if numarr[5] != 13 and numarr[2] != 13:
                flagforchange = -1
            if numarr[5] == 13 and numarr[2] == 13:
                flagforchange = -1
            
            if numarr[0] == -1:
                numarr[0] = 0
            if numarr[3] == -1:
                numarr[3] = 0
            if numarr[6] == -1:
                numarr[6] = 0
            
            if flagforchange == -1:
                sigforglaxy.append(-1)
            else:
                sigforglaxy.append(0) 
                glaxychange[i][0] = numarr[2] - 10
                glaxychange[i][1] = numarr[0] * 10 + numarr[1]
                glaxychange[i][2] = numarr[3] * 10 + numarr[4]
                glaxychange[i][3] = numarr[6] * 10 + numarr[7]  
        for i in range(100):
            if sigforglaxy[i] == 0:
                if glaxychange[i][0] == 0:
                    tempstr = str(glaxychange[i][1]) + ' + ' + str(glaxychange[i][2]) + ' = ' + str(glaxychange[i][3])
                    strformula.append(tempstr)
                elif glaxychange[i][0] == 1:
                    tempstr = str(glaxychange[i][1]) + ' - ' + str(glaxychange[i][2]) + ' = ' + str(glaxychange[i][3])
                    strformula.append(tempstr)
                elif glaxychange[i][0] == 2:
                    tempstr = str(glaxychange[i][1]) + ' × ' + str(glaxychange[i][2]) + ' = ' + str(glaxychange[i][3])
                    strformula.append(tempstr)
                    
                if glaxy[i][0] == 0:
                    tempstr = str(glaxy[i][1]) + ' + ' + str(glaxy[i][2]) + ' = ' + str(glaxy[i][3])
                    stranswer.append(tempstr)
                elif glaxy[i][0] == 1:
                    tempstr = str(glaxy[i][1]) + ' - ' + str(glaxy[i][2]) + ' = ' + str(glaxy[i][3])
                    stranswer.append(tempstr)
                elif glaxy[i][0] == 2:
                    tempstr = str(glaxy[i][1]) + ' × ' + str(glaxy[i][2]) + ' = ' + str(glaxy[i][3])
                    stranswer.append(tempstr)
                numstr = numstr + 1
                ordernum.append(i)
        
        #题目的生成，采用随机的方式生成题库，对应移动两根火柴
        for i in range(100):
            glaxy2.append([])
            signforstr = random.randint(0,2) #0-2对应加减乘
            if signforstr == 0:
                sign = 1
                while sign == 1:
                    firstnum = random.randint(0,99)
                    secondnum = random.randint(0,99)
                    resultnum = firstnum + secondnum
                    if resultnum <= 99:
                        sign = 0
                glaxy2[i].append(signforstr)
                glaxy2[i].append(firstnum)
                glaxy2[i].append(secondnum)
                glaxy2[i].append(resultnum)
            elif signforstr == 1:
                sign = 1
                while sign == 1:
                    firstnum = random.randint(0,99)
                    secondnum = random.randint(0,99)
                    if firstnum >= secondnum:
                        sign = 0
                resultnum = firstnum - secondnum
                glaxy2[i].append(signforstr)
                glaxy2[i].append(firstnum)
                glaxy2[i].append(secondnum)
                glaxy2[i].append(resultnum)
            elif signforstr == 2:
                sign = 1
                while sign == 1:
                    firstnum = random.randint(0,99)
                    secondnum = random.randint(0,99)
                    resultnum = firstnum * secondnum
                    if resultnum <= 99:
                        sign = 0
                glaxy2[i].append(signforstr)
                glaxy2[i].append(firstnum)
                glaxy2[i].append(secondnum)
                glaxy2[i].append(resultnum)
        for i in range(100):
            glaxychange2.append([])
            glaxychange2[i].append(glaxy2[i][0])
            glaxychange2[i].append(glaxy2[i][1])
            glaxychange2[i].append(glaxy2[i][2])
            glaxychange2[i].append(glaxy2[i][3])
        for i in range(100):
            numarr = [0,0,0,0,0,0,0,0] #按位存储
            numarr[2] = glaxychange2[i][0] + 10
            numarr[0] = glaxychange2[i][1] // 10
            numarr[1] = glaxychange2[i][1] % 10
            numarr[3] = glaxychange2[i][2] // 10
            numarr[4] = glaxychange2[i][2] % 10
            numarr[5] = 13
            numarr[6] = glaxychange2[i][3] // 10
            numarr[7] = glaxychange2[i][3] % 10
            #输入数字十位位0则视为空
            if numarr[0] == 0:
                numarr[0] = -1
            if numarr[3] == 0:
                numarr[3] = -1
            if numarr[6] == 0:
                numarr[6] = -1
            #数字自身移动火柴棍的变化
            position0 = []
            nump0 = 0
            #数字加上一根火柴棍的变化
            position1 = []
            nump1 = 0
            #数字移去一根火柴棍的变化
            positionm1 = []
            numpm1 = 0
            #数字自身移动两根火柴棍的变化
            position02 = []
            nump02 = 0
            #数字加上一根火柴棍再自已移动一根的变化
            position1move = []
            nump1move = 0
            #数字移去一根火柴棍再自己移动一根的变化
            positionm1move = []
            numpm1move = 0
            #数字加上两根火柴棍的变化
            position2 = []
            nump2 = 0
            #数字移去两根火柴棍的变化
            positionm2 = []
            numpm2 = 0
            #position与nump赋值
            for j in range(8):
                if numarr[j] != -1:
                    for k in range(14):
                        if information[numarr[j]][k] == 1:
                            position1.append([j,k])
                            nump1 = nump1 + 1
            for j in range(8):
                if numarr[j] != -1:
                    for k in range(14):
                        if information[numarr[j]][k] == 0:
                            position0.append([j,k])
                            nump0 = nump0 + 1
            for j in range(8):
                if numarr[j] != -1:
                    for k in range(14):
                        if information[numarr[j]][k] == -1:
                            positionm1.append([j,k])
                            numpm1 = numpm1 + 1
            for j in range(8):
                if numarr[j] != -1:
                    for k in range(14):
                        if information2[numarr[j]][k] == 0:
                            position02.append([j,k])
                            nump02 = nump02 + 1
            for j in range(8):
                if numarr[j] != -1:
                    for k in range(14):
                        if information2[numarr[j]][k] == 1:
                            position1move.append([j,k])
                            nump1move = nump1move + 1
            for j in range(8):
                if numarr[j] != -1:
                    for k in range(14):
                        if information2[numarr[j]][k] == -1:
                            positionm1move.append([j,k])
                            numpm1move = numpm1move + 1
            for j in range(8):
                if numarr[j] != -1:
                    for k in range(14):
                        if information2[numarr[j]][k] == 2:
                            position2.append([j,k])
                            nump2 = nump2 + 1
            for j in range(8):
                if numarr[j] != -1:
                    for k in range(14):
                        if information2[numarr[j]][k] == -2:
                            positionm2.append([j,k])
                            numpm2 = numpm2 + 1
            flag = [0,0,0,0,0,0,0]
            flag1num = 0
            if nump02 != 0:
                flag[0] = 1
                flag1num = flag1num +1
            if nump2 != 0 and numpm2 != 0:
                flag[1] = 1
                flag1num = flag1num +1
            if nump2 != 0 and numpm1 >= 2: 
                flag[2] = 1
                flag1num = flag1num +1
            if numpm2 != 0 and nump1 >= 2:
                flag[3] = 1
                flag1num = flag1num +1
            if nump0 >=2:
                flag[4] = 1
                flag1num = flag1num +1
            if nump1 >= 2 and numpm1 >= 2:
                flag[5] = 1
                flag1num = flag1num +1
            if (nump0 != 0 and nump1 != 0 and numpm1 != 1 ) or (nump1move != 0 and numpm1 != 0 ) or (numpm1move != 0 and nump1 != 0):
                flag[6] = 1
                flag1num = flag1num +1
            chooseway = random.randint(0,flag1num - 1)
            numcount = 0
            for chosenone in range(7):
                if flag[chosenone] == 1:
                    numcount = numcount + 1
                if numcount == (chooseway + 1):
                    break
            flagforchange = 0
            if chosenone == 0:
                randnum = random.randint(0,nump02 - 1)
                numarr[position02[randnum][0]] = position02[randnum][1]
                if numarr[5] != 13 or numarr[2] == 13:
                    flagforchange = -1
                if numarr[5] != 13 and numarr[2] != 13:
                    flagforchange = -1
                if numarr[5] == 13 and numarr[2] == 13:
                    flagforchange = -1
                if numarr[0] == -1:
                    numarr[0] = 0
                if numarr[3] == -1:
                    numarr[3] = 0
                if numarr[6] == -1:
                    numarr[6] = 0
                if flagforchange == -1:
                    sigforglaxy2.append(-1)
                else:
                    sigforglaxy2.append(0)
                    glaxychange2[i][0] = numarr[2] - 10
                    glaxychange2[i][1] = numarr[0] * 10 + numarr[1]
                    glaxychange2[i][2] = numarr[3] * 10 + numarr[4]
                    glaxychange2[i][3] = numarr[6] * 10 + numarr[7]
            elif chosenone == 1:
                randnum1 = random.randint(0,nump2 - 1)
                randnum2 = random.randint(0,numpm2 - 1)
                rands = 0
                while position2[randnum1][0] == positionm2[randnum2][0] and rands <= 10:
                    randnum2 = random.randint(0,numpm2 - 1)
                    rands = rands + 1
                if position2[randnum1][0] == positionm2[randnum2][0]:
                    flagforchange = -1
                else:
                    numarr[position2[randnum1][0]] = position2[randnum1][1]
                    numarr[positionm2[randnum2][0]] = positionm2[randnum2][1]
                if numarr[5] != 13 or numarr[2] == 13:
                    flagforchange = -1
                if numarr[5] != 13 and numarr[2] != 13:
                    flagforchange = -1
                if numarr[5] == 13 and numarr[2] == 13:
                    flagforchange = -1
                if numarr[0] == -1:
                    numarr[0] = 0
                if numarr[3] == -1:
                    numarr[3] = 0
                if numarr[6] == -1:
                    numarr[6] = 0
                if flagforchange == -1:
                    sigforglaxy2.append(-1)
                else:
                    sigforglaxy2.append(0)
                    glaxychange2[i][0] = numarr[2] - 10
                    glaxychange2[i][1] = numarr[0] * 10 + numarr[1]
                    glaxychange2[i][2] = numarr[3] * 10 + numarr[4]
                    glaxychange2[i][3] = numarr[6] * 10 + numarr[7]
            elif chosenone == 2:
                randnum1 = random.randint(0,nump2 - 1)
                randnum2 = random.randint(0,numpm1 - 1)
                randnum3 = random.randint(0,numpm1 - 1)
                rands = 0
                while (position2[randnum1][0] == positionm1[randnum2][0] or position2[randnum1][0] == positionm1[randnum3][0] or positionm1[randnum2][0] == positionm1[randnum3][0] or randnum2 == randnum3)and rands <= 10:
                    randnum2 = random.randint(0,numpm1 - 1)
                    randnum3 = random.randint(0,numpm1 - 1)
                    rands = rands + 1
                if position2[randnum1][0] == positionm1[randnum2][0] or position2[randnum1][0] == positionm1[randnum3][0] or positionm1[randnum2][0] == positionm1[randnum3][0] or randnum2 == randnum3:
                    flagforchange = -1
                else:
                    numarr[position2[randnum1][0]] = position2[randnum1][1]
                    numarr[positionm1[randnum2][0]] = positionm1[randnum2][1]
                    numarr[positionm1[randnum3][0]] = positionm1[randnum3][1]
                if numarr[5] != 13 or numarr[2] == 13:
                    flagforchange = -1
                if numarr[5] != 13 and numarr[2] != 13:
                    flagforchange = -1
                if numarr[5] == 13 and numarr[2] == 13:
                    flagforchange = -1
                if numarr[0] == -1:
                    numarr[0] = 0
                if numarr[3] == -1:
                    numarr[3] = 0
                if numarr[6] == -1:
                    numarr[6] = 0
                if flagforchange == -1:
                    sigforglaxy2.append(-1)
                else:
                    sigforglaxy2.append(0)
                    glaxychange2[i][0] = numarr[2] - 10
                    glaxychange2[i][1] = numarr[0] * 10 + numarr[1]
                    glaxychange2[i][2] = numarr[3] * 10 + numarr[4]
                    glaxychange2[i][3] = numarr[6] * 10 + numarr[7]
            elif chosenone == 3:
                randnum1 = random.randint(0,numpm2 - 1)
                randnum2 = random.randint(0,nump1 - 1)
                randnum3 = random.randint(0,nump1 - 1)
                rands = 0
                while (positionm2[randnum1][0] == position1[randnum2][0] or positionm2[randnum1][0] == position1[randnum3][0] or position1[randnum2][0] == position1[randnum3][0] or randnum2 == randnum3)and rands <= 10:
                    randnum2 = random.randint(0,nump1 - 1)
                    randnum3 = random.randint(0,nump1 - 1)
                    rands = rands + 1
                if positionm2[randnum1][0] == position1[randnum2][0] or positionm2[randnum1][0] == position1[randnum3][0] or position1[randnum2][0] == position1[randnum3][0] or randnum2 == randnum3:
                    flagforchange = -1
                else:
                    numarr[positionm2[randnum1][0]] = positionm2[randnum1][1]
                    numarr[position1[randnum2][0]] = position1[randnum2][1]
                    numarr[position1[randnum3][0]] = position1[randnum3][1]
                if numarr[5] != 13 or numarr[2] == 13:
                    flagforchange = -1
                if numarr[5] != 13 and numarr[2] != 13:
                    flagforchange = -1
                if numarr[5] == 13 and numarr[2] == 13:
                    flagforchange = -1
                if numarr[0] == -1:
                    numarr[0] = 0
                if numarr[3] == -1:
                    numarr[3] = 0
                if numarr[6] == -1:
                    numarr[6] = 0
                if flagforchange == -1:
                    sigforglaxy2.append(-1)
                else:
                    sigforglaxy2.append(0)
                    glaxychange2[i][0] = numarr[2] - 10
                    glaxychange2[i][1] = numarr[0] * 10 + numarr[1]
                    glaxychange2[i][2] = numarr[3] * 10 + numarr[4]
                    glaxychange2[i][3] = numarr[6] * 10 + numarr[7]
            elif chosenone == 4:
                randnum1 = random.randint(0,nump0 - 1)
                randnum2 = random.randint(0,nump0 - 1)
                rands = 0
                while (position0[randnum1][0] == position0[randnum2][0] or randnum1 == randnum2) and rands <= 10:
                    randnum2 = random.randint(0,nump0 - 1)
                    rands = rands + 1
                if position0[randnum1][0] == position0[randnum2][0]:
                    flagforchange = -1
                else:
                    numarr[position0[randnum1][0]] = position0[randnum1][1]
                    numarr[position0[randnum2][0]] = position0[randnum2][1]
                if numarr[5] != 13 or numarr[2] == 13:
                    flagforchange = -1
                if numarr[5] != 13 and numarr[2] != 13:
                    flagforchange = -1
                if numarr[5] == 13 and numarr[2] == 13:
                    flagforchange = -1
                if numarr[0] == -1:
                    numarr[0] = 0
                if numarr[3] == -1:
                    numarr[3] = 0
                if numarr[6] == -1:
                    numarr[6] = 0
                if flagforchange == -1:
                    sigforglaxy2.append(-1)
                else:
                    sigforglaxy2.append(0)
                    glaxychange2[i][0] = numarr[2] - 10
                    glaxychange2[i][1] = numarr[0] * 10 + numarr[1]
                    glaxychange2[i][2] = numarr[3] * 10 + numarr[4]
                    glaxychange2[i][3] = numarr[6] * 10 + numarr[7]
            elif chosenone == 5:
                randnum1 = random.randint(0,nump1 - 1)
                randnum2 = random.randint(0,nump1 - 1)
                randnum3 = random.randint(0,numpm1 - 1)
                randnum4 = random.randint(0,numpm1 - 1)
                rands = 0
                while (position1[randnum1][0] == position1[randnum2][0] or position1[randnum1][0] == positionm1[randnum3][0] or position1[randnum1][0] == positionm1[randnum4][0] or position1[randnum2][0] == positionm1[randnum3][0] or position1[randnum2][0] == positionm1[randnum4][0] or positionm1[randnum3][0] == positionm1[randnum4][0] or randnum1 == randnum2 or randnum3 == randnum4) and rands <= 10:
                    randnum2 = random.randint(0,nump1 - 1)
                    randnum3 = random.randint(0,numpm1 - 1)
                    randnum4 = random.randint(0,numpm1 - 1)
                    rands = rands + 1
                if position1[randnum1][0] == position1[randnum2][0] or position1[randnum1][0] == positionm1[randnum3][0] or position1[randnum1][0] == positionm1[randnum4][0] or position1[randnum2][0] == positionm1[randnum3][0] or position1[randnum2][0] == positionm1[randnum4][0] or positionm1[randnum3][0] == positionm1[randnum4][0] or randnum1 == randnum2 or randnum3 == randnum4:
                    flagforchange = -1
                else:
                    numarr[position1[randnum1][0]] = position1[randnum1][1]
                    numarr[position1[randnum2][0]] = position1[randnum2][1]
                    numarr[positionm1[randnum3][0]] = positionm1[randnum3][1]
                    numarr[positionm1[randnum4][0]] = positionm1[randnum4][1]
                if numarr[5] != 13 or numarr[2] == 13:
                    flagforchange = -1
                if numarr[5] != 13 and numarr[2] != 13:
                    flagforchange = -1
                if numarr[5] == 13 and numarr[2] == 13:
                    flagforchange = -1
                if numarr[0] == -1:
                    numarr[0] = 0
                if numarr[3] == -1:
                    numarr[3] = 0
                if numarr[6] == -1:
                    numarr[6] = 0
                if flagforchange == -1:
                    sigforglaxy2.append(-1)
                else:
                    sigforglaxy2.append(0)
                    glaxychange2[i][0] = numarr[2] - 10
                    glaxychange2[i][1] = numarr[0] * 10 + numarr[1]
                    glaxychange2[i][2] = numarr[3] * 10 + numarr[4]
                    glaxychange2[i][3] = numarr[6] * 10 + numarr[7]
            elif chosenone == 6:
                modelnum = random.randint(0,2)
                if modelnum == 0:
                    if nump0 != 0 and nump1 != 0 and numpm1 != 1:
                        randnum1 = random.randint(0,nump0 - 1)
                        randnum2 = random.randint(0,nump1 - 1)
                        randnum3 = random.randint(0,numpm1 - 1)
                        rands = 0
                        while (position0[randnum1][0] == position1[randnum2][0] or position0[randnum1][0] == positionm1[randnum3][0] or position1[randnum2][0] == positionm1[randnum3][0] ) and rands <= 10:
                            randnum2 = random.randint(0,nump1 - 1)
                            randnum3 = random.randint(0,numpm1 - 1)
                            rands = rands + 1
                        if position0[randnum1][0] == position1[randnum2][0] or position0[randnum1][0] == positionm1[randnum3][0] or position1[randnum2][0] == positionm1[randnum3][0] :
                            flagforchange = -1
                        else:
                            numarr[position0[randnum1][0]] = position0[randnum1][1]
                            numarr[position1[randnum2][0]] = position1[randnum2][1]
                            numarr[positionm1[randnum3][0]] = positionm1[randnum3][1]
                    else:
                        flagforchange = -1
                    if numarr[5] != 13 or numarr[2] == 13:
                        flagforchange = -1
                    if numarr[5] != 13 and numarr[2] != 13:
                        flagforchange = -1
                    if numarr[5] == 13 and numarr[2] == 13:
                        flagforchange = -1
                    if numarr[0] == -1:
                        numarr[0] = 0
                    if numarr[3] == -1:
                        numarr[3] = 0
                    if numarr[6] == -1:
                        numarr[6] = 0
                    if flagforchange == -1:
                        sigforglaxy2.append(-1)
                    else:
                        sigforglaxy2.append(0)
                        glaxychange2[i][0] = numarr[2] - 10
                        glaxychange2[i][1] = numarr[0] * 10 + numarr[1]
                        glaxychange2[i][2] = numarr[3] * 10 + numarr[4]
                        glaxychange2[i][3] = numarr[6] * 10 + numarr[7]
                elif modelnum == 1:
                    if  nump1move != 0 and numpm1 != 0:
                        randnum1 = random.randint(0,nump1move - 1)
                        randnum2 = random.randint(0,numpm1 - 1)
                        rands = 0
                        while position1move[randnum1][0] == positionm1[randnum2][0] and rands <= 10:
                            randnum2 = random.randint(0,numpm1 - 1)
                            rands = rands + 1
                        if position1move[randnum1][0] == positionm1[randnum2][0]:
                            flagforchange = -1
                    else:
                        flagforchange = -1 
                    if numarr[5] != 13 or numarr[2] == 13:
                        flagforchange = -1
                    if numarr[5] != 13 and numarr[2] != 13:
                        flagforchange = -1
                    if numarr[5] == 13 and numarr[2] == 13:
                        flagforchange = -1
                    if numarr[0] == -1:
                        numarr[0] = 0
                    if numarr[3] == -1:
                        numarr[3] = 0
                    if numarr[6] == -1:
                        numarr[6] = 0
                    if flagforchange == -1:
                        sigforglaxy2.append(-1)
                    else:
                        sigforglaxy2.append(0)
                        glaxychange2[i][0] = numarr[2] - 10
                        glaxychange2[i][1] = numarr[0] * 10 + numarr[1]
                        glaxychange2[i][2] = numarr[3] * 10 + numarr[4]
                        glaxychange2[i][3] = numarr[6] * 10 + numarr[7]
                elif modelnum == 2:
                    if  numpm1move != 0 and nump1 != 0:
                        randnum1 = random.randint(0,numpm1move - 1)
                        randnum2 = random.randint(0,nump1 - 1)
                        rands = 0
                        while positionm1move[randnum1][0] == position1[randnum2][0] and rands <= 10:
                            randnum2 = random.randint(0,nump1 - 1)
                            rands = rands + 1
                        if positionm1move[randnum1][0] == position1[randnum2][0]:
                            flagforchange = -1
                    else:
                        flagforchange = -1 
                    if numarr[5] != 13 or numarr[2] == 13:
                        flagforchange = -1
                    if numarr[5] != 13 and numarr[2] != 13:
                        flagforchange = -1
                    if numarr[5] == 13 and numarr[2] == 13:
                        flagforchange = -1
                    if numarr[0] == -1:
                        numarr[0] = 0
                    if numarr[3] == -1:
                        numarr[3] = 0
                    if numarr[6] == -1:
                        numarr[6] = 0
                    if flagforchange == -1:
                        sigforglaxy2.append(-1)
                    else:
                        sigforglaxy2.append(0)
                        glaxychange2[i][0] = numarr[2] - 10
                        glaxychange2[i][1] = numarr[0] * 10 + numarr[1]
                        glaxychange2[i][2] = numarr[3] * 10 + numarr[4]
                        glaxychange2[i][3] = numarr[6] * 10 + numarr[7]
        for i in range(100):
            if sigforglaxy2[i] == 0:
                if glaxychange2[i][0] == 0:
                    tempstr = str(glaxychange2[i][1]) + ' + ' + str(glaxychange2[i][2]) + ' = ' + str(glaxychange2[i][3])
                    strformula2.append(tempstr)
                elif glaxychange2[i][0] == 1:
                    tempstr = str(glaxychange2[i][1]) + ' - ' + str(glaxychange2[i][2]) + ' = ' + str(glaxychange2[i][3])
                    strformula2.append(tempstr)
                elif glaxychange2[i][0] == 2:
                    tempstr = str(glaxychange2[i][1]) + ' × ' + str(glaxychange2[i][2]) + ' = ' + str(glaxychange2[i][3])
                    strformula2.append(tempstr)
                    
                if glaxy2[i][0] == 0:
                    tempstr = str(glaxy2[i][1]) + ' + ' + str(glaxy2[i][2]) + ' = ' + str(glaxy2[i][3])
                    stranswer2.append(tempstr)
                elif glaxy2[i][0] == 1:
                    tempstr = str(glaxy2[i][1]) + ' - ' + str(glaxy2[i][2]) + ' = ' + str(glaxy2[i][3])
                    stranswer2.append(tempstr)
                elif glaxy2[i][0] == 2:
                    tempstr = str(glaxy2[i][1]) + ' × ' + str(glaxy2[i][2]) + ' = ' + str(glaxy2[i][3])
                    stranswer2.append(tempstr)
                numstr2 = numstr2 + 1
                ordernum2.append(i)
        
        self.randequ = glaxy[:]
        global problem
        global answer
        global problemnum
        global answernum
        global num
        global sigforqa
        global order
        global problem2
        global answer2
        global problemnum2
        global answernum2
        global num2
        global sigforqa2
        global order2
        problem = strformula[:]
        answer = stranswer[:]
        answernum = glaxy[:]
        problemnum= glaxychange[:]
        num = numstr
        sigforqa = sigforglaxy[:]
        order = ordernum[:]
        problem2 = strformula2[:]
        answer2 = stranswer2[:]
        problemnum2 = glaxychange2[:]
        answernum2 = glaxy2[:]
        num2 = numstr2
        sigforqa2 = sigforglaxy2[:]
        order2 = ordernum2[:]
        
        self.setupUi(just_fun) #界面绘制交给InitUi方法
    
    #获取输入数字的值，并存储
    def getinputnum1(self):
        tempstr = self.firstnum.text()
        tempnum = int(tempstr)
        self.inputnum1 = tempnum
        return tempnum
    def getinputnum2(self):
        tempstr = self.secondnum.text()
        tempnum = int(tempstr)
        self.inputnum2 = tempnum
        return tempnum
    def getinputnum3(self):
        tempstr = self.resultnum.text()
        tempnum = int(tempstr)
        self.inputnum3 = tempnum
        return tempnum
    
    #获取输入符号的值，并存储，+，-，×，=分别对应数字值1,2,3,4
    def getinputsign1(self):
        tempvalue = self.symbol.currentIndex()
        self.inputsign1 = tempvalue
        return tempvalue
    def getinputsign2(self):
        tempvalue = 4 #此符号通常为等号，故赋值为4
        self.inputsign2 = tempvalue
        return tempvalue
    
    #存储每次计算的结果
    def setresult(self,num1,num2,num3,sign1,sign2):
        self.resultnum1 = num1
        self.resultnum2 = num2
        self.resultnum3 = num3
        self.resultsign1 = sign1
        self.resultsign2 = sign2
    
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
    
    #搜索结果（数字和符号）的显示
    def showresult(self):
        #按位显示，故将数字的十位与个位分别提取
        num1of10 = self.resultnum1 // 10
        if num1of10 == 0:
            num1of10 = ''
        num1of1 = self.resultnum1 % 10 
        num2of10 = self.resultnum2 // 10
        if num2of10 == 0:
            num2of10 = ''
        num2of1 = self.resultnum2 % 10 
        num3of10 = self.resultnum3 // 10
        if num3of10 == 0:
            num3of10 = ''
        num3of1 = self.resultnum3 % 10
        sign1 = self.resultsign1
        sign2 = self.resultsign2
        self.show1num1_2.display(num1of10)
        self.show1num2_2.display(num1of1)
        self.show2num1_2.display(num2of10)
        self.show2num2_2.display(num2of1)
        self.show3num1_2.display(num3of10)
        self.show3num2_2.display(num3of1)
        temppix1 = QPixmap(self.numtopicture(sign1))
        self.showsymbol2.setPixmap(temppix1)
        temppix2 = QPixmap(self.numtopicture(sign2))
        self.showsymbol2_2.setPixmap(temppix2)
    
    #输入的等式（数字和符号）的显示，其中数字一位一位显示（空输入不显示）
    def disshow1num1(self):
        currentstr = self.firstnum.text()
        if currentstr == '':
            currentnum = 0
            inputnum = 0
        else:
            currentnum = int(currentstr)
            inputnum = currentnum//10
            if inputnum == 0:
                inputnum = ''
        self.show1num1.display(inputnum)
    def disshow1num2(self):
        currentstr = self.firstnum.text()
        if currentstr == '':
            currentnum = 0
        else:
            currentnum = int(currentstr)
        inputnum = currentnum%10
        self.show1num2.display(inputnum)  
    def disshow2num1(self):
        currentstr = self.secondnum.text()
        if currentstr == '':
            currentnum = 0
            inputnum = 0
        else:
            currentnum = int(currentstr)
            inputnum = currentnum//10
            if inputnum == 0:
                inputnum = ''
        self.show2num1.display(inputnum)
    def disshow2num2(self):
        currentstr = self.secondnum.text()
        if currentstr == '':
            currentnum = 0
        else:
            currentnum = int(currentstr)
        inputnum = currentnum%10
        self.show2num2.display(inputnum)   
    def disshow3num1(self):
        currentstr = self.resultnum.text()
        if currentstr == '':
            currentnum = 0
            inputnum = 0
        else:
            currentnum = int(currentstr)
            inputnum = currentnum//10
            if inputnum == 0:
                inputnum = ''
        self.show3num1.display(inputnum)
    def disshow3num2(self):
        currentstr = self.resultnum.text()
        if currentstr == '':
            currentnum = 0
        else:
            currentnum = int(currentstr)
        inputnum = currentnum%10
        self.show3num2.display(inputnum)
    
    #获取用户选择的数学算符，并予以显示
    def setoperation(self):
        chooseone = self.symbol.currentIndex()
        if chooseone == 0:
            myPix1 = QPixmap("./emp.png")
            self.showsymbol.setPixmap(myPix1)
        elif chooseone == 1:
            myPix2 = QPixmap("./plus.png")
            self.showsymbol.setPixmap(myPix2)
        elif chooseone == 2:
            myPix3 = QPixmap("./min.png")
            self.showsymbol.setPixmap(myPix3)
        elif chooseone == 3:
            myPix4 = QPixmap("./mul.png")
            self.showsymbol.setPixmap(myPix4)
        elif chooseone == 4:
            myPix5 = QPixmap("./equ.png")
            self.showsymbol.setPixmap(myPix5)
        else:
            myPix6 = QPixmap("./emp.png")
            self.showsymbol.setPixmap(myPix6)
    
    #检测输入是否超过两位数，超过则报错
    def showerror(self):
        firststr = self.firstnum.text()
        if firststr == '':
            firstnu = 0
        else:
            firstnu = int(firststr)
        secondstr = self.secondnum.text()
        if secondstr == '':
            secondnu = 0
        else:
            secondnu = int(secondstr)
        resultstr = self.resultnum.text()
        if resultstr == '':
            resultnu = 0
        else:
            resultnu = int(resultstr)
        #输入数字只能为两位数
        if firstnu > 99:
            ershow = QMessageBox.warning(self, "警告", "输入数字超出范围", QMessageBox.Cancel)
            self.firstnum.clear()
        if secondnu > 99:
            ershow = QMessageBox.warning(self, "警告", "输入数字超出范围", QMessageBox.Cancel)
            self.secondnum.clear()
        if resultnu > 99:
            ershow = QMessageBox.warning(self, "警告", "输入数字超出范围", QMessageBox.Cancel)
            self.resultnum.clear()
    
    #随机生成成立的等式
    def randequalformula(self):
        randnum = random.randint(0,99)
        randfor = self.randequ[randnum]
        self.firstnum.setText(str(randfor[1]))
        self.secondnum.setText(str(randfor[2]))
        self.resultnum.setText(str(randfor[3]))
        self.symbol.setCurrentIndex(randfor[0] + 1)
    
    #按位存储的数字与实际数字之间的转换
    def solotowhole(self, num):
        if num[0] == -1:
            num[0] = 0
        if num[3] == -1:
            num[3] = 0
        if num[6] == -1:
            num[6] = 0
        formula = []
        formula.append(num[2] - 10)
        formula.append(num[0] * 10 + num[1])
        formula.append(num[3] * 10 + num[4])
        formula.append(num[6] * 10 + num[7])
        return formula
    
    #移动一个火柴棍的搜索函数       
    def deal(self):
        difficulty1 = []
        difficulty2 = []
        information = [[9,9,9,9,9,9,0,9,1,0,9,9,9,9],
                       [9,9,9,9,9,9,9,1,9,9,9,9,9,9],
                       [9,9,9,0,9,9,9,9,9,9,9,9,9,9],
                       [9,9,0,9,9,0,9,9,9,1,9,9,9,9],
                       [9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                       [9,9,9,0,9,9,1,9,9,1,9,9,9,9],
                       [0,9,9,9,9,-1,9,9,1,0,9,9,9,9],
                       [9,-1,9,9,9,9,9,9,9,9,9,9,9,9],
                       [-1,9,9,9,9,9,-1,9,9,-1,9,9,9,9],
                       [0,9,9,-1,9,-1,0,9,1,9,9,9,9,9],
                       [9,9,9,9,9,9,9,9,9,9,9,-1,9,0],
                       [9,9,9,9,9,9,9,9,9,9,1,9,9,1],
                       [9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                       [9,9,9,9,9,9,9,9,9,9,0,-1,9,9]] #移动火柴棍时数字变化情况的信息存储列表
        numofinfor = [3,1,1,3,0,3,4,1,3,5,2,2,0,2] #每个数字可以变化的情况数量
        equalarr = [] #输入等式存储
        equalarr.append(self.getinputsign1())
        equalarr.append(self.getinputnum1())
        equalarr.append(self.getinputnum2())
        equalarr.append(self.getinputnum3())
        solution = []
        solutionnum = 0
        exchangesig = []
        numarr = [0,0,0,0,0,0,0,0] #按位存储
        #数字自身移动火柴棍的变化
        position0 = []
        nump0 = 0
        #数字加上一根火柴棍的变化
        position1 = []
        nump1 = 0
        #数字移去一根火柴棍的变化
        positionm1 = []
        numpm1 = 0
        numarr[2] = equalarr[0] + 9
        numarr[0] = equalarr[1] // 10
        numarr[1] = equalarr[1] % 10
        numarr[3] = equalarr[2] // 10
        numarr[4] = equalarr[2] % 10
        numarr[5] = 13
        numarr[6] = equalarr[3] // 10
        numarr[7] = equalarr[3] % 10
        #输入数字十位位0则视为空
        if numarr[0] == 0:
            numarr[0] = -1
        if numarr[3] == 0:
            numarr[3] = -1
        if numarr[6] == 0:
            numarr[6] = -1
        #position与nump赋值
        for j in range(8):
            if numarr[j] != -1:
                for k in range(14):
                    if information[numarr[j]][k] == 1:
                        position1.append([j,k])
                        nump1 = nump1 + 1
        for j in range(8):
            if numarr[j] != -1:
                for k in range(14):
                    if information[numarr[j]][k] == 0:
                        position0.append([j,k])
                        nump0 = nump0 + 1
        for j in range(8):
            if numarr[j] != -1:
                for k in range(14):
                    if information[numarr[j]][k] == -1:
                        positionm1.append([j,k])
                        numpm1 = numpm1 + 1

        correctsign = 0 #搜索成功的标志
        exchangesign = 0 #式子等号位置变化的标志
        if nump0 != 0 : #火柴棍在一个数字上移动
            for i in range(nump0):
                numarrcopy = numarr[:]
                numarrcopy[position0[i][0]] = position0[i][1]
                if numarrcopy[5] != 13 or numarrcopy[2] == 13:
                    continue
                tempequal = self.solotowhole(numarrcopy)
                correctsign = 0
                #等式检验
                if tempequal[0] == 0:
                    if tempequal[1] + tempequal[2] == tempequal[3]:
                        correctsign = 1
                elif tempequal[0] == 1:
                    if tempequal[1] - tempequal[2] == tempequal[3]:
                        correctsign = 1
                elif tempequal[0] == 2:
                    if tempequal[1] * tempequal[2] == tempequal[3]:
                        correctsign = 1
                if correctsign == 1:
                    finalanswer = tempequal[:]
                    solution.append(finalanswer)
                    solutionnum = solutionnum + 1
                    exchangesig.append(exchangesign)
                    difficulty1.append(1)
                    if numarrcopy[2] != numarr[2]:
                        difficulty2.append(2)
                    elif numarrcopy[5] != numarr[5]:
                        difficulty2.append(3)
                    else:
                        difficulty2.append(1)
        if nump1 != 0 and numpm1 != 0: #火柴棍在不同数字之间移动
            for i in range(nump1):
                for j in range(numpm1):
                    numarrcopy = numarr[:]
                    numarrcopy[position1[i][0]] = position1[i][1]
                    numarrcopy[positionm1[j][0]] = positionm1[j][1]
                    correctsign = 0
                    exchangesign = 0
                    if numarrcopy[2] != 13 and numarrcopy[5] != 13: #不是等式则跳过
                        continue
                    if numarrcopy[2] == 13 and numarrcopy[5] == 13: #连等式如 ‘1 = 1 = 1’
                        tempequal = self.solotowhole(numarrcopy)
                        if tempequal[1] == tempequal[2] and tempequal[2] == tempequal[3]:
                            correctsign = 1
                    elif numarrcopy[2] == 13 and numarrcopy[5] != 13: #等号变位等式如 ‘7 = 8 - 1’
                        exchangesign = 1
                        numarrcopy[2] = numarrcopy[5]
                        numarrcopy[5] = 13
                        tempequal = self.solotowhole(numarrcopy)
                        #等式检验
                        if tempequal[0] == 0:
                            if tempequal[1] == tempequal[2] + tempequal[3]:
                                correctsign = 1
                        elif tempequal[0] == 1:
                            if tempequal[1] == tempequal[2] - tempequal[3]:
                                correctsign = 1
                        elif tempequal[0] == 2:
                            if tempequal[1] == tempequal[2] * tempequal[3]:
                                correctsign = 1
                    else: #正常等式
                        tempequal = self.solotowhole(numarrcopy)
                        #等式检验
                        if tempequal[0] == 0:
                            if tempequal[1] + tempequal[2] == tempequal[3]:
                                correctsign = 1
                        elif tempequal[0] == 1:
                            if tempequal[1] - tempequal[2] == tempequal[3]:
                                correctsign = 1
                        elif tempequal[0] == 2:
                            if tempequal[1] * tempequal[2] == tempequal[3]:
                                correctsign = 1
                    if correctsign == 1:
                        finalanswer = tempequal[:]
                        solution.append(finalanswer)
                        exchangesig.append(exchangesign)
                        solutionnum = solutionnum + 1
                        difficulty1.append(2)
                        if numarrcopy[2] != numarr[2]:
                            difficulty2.append(2)
                        elif numarrcopy[5] != numarr[5]:
                            difficulty2.append(3)
                        else:
                            difficulty2.append(1)
        finaldifficulty = []
        #判断有无解，有则显示，无则提示
        if solutionnum == 0:
            ershow = QMessageBox.warning(self, "对不起", "该式子无解,请重新输入", QMessageBox.Cancel)
            self.firstnum.clear()
            self.secondnum.clear()
            self.resultnum.clear()
        else:
            self.searesult = solution[:]
            self.searesultnum = solutionnum
            self.exchangemes = exchangesig[:]
            self.currentnum = solutionnum - 1
            sumdifficulty = 0
            for i in range(solutionnum):
                finaldifficulty.append(difficulty1[i]*0.4*2.5 + difficulty2[i]*0.6*5/3) #难度定义
                sumdifficulty = sumdifficulty + difficulty1[i]*0.4*2.5 + difficulty2[i]*0.6*5/3 #总难度
            averagefifficulty = sumdifficulty/solutionnum #平均难度
            totaldifficulty = averagefifficulty*0.5 + solutionnum/5 #综合难度定义
            self.evaluedifficulty = finaldifficulty[:]
            if exchangesign == 0:
                tempresultnum1 = finalanswer[1]
                tempresultnum2 = finalanswer[2]
                tempresultnum3 = finalanswer[3]
                tempresultsign1 = finalanswer[0] + 1
                tempresultsign2 = 4
            else:
                tempresultnum1 = finalanswer[1]
                tempresultnum2 = finalanswer[2]
                tempresultnum3 = finalanswer[3]
                tempresultsign1 = 4
                tempresultsign2 = finalanswer[0] + 1
            glaxynu = []
            glaxynu.append(tempresultnum1)
            glaxynu.append(tempresultnum2)
            glaxynu.append(tempresultnum3)
            glaxynu.append(tempresultsign1)
            glaxynu.append(tempresultsign2)
            self.showresultstr(glaxynu[:])
            self.setresult(tempresultnum1,tempresultnum2,tempresultnum3,tempresultsign1,tempresultsign2)
            self.showresult()
            self.showstar(round(self.evaluedifficulty[solutionnum - 1]))
            self.showstar2(round(totaldifficulty))
    
    #移动两根火柴棍的搜索函数
    def deal2(self):
        difficulty1 = []
        difficulty2 = []
        information = [[9,9,9,9,9,9,0,9,1,0,9,9,9,9],
                       [9,9,9,9,9,9,9,1,9,9,9,9,9,9],
                       [9,9,9,0,9,9,9,9,9,9,9,9,9,9],
                       [9,9,0,9,9,0,9,9,9,1,9,9,9,9],
                       [9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                       [9,9,9,0,9,9,1,9,9,1,9,9,9,9],
                       [0,9,9,9,9,-1,9,9,1,0,9,9,9,9],
                       [9,-1,9,9,9,9,9,9,9,9,9,9,9,9],
                       [-1,9,9,9,9,9,-1,9,9,-1,9,9,9,9],
                       [0,9,9,-1,9,-1,0,9,1,9,9,9,9,9],
                       [9,9,9,9,9,9,9,9,9,9,9,-1,9,0],
                       [9,9,9,9,9,9,9,9,9,9,1,9,9,1],
                       [9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                       [9,9,9,9,9,9,9,9,9,9,0,-1,9,9]] #移动一根火柴棍时数字变化情况的信息存储列表
        information2 = [[9,9,-1,-1,9,-1,0,9,1,0,9,9,9,9],
                        [9,9,9,9,2,9,9,9,9,9,9,9,9,9],
                        [1,9,9,0,9,0,1,9,2,1,9,9,9,9],
                        [1,9,0,9,-1,0,1,-2,2,1,9,9,9,9],
                        [9,-2,9,1,9,1,9,-1,9,2,9,9,9,9],
                        [1,9,0,0,-1,9,1,9,2,1,9,9,9,9],
                        [0,9,-1,-1,9,-1,9,9,1,0,9,9,9,9],
                        [9,-1,9,2,1,9,9,9,9,9,9,9,9,9],
                        [-1,9,-2,-2,9,-2,-1,9,9,-1,9,9,9,9],
                        [0,9,-1,-1,-2,-1,0,9,1,9,9,9,9,9],
                        [9,9,9,9,9,9,9,9,9,9,9,-1,0,0],
                        [9,9,9,9,9,9,9,9,9,9,1,9,9,9],
                        [9,9,9,9,9,9,9,9,9,9,0,-1,9,0],
                        [9,9,9,9,9,9,9,9,9,9,0,-1,0,9]] #移动两根火柴棍时数字变化情况的信息存储列表
        numofinfor = [3,1,1,3,0,3,4,1,3,5,2,2,0,2] #每个数字可以变化的情况数量
        numofinfor2 = [6,1,6,8,5,7,6,3,6,7,3,1,3,3] #每个数字可以变化的情况数量
        equalarr = [] #输入等式存储
        equalarr.append(self.getinputsign1())
        equalarr.append(self.getinputnum1())
        equalarr.append(self.getinputnum2())
        equalarr.append(self.getinputnum3())
        solution = [] #所有解的集合
        solutionnum = 0 #所有解的数量
        exchangesig = [] #解等式等号是否变位的标志数组
        numarr = [0,0,0,0,0,0,0,0] #按位存储
        numarr[2] = equalarr[0] + 9
        numarr[0] = equalarr[1] // 10
        numarr[1] = equalarr[1] % 10
        numarr[3] = equalarr[2] // 10
        numarr[4] = equalarr[2] % 10
        numarr[5] = 13
        numarr[6] = equalarr[3] // 10
        numarr[7] = equalarr[3] % 10
        #输入数字十位位0则视为空
        if numarr[0] == 0:
            numarr[0] = -1
        if numarr[3] == 0:
            numarr[3] = -1
        if numarr[6] == 0:
            numarr[6] = -1
        #数字自身移动火柴棍的变化
        position0 = []
        nump0 = 0
        #数字加上一根火柴棍的变化
        position1 = []
        nump1 = 0
        #数字移去一根火柴棍的变化
        positionm1 = []
        numpm1 = 0
        #数字自身移动两根火柴棍的变化
        position02 = []
        nump02 = 0
        #数字加上一根火柴棍再自已移动一根的变化
        position1move = []
        nump1move = 0
        #数字移去一根火柴棍再自己移动一根的变化
        positionm1move = []
        numpm1move = 0
        #数字加上两根火柴棍的变化
        position2 = []
        nump2 = 0
        #数字移去两根火柴棍的变化
        positionm2 = []
        numpm2 = 0
        #position与nump赋值
        for j in range(8):
            if numarr[j] != -1:
                for k in range(14):
                    if information[numarr[j]][k] == 1:
                        position1.append([j,k])
                        nump1 = nump1 + 1
        for j in range(8):
            if numarr[j] != -1:
                for k in range(14):
                    if information[numarr[j]][k] == 0:
                        position0.append([j,k])
                        nump0 = nump0 + 1
        for j in range(8):
            if numarr[j] != -1:
                for k in range(14):
                    if information[numarr[j]][k] == -1:
                        positionm1.append([j,k])
                        numpm1 = numpm1 + 1
        for j in range(8):
            if numarr[j] != -1:
                for k in range(14):
                    if information2[numarr[j]][k] == 0:
                        position02.append([j,k])
                        nump02 = nump02 + 1
        for j in range(8):
            if numarr[j] != -1:
                for k in range(14):
                    if information2[numarr[j]][k] == 1:
                        position1move.append([j,k])
                        nump1move = nump1move + 1
        for j in range(8):
            if numarr[j] != -1:
                for k in range(14):
                    if information2[numarr[j]][k] == -1:
                        positionm1move.append([j,k])
                        numpm1move = numpm1move + 1
        for j in range(8):
            if numarr[j] != -1:
                for k in range(14):
                    if information2[numarr[j]][k] == 2:
                        position2.append([j,k])
                        nump2 = nump2 + 1
        for j in range(8):
            if numarr[j] != -1:
                for k in range(14):
                    if information2[numarr[j]][k] == -2:
                        positionm2.append([j,k])
                        numpm2 = numpm2 + 1
        correctsign = 0 #搜索成功的标志
        exchangesign = 0 #式子等号位置变化的标志
        if nump02 != 0: #一个数字移动两根
            for i in range(nump02):
                numarrcopy = numarr[:]
                numarrcopy[position02[i][0]] = position02[i][1]
                correctsign = 0
                if numarrcopy[5] != 13 or numarrcopy[2] != 13:
                    continue
                elif numarrcopy[5] == 13 and numarrcopy[2] == 13:
                    tempequal = self.solotowhole(numarrcopy)
                    if tempequal[1] == tempequal[2] and tempequal[2] == tempequal[3]:
                        correctsign = 1
                else:
                    tempequal = self.solotowhole(numarrcopy)
                    #等式检验
                    if tempequal[0] == 0:
                        if tempequal[1] + tempequal[2] == tempequal[3]:
                            correctsign = 1
                    elif tempequal[0] == 1:
                        if tempequal[1] - tempequal[2] == tempequal[3]:
                            correctsign = 1
                    elif tempequal[0] == 2:
                        if tempequal[1] * tempequal[2] == tempequal[3]:
                            correctsign = 1
                if correctsign == 1:
                    finalanswer = tempequal[:]
                    solution.append(finalanswer)
                    exchangesig.append(exchangesign)
                    solutionnum = solutionnum + 1
                    difficulty1.append(1)
                    if numarrcopy[2] != numarr[2]:
                        difficulty2.append(2)
                    elif numarrcopy[5] != numarr[5]:
                        difficulty2.append(3)
                    else:
                        difficulty2.append(1)
        if nump2 != 0 and numpm2 != 0: #一个数字移走两根，另一个数字加上两根
            for i in range(nump2):
                for j in range(numpm2):
                    if position2[i][0] != positionm2[j][0]:
                        numarrcopy = numarr[:]
                        numarrcopy[position2[i][0]] = position2[i][1]
                        numarrcopy[positionm2[j][0]] = positionm2[j][1]
                        correctsign = 0
                        exchangesign = 0
                        tempequal = self.solotowhole(numarrcopy)
                        #等式检验
                        if tempequal[0] == 0:
                            if tempequal[1] + tempequal[2] == tempequal[3]:
                                correctsign = 1
                        elif tempequal[0] == 1:
                            if tempequal[1] - tempequal[2] == tempequal[3]:
                                correctsign = 1
                        elif tempequal[0] == 2:
                            if tempequal[1] * tempequal[2] == tempequal[3]:
                                correctsign = 1
                        if correctsign == 1:
                            finalanswer = tempequal[:]
                            solution.append(finalanswer)
                            exchangesig.append(exchangesign)
                            solutionnum = solutionnum + 1
                            difficulty1.append(2)
                            if numarrcopy[2] != numarr[2]:
                                difficulty2.append(2)
                            elif numarrcopy[5] != numarr[5]:
                                difficulty2.append(3)
                            else:
                                difficulty2.append(1)
        if nump2 != 0 and numpm1 >= 2: #一个数字加上两根，另外两个数字各减去一根
            for i in range(nump2):
                for j in range(numpm1 - 1):
                    for k in range(numpm1 - j - 1):
                        if position2[i][0] != positionm1[j][0] and position2[i][0] != positionm1[j+k+1][0] and positionm1[j][0] != positionm1[j+k+1][0]:
                            numarrcopy = numarr[:]
                            numarrcopy[position2[i][0]] = position2[i][1]
                            numarrcopy[positionm1[j][0]] = positionm1[j][1]
                            numarrcopy[positionm1[j+k+1][0]] = positionm1[j+k+1][1]
                            correctsign = 0
                            exchangesign = 0
                            if numarrcopy[2] != 13 and numarrcopy[5] != 13: #不是等式则跳过
                                continue
                            else: #正常等式
                                tempequal = self.solotowhole(numarrcopy)
                                #等式检验
                                if tempequal[0] == 0:
                                    if tempequal[1] + tempequal[2] == tempequal[3]:
                                        correctsign = 1
                                elif tempequal[0] == 1:
                                    if tempequal[1] - tempequal[2] == tempequal[3]:
                                        correctsign = 1
                                elif tempequal[0] == 2:
                                    if tempequal[1] * tempequal[2] == tempequal[3]:
                                        correctsign = 1
                            if correctsign == 1:
                                finalanswer = tempequal[:]
                                solution.append(finalanswer)
                                exchangesig.append(exchangesign)
                                solutionnum = solutionnum + 1
                                difficulty1.append(3)
                                if numarrcopy[2] != numarr[2]:
                                    difficulty2.append(2)
                                elif numarrcopy[5] != numarr[5]:
                                    difficulty2.append(3)
                                else:
                                    difficulty2.append(1)
        if numpm2 != 0 and nump1 >= 2: #一个数字减去两根，另外两个数字各加上一根
            for i in range(numpm2):
                for j in range(nump1 - 1):
                    for k in range(nump1 - j - 1):
                        if positionm2[i][0] != position1[j][0] and positionm2[i][0] != position1[j+k+1][0] and position1[j][0] != position1[j+k+1][0]:
                            numarrcopy = numarr[:]
                            numarrcopy[positionm2[i][0]] = positionm2[i][1]
                            numarrcopy[position1[j][0]] = position1[j][1]
                            numarrcopy[position1[j+k+1][0]] = position1[j+k+1][1]
                            correctsign = 0
                            exchangesign = 0
                            if numarrcopy[2] != 13 and numarrcopy[5] != 13: #不是等式则跳过
                                continue
                            elif numarrcopy[2] == 13 and numarrcopy[5] == 13: #连等式如 ‘1 = 1 = 1’
                                tempequal = self.solotowhole(numarrcopy)
                                if tempequal[1] == tempequal[2] and tempequal[2] == tempequal[3]:
                                    correctsign = 1
                            else: #正常等式
                                tempequal = self.solotowhole(numarrcopy)
                                #等式检验
                                if tempequal[0] == 0:
                                    if tempequal[1] + tempequal[2] == tempequal[3]:
                                        correctsign = 1
                                elif tempequal[0] == 1:
                                    if tempequal[1] - tempequal[2] == tempequal[3]:
                                        correctsign = 1
                                elif tempequal[0] == 2:
                                    if tempequal[1] * tempequal[2] == tempequal[3]:
                                        correctsign = 1
                            if correctsign == 1:
                                finalanswer = tempequal[:]
                                solution.append(finalanswer)
                                exchangesig.append(exchangesign)
                                solutionnum = solutionnum + 1
                                difficulty1.append(3)
                                if numarrcopy[2] != numarr[2]:
                                    difficulty2.append(2)
                                elif numarrcopy[5] != numarr[5]:
                                    difficulty2.append(3)
                                else:
                                    difficulty2.append(1)
        if nump0 >=2: #两根数字各自移动一根
            for i in range(nump0 - 1):
                for j in range(nump0 - i - 1):
                    if position0[i][0] != position0[i+j+1][0]:
                        numarrcopy = numarr[:]
                        numarrcopy[position0[i][0]] = position0[i][1]
                        numarrcopy[position0[i+j+1][0]] = position0[i+j+1][1]
                        correctsign = 0
                        exchangesign = 0
                        if numarrcopy[2] != 13 and numarrcopy[5] != 13: #不是等式则跳过
                            continue
                        elif numarrcopy[2] == 13 and numarrcopy[5] == 13: #连等式如 ‘1 = 1 = 1’
                            tempequal = self.solotowhole(numarrcopy)
                            if tempequal[1] == tempequal[2] and tempequal[2] == tempequal[3]:
                                correctsign = 1
                        elif numarrcopy[2] == 13 and numarrcopy[5] != 13: #等号变位等式如 ‘7 = 8 - 1’
                            exchangesign = 1
                            numarrcopy[2] = numarrcopy[5]
                            numarrcopy[5] = 13
                            tempequal = self.solotowhole(numarrcopy)
                            #等式检验
                            if tempequal[0] == 0:
                                if tempequal[1] == tempequal[2] + tempequal[3]:
                                    correctsign = 1
                            elif tempequal[0] == 1:
                                if tempequal[1] == tempequal[2] - tempequal[3]:
                                    correctsign = 1
                            elif tempequal[0] == 2:
                                if tempequal[1] == tempequal[2] * tempequal[3]:
                                    correctsign = 1
                        else: #正常等式
                            tempequal = self.solotowhole(numarrcopy)
                            #等式检验
                            if tempequal[0] == 0:
                                if tempequal[1] + tempequal[2] == tempequal[3]:
                                    correctsign = 1
                            elif tempequal[0] == 1:
                                if tempequal[1] - tempequal[2] == tempequal[3]:
                                    correctsign = 1
                            elif tempequal[0] == 2:
                                if tempequal[1] * tempequal[2] == tempequal[3]:
                                    correctsign = 1
                        if correctsign == 1:
                            finalanswer = tempequal[:]
                            solution.append(finalanswer)
                            exchangesig.append(exchangesign)
                            solutionnum = solutionnum + 1
                            difficulty1.append(2)
                            if numarrcopy[2] != numarr[2]:
                                difficulty2.append(2)
                            elif numarrcopy[5] != numarr[5]:
                                difficulty2.append(3)
                            else:
                                difficulty2.append(1)
        if nump1 >= 2 and numpm1 >= 2: #两根数字加上一根，两个数字减去一根
            for i in range(nump1 - 1):
                for j in range(nump1 - i - 1):
                    for m in range(numpm1 - 1):
                        for n in range(numpm1 - m - 1):
                            if position1[i][0] != position1[i+j+1][0] and position1[i][0] != positionm1[m][0] and position1[i][0] != positionm1[m+n+1][0] and position1[i+j+1][0] != positionm1[m][0] and position1[i+j+1][0] != positionm1[m+n+1][0] and positionm1[m][0] != positionm1[m+n+1][0]:
                                numarrcopy = numarr[:]
                                numarrcopy[position1[i][0]] = position1[i][1]
                                numarrcopy[position1[i+j+1][0]] = position1[i+j+1][1]
                                numarrcopy[positionm1[m][0]] = positionm1[m][1]
                                numarrcopy[positionm1[m+n+1][0]] = positionm1[m+n+1][1]
                                correctsign = 0
                                exchangesign = 0
                                if numarrcopy[2] != 13 and numarrcopy[5] != 13: #不是等式则跳过
                                    continue
                                elif numarrcopy[2] == 13 and numarrcopy[5] == 13: #连等式如 ‘1 = 1 = 1’
                                    tempequal = self.solotowhole(numarrcopy)
                                    if tempequal[1] == tempequal[2] and tempequal[2] == tempequal[3]:
                                        correctsign = 1
                                elif numarrcopy[2] == 13 and numarrcopy[5] != 13: #等号变位等式如 ‘7 = 8 - 1’
                                    exchangesign = 1
                                    numarrcopy[2] = numarrcopy[5]
                                    numarrcopy[5] = 13
                                    tempequal = self.solotowhole(numarrcopy)
                                    #等式检验
                                    if tempequal[0] == 0:
                                        if tempequal[1] == tempequal[2] + tempequal[3]:
                                            correctsign = 1
                                    elif tempequal[0] == 1:
                                        if tempequal[1] == tempequal[2] - tempequal[3]:
                                            correctsign = 1
                                    elif tempequal[0] == 2:
                                        if tempequal[1] == tempequal[2] * tempequal[3]:
                                            correctsign = 1
                                else: #正常等式
                                    tempequal = self.solotowhole(numarrcopy)
                                    #等式检验
                                    if tempequal[0] == 0:
                                        if tempequal[1] + tempequal[2] == tempequal[3]:
                                            correctsign = 1
                                    elif tempequal[0] == 1:
                                        if tempequal[1] - tempequal[2] == tempequal[3]:
                                            correctsign = 1
                                    elif tempequal[0] == 2:
                                        if tempequal[1] * tempequal[2] == tempequal[3]:
                                            correctsign = 1
                                if correctsign == 1:
                                    finalanswer = tempequal[:]
                                    solution.append(finalanswer)
                                    exchangesig.append(exchangesign)
                                    solutionnum = solutionnum + 1
                                    difficulty1.append(4)
                                    if numarrcopy[2] != numarr[2]:
                                        difficulty2.append(2)
                                    elif numarrcopy[5] != numarr[5]:
                                        difficulty2.append(3)
                                    else:
                                        difficulty2.append(1)
        if (nump0 != 0 and nump1 != 0 and numpm1 != 1 ) or (nump1move != 0 and numpm1 != 0 ) or (numpm1move != 0 and nump1 != 0): #一个数字自移一根，两个数字加一根移走一根
            if nump0 != 0 and nump1 != 0 and numpm1 != 1:
                for i in range(nump0):
                    for j in range(nump1):
                        for k in range(numpm1):
                            if position0[i][0] != position1[j][0] and position0[i][0] != positionm1[k][0] and position1[j][0] != positionm1[k][0]:
                                numarrcopy = numarr[:]
                                numarrcopy[position0[i][0]] = position0[i][1]
                                numarrcopy[position1[j][0]] = position1[j][1]
                                numarrcopy[positionm1[k][0]] = positionm1[k][1]
                                correctsign = 0
                                exchangesign = 0
                                if numarrcopy[2] != 13 and numarrcopy[5] != 13: #不是等式则跳过
                                    continue
                                elif numarrcopy[2] == 13 and numarrcopy[5] == 13: #连等式如 ‘1 = 1 = 1’
                                    tempequal = self.solotowhole(numarrcopy)
                                    if tempequal[1] == tempequal[2] and tempequal[2] == tempequal[3]:
                                        correctsign = 1
                                elif numarrcopy[2] == 13 and numarrcopy[5] != 13: #等号变位等式如 ‘7 = 8 - 1’
                                    exchangesign = 1
                                    numarrcopy[2] = numarrcopy[5]
                                    numarrcopy[5] = 13
                                    tempequal = self.solotowhole(numarrcopy)
                                    #等式检验
                                    if tempequal[0] == 0:
                                        if tempequal[1] == tempequal[2] + tempequal[3]:
                                            correctsign = 1
                                    elif tempequal[0] == 1:
                                        if tempequal[1] == tempequal[2] - tempequal[3]:
                                            correctsign = 1
                                    elif tempequal[0] == 2:
                                        if tempequal[1] == tempequal[2] * tempequal[3]:
                                            correctsign = 1
                                else: #正常等式
                                    tempequal = self.solotowhole(numarrcopy)
                                    #等式检验
                                    if tempequal[0] == 0:
                                        if tempequal[1] + tempequal[2] == tempequal[3]:
                                            correctsign = 1
                                    elif tempequal[0] == 1:
                                        if tempequal[1] - tempequal[2] == tempequal[3]:
                                            correctsign = 1
                                    elif tempequal[0] == 2:
                                        if tempequal[1] * tempequal[2] == tempequal[3]:
                                            correctsign = 1
                                if correctsign == 1:
                                    finalanswer = tempequal[:]
                                    solution.append(finalanswer)
                                    exchangesig.append(exchangesign)
                                    solutionnum = solutionnum + 1
                                    difficulty1.append(3)
                                    if numarrcopy[2] != numarr[2]:
                                        difficulty2.append(2)
                                    elif numarrcopy[5] != numarr[5]:
                                        difficulty2.append(3)
                                    else:
                                        difficulty2.append(1)
            if nump1move != 0 and numpm1 != 0:
                for i in range(nump1move):
                    for j in range(numpm1):
                        if position1move[i][0] != positionm1[j][0]:
                            numarrcopy = numarr[:]
                            numarrcopy[position1move[i][0]] = position1move[i][1]
                            numarrcopy[positionm1[j][0]] = positionm1[j][1]
                            correctsign = 0
                            exchangesign = 0
                            if numarrcopy[2] != 13 and numarrcopy[5] != 13: #不是等式则跳过
                                continue
                            elif numarrcopy[2] == 13 and numarrcopy[5] == 13: #连等式如 ‘1 = 1 = 1’
                                tempequal = self.solotowhole(numarrcopy)
                                if tempequal[1] == tempequal[2] and tempequal[2] == tempequal[3]:
                                    correctsign = 1
                            elif numarrcopy[2] == 13 and numarrcopy[5] != 13: #等号变位等式如 ‘7 = 8 - 1’
                                exchangesign = 1
                                numarrcopy[2] = numarrcopy[5]
                                numarrcopy[5] = 13
                                tempequal = self.solotowhole(numarrcopy)
                                #等式检验
                                if tempequal[0] == 0:
                                    if tempequal[1] == tempequal[2] + tempequal[3]:
                                        correctsign = 1
                                elif tempequal[0] == 1:
                                    if tempequal[1] == tempequal[2] - tempequal[3]:
                                        correctsign = 1
                                elif tempequal[0] == 2:
                                    if tempequal[1] == tempequal[2] * tempequal[3]:
                                        correctsign = 1
                            else: #正常等式
                                tempequal = self.solotowhole(numarrcopy)
                                #等式检验
                                if tempequal[0] == 0:
                                    if tempequal[1] + tempequal[2] == tempequal[3]:
                                        correctsign = 1
                                elif tempequal[0] == 1:
                                    if tempequal[1] - tempequal[2] == tempequal[3]:
                                        correctsign = 1
                                elif tempequal[0] == 2:
                                    if tempequal[1] * tempequal[2] == tempequal[3]:
                                        correctsign = 1
                            if correctsign == 1:
                                finalanswer = tempequal[:]
                                solution.append(finalanswer)
                                exchangesig.append(exchangesign)
                                solutionnum = solutionnum + 1
                                difficulty1.append(5)
                                if numarrcopy[2] != numarr[2]:
                                    difficulty2.append(2)
                                elif numarrcopy[5] != numarr[5]:
                                    difficulty2.append(3)
                                else:
                                    difficulty2.append(1)
            if numpm1move != 0 and nump1 != 0:
                for i in range(numpm1move):
                    for j in range(nump1):
                        if positionm1move[i][0] != position1[j][0]:
                            numarrcopy = numarr[:]
                            numarrcopy[positionm1move[i][0]] = positionm1move[i][1]
                            numarrcopy[position1[j][0]] = position1[j][1]
                            correctsign = 0
                            exchangesign = 0
                            if numarrcopy[2] != 13 and numarrcopy[5] != 13: #不是等式则跳过
                                continue
                            elif numarrcopy[2] == 13 and numarrcopy[5] == 13: #连等式如 ‘1 = 1 = 1’
                                tempequal = self.solotowhole(numarrcopy)
                                if tempequal[1] == tempequal[2] and tempequal[2] == tempequal[3]:
                                    correctsign = 1
                            elif numarrcopy[2] == 13 and numarrcopy[5] != 13: #等号变位等式如 ‘7 = 8 - 1’
                                exchangesign = 1
                                numarrcopy[2] = numarrcopy[5]
                                numarrcopy[5] = 13
                                tempequal = self.solotowhole(numarrcopy)
                                #等式检验
                                if tempequal[0] == 0:
                                    if tempequal[1] == tempequal[2] + tempequal[3]:
                                        correctsign = 1
                                elif tempequal[0] == 1:
                                    if tempequal[1] == tempequal[2] - tempequal[3]:
                                        correctsign = 1
                                elif tempequal[0] == 2:
                                    if tempequal[1] == tempequal[2] * tempequal[3]:
                                        correctsign = 1
                            else: #正常等式
                                tempequal = self.solotowhole(numarrcopy)
                                #等式检验
                                if tempequal[0] == 0:
                                    if tempequal[1] + tempequal[2] == tempequal[3]:
                                        correctsign = 1
                                elif tempequal[0] == 1:
                                    if tempequal[1] - tempequal[2] == tempequal[3]:
                                        correctsign = 1
                                elif tempequal[0] == 2:
                                    if tempequal[1] * tempequal[2] == tempequal[3]:
                                        correctsign = 1
                            if correctsign == 1:
                                finalanswer = tempequal[:]
                                solution.append(finalanswer)
                                exchangesig.append(exchangesign)
                                solutionnum = solutionnum + 1
                                difficulty1.append(5)
                                if numarrcopy[2] != numarr[2]:
                                    difficulty2.append(2)
                                elif numarrcopy[5] != numarr[5]:
                                    difficulty2.append(3)
                                else:
                                    difficulty2.append(1)
        #判断有无解，有则显示，无则提示
        finaldifficulty = []
        if solutionnum == 0:
            ershow = QMessageBox.warning(self, "对不起", "该式子无解,请重新输入", QMessageBox.Cancel)
            self.firstnum.clear()
            self.secondnum.clear()
            self.resultnum.clear()
        else:
            self.searesult = solution[:]
            self.searesultnum = solutionnum
            self.exchangemes = exchangesig[:]
            self.currentnum = solutionnum - 1
            sumdifficulty = 0
            for i in range(solutionnum):
                finaldifficulty.append(difficulty1[i]*0.4 + difficulty2[i]*0.6*5/3)#难度定义
                sumdifficulty = sumdifficulty + difficulty1[i]*0.4 + difficulty2[i]*0.6*5/3#难度求和
            averagefifficulty = sumdifficulty/solutionnum#平均难度
            totaldifficulty = averagefifficulty*0.5 + solutionnum/5#综合难度定义
            self.evaluedifficulty = finaldifficulty[:]
            if exchangesign == 0:
                tempresultnum1 = finalanswer[1]
                tempresultnum2 = finalanswer[2]
                tempresultnum3 = finalanswer[3]
                tempresultsign1 = finalanswer[0] + 1
                tempresultsign2 = 4
            else:
                tempresultnum1 = finalanswer[1]
                tempresultnum2 = finalanswer[2]
                tempresultnum3 = finalanswer[3]
                tempresultsign1 = 4
                tempresultsign2 = finalanswer[0] + 1
            glaxynu = []
            glaxynu.append(tempresultnum1)
            glaxynu.append(tempresultnum2)
            glaxynu.append(tempresultnum3)
            glaxynu.append(tempresultsign1)
            glaxynu.append(tempresultsign2)
            self.showresultstr(glaxynu[:])
            self.setresult(tempresultnum1,tempresultnum2,tempresultnum3,tempresultsign1,tempresultsign2)
            self.showresult()
            self.showstar(round(self.evaluedifficulty[solutionnum - 1]))
            self.showstar2(round(totaldifficulty))
    
    #根据选择的模式选择搜索方式
    def search(self):
        tempmodel = self.modelchoose.currentIndex()
        if tempmodel == 1:
            self.deal()
        elif tempmodel == 2:
            self.deal2()
        else:
            self.deal()
        self.resultmes.setText('共有' + str(self.searesultnum) + '个答案')
        self.currentnum = self.searesultnum - 1
        self.beforeone.setEnabled(True)
        self.nextone.setEnabled(True)
    
    #选择上一个答案
    def frontone(self):
        tempnum = self.currentnum
        if tempnum == 0:
            frontnum = self.searesultnum - 1
            self.currentnum = frontnum
        else:
            frontnum = tempnum - 1
            self.currentnum = frontnum
        if self.exchangemes[frontnum] == 0:
            tempresultnum1 = self.searesult[frontnum][1]
            tempresultnum2 = self.searesult[frontnum][2]
            tempresultnum3 = self.searesult[frontnum][3]
            tempresultsign1 = self.searesult[frontnum][0] + 1
            tempresultsign2 = 4
        else:
            tempresultnum1 = self.searesult[frontnum][1]
            tempresultnum2 = self.searesult[frontnum][2]
            tempresultnum3 = self.searesult[frontnum][3]
            tempresultsign1 = 4
            tempresultsign2 = self.searesult[frontnum][0] + 1
        glaxynu = []
        glaxynu.append(tempresultnum1)
        glaxynu.append(tempresultnum2)
        glaxynu.append(tempresultnum3)
        glaxynu.append(tempresultsign1)
        glaxynu.append(tempresultsign2)
        self.showresultstr(glaxynu[:])
        self.setresult(tempresultnum1,tempresultnum2,tempresultnum3,tempresultsign1,tempresultsign2)
        self.showresult()
        self.showstar(round(self.evaluedifficulty[frontnum]))
        
    #选择下一个答案
    def afterone(self):
        tempnum = self.currentnum
        if tempnum == self.searesultnum - 1:
            afternum = 0
            self.currentnum = afternum
        else:
            afternum = tempnum + 1
            self.currentnum = afternum
        if self.exchangemes[afternum] == 0:
            tempresultnum1 = self.searesult[afternum][1]
            tempresultnum2 = self.searesult[afternum][2]
            tempresultnum3 = self.searesult[afternum][3]
            tempresultsign1 = self.searesult[afternum][0] + 1
            tempresultsign2 = 4
        else:
            tempresultnum1 = self.searesult[afternum][1]
            tempresultnum2 = self.searesult[afternum][2]
            tempresultnum3 = self.searesult[afternum][3]
            tempresultsign1 = 4
            tempresultsign2 = self.searesult[afternum][0] + 1
        glaxynu = []
        glaxynu.append(tempresultnum1)
        glaxynu.append(tempresultnum2)
        glaxynu.append(tempresultnum3)
        glaxynu.append(tempresultsign1)
        glaxynu.append(tempresultsign2)
        self.showresultstr(glaxynu[:])
        self.setresult(tempresultnum1,tempresultnum2,tempresultnum3,tempresultsign1,tempresultsign2)
        self.showresult()
        self.showstar(round(self.evaluedifficulty[afternum]))
    
    #显示题目难度星级的接口函数
    def showstar(self,num):
        tempnum = num
        pix1 = QPixmap("./star.png")
        pix2 = QPixmap("./starempty.png")
        if tempnum == 1:#显示一个星星
            self.star1.setPixmap(pix1)
            self.star2.setPixmap(pix2)
            self.star3.setPixmap(pix2)
            self.star4.setPixmap(pix2)
            self.star5.setPixmap(pix2)
        elif tempnum == 2:#显示两个星星
            self.star1.setPixmap(pix1)
            self.star2.setPixmap(pix1)
            self.star3.setPixmap(pix2)
            self.star4.setPixmap(pix2)
            self.star5.setPixmap(pix2)
        elif tempnum == 3:#显示三个星星
            self.star1.setPixmap(pix1)
            self.star2.setPixmap(pix1)
            self.star3.setPixmap(pix1)
            self.star4.setPixmap(pix2)
            self.star5.setPixmap(pix2)
        elif tempnum == 4:#显示四个星星
            self.star1.setPixmap(pix1)
            self.star2.setPixmap(pix1)
            self.star3.setPixmap(pix1)
            self.star4.setPixmap(pix1)
            self.star5.setPixmap(pix2)
        elif tempnum == 5:#显示五个星星
            self.star1.setPixmap(pix1)
            self.star2.setPixmap(pix1)
            self.star3.setPixmap(pix1)
            self.star4.setPixmap(pix1)
            self.star5.setPixmap(pix1)
    
    #显示题目综合难度星级的接口函数
    def showstar2(self,num):
        tempnum = num
        if tempnum > 5 :
            tempnum = 5
        pix1 = QPixmap("./star.png")
        pix2 = QPixmap("./starempty.png")
        if tempnum == 1:#显示一个星星
            self.star1_2.setPixmap(pix1)
            self.star2_2.setPixmap(pix2)
            self.star3_2.setPixmap(pix2)
            self.star4_2.setPixmap(pix2)
            self.star5_2.setPixmap(pix2)
        elif tempnum == 2:#显示两个星星
            self.star1_2.setPixmap(pix1)
            self.star2_2.setPixmap(pix1)
            self.star3_2.setPixmap(pix2)
            self.star4_2.setPixmap(pix2)
            self.star5_2.setPixmap(pix2)
        elif tempnum == 3:#显示三个星星
            self.star1_2.setPixmap(pix1)
            self.star2_2.setPixmap(pix1)
            self.star3_2.setPixmap(pix1)
            self.star4_2.setPixmap(pix2)
            self.star5_2.setPixmap(pix2)
        elif tempnum == 4:#显示四个星星
            self.star1_2.setPixmap(pix1)
            self.star2_2.setPixmap(pix1)
            self.star3_2.setPixmap(pix1)
            self.star4_2.setPixmap(pix1)
            self.star5_2.setPixmap(pix2)
        elif tempnum == 5:#显示五个星星
            self.star1_2.setPixmap(pix1)
            self.star2_2.setPixmap(pix1)
            self.star3_2.setPixmap(pix1)
            self.star4_2.setPixmap(pix1)
            self.star5_2.setPixmap(pix1)
    
    #显示结果等式的字符串
    def showresultstr(self,glaxynum):
       tempnum = glaxynum[:]
       str1 = str(tempnum[0])
       str2 = str(tempnum[1])
       str3 = str(tempnum[2])
       if tempnum[3] == 1:
           str4 = ' + '
       elif tempnum[3] == 2:
           str4 = ' - '
       elif tempnum[3] == 3:
           str4 = ' × '
       elif tempnum[3] == 4:
           str4 = ' = '
           
       if tempnum[4] == 1:
           str5 = ' + '
       elif tempnum[4] == 2:
           str5 = ' - '
       elif tempnum[4] == 3:
           str5 = ' × '
       elif tempnum[4] == 4:
           str5 = ' = '
       tempstr = str1 + str4 + str2 + str5 +str3
       self.lineEdit.setText(tempstr)
       
    #选择固定题目的显示
    def confirmchoose(self):
        fixglaxychange = [[2, 0, 87, 9], [2, 4, 72, 49],[1, 7, 1, 1], [2, 63, 0, 8], [1, 30, 7, 22],
                          [0, 96, 36, 50], [1, 58, 14, 24], [1, 55, 28, 36], [1, 7, 8, 1], [1, 17, 0, 11],
                          [2, 18, 1, 70],[2, 16, 5, 48], [1, 70, 30, 40], [0, 13, 39, 54], [1, 81, 75, 0], 
                          [1, 91, 32, 39],[2, 3, 22, 69], [0, 2, 84, 87], [1, 10, 20, 38], [1, 79, 24, 52]] #规定题组
        tempnum = self.chooseformula.currentIndex()
        self.firstnum.setText(str(fixglaxychange[tempnum - 1][1]))
        self.secondnum.setText(str(fixglaxychange[tempnum - 1][2]))
        self.resultnum.setText(str(fixglaxychange[tempnum - 1][3]))
        self.symbol.setCurrentIndex(fixglaxychange[tempnum - 1][0] + 1)
    
    #清空输入框
    def wholeclear(self):
        self.firstnum.clear()
        self.secondnum.clear()
        self.resultnum.clear()
    
    #UI初始化
    def setupUi(self, just_fun):
        just_fun.setObjectName("just_fun")
        just_fun.resize(703, 605)
        self.remider1 = QtWidgets.QLabel(just_fun)
        self.remider1.setGeometry(QtCore.QRect(30, 40, 600, 25))
        self.remider1.setObjectName("remider1")
        self.firstnum = QtWidgets.QLineEdit(just_fun)
        self.firstnum.setGeometry(QtCore.QRect(30, 80, 111, 20))
        self.firstnum.setObjectName("firstnum")
        self.firstnum.setAlignment(QtCore.Qt.AlignCenter)
        self.secondnum = QtWidgets.QLineEdit(just_fun)
        self.secondnum.setGeometry(QtCore.QRect(250, 80, 113, 20))
        self.secondnum.setObjectName("secondnum")
        self.secondnum.setAlignment(QtCore.Qt.AlignCenter)
        self.resultnum = QtWidgets.QLineEdit(just_fun)
        self.resultnum.setGeometry(QtCore.QRect(450, 80, 113, 20))
        self.resultnum.setObjectName("resultnum")
        self.resultnum.setAlignment(QtCore.Qt.AlignCenter)
        self.equalsign = QtWidgets.QLabel(just_fun)
        self.equalsign.setGeometry(QtCore.QRect(410, 80, 16, 21))
        self.equalsign.setObjectName("equalsign")
        self.symbol = QtWidgets.QComboBox(just_fun)
        self.symbol.setGeometry(QtCore.QRect(160, 80, 69, 22))
        self.symbol.setObjectName("symbol")
        self.symbol.addItem("")
        self.symbol.setItemText(0, "")
        self.symbol.addItem("")
        self.symbol.addItem("")
        self.symbol.addItem("")
        self.symbol.addItem("")
        self.show1num1 = QtWidgets.QLCDNumber(just_fun)
        self.show1num1.setGeometry(QtCore.QRect(30, 120, 51, 71))
        self.show1num1.setDigitCount(1)
        self.show1num1.setObjectName("show1num1")
        self.show2num1 = QtWidgets.QLCDNumber(just_fun)
        self.show2num1.setGeometry(QtCore.QRect(250, 120, 51, 71))
        self.show2num1.setDigitCount(1)
        self.show2num1.setObjectName("show2num1")
        self.show3num1 = QtWidgets.QLCDNumber(just_fun)
        self.show3num1.setGeometry(QtCore.QRect(450, 120, 51, 71))
        self.show3num1.setDigitCount(1)
        self.show3num1.setObjectName("show3num1")
        self.showsymbol = QtWidgets.QLabel(just_fun)
        self.showsymbol.setGeometry(QtCore.QRect(170, 130, 41, 51))
        self.showsymbol.setText("")
        self.showsymbol.setPixmap(QtGui.QPixmap(":/operator/emp.png"))
        self.showsymbol.setScaledContents(True)
        self.showsymbol.setObjectName("showsymbol")
        self.pushButton = QtWidgets.QPushButton(just_fun)
        self.pushButton.setGeometry(QtCore.QRect(360, 280, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.modelchoose = QtWidgets.QComboBox(just_fun)
        self.modelchoose.setGeometry(QtCore.QRect(200, 280, 123, 22))
        self.modelchoose.setObjectName("modelchoose")
        self.modelchoose.addItem("")
        self.modelchoose.setItemText(0, "")
        self.modelchoose.addItem("")
        self.modelchoose.addItem("")
        self.remider2 = QtWidgets.QLabel(just_fun)
        self.remider2.setGeometry(QtCore.QRect(30, 280, 170, 25))
        self.remider2.setObjectName("remider2")
        self.remider3 = QtWidgets.QLabel(just_fun)
        self.remider3.setGeometry(QtCore.QRect(30, 330, 150, 25))
        self.remider3.setObjectName("remider3")
        self.lineEdit = QtWidgets.QLineEdit(just_fun)
        self.lineEdit.setGeometry(QtCore.QRect(30, 360, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.show1num1_2 = QtWidgets.QLCDNumber(just_fun)
        self.show1num1_2.setGeometry(QtCore.QRect(30, 400, 51, 71))
        self.show1num1_2.setDigitCount(1)
        self.show1num1_2.setObjectName("show1num1_2")
        self.show2num1_2 = QtWidgets.QLCDNumber(just_fun)
        self.show2num1_2.setGeometry(QtCore.QRect(250, 400, 51, 71))
        self.show2num1_2.setDigitCount(1)
        self.show2num1_2.setObjectName("show2num1_2")
        self.show3num1_2 = QtWidgets.QLCDNumber(just_fun)
        self.show3num1_2.setGeometry(QtCore.QRect(450, 400, 51, 71))
        self.show3num1_2.setDigitCount(1)
        self.show3num1_2.setObjectName("show3num1_2")
        self.showsymbol_2 = QtWidgets.QLabel(just_fun)
        self.showsymbol_2.setGeometry(QtCore.QRect(390, 130, 41, 51))
        self.showsymbol_2.setText("")
        self.showsymbol_2.setPixmap(QtGui.QPixmap(":/operator/equ.png"))
        self.showsymbol_2.setScaledContents(True)
        self.showsymbol_2.setObjectName("showsymbol_2")
        self.showsymbol2 = QtWidgets.QLabel(just_fun)
        self.showsymbol2.setGeometry(QtCore.QRect(170, 410, 41, 51))
        self.showsymbol2.setText("")
        self.showsymbol2.setPixmap(QtGui.QPixmap(":/operator/emp.png"))
        self.showsymbol2.setScaledContents(True)
        self.showsymbol2.setObjectName("showsymbol2")
        self.showsymbol2_2 = QtWidgets.QLabel(just_fun)
        self.showsymbol2_2.setGeometry(QtCore.QRect(390, 410, 41, 51))
        self.showsymbol2_2.setText("")
        self.showsymbol2_2.setPixmap(QtGui.QPixmap(":/operator/emp.png"))
        self.showsymbol2_2.setScaledContents(True)
        self.showsymbol2_2.setObjectName("showsymbol2_2")
        self.show1num2 = QtWidgets.QLCDNumber(just_fun)
        self.show1num2.setGeometry(QtCore.QRect(90, 120, 51, 71))
        self.show1num2.setDigitCount(1)
        self.show1num2.setObjectName("show1num2")
        self.show2num2 = QtWidgets.QLCDNumber(just_fun)
        self.show2num2.setGeometry(QtCore.QRect(310, 120, 51, 71))
        self.show2num2.setDigitCount(1)
        self.show2num2.setObjectName("show2num2")
        self.show3num2 = QtWidgets.QLCDNumber(just_fun)
        self.show3num2.setGeometry(QtCore.QRect(510, 120, 51, 71))
        self.show3num2.setDigitCount(1)
        self.show3num2.setObjectName("show3num2")
        self.show1num2_2 = QtWidgets.QLCDNumber(just_fun)
        self.show1num2_2.setGeometry(QtCore.QRect(90, 400, 51, 71))
        self.show1num2_2.setDigitCount(1)
        self.show1num2_2.setObjectName("show1num2_2")
        self.show2num2_2 = QtWidgets.QLCDNumber(just_fun)
        self.show2num2_2.setGeometry(QtCore.QRect(310, 400, 51, 71))
        self.show2num2_2.setDigitCount(1)
        self.show2num2_2.setObjectName("show2num2_2")
        self.show3num2_2 = QtWidgets.QLCDNumber(just_fun)
        self.show3num2_2.setGeometry(QtCore.QRect(510, 400, 51, 71))
        self.show3num2_2.setDigitCount(1)
        self.show3num2_2.setObjectName("show3num2_2")
        self.confirm = QtWidgets.QPushButton(just_fun)
        self.confirm.setGeometry(QtCore.QRect(360, 220, 90, 30))
        self.confirm.setObjectName("confirm")
        self.randequal = QtWidgets.QPushButton(just_fun)
        self.randequal.setGeometry(QtCore.QRect(580, 75, 120, 35))
        self.randequal.setObjectName("pushButton")
        self.chooseformula = QtWidgets.QComboBox(just_fun)
        self.chooseformula.setGeometry(QtCore.QRect(200, 220, 123, 22))
        self.chooseformula.setObjectName("chooseformula")
        self.chooseformula.addItem("")
        self.chooseformula.setItemText(0, "")
        self.nextone = QtWidgets.QPushButton(just_fun)
        self.nextone.setGeometry(QtCore.QRect(560, 360, 90, 30))
        self.nextone.setObjectName("nextone")
        self.beforeone = QtWidgets.QPushButton(just_fun)
        self.beforeone.setGeometry(QtCore.QRect(440, 360, 90, 30))
        self.beforeone.setObjectName("beforeone")
        self.resultmes = QtWidgets.QLabel(just_fun)
        self.resultmes.setGeometry(QtCore.QRect(250, 360, 101, 20))
        self.resultmes.setObjectName("resultmes")
        for i in range(20):
            self.chooseformula.addItem("")
        self.clear = QtWidgets.QPushButton(just_fun)
        self.clear.setGeometry(QtCore.QRect(490, 220, 90, 30))
        self.clear.setObjectName("clear")
        self.watchmore = QtWidgets.QPushButton(just_fun)
        self.watchmore.setGeometry(QtCore.QRect(420, 490, 260, 80))
        self.watchmore.setObjectName("watchmore")
        portValidator = QIntValidator(0,65536)
        self.firstnum.setValidator(portValidator)
        self.secondnum.setValidator(portValidator)
        self.resultnum.setValidator(portValidator)
        self.remider4 = QtWidgets.QLabel(just_fun)
        self.remider4.setGeometry(QtCore.QRect(30, 220, 131, 21))
        self.remider4.setObjectName("remider4")
        self.remider5 = QtWidgets.QLabel(just_fun)
        self.remider5.setGeometry(QtCore.QRect(30, 500, 121, 21))
        self.remider5.setObjectName("remider5")
        self.star1 = QtWidgets.QLabel(just_fun)
        self.star1.setGeometry(QtCore.QRect(160, 490, 31, 31))
        self.star1.setText("")
        self.star1.setScaledContents(True)
        self.star1.setAlignment(QtCore.Qt.AlignCenter)
        self.star1.setObjectName("star1")
        self.star2 = QtWidgets.QLabel(just_fun)
        self.star2.setGeometry(QtCore.QRect(200, 490, 31, 31))
        self.star2.setText("")
        self.star2.setScaledContents(True)
        self.star2.setAlignment(QtCore.Qt.AlignCenter)
        self.star2.setObjectName("star2")
        self.star3 = QtWidgets.QLabel(just_fun)
        self.star3.setGeometry(QtCore.QRect(240, 490, 31, 31))
        self.star3.setText("")
        self.star3.setScaledContents(True)
        self.star3.setAlignment(QtCore.Qt.AlignCenter)
        self.star3.setObjectName("star3")
        self.star4 = QtWidgets.QLabel(just_fun)
        self.star4.setGeometry(QtCore.QRect(280, 490, 31, 31))
        self.star4.setText("")
        self.star4.setScaledContents(True)
        self.star4.setAlignment(QtCore.Qt.AlignCenter)
        self.star4.setObjectName("star4")
        self.star5 = QtWidgets.QLabel(just_fun)
        self.star5.setGeometry(QtCore.QRect(320, 490, 31, 31))
        self.star5.setText("")
        self.star5.setScaledContents(True)
        self.star5.setAlignment(QtCore.Qt.AlignCenter)
        self.star5.setObjectName("star5")
        self.star4_2 = QtWidgets.QLabel(just_fun)
        self.star4_2.setGeometry(QtCore.QRect(280, 540, 31, 31))
        self.star4_2.setText("")
        self.star4_2.setScaledContents(True)
        self.star4_2.setAlignment(QtCore.Qt.AlignCenter)
        self.star4_2.setObjectName("star4_2")
        self.star3_2 = QtWidgets.QLabel(just_fun)
        self.star3_2.setGeometry(QtCore.QRect(240, 540, 31, 31))
        self.star3_2.setText("")
        self.star3_2.setScaledContents(True)
        self.star3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.star3_2.setObjectName("star3_2")
        self.star2_2 = QtWidgets.QLabel(just_fun)
        self.star2_2.setGeometry(QtCore.QRect(200, 540, 31, 31))
        self.star2_2.setText("")
        self.star2_2.setScaledContents(True)
        self.star2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.star2_2.setObjectName("star2_2")
        self.remider5_2 = QtWidgets.QLabel(just_fun)
        self.remider5_2.setGeometry(QtCore.QRect(30, 550, 121, 21))
        self.remider5_2.setObjectName("remider5_2")
        self.star5_2 = QtWidgets.QLabel(just_fun)
        self.star5_2.setGeometry(QtCore.QRect(320, 540, 31, 31))
        self.star5_2.setText("")
        self.star5_2.setScaledContents(True)
        self.star5_2.setAlignment(QtCore.Qt.AlignCenter)
        self.star5_2.setObjectName("star5_2")
        self.star1_2 = QtWidgets.QLabel(just_fun)
        self.star1_2.setGeometry(QtCore.QRect(160, 540, 31, 31))
        self.star1_2.setText("")
        self.star1_2.setScaledContents(True)
        self.star1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.star1_2.setObjectName("star1_2")
        pix2 = QPixmap("./starempty.png")
        self.star1.setPixmap(pix2)
        self.star2.setPixmap(pix2)
        self.star3.setPixmap(pix2)
        self.star4.setPixmap(pix2)
        self.star5.setPixmap(pix2)
        self.star1_2.setPixmap(pix2)
        self.star2_2.setPixmap(pix2)
        self.star3_2.setPixmap(pix2)
        self.star4_2.setPixmap(pix2)
        self.star5_2.setPixmap(pix2)
        self.beforeone.setEnabled(False)
        self.nextone.setEnabled(False)
        
        self.retranslateUi(just_fun)
        #信号槽连接
        self.symbol.currentIndexChanged['QString'].connect(self.setoperation)
        self.firstnum.textChanged['QString'].connect(self.disshow1num1)
        self.firstnum.textChanged['QString'].connect(self.disshow1num2)
        self.secondnum.textChanged['QString'].connect(self.disshow2num1)
        self.secondnum.textChanged['QString'].connect(self.disshow2num2)
        self.resultnum.textChanged['QString'].connect(self.disshow3num1)
        self.resultnum.textChanged['QString'].connect(self.disshow3num2)
        self.firstnum.textChanged['QString'].connect(self.showerror)
        self.secondnum.textChanged['QString'].connect(self.showerror)
        self.resultnum.textChanged['QString'].connect(self.showerror)
        self.pushButton.clicked.connect(self.search)
        self.confirm.clicked.connect(self.confirmchoose)
        self.clear.clicked.connect(self.wholeclear)
        self.beforeone.clicked.connect(self.frontone)
        self.nextone.clicked.connect(self.afterone)
        self.watchmore.clicked.connect(myshowqa.show)
        self.randequal.clicked.connect(self.randequalformula)
        #样式变化
        self.confirm.setStyleSheet("QPushButton{border-image: url(button.png)}"
         "QPushButton:hover{border-image: url(buttonon.png)}"
         "QPushButton:pressed{border-image: url(buttonpre.png)}")
        self.confirm.setFont(QFont("方正经黑简体", 12))
        self.clear.setStyleSheet("QPushButton{border-image: url(button.png)}"
         "QPushButton:hover{border-image: url(buttonon.png)}"
         "QPushButton:pressed{border-image: url(buttonpre.png)}")
        self.clear.setFont(QFont("方正经黑简体", 12))
        self.randequal.setStyleSheet("QPushButton{border-image: url(button.png)}"
         "QPushButton:hover{border-image: url(buttonon.png)}"
         "QPushButton:pressed{border-image: url(buttonpre.png)}")
        self.randequal.setFont(QFont("方正经黑简体", 10))
        self.watchmore.setStyleSheet("QPushButton{border-image: url(button2.png)}"
         "QPushButton:hover{border-image: url(buttonon2.png)}"
         "QPushButton:pressed{border-image: url(buttonpres2.png)}")
        self.watchmore.setFont(QFont("方正经黑简体", 12))
        self.pushButton.setStyleSheet("QPushButton{border-image: url(button.png)}"
         "QPushButton:hover{border-image: url(buttonon.png)}"
         "QPushButton:pressed{border-image: url(buttonpre.png)}")
        self.pushButton.setFont(QFont("方正经黑简体", 12))
        self.beforeone.setStyleSheet("QPushButton{border-image: url(button.png)}"
         "QPushButton:hover{border-image: url(buttonon.png)}"
         "QPushButton:pressed{border-image: url(buttonpre.png)}")
        self.beforeone.setFont(QFont("方正经黑简体", 12))
        self.nextone.setStyleSheet("QPushButton{border-image: url(button.png)}"
         "QPushButton:hover{border-image: url(buttonon.png)}"
         "QPushButton:pressed{border-image: url(buttonpre.png)}")
        self.nextone.setFont(QFont("方正经黑简体", 12))
        self.firstnum.setStyleSheet("QLineEdit{border-image: url(lineedit.png)}")
        self.secondnum.setStyleSheet("QLineEdit{border-image: url(lineedit.png)}")
        self.resultnum.setStyleSheet("QLineEdit{border-image: url(lineedit.png)}")
        self.lineEdit.setStyleSheet("QLineEdit{border-image: url(lineedit.png)}")
        self.symbol.setStyleSheet("QComboBox{border-image: url(combox.png)}"
                                  "QComboBox::drop-down{border:none}"
                                  "QComboBox::down-arrow {border-image: url(arrow.png)}")
        self.chooseformula.setStyleSheet("QComboBox{border-image: url(combox.png)}"
                                  "QComboBox::drop-down{border:none}"
                                  "QComboBox::down-arrow {border-image: url(arrow.png)}")
        self.modelchoose.setStyleSheet("QComboBox{border-image: url(combox.png)}"
                                  "QComboBox::drop-down{border:none}"
                                  "QComboBox::down-arrow {border-image: url(arrow.png)}")
        self.remider1.setFont(QFont("方正清刻本悦宋简体",13))
        self.remider2.setFont(QFont("方正清刻本悦宋简体",13))
        self.remider3.setFont(QFont("方正清刻本悦宋简体",13))
        self.remider4.setFont(QFont("方正清刻本悦宋简体",13))
        self.remider5.setFont(QFont("方正清刻本悦宋简体",12))
        self.remider5_2.setFont(QFont("方正清刻本悦宋简体",12))
        self.equalsign.setFont(QFont("方正清刻本悦宋简体",13))
        self.resultmes.setFont(QFont("方正清刻本悦宋简体",12))
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
        self.show1num1_2.setSegmentStyle(QLCDNumber.Flat)
        self.show1num1_2.setStyleSheet("border: 1px #ead273; color: #cb2d2d;")
        self.show2num1_2.setSegmentStyle(QLCDNumber.Flat)
        self.show2num1_2.setStyleSheet("border: 1px #ead273; color: #cb2d2d;")
        self.show3num1_2.setSegmentStyle(QLCDNumber.Flat)
        self.show3num1_2.setStyleSheet("border: 1px #ead273; color: #cb2d2d;")
        self.show1num2_2.setSegmentStyle(QLCDNumber.Flat)
        self.show1num2_2.setStyleSheet("border: 1px #ead273; color: #030000;")
        self.show2num2_2.setSegmentStyle(QLCDNumber.Flat)
        self.show2num2_2.setStyleSheet("border: 1px #ead273; color: #030000;")
        self.show3num2_2.setSegmentStyle(QLCDNumber.Flat)
        self.show3num2_2.setStyleSheet("border: 1px #ead273; color: #030000;")
        QtCore.QMetaObject.connectSlotsByName(just_fun)
    def retranslateUi(self, just_fun):
        _translate = QtCore.QCoreApplication.translate
        just_fun.setWindowTitle(_translate("just_fun", "Form"))
        self.remider1.setText(_translate("just_fun", "请输入一个式子或从下面选择一个式子或随机生成一个等式"))
        self.equalsign.setText(_translate("just_fun", "="))
        self.symbol.setItemText(1, _translate("just_fun", "+"))
        self.symbol.setItemText(2, _translate("just_fun", "-"))
        self.symbol.setItemText(3, _translate("just_fun", "×"))
        self.symbol.setItemText(4, _translate("just_fun", "="))
        fixstrformula = ['0 × 87 = 9', '4 × 72 = 49', '7 - 1 = 1', '63 × 0 = 8', '30 - 7 = 22', 
                         '96 + 36 = 50', '58 - 14 = 24', '55 - 28 = 36', '7 - 8 = 1', '17 - 0 = 11', 
                         '18 × 1 = 70', '16 × 5 = 48', '70 - 30 = 40', '13 + 39 = 54', '81 - 75 = 0', 
                         '91 - 32 = 39', '3 × 22 = 69', '2 + 84 = 87', '10 - 20 = 38', '79 - 24 = 52']
        for i in range(20):
            self.chooseformula.setItemText(i+1, _translate("just_fun", fixstrformula[i]))
        self.pushButton.setText(_translate("just_fun", "开始搜索"))
        self.modelchoose.setItemText(1, _translate("just_fun", "变换一根火柴"))
        self.modelchoose.setItemText(2, _translate("just_fun", "变换两根火柴"))
        self.remider2.setText(_translate("just_fun", "请选择变换方式"))
        self.remider3.setText(_translate("just_fun", "结果如下"))
        self.confirm.setText(_translate("just_fun", "确定"))
        self.randequal.setText(_translate("just_fun", "随机生成等式"))
        self.clear.setText(_translate("just_fun", "清空"))
        self.watchmore.setText(_translate("just_fun", "查看更多题目与答案"))
        self.nextone.setText(_translate("just_fun", "下一个"))
        self.beforeone.setText(_translate("just_fun", "上一个"))
        self.resultmes.setText(_translate("just_fun", " "))
        self.remider4.setText(_translate("just_fun", "可选择的等式"))
        self.remider5.setText(_translate("just_fun", "该题目难度为："))
        self.remider5_2.setText(_translate("just_fun", "综合难度为："))

            
if __name__ == "__main__":
    #init 
    app = QApplication(sys.argv)
    myfun = QWidget()
    myshowqa = QDialog()
    
    #config
    mywin = Ui_just_fun(myfun)
    mywin2 = ShowQa(myshowqa,problem[:],answer[:],problemnum[:],answernum[:],num,sigforqa[:],order[:],problem2[:],answer2[:],problemnum2[:],answernum2[:],num2,sigforqa2[:],order2[:])
    #设置窗口的标题与背景
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("background.jfif").scaled(myfun.size())))
    myfun.setPalette(palette)
    myfun.setWindowTitle("火柴棍小游戏")
    palette2 = QPalette()
    palette2.setBrush(QPalette.Background, QBrush(QPixmap("background.jfif").scaled(myshowqa.size())))
    myshowqa.setPalette(palette2)
    myshowqa.setWindowTitle("更多的题目和答案")
    
    myfun.show()
    
    sys.exit(app.exec_()) 
