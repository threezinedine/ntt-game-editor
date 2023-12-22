import PyQt5
import viewmodels
import ui
import nttinject


@nttinject.dependency_inject(viewmodels.GameEditorCentralWidgetViewModel)
class GameEditorCentralWidgetView(PyQt5.QtWidgets.QWidget):
    def __init__(
        self,
        vmGameEditorCentralWidgetViewModel: viewmodels.GameEditorCentralWidgetViewModel,
    ) -> None:
        super().__init__()
        self._vmGameEditorCentralWidgetViewModel = vmGameEditorCentralWidgetViewModel

        self._ui = ui.Ui_GameEditorCentralWidget()
        self._ui.setupUi(self)
