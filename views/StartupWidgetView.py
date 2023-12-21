from typing import *
from PyQt5.QtWidgets import *
from ui import *
from constants import *
from components import *
from viewmodels import *
from nttinject import *
from ntt_signal import *
from .NewProjectDialogView import *


@dependency_inject(StartupWidgetViewModel)
class StartupWidgetView(QWidget):
    def __init__(self, vmStartupWidgetViewModel: StartupWidgetViewModel) -> None:
        super().__init__()
        self._ui = Ui_StartupWidget()
        self._ui.setupUi(self)
        self.CloseSignal = Signal()

        self._vmStartupWidgetViewModel = vmStartupWidgetViewModel

        self._LoadTemplates()
        self._ui.browseProjectButton.clicked.connect(self._OnClicked_BrowseProject)

        self._vmStartupWidgetViewModel.OpenProjectErrorSignal.Connect(
            self._OnOpenProjectErrorRaise
        )

    def _LoadTemplates(self) -> None:
        for strTemplateInfo in self._vmStartupWidgetViewModel.TemplatesInfo:
            strTemplateName = strTemplateInfo
            wTemplateLabel = DoubleClickedLabel(strTemplateName)
            wTemplateLabel.onDoubleClicked.Connect(self._OnClicked_TemplateButton)
            self._ui.templatesLayout.addWidget(wTemplateLabel)

        self._ui.templatesLayout.addItem(
            QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
            )
        )

    def _OnClicked_TemplateButton(self, strTemplateName: str) -> None:
        wNewProjectDialog = NewProjectDialogView(
            self._vmStartupWidgetViewModel.TemplateNames, strTemplateName
        )

        bResult: bool = wNewProjectDialog.exec_()
        if bResult:
            self.CloseSignal.Emit()

    def _OnOpenProjectErrorRaise(self, strErrorMessage: str) -> None:
        QMessageBox.critical(self, "Open Project Failed", strErrorMessage)

    def _OnClicked_BrowseProject(self) -> None:
        options = QFileDialog.Options()

        wFileDialog = QFileDialog(self, options=options)
        wFileDialog.setNameFilter("Text Files (*.txt);;All Files (*)")

        strFile, _ = QFileDialog().getOpenFileName(
            self,
            "Choose Project",
            DEFAULT_PROJECT_PATH,
            f"NTT Engine Project (*.{PROJECT_EXTENSION})",
            options=options,
        )

        if strFile:
            bResult = self._vmStartupWidgetViewModel.OpenProject(strFile)
            if bResult:
                self.CloseSignal.Emit()
