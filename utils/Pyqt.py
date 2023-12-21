from PyQt5.QtWidgets import *


def ClearLayoutItem(layout: QLayout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
