from PyQt5.QtWidgets import *
from viewmodels import *
from constants import *
from typing import *
from ui import *

from .GameEditorCentralWidgetView import GameEditorCentralWidgetView
from .LogDockWidgetView import *


class GameEditorWindowView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self._ui = Ui_GameEditorWindow()
        self._ui.setupUi(self)

        self.setCentralWidget(GameEditorCentralWidgetView())

        self._ui.logDockWidget.setWidget(LogDockWidgetView())
