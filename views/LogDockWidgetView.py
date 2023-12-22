import PyQt5.QtWidgets
import nttinject
import ui
import viewmodels


@nttinject.dependency_inject(viewmodels.LogDockWidgetViewModel)
class LogDockWidgetView(PyQt5.QtWidgets.QWidget):
    def __init__(
        self,
        vmLogDockWidgetViewModel: viewmodels.LogDockWidgetViewModel,
    ) -> None:
        super().__init__()

        self._ui = ui.Ui_LogWidget()
        self._ui.setupUi(self)

        self._vmLogDockWidgetViewModel = vmLogDockWidgetViewModel

        self._vmLogDockWidgetViewModel.NewLogMessgeSignal.Connect(
            self._OnLogMessagesChange
        )
        self._ui.clearLogButton.clicked.connect(self._OnClicked_ClearLogButton)

    def _OnLogMessagesChange(self) -> None:
        self._ui.logTreeWidget.clear()

        for tupMessageInfo in self._vmLogDockWidgetViewModel.MessagesInfo:
            wItem = PyQt5.QtWidgets.QTreeWidgetItem(self._ui.logTreeWidget)

            for i, data in enumerate(tupMessageInfo):
                wItem.setData(i, 0, str(data))

    def _OnClicked_ClearLogButton(self) -> None:
        self._vmLogDockWidgetViewModel.ClearLog()
