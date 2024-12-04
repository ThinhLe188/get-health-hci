import common.constants as const
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QMouseEvent, QPainter
from PyQt5.QtWidgets import QStyle, QStyleOption, QWidget, QVBoxLayout


class ButtonWidget(QWidget):
    clicked = pyqtSignal()

    def __init__(self):
        """Initialize button widget
        """
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)    


    # override the mousePressEvent to emit the custom signal
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # create a QStyleOption and initialize it
        option = QStyleOption()
        option.initFrom(self)
        # use the style to draw the widget
        self.style().drawPrimitive(QStyle.PE_Widget, option, painter, self)
        painter.end()