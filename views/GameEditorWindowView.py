import PyQt5
import viewmodels
import ui
import nttinject

from .GameEditorCentralWidgetView import GameEditorCentralWidgetView
from .LogDockWidgetView import LogDockWidgetView


@nttinject.dependency_inject(viewmodels.GameEditorWindowViewModel)
class GameEditorWindowView(PyQt5.QtWidgets.QMainWindow):
    def __init__(
        self,
        vmGameEditorWindowViewModel: viewmodels.GameEditorWindowViewModel,
    ) -> None:
        super().__init__()
        self._vmGameEditorWindowViewModel = vmGameEditorWindowViewModel

        self._ui = ui.Ui_GameEditorWindow()
        self._ui.setupUi(self)

        self.setCentralWidget(GameEditorCentralWidgetView())

        self._ui.logDockWidget.setWidget(LogDockWidgetView())

        self._vmGameEditorWindowViewModel.EditorWindowTitleChangedSignal.Connect(
            self._OnWindowTitleChanged
        )
        self._vmGameEditorWindowViewModel.EditorWindowTitleChangedSignal.Emit()

    def _OnWindowTitleChanged(self) -> None:
        self.setWindowTitle(self._vmGameEditorWindowViewModel.WindowTitle)
