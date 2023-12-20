from typing import *
from PyQt5.QtWidgets import *
from ui import *
from constants import *
from components import *
from viewmodels import *
from nttinject import *

from .NewProjectDialog import NewProjectDialog


@dependency_inject(StartupWidgetViewModel)
class StartupWidgetView(QWidget):
    def __init__(self, vmStartupWidgetViewModel: StartupWidgetViewModel) -> None:
        super().__init__()
        self._ui = Ui_StartupWidget()
        self._ui.setupUi(self)

        self._vmStartupWidgetViewModel = vmStartupWidgetViewModel

        self._LoadTemplates()

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
        wNewProjectDialog = NewProjectDialog(
            self._vmStartupWidgetViewModel.TemplateNames, strTemplateName
        )

        bResult: bool = wNewProjectDialog.exec_()
