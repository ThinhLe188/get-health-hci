import common.constants as const
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QMessageBox, QScrollArea,
                             QVBoxLayout, QWidget)


class PhysicalPage(QWidget):
    def __init__(self):
        """Initialize physical health page
        """
        super().__init__()
        self.setStyleSheet('background-color: rgb(0, 0, 255);')
        self.setFixedHeight(1864)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        layout.addStretch()