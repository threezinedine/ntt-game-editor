from typing import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ntt_signal import Signal
from utils import *


class DoubleClickedLabel(QLabel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.onDoubleClicked = Signal(str)

        self.setStyleSheet(CssLoader("double-clicked-label.css").Content)
        self.setCursor(Qt.PointingHandCursor)

    def mouseDoubleClickEvent(self, a0: Union[QMouseEvent, None]) -> None:
        self.onDoubleClicked.Emit(self.text())
        return super().mouseDoubleClickEvent(a0)
