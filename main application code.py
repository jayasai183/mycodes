# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from NewWindow import Ui_New
from EvalWindow import Ui_evaluate
from OpenWindow import Ui_Dialog as form
from ScoreWindow import Ui_Dialog
from tkinter import messagebox
import sys
import sqlite3
mycricket=sqlite3.connect("cricket.db")
curs=mycricket.cursor()




class Ui_MainWindow(object):
    def __init__(self):
        self.evalDialog = QtWidgets.QMainWindow()
        self.new_screen = Ui_New()                           
        self.new_screen.setupUi(self.evalDialog)
        
        self.EvaluateWindow= QtWidgets.QMainWindow()
        self.eval_screen= Ui_evaluate()
        self.eval_screen.setupUi(self.EvaluateWindow)

        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen= form()
        self.open_screen.setupUi(self.openDialog)

        self.scoreDialog = QtWidgets.QMainWindow()
        self.score_screen= Ui_Dialog()
        self.score_screen.setupUi(self.scoreDialog)

        
        
    def setupUi(self, MainWindow):
        self.Batsmancount=0
        self.Bowcount=0
        self.wkeepercount=0
        self.allcount=0
        self.avl=1000
        self.used=0
       
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 151, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 90, 151, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 90, 101, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 85, 161, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 90, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 130, 161, 41))
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(510, 140, 141, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 40, 101, 21))
        self.label.setObjectName("label")
        self.batsmancount = QtWidgets.QLineEdit(self.centralwidget)
        self.batsmancount.setGeometry(QtCore.QRect(110, 40, 41, 21))
        self.batsmancount.setObjectName("batsmancount")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 40, 91, 16))
        self.label_2.setObjectName("label_2")
        self.bowlcount = QtWidgets.QLineEdit(self.centralwidget)
        self.bowlcount.setGeometry(QtCore.QRect(260, 40, 41, 21))
        self.bowlcount.setObjectName("bowlcount")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 40, 111, 16))
        self.label_3.setObjectName("label_3")
        self.Allcount = QtWidgets.QLineEdit(self.centralwidget)
        self.Allcount.setGeometry(QtCore.QRect(430, 40, 51, 20))
        self.Allcount.setObjectName("Allcount")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 40, 141, 16))
        self.label_4.setObjectName("label_4")
        self.Wkeepercount = QtWidgets.QLineEdit(self.centralwidget)
        self.Wkeepercount.setGeometry(QtCore.QRect(650, 40, 51, 20))
        self.Wkeepercount.setObjectName("Wkeepercount")
        self.BAT = QtWidgets.QRadioButton(self.centralwidget)
        self.BAT.setGeometry(QtCore.QRect(10, 140, 62, 31))
        self.BAT.setObjectName("BAT")
        self.BOW = QtWidgets.QRadioButton(self.centralwidget)
        self.BOW.setGeometry(QtCore.QRect(70, 140, 71, 31))
        self.BOW.setObjectName("BOW")
        self.WK = QtWidgets.QRadioButton(self.centralwidget)
        self.WK.setGeometry(QtCore.QRect(150, 140, 62, 31))
        self.WK.setObjectName("WK")
        self.AR = QtWidgets.QRadioButton(self.centralwidget)
        self.AR.setGeometry(QtCore.QRect(210, 140, 62, 31))
        self.AR.setObjectName("AR")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 180, 311, 231))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(370, 180, 281, 231))
        self.listWidget_2.setObjectName("listWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menuManageTeams = QtWidgets.QMenu(self.menubar)
        self.menuManageTeams.setObjectName("menuManageTeams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.NEWteam = QtWidgets.QAction(MainWindow)
        self.NEWteam.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.NEWteam.setObjectName("NEWteam")
        self.NEWteam.triggered.connect(self.file_new)
        self.OPENteam = QtWidgets.QAction(MainWindow)
        self.OPENteam.setObjectName("OPENteam")
        self.OPENteam.triggered.connect(self.file_open)
        self.SAVEteam = QtWidgets.QAction(MainWindow)
        self.SAVEteam.setObjectName("SAVEteam")
        self.SAVEteam.triggered.connect(self.file_save)
        self.EVALUATEteam = QtWidgets.QAction(MainWindow)
        self.EVALUATEteam.setObjectName("EVALUATEteam")
        self.EVALUATEteam.triggered.connect(self.file_evaluate)
        self.Quit = QtWidgets.QAction(MainWindow)
        self.Quit.setObjectName("Quit")
        self.Quit.triggered.connect(self.quit)
        self.menuManageTeams.addAction(self.NEWteam)
        self.menuManageTeams.addAction(self.OPENteam)
        self.menuManageTeams.addAction(self.SAVEteam)
        self.menuManageTeams.addAction(self.EVALUATEteam)
        self.menuManageTeams.addAction(self.Quit)
        self.menubar.addAction(self.menuManageTeams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        
        #RADIOBUTTON clicked
        self.BAT.clicked.connect(self.load_names)
        self.BOW.clicked.connect(self.load_names)
        self.AR.clicked.connect(self.load_names)
        self.WK.clicked.connect(self.load_names)

        #DOUBLE CLICK
        self.listWidget.itemDoubleClicked.connect(self.removelist1)
        self.listWidget_2.itemDoubleClicked.connect(self.removelist2)

        self.items = []


        self.new_screen.pushButton.clicked.connect(self.new_team)
        self.open_screen.pushButton.clicked.connect(self.open_team)

        self.eval_screen.comboBox_2.currentTextChanged.connect(self.combo)
        self.eval_screen.pushButton.clicked.connect(self.score)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">your selections</span></p><p><br/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Points Available:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Points Used:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Team Name:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Batsmen(BAT)</p></body></html>"))
        self.batsmancount.setText(_translate("MainWindow","0"))
        self.label_2.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.bowlcount.setText(_translate("MainWindow","0"))
        self.label_3.setText(_translate("MainWindow", "Allrounder(AR)"))
        self.Allcount.setText(_translate("MainWindow","0"))
        self.label_4.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.Wkeepercount.setText(_translate("MainWindow","0"))
        self.BAT.setText(_translate("MainWindow", "BAT"))
        self.BOW.setText(_translate("MainWindow", "BOW"))
        self.WK.setText(_translate("MainWindow", "WK"))
        self.AR.setText(_translate("MainWindow", "AR"))
        self.menuManageTeams.setTitle(_translate("MainWindow", "ManageTeams"))
        self.NEWteam.setText(_translate("MainWindow", "NEW team"))
        self.NEWteam.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.OPENteam.setText(_translate("MainWindow", "OPEN team"))
        self.OPENteam.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.SAVEteam.setText(_translate("MainWindow", "SAVE team"))
        self.SAVEteam.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.EVALUATEteam.setText(_translate("MainWindow", "EVALUATE team"))
        self.Quit.setText(_translate("MainWindow", "Quit"))


        
    #NEW FILE MENU
    def file_new(self):
        self.evalDialog.show()

    #FILE OPENING MENU
    def file_open(self):
        self.openDialog.show()

    #FILE SAVING MENU
    def file_save(self):
        if self.listWidget_2.count()<11:
            messagebox.showerror("Error", "Insufficient Players/team name required")
        else:
            for index in range(self.listWidget_2.count()):
                self.items.append((self.listWidget_2.item(index).text()))
            
            actual_score=[]
            for player in self.items:
                curs.execute("SELECT score from match WHERE Player='"+player+"';")
                actual_score.append(curs.fetchone())
            
            score=[]
            for i in range(len(actual_score)):
                score.append(actual_score[i][0])
            List= tuple(zip(self.items,score))
            myteam= sqlite3.connect('TEAM.db')
            curser= myteam.cursor()
            teamname= self.lineEdit_3.text()
            
            for x in range(len(List)):
                
                curser.execute("INSERT INTO teams ('names','players','scores') VALUES ('%s','%s','%d')"%(teamname,List[x][0],List[x][1]))

            myteam.commit()
            
                
                

    #Evaluate MENU
    def file_evaluate(self):
        self.EvaluateWindow.show()

    def combo(self):
        self.eval_screen.comboBox.currentTextChanged.connect(self.combo2)

    def combo2(self):
        myteam= sqlite3.connect('Team.db')
        curser= myteam.cursor()
        team=self.eval_screen.comboBox.currentText()
        curser.execute("SELECT players from teams WHERE names='"+team+"';")
        player=curser.fetchall()
        self.eval_screen.listWidget.clear()
        for i in range(len(player)):
            item=(player[i][0])
            self.eval_screen.listWidget.addItem(item)
        curser.execute("SELECT scores from teams where names='"+team+"';")
        score=curser.fetchall()
        self.teamscore=[]
        for i in range(len(score)):
            self.teamscore.append(score[i][0])
        self.eval_screen.listWidget_2.clear()
        for i in range(len(score)):
            items=(str(score[i][0]))
            self.eval_screen.listWidget_2.addItem(items)

            

    #SCORE CALCULATION  
    def score(self):
        self.scoreDialog.show()
        self.score_screen.lineEdit.setText(str(sum(self.teamscore)))
        

    #QUITING METHOD  
    def quit(self):
        sys.exit()


    def new_team(self):
        self.tname=self.new_screen.lineEdit.text()
        self.listWidget_2.clear()
        self.lineEdit_3.setText(self.tname)
        self.lineEdit.setText(str(self.avl))
        self.evalDialog.close()

    def open_team(self):
        myteam= sqlite3.connect('TEAM.db')
        curser= myteam.cursor()
        topen=self.open_screen.lineEdit.text()
        curser.execute("SELECT players from teams where names='"+topen+"';")
        si=curser.fetchall()
        self.listWidget_2.clear()
        if si==[]:
            messagebox.showerror("Error", "team not found")
        else:
            self.lineEdit_3.setText(topen)
            for i in range(len(si)):
                item=si[i][0]
                self.listWidget_2.addItem(item)
            
        self.open_screen.lineEdit.clear()
        self.openDialog.close()
            
        
        
        

    def load_names(self):
        BAT='BAT'
        BOWL='BWL'
        AR='AR'
        WK='WK'
        if self.BAT.isChecked()==True:
            curs.execute("select Player from match where ctg='"+BAT+"';")
            BT=curs.fetchall()
            self.listWidget.clear()
            for i in range(len(BT)):
                item=BT[i][0]
                self.listWidget.addItem(item)

        if self.BOW.isChecked()==True:
            curs.execute("select Player from match where ctg='"+BOWL+"';")
            BW=curs.fetchall()
            self.listWidget.clear()
            for i in range(len(BW)):
                item2=BW[i][0]
                self.listWidget.addItem(item2)

        if self.AR.isChecked()==True:
            curs.execute("select Player from match where ctg='"+AR+"';")
            A=curs.fetchall()
            self.listWidget.clear()
            for i in range(len(A)):
                item3=A[i][0]
                self.listWidget.addItem(item3)

        if self.WK.isChecked()==True:
            curs.execute("select Player from match where ctg='"+WK+"';")
            W=curs.fetchall()
            self.listWidget.clear()
            for i in range(len(W)):
                item4=W[i][0]
                self.listWidget.addItem(item4)

                
    def removelist1(self, item):
        if self.BAT.isChecked()==True:
            self.Batsmancount+=1
            if (self.Batsmancount>=0 and self.Batsmancount<5):
                 self.listWidget.takeItem(self.listWidget.row(item))
                 curs.execute("SELECT points from match WHERE Player='"+item.text()+"';")
                 row=curs.fetchone()
                 if self.avl<int(row[0]):
                     messagebox.showerror("Error", "Points Exhausted")
                 else:
                     self.avl-=int(row[0])
                     self.used+=int(row[0])
                     self.lineEdit_2.setText(str(self.used))
                     self.lineEdit.setText(str(self.avl))
                     self.listWidget_2.addItem(item.text())
                     self.batsmancount.setText(str(self.Batsmancount))
            else:
                messagebox.showerror("Error", "only 4 batsmen are allowed")

        elif self.BOW.isChecked()==True:
            self.Bowcount+=1
            if (self.Bowcount>=0 and self.Bowcount<5):
                self.listWidget.takeItem(self.listWidget.row(item))
                curs.execute("SELECT points from match WHERE Player='"+item.text()+"';")
                row=curs.fetchone()
                if self.avl<int(row[0]):
                     messagebox.showerror("Error", "Points Exhausted")
                else:
                     self.avl-=int(row[0])
                     self.used+=int(row[0])
                     self.lineEdit_2.setText(str(self.used))
                     self.lineEdit.setText(str(self.avl))
                     self.listWidget_2.addItem(item.text())
                     self.bowlcount.setText(str(self.Bowcount))
            else:
                messagebox.showerror("Error", "only 4 bowlers are allowed")

        elif self.WK.isChecked()==True:
            self.wkeepercount+=1
            if (self.wkeepercount>=0 and self.wkeepercount<2):
                self.listWidget.takeItem(self.listWidget.row(item))
                curs.execute("SELECT points from match WHERE Player='"+item.text()+"';")
                row=curs.fetchone()
                if self.avl<int(row[0]):
                     messagebox.showerror("Error", "Points Exhausted")
                else:
                     self.avl-=int(row[0])
                     self.used+=int(row[0])
                     self.lineEdit_2.setText(str(self.used))
                     self.lineEdit.setText(str(self.avl))
                     self.listWidget_2.addItem(item.text())
                     self.Wkeepercount.setText(str(self.wkeepercount))
            else:
                messagebox.showerror("Error", "only 1 wicket-keeper is allowed")

        elif self.AR.isChecked()==True:
            self.allcount+=1
            if (self.allcount>=0 and self.allcount<3):
                self.listWidget.takeItem(self.listWidget.row(item))
                curs.execute("SELECT points from match WHERE Player='"+item.text()+"';")
                row=curs.fetchone()
                if self.avl<int(row[0]):
                     messagebox.showerror("Error", "Points Exhausted")
                else:
                     self.avl-=int(row[0])
                     self.used+=int(row[0])
                     self.lineEdit_2.setText(str(self.used))
                     self.lineEdit.setText(str(self.avl))
                     self.listWidget_2.addItem(item.text())
                     self.Allcount.setText(str(self.allcount))
            else:
                messagebox.showerror("Error", "only 2 all-rounders are allowed")


    def removelist2(self,item):
        
        if self.BAT.isChecked()==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.Batsmancount=self.Batsmancount-1
            self.listWidget.addItem(item.text())
            self.batsmancount.setText(str(self.Batsmancount))
            curs.execute("SELECT points from match WHERE Player='"+item.text()+"';")
            row=curs.fetchone()
            self.avl+=int(row[0])
            self.used-=int(row[0])
            self.lineEdit_2.setText(str(self.used))
            self.lineEdit.setText(str(self.avl))

        elif self.BOW.isChecked()==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.Bowcount=self.Bowcount-1
            self.listWidget.addItem(item.text())
            self.bowlcount.setText(str(self.Bowcount))
            curs.execute("SELECT points from match WHERE Player='"+item.text()+"';")
            row=curs.fetchone()
            self.avl+=int(row[0])
            self.used-=int(row[0])
            self.lineEdit_2.setText(str(self.used))
            self.lineEdit.setText(str(self.avl))

        elif self.WK.isChecked()==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.wkeepercount-=1
            self.listWidget.addItem(item.text())
            self.Wkeepercount.setText(str(self.wkeepercount))
            curs.execute("SELECT points from match WHERE Player='"+item.text()+"';")
            row=curs.fetchone()
            self.avl+=int(row[0])
            self.used-=int(row[0])
            self.lineEdit_2.setText(str(self.used))
            self.lineEdit.setText(str(self.avl))

        elif self.AR.isChecked()==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.allcount-=1
            self.listWidget.addItem(item.text())
            self.Allcount.setText(str(self.allcount))
            curs.execute("SELECT points from match WHERE Player='"+item.text()+"';")
            row=curs.fetchone()
            self.avl+=int(row[0])
            self.used-=int(row[0])
            self.lineEdit_2.setText(str(self.used))
            self.lineEdit.setText(str(self.avl))

        

            
        
            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
