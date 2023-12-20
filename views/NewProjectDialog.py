from PyQt5.QtWidgets import *
from typing import *
from viewmodels import *
from models import *
from constants import *
from ui import *
from nttinject import *


@dependency_inject(NewProjectDialogViewModel)
class NewProjectDialog(QDialog):
    def __init__(
        self,
        vmNewProjectDialogViewModel: NewProjectDialogViewModel,
        strTemplateNames: List[str],
        strTemplateName: str,
    ) -> None:
        super().__init__()

        self._vmNewProjectDialogViewModel = vmNewProjectDialogViewModel
        self._strTemplateName = strTemplateName
        self._ui = Ui_NewProjectDialog()
        self._ui.setupUi(self)

        for strName in strTemplateNames:
            self._ui.templateComboBox.addItem(strName)

        self._Init()

        self._vmNewProjectDialogViewModel.ProjectName = UNTILTLED_PROJECT_NAME
        self._vmNewProjectDialogViewModel.TemplateName = strTemplateName
        self._vmNewProjectDialogViewModel.ProjectPath = DEFAULT_PROJECT_PATH

    def _Init(self) -> None:
        self._vmNewProjectDialogViewModel.ProjectNameSignal.Connect(
            self._OnProjectNameChanged
        )
        self._vmNewProjectDialogViewModel.ProjectFullPathSignal.Connect(
            self._OnProjectFullPathChanged
        )

        self._vmNewProjectDialogViewModel.TemplateNameSignal.Connect(
            self._OnTemplateNameChanged
        )

        self._ui.browseButton.clicked.connect(self._OnClickedBrowseButton)
        self._ui.nameLineEdit.textChanged.connect(self._OnTextChangedProjectName)

    def _OnProjectNameChanged(self, strProjectName: str) -> None:
        self._ui.nameLineEdit.setText(strProjectName)

    def _OnProjectFullPathChanged(self, strProjectPath: str) -> None:
        self._ui.pathLineEdit.setText(self._vmNewProjectDialogViewModel.ProjectFullPath)

    def _OnTemplateNameChanged(self, strTemplateName: str) -> None:
        self._ui.templateComboBox.setCurrentText(strTemplateName)

    def _OnTextChangedProjectName(self, strText: str) -> None:
        self._vmNewProjectDialogViewModel.ProjectName = strText

    def _OnClickedBrowseButton(self) -> None:
        options = QFileDialog.Options()

        options |= QFileDialog.ShowDirsOnly

        strFolderPath: str = QFileDialog.getExistingDirectory(
            self,
            "Choose Folder",
            self._vmNewProjectDialogViewModel.ProjectPath,
            options=options,
        )

        if strFolderPath is not None:
            self._vmNewProjectDialogViewModel.ProjectPath = strFolderPath
        else:
            pass
