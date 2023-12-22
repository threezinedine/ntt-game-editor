import PyQt5
import nttinject
import ui
import viewmodels


@nttinject.dependency_inject(viewmodels.LogDockWidgetViewModel)
class LogDockWidgetView(PyQt5.QtWidgets.QWidget):
    def __init__(
        self, vmLogDockWidgetViewModel: viewmodels.LogDockWidgetViewModel
    ) -> None:
        super().__init__()

        self._ui = ui.Ui_LogWidget()
        self._ui.setupUi(self)

        self._vmLogDockWidgetViewModel = vmLogDockWidgetViewModel
