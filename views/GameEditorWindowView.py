from PyQt5.QtWidgets import *
from viewmodels import *
from constants import *
from typing import *
from ui import *

from .GameEditorCentralWidgetView import GameEditorCentralWidgetView
from .LogDockWidgetView import *


@dependency_inject(GameEditorWindowViewModel)
class GameEditorWindowView(QMainWindow):
    def __init__(self, vmGameEditorWindowViewModel: GameEditorWindowViewModel) -> None:
        super().__init__()
        self._vmGameEditorWindowViewModel = vmGameEditorWindowViewModel

        self._ui = Ui_GameEditorWindow()
        self._ui.setupUi(self)

        self.setCentralWidget(GameEditorCentralWidgetView())

        self._ui.logDockWidget.setWidget(LogDockWidgetView())

        self._vmGameEditorWindowViewModel.EditorWindowTitleChangedSignal.Connect(
            self._OnWindowTitleChanged
        )
        self._vmGameEditorWindowViewModel.EditorWindowTitleChangedSignal.Emit()

    def _OnWindowTitleChanged(self) -> None:
        self.setWindowTitle(self._vmGameEditorWindowViewModel.WindowTitle)
