import PyQt5


def ClearLayoutItem(layout: PyQt5.QtWidgets.QLayout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
