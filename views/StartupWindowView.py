import PyQt5
import ui

from .StartupWidgetView import StartupWidgetView
from .GameEditorWindowView import GameEditorWindowView


class StartupWindowView(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, wGameEditorWindow: GameEditorWindowView) -> None:
        super().__init__()
        self._ui = ui.Ui_StartupWindow()
        self._ui.setupUi(self)
        self._wGameEditorWindow = wGameEditorWindow

        wStartupWidget = StartupWidgetView()
        self.setCentralWidget(wStartupWidget)

        wStartupWidget.CloseSignal.Connect(self._OnOpenGameEditor)

    def _OnOpenGameEditor(self) -> None:
        self.close()
        self._wGameEditorWindow.showMaximized()
