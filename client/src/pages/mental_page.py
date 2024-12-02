import common.constants as const
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QMessageBox, QScrollArea,
                             QVBoxLayout, QWidget, QPushButton)


class MentalPage(QWidget):
    def __init__(self):
        """Initialize mental health page
        """
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)