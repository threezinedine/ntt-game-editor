# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/ui_files\GameEditor.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameEditorWindow(object):
    def setupUi(self, GameEditorWindow):
        GameEditorWindow.setObjectName("GameEditorWindow")
        GameEditorWindow.resize(416, 380)
        self.centralwidget = QtWidgets.QWidget(GameEditorWindow)
        self.centralwidget.setObjectName("centralwidget")
        GameEditorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GameEditorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        GameEditorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GameEditorWindow)
        self.statusbar.setObjectName("statusbar")
        GameEditorWindow.setStatusBar(self.statusbar)
        self.logDockWidget = QtWidgets.QDockWidget(GameEditorWindow)
        self.logDockWidget.setObjectName("logDockWidget")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.logDockWidget.setWidget(self.dockWidgetContents_2)
        GameEditorWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.logDockWidget)
        self.actionFile = QtWidgets.QAction(GameEditorWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionProject = QtWidgets.QAction(GameEditorWindow)
        self.actionProject.setObjectName("actionProject")
        self.actionFile_2 = QtWidgets.QAction(GameEditorWindow)
        self.actionFile_2.setObjectName("actionFile_2")
        self.actionFile_3 = QtWidgets.QAction(GameEditorWindow)
        self.actionFile_3.setObjectName("actionFile_3")
        self.actionSave = QtWidgets.QAction(GameEditorWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(GameEditorWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionUndo = QtWidgets.QAction(GameEditorWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.menuNew.addAction(self.actionFile)
        self.menuNew.addAction(self.actionProject)
        self.menuOpen.addAction(self.actionFile_2)
        self.menuOpen.addAction(self.actionFile_3)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUndo)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(GameEditorWindow)
        QtCore.QMetaObject.connectSlotsByName(GameEditorWindow)

    def retranslateUi(self, GameEditorWindow):
        _translate = QtCore.QCoreApplication.translate
        GameEditorWindow.setWindowTitle(_translate("GameEditorWindow", "Game Editor"))
        self.menuFile.setTitle(_translate("GameEditorWindow", "File"))
        self.menuNew.setTitle(_translate("GameEditorWindow", "New"))
        self.menuOpen.setTitle(_translate("GameEditorWindow", "Open"))
        self.logDockWidget.setWindowTitle(_translate("GameEditorWindow", "Log"))
        self.actionFile.setText(_translate("GameEditorWindow", "Project"))
        self.actionProject.setText(_translate("GameEditorWindow", "File"))
        self.actionFile_2.setText(_translate("GameEditorWindow", "Project"))
        self.actionFile_3.setText(_translate("GameEditorWindow", "File"))
        self.actionSave.setText(_translate("GameEditorWindow", "Save"))
        self.actionSave_As.setText(_translate("GameEditorWindow", "Save As"))
        self.actionUndo.setText(_translate("GameEditorWindow", "Undo"))
