from PyQt5.QtWidgets import *
from constants import *
from typing import *
from viewmodels import *
from services import *
from ui import *
from nttinject import *


@dependency_inject(GameEditorCentralWidgetViewModel)
class GameEditorCentralWidgetView(QWidget):
    def __init__(
        self, vmGameEditorCentralWidgetViewModel: GameEditorCentralWidgetViewModel
    ) -> None:
        super().__init__()
        self._vmGameEditorCentralWidgetViewModel = vmGameEditorCentralWidgetViewModel

        self._ui = Ui_GameEditorCentralWidget()
        self._ui.setupUi(self)
