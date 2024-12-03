import common.constants as const
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QMessageBox, QScrollArea,
                             QVBoxLayout, QWidget)


class NewsPage(QWidget):
    def __init__(self):
        """Initialize health news page
        """
        super().__init__()
        self.setStyleSheet('background-color: rgb(255, 0, 0);')
        self.setFixedHeight(1864)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)