# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_New(object):
    def setupUi(self, New):
        New.setObjectName("New")
        New.resize(400, 300)
        self.label = QtWidgets.QLabel(New)
        self.label.setGeometry(QtCore.QRect(70, 5, 321, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(New)
        self.lineEdit.setGeometry(QtCore.QRect(72, 70, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(New)
        self.pushButton.setGeometry(QtCore.QRect(150, 130, 91, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(New)
        QtCore.QMetaObject.connectSlotsByName(New)

    def retranslateUi(self, New):
        _translate = QtCore.QCoreApplication.translate
        New.setWindowTitle(_translate("New", "New"))
        self.label.setText(_translate("New", "<html><head/><body><p><span style=\" font-size:10pt;\">Enter Name of the team:</span></p></body></html>"))
        self.pushButton.setText(_translate("New", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New = QtWidgets.QDialog()
    ui = Ui_New()
    ui.setupUi(New)
    New.show()
    sys.exit(app.exec_())
