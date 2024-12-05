from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class ButtonLabel(QLabel):
    clicked = pyqtSignal(bool)
    def __init__(self, icon: str, icon_fill: str):
        super().__init__()
        self._icon = icon
        self._icon_fill = icon_fill
        pixmap = QPixmap(icon)
        self.setFixedSize(25, 25)
        self.setPixmap(pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.setAlignment(Qt.AlignCenter)
        self._is_toggled = False


    def click(self):
        self._is_toggled = not self._is_toggled
        self.update_background()
        self.clicked.emit(self._is_toggled)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.click()
        super().mousePressEvent(event)


    def update_background(self):
        if self._is_toggled:
            pixmap = QPixmap(self._icon_fill)
        else:
            pixmap = QPixmap(self._icon)

        self.setFixedSize(25, 25)
        self.setPixmap(pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.setAlignment(Qt.AlignCenter)