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
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(NewProjectDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nameLineEdit = QtWidgets.QLineEdit(NewProjectDialog)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.label_2 = QtWidgets.QLabel(NewProjectDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.templateComboBox = QtWidgets.QComboBox(NewProjectDialog)
        self.templateComboBox.setObjectName("templateComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.templateComboBox)
        self.label_3 = QtWidgets.QLabel(NewProjectDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(NewProjectDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectRadioButton = QtWidgets.QRadioButton(NewProjectDialog)
        self.projectRadioButton.setChecked(True)
        self.projectRadioButton.setObjectName("projectRadioButton")
        self.horizontalLayout.addWidget(self.projectRadioButton)
        self.libraryRadioButton = QtWidgets.QRadioButton(NewProjectDialog)
        self.libraryRadioButton.setObjectName("libraryRadioButton")
        self.horizontalLayout.addWidget(self.libraryRadioButton)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pathLineEdit = QtWidgets.QLineEdit(NewProjectDialog)
        self.pathLineEdit.setReadOnly(True)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.horizontalLayout_2.addWidget(self.pathLineEdit)
        self.browseButton = QtWidgets.QPushButton(NewProjectDialog)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout_2.addWidget(self.browseButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewProjectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewProjectDialog)
        self.buttonBox.accepted.connect(NewProjectDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(NewProjectDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(NewProjectDialog)

    def retranslateUi(self, NewProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        NewProjectDialog.setWindowTitle(_translate("NewProjectDialog", "Dialog"))
        self.label.setText(_translate("NewProjectDialog", "Name"))
        self.label_2.setText(_translate("NewProjectDialog", "Template"))
        self.label_3.setText(_translate("NewProjectDialog", "Path"))
        self.label_4.setText(_translate("NewProjectDialog", "Project Type"))
        self.projectRadioButton.setText(_translate("NewProjectDialog", "Project"))
        self.libraryRadioButton.setText(_translate("NewProjectDialog", "Library"))
        self.browseButton.setText(_translate("NewProjectDialog", "Browse"))