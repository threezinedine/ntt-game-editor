# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/ui_files\StartupWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartupWindow(object):
    def setupUi(self, StartupWindow):
        StartupWindow.setObjectName("StartupWindow")
        StartupWindow.resize(600, 498)
        self.centralwidget = QtWidgets.QWidget(StartupWindow)
        self.centralwidget.setObjectName("centralwidget")
        StartupWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartupWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName("menubar")
        StartupWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StartupWindow)
        self.statusbar.setObjectName("statusbar")
        StartupWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StartupWindow)
        QtCore.QMetaObject.connectSlotsByName(StartupWindow)

    def retranslateUi(self, StartupWindow):
        _translate = QtCore.QCoreApplication.translate
        StartupWindow.setWindowTitle(_translate("StartupWindow", "NTT Engine"))
