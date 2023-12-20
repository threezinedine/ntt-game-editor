from typing import *
from PyQt5.QtWidgets import *
from ui import *
from constants import *

from .StartupWidgetView import *


class StartupWindowView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._ui = Ui_StartupWindow()
        self._ui.setupUi(self)

        wStartupWidget = StartupWidgetView()
        self.setCentralWidget(wStartupWidget)