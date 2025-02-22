# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 572)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputData = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputData.setGeometry(QtCore.QRect(10, 10, 841, 131))
        self.inputData.setObjectName("inputData")
        self.resultData = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.resultData.setGeometry(QtCore.QRect(10, 150, 841, 141))
        self.resultData.setObjectName("resultData")
        self.typeGet = QtWidgets.QComboBox(self.centralwidget)
        self.typeGet.setGeometry(QtCore.QRect(20, 480, 161, 22))
        self.typeGet.setObjectName("typeGet")
        self.typeGet.addItem("")
        self.typeGet.addItem("")
        self.typeGet.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 450, 71, 21))
        self.label.setObjectName("label")
        self.numThread = QtWidgets.QSpinBox(self.centralwidget)
        self.numThread.setGeometry(QtCore.QRect(300, 450, 51, 22))
        self.numThread.setMinimum(1)
        self.numThread.setObjectName("numThread")
        self.typeLogin = QtWidgets.QComboBox(self.centralwidget)
        self.typeLogin.setGeometry(QtCore.QRect(20, 450, 161, 22))
        self.typeLogin.setObjectName("typeLogin")
        self.typeLogin.addItem("")
        self.typeLogin.addItem("")
        self.typeLogin.addItem("")
        self.btnEvent = QtWidgets.QPushButton(self.centralwidget)
        self.btnEvent.setGeometry(QtCore.QRect(680, 460, 151, 61))
        self.btnEvent.setObjectName("btnEvent")
        self.btnExportFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnExportFile.setGeometry(QtCore.QRect(230, 500, 121, 31))
        self.btnExportFile.setObjectName("btnExportFile")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 450, 201, 21))
        self.label_2.setObjectName("label_2")
        self.success_total = QtWidgets.QLabel(self.centralwidget)
        self.success_total.setGeometry(QtCore.QRect(600, 450, 61, 21))
        self.success_total.setObjectName("success_total")
        self.typeResult = QtWidgets.QComboBox(self.centralwidget)
        self.typeResult.setGeometry(QtCore.QRect(20, 510, 161, 22))
        self.typeResult.setObjectName("typeResult")
        self.typeResult.addItem("")
        self.typeResult.addItem("")
        self.typeResult.addItem("")
        self.btnContactAdmin = QtWidgets.QPushButton(self.centralwidget)
        self.btnContactAdmin.setGeometry(QtCore.QRect(440, 490, 151, 41))
        self.btnContactAdmin.setObjectName("btnContactAdmin")
        self.status = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 300, 841, 141))
        self.status.setObjectName("status")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TOOL GET TÀI NGUYÊN HÀNG LOẠT- K.Auto"))
        self.inputData.setPlaceholderText(_translate("MainWindow", "NHẬP TÀI NGUYÊN VÀO ĐÂY"))
        self.resultData.setPlaceholderText(_translate("MainWindow", "TÀI NGUYÊN SAU KHI CHẠY SẼ XUẤT HIỆN Ở ĐÂY"))
        self.typeGet.setItemText(0, _translate("MainWindow", "CHỌN DẠNG GET"))
        self.typeGet.setItemText(1, _translate("MainWindow", "COOKIE"))
        self.typeGet.setItemText(2, _translate("MainWindow", "ACCESS_TOKEN EAAB"))
        self.label.setText(_translate("MainWindow", "SỐ LUỒNG"))
        self.typeLogin.setItemText(0, _translate("MainWindow", "CHỌN DẠNG LOGIN"))
        self.typeLogin.setItemText(1, _translate("MainWindow", "COOKIE"))
        self.typeLogin.setItemText(2, _translate("MainWindow", "USER|PASS|2Fa"))
        self.btnEvent.setText(_translate("MainWindow", "BẮT ĐẦU"))
        self.btnExportFile.setText(_translate("MainWindow", "EXPORT FILE"))
        self.label_2.setText(_translate("MainWindow", "THÀNH CÔNG/ĐÃ CHẠY/TỔNG :"))
        self.success_total.setText(_translate("MainWindow", "0/0/0"))
        self.typeResult.setItemText(0, _translate("MainWindow", "CHỌN DẠNG XUẤT"))
        self.typeResult.setItemText(1, _translate("MainWindow", "UID|RESULT"))
        self.typeResult.setItemText(2, _translate("MainWindow", "RESULT"))
        self.btnContactAdmin.setText(_translate("MainWindow", "LIÊN HỆ ADMIN"))
        self.status.setPlaceholderText(_translate("MainWindow", "TOOL ĐƯỢC PHÁT TRIỂN BỞI K.AUTO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
