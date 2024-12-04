from components.button.button_widget import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class NavBarButtonWidget(ButtonWidget):
    def __init__(self, text: str, icon: str):
        super().__init__()
        self.setObjectName('widget_button')
        self.setFixedWidth(const.BUTTON_W)
        layout = self.layout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # add icon
        label_icon = QLabel(objectName='label_icon_button')
        pixmap = QPixmap(icon)
        label_icon.setFixedSize(25, 25)
        label_icon.setPixmap(pixmap.scaled(label_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(label_icon, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        layout.addWidget(QLabel(text, objectName='label_icon_button'))