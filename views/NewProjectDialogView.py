import PyQt5
import typing
import viewmodels
import constants
import ui
import nttinject


@nttinject.dependency_inject(viewmodels.NewProjectDialogViewModel)
class NewProjectDialogView(PyQt5.QtWidgets.QDialog):
    def __init__(
        self,
        vmNewProjectDialogViewModel: viewmodels.NewProjectDialogViewModel,
        strTemplateNames: typing.List[str],
        strTemplateName: str,
    ) -> None:
        super().__init__()

        self._vmNewProjectDialogViewModel = vmNewProjectDialogViewModel
        self._strTemplateName = strTemplateName
        self._ui = ui.Ui_NewProjectDialog()
        self._ui.setupUi(self)

        for strName in strTemplateNames:
            self._ui.templateComboBox.addItem(strName)

        self._Init()
        self._vmNewProjectDialogViewModel.TemplateName = strTemplateName
        self._Reset()

    def _Reset(self) -> None:
        self._vmNewProjectDialogViewModel.ProjectName = constants.UNTILTLED_PROJECT_NAME
        self._vmNewProjectDialogViewModel.ProjectPath = constants.DEFAULT_PROJECT_PATH

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
        self._vmNewProjectDialogViewModel.IsValidSignal.Connect(
            self._OnProjectIsValidChanged
        )
        self._vmNewProjectDialogViewModel.CreateProjectErrorSignal.Connect(
            self._OnCreateProjectRaiseError
        )

        self._ui.browseButton.clicked.connect(self._OnClickedBrowseButton)
        self._ui.nameLineEdit.textChanged.connect(self._OnTextChangedProjectName)
        self._ui.cancelButton.clicked.connect(self._OnClickedCancelButton)
        self._ui.newButton.clicked.connect(self._OnClickedNewButton)

    def _OnProjectNameChanged(self, strProjectName: str) -> None:
        self._ui.nameLineEdit.setText(strProjectName)

    def _OnProjectFullPathChanged(self, strProjectPath: str) -> None:
        self._ui.pathLineEdit.setText(self._vmNewProjectDialogViewModel.ProjectFullPath)

    def _OnTemplateNameChanged(self, strTemplateName: str) -> None:
        self._ui.templateComboBox.setCurrentText(strTemplateName)

    def _OnTextChangedProjectName(self, strText: str) -> None:
        self._vmNewProjectDialogViewModel.ProjectName = strText

    def _OnProjectIsValidChanged(self) -> None:
        self._ui.newButton.setEnabled(self._vmNewProjectDialogViewModel.IsValid)

    def _OnClickedBrowseButton(self) -> None:
        options = PyQt5.QtWidgetsQFileDialog.Options()

        options |= PyQt5.QtWidgets.QFileDialog.ShowDirsOnly

        strFolderPath: str = PyQt5.QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Choose Folder",
            self._vmNewProjectDialogViewModel.ProjectPath,
            options=options,
        )

        if strFolderPath is not None:
            self._vmNewProjectDialogViewModel.ProjectPath = strFolderPath
        else:
            pass

    def _OnClickedCancelButton(self) -> None:
        self.reject()

    def _OnClickedNewButton(self) -> None:
        bResult = self._vmNewProjectDialogViewModel.CreateNewProject()
        if bResult:
            self.accept()
        else:
            self._Reset()

    def _OnCreateProjectRaiseError(self, strErrorMessage: str) -> None:
        PyQt5.QtWidgets.QMessageBox.critical(
            self, "Create Project Error", strErrorMessage
        )
