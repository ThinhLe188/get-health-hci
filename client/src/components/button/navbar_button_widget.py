from components.button.button_widget import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class NavBarButtonWidget(ButtonWidget):
    def __init__(self, icon: str):
        """Initialize button widget

        Args:
            icon (str): Icon path
        """
        super().__init__()
        self.setObjectName('widget_button')
        self.setFixedWidth(const.BUTTON_W)
        layout = self.layout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # add icon
        label_icon = QLabel()
        pixmap = QPixmap(icon)
        label_icon.setFixedSize(30, 30)
        label_icon.setPixmap(pixmap.scaled(label_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(label_icon)