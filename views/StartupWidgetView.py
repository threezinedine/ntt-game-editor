import typing
import PyQt5
import ui
import constants
import components
import nttinject
import ntt_signal
import viewmodels
import utils

from .NewProjectDialogView import NewProjectDialogView


@nttinject.dependency_inject(viewmodels.StartupWidgetViewModel)
class StartupWidgetView(PyQt5.QtWidgets.QWidget):
    def __init__(
        self,
        vmStartupWidgetViewModel: viewmodels.StartupWidgetViewModel,
    ) -> None:
        super().__init__()
        self._ui = ui.Ui_StartupWidget()
        self._ui.setupUi(self)
        self.CloseSignal = ntt_signal.Signal()

        self._vmStartupWidgetViewModel = vmStartupWidgetViewModel

        self._LoadTemplates()
        self._LoadRecentProjects()
        self._ui.browseProjectButton.clicked.connect(self._OnClicked_BrowseProject)
        self._ui.clearRecentProjectsButton.clicked.connect(
            self._OnClicked_ClearRecentProjectsButton
        )

        self._vmStartupWidgetViewModel.OpenProjectErrorSignal.Connect(
            self._OnOpenProjectErrorRaise
        )

    def _LoadTemplates(self) -> None:
        for strTemplateInfo in self._vmStartupWidgetViewModel.TemplatesInfo:
            strTemplateName = strTemplateInfo
            wTemplateLabel = components.DoubleClickedLabel(strTemplateName)
            wTemplateLabel.onDoubleClicked.Connect(self._OnClicked_TemplateButton)
            self._ui.templatesLayout.addWidget(wTemplateLabel)

        self._ui.templatesLayout.addItem(
            PyQt5.QtWidgets.QSpacerItem(
                20,
                40,
                PyQt5.QtWidgets.QSizePolicy.Minimum,
                PyQt5.QtWidgets.QSizePolicy.Expanding,
            )
        )

    def _LoadRecentProjects(self) -> None:
        for strProjectFile in reversed(self._vmStartupWidgetViewModel.RecentProjects):
            wProjectLabel = components.DoubleClickedLabel(strProjectFile)
            wProjectLabel.onDoubleClicked.Connect(self._OnClicked_ProjectButton)
            self._ui.recentProjectsLayout.addWidget(wProjectLabel)

        self._ui.recentProjectsLayout.addItem(
            PyQt5.QtWidgets.QSpacerItem(
                20,
                40,
                PyQt5.QtWidgets.QSizePolicy.Minimum,
                PyQt5.QtWidgets.QSizePolicy.Expanding,
            )
        )

    def _OnClicked_ProjectButton(self, strProjectFile: str) -> None:
        bResult = self._vmStartupWidgetViewModel.OpenProject(strProjectFile)
        if bResult:
            self.CloseSignal.Emit()

    def _OnClicked_TemplateButton(self, strTemplateName: str) -> None:
        wNewProjectDialog = NewProjectDialogView(
            self._vmStartupWidgetViewModel.TemplateNames, strTemplateName
        )

        bResult: bool = wNewProjectDialog.exec_()
        if bResult:
            self.CloseSignal.Emit()

    def _OnOpenProjectErrorRaise(self, strErrorMessage: str) -> None:
        PyQt5.QtWidgets.QMessageBox.critical(
            self, "Open Project Failed", strErrorMessage
        )

    def _OnClicked_BrowseProject(self) -> None:
        options = PyQt5.QtWidgets.QFileDialog.Options()

        wFileDialog = PyQt5.QtWidgets.QFileDialog(self, options=options)
        wFileDialog.setNameFilter("Text Files (*.txt);;All Files (*)")

        strFile, _ = PyQt5.QtWidgets.QFileDialog().getOpenFileName(
            self,
            "Choose Project",
            constants.DEFAULT_PROJECT_PATH,
            f"NTT Engine Project (*.{constants.PROJECT_EXTENSION})",
            options=options,
        )

        if strFile:
            bResult = self._vmStartupWidgetViewModel.OpenProject(strFile)
            if bResult:
                self.CloseSignal.Emit()

    def _OnClicked_ClearRecentProjectsButton(self) -> None:
        self._vmStartupWidgetViewModel.ClearRecentProjects()
        utils.ClearLayoutItem(self._ui.recentProjectsLayout)
