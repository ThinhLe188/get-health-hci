from components.button.button_widget import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class SideBarButtonWidget(ButtonWidget):
    def __init__(self, text: str, icon: str):
        """Initialize button widget

        Args:
            text (str): Display text
            icon (str): Icon path
        """
        super().__init__()
        self.setObjectName('widget_sidebar_button')
        self.setFixedSize(const.SIDEBAR_W, const.BUTTON_H)
        layout = self.layout()
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(30, 0, 0, 0)
        layout.setSpacing(15)
        # add icon
        label_icon = QLabel()
        pixmap = QPixmap(icon)
        label_icon.setFixedSize(30, 30)
        label_icon.setPixmap(pixmap.scaled(label_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(label_icon)
        # add text
        layout.addWidget(QLabel(text, objectName='label_sidebar_button'))