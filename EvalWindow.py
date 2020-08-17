# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EvalWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
myteam= sqlite3.connect("Team.db")


class Ui_evaluate(object):
    def setupUi(self, evaluate):
        evaluate.setObjectName("evaluate")
        evaluate.resize(465, 338)
        self.label = QtWidgets.QLabel(evaluate)
        self.label.setGeometry(QtCore.QRect(0, 10, 461, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(evaluate)
        self.comboBox.setGeometry(QtCore.QRect(120, 50, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(evaluate)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(evaluate)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 121, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(evaluate)
        self.comboBox_2.setGeometry(QtCore.QRect(370, 50, 91, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(evaluate)
        self.label_4.setGeometry(QtCore.QRect(20, 85, 131, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(evaluate)
        self.label_5.setGeometry(QtCore.QRect(320, 79, 91, 31))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(evaluate)
        self.pushButton.setGeometry(QtCore.QRect(100, 300, 271, 31))
        self.pushButton.setObjectName("pushButton")
        self.listWidget_2 = QtWidgets.QListWidget(evaluate)
        self.listWidget_2.setGeometry(QtCore.QRect(245, 110, 211, 181))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget = QtWidgets.QListWidget(evaluate)
        self.listWidget.setGeometry(QtCore.QRect(0, 110, 231, 181))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(evaluate)
        QtCore.QMetaObject.connectSlotsByName(evaluate)

    def retranslateUi(self, evaluate):
        _translate = QtCore.QCoreApplication.translate
        evaluate.setWindowTitle(_translate("evaluate", "Evaluation"))
        self.label.setText(_translate("evaluate", "<html><head/><body><p><span style=\" font-size:10pt;\">Evaluate the performance of your fantasy team:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("evaluate", "-select team-"))
        self.label_2.setText(_translate("evaluate", "<html><head/><body><p><span style=\" font-size:10pt;\">select team:</span></p></body></html>"))
        self.label_3.setText(_translate("evaluate", "<html><head/><body><p><span style=\" font-size:10pt;\">select match:</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("evaluate", "-select match-"))
        self.comboBox_2.setItemText(1, _translate("evaluate", "Match 1"))
        self.comboBox_2.setItemText(2, _translate("evaluate", "Match 2"))
        self.comboBox_2.setItemText(3, _translate("evaluate", "Match 3"))
        self.comboBox_2.setItemText(4, _translate("evaluate", "Match 4"))
        self.label_4.setText(_translate("evaluate", "<html><head/><body><p><span style=\" font-size:10pt;\">Players</span></p></body></html>"))
        self.label_5.setText(_translate("evaluate", "<html><head/><body><p><span style=\" font-size:10pt;\">Score</span></p></body></html>"))
        self.pushButton.setText(_translate("evaluate", "Calculate score"))

        cu= myteam.cursor()
        cu.execute("SELECT names from teams;")
        team= cu.fetchall()
        teamlist=[]
        for i in range(len(team)):
            teamlist.append(team[i][0])

        for name in set(teamlist):
            self.comboBox.addItem(name)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluate = QtWidgets.QDialog()
    ui = Ui_evaluate()
    ui.setupUi(evaluate)
    evaluate.show()
    sys.exit(app.exec_())
