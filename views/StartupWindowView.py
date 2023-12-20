from typing import *
from PyQt5.QtWidgets import *
from ui import *
from constants import *

from .StartupWidgetView import *
from .GameEditorWindowView import *


class StartupWindowView(QMainWindow):
    def __init__(self, wGameEditorWindow: GameEditorWindowView) -> None:
        super().__init__()
        self._ui = Ui_StartupWindow()
        self._ui.setupUi(self)
        self._wGameEditorWindow = wGameEditorWindow

        wStartupWidget = StartupWidgetView()
        self.setCentralWidget(wStartupWidget)

        wStartupWidget.CloseSignal.Connect(self._OnOpenGameEditor)

    def _OnOpenGameEditor(self) -> None:
        self.close()
        self._wGameEditorWindow.showMaximized()
