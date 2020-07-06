from PyQt5.QtWidgets import QStackedWidget

from config import tables


class StackedWidget(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        for table in tables:
            self.addWidget(table(parent=parent))
        self.setMinimumWidth(200)
