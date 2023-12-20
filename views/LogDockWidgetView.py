from PyQt5.QtWidgets import *
from nttinject import *
from ui import *
from services import *
from constants import *
from viewmodels import *


@dependency_inject(LogDockWidgetViewModel)
class LogDockWidgetView(QWidget):
    def __init__(self, vmLogDockWidgetViewModel: LogDockWidgetViewModel) -> None:
        super().__init__()

        self._ui = Ui_LogWidget()
        self._ui.setupUi(self)

        self._vmLogDockWidgetViewModel = vmLogDockWidgetViewModel
