# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/ui_files\NewWindowDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewProjectDialog(object):
    def setupUi(self, NewProjectDialog):
        NewProjectDialog.setObjectName("NewProjectDialog")
        NewProjectDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewProjectDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(NewProjectDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nameLineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pathLineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.pathLineEdit.setReadOnly(True)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.horizontalLayout_2.addWidget(self.pathLineEdit)
        self.browseButton = QtWidgets.QPushButton(self.frame_2)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout_2.addWidget(self.browseButton)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.templateComboBox = QtWidgets.QComboBox(self.frame_2)
        self.templateComboBox.setObjectName("templateComboBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.templateComboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectRadioButton = QtWidgets.QRadioButton(self.frame_2)
        self.projectRadioButton.setChecked(True)
        self.projectRadioButton.setObjectName("projectRadioButton")
        self.horizontalLayout.addWidget(self.projectRadioButton)
        self.libraryRadioButton = QtWidgets.QRadioButton(self.frame_2)
        self.libraryRadioButton.setObjectName("libraryRadioButton")
        self.horizontalLayout.addWidget(self.libraryRadioButton)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(NewProjectDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(self.frame)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.newButton = QtWidgets.QPushButton(self.frame)
        self.newButton.setObjectName("newButton")
        self.horizontalLayout_3.addWidget(self.newButton)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignBottom)

        self.retranslateUi(NewProjectDialog)
        QtCore.QMetaObject.connectSlotsByName(NewProjectDialog)

    def retranslateUi(self, NewProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        NewProjectDialog.setWindowTitle(_translate("NewProjectDialog", "Dialog"))
        self.label.setText(_translate("NewProjectDialog", "Name"))
        self.label_3.setText(_translate("NewProjectDialog", "Path"))
        self.label_2.setText(_translate("NewProjectDialog", "Template"))
        self.label_4.setText(_translate("NewProjectDialog", "Project Type"))
        self.browseButton.setText(_translate("NewProjectDialog", "Browse"))
        self.projectRadioButton.setText(_translate("NewProjectDialog", "Project"))
        self.libraryRadioButton.setText(_translate("NewProjectDialog", "Library"))
        self.cancelButton.setText(_translate("NewProjectDialog", "Cancel"))
        self.newButton.setText(_translate("NewProjectDialog", "New"))
