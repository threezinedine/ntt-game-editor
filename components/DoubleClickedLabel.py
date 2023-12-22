import typing
import PyQt5
import ntt_signal
import utils


class DoubleClickedLabel(PyQt5.QtWidgets.QLabel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.onDoubleClicked = ntt_signal.Signal(str)

        self.setStyleSheet(utils.CssLoader("double-clicked-label.css").Content)
        self.setCursor(PyQt5.QtCore.Qt.PointingHandCursor)

    def mouseDoubleClickEvent(
        self, a0: typing.Union[PyQt5.QtGui.QMouseEvent, None]
    ) -> None:
        self.onDoubleClicked.Emit(self.text())
        return super().mouseDoubleClickEvent(a0)
