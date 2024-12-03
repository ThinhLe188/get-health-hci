from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QMouseEvent, QPainter, QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QStyle, QStyleOption, QWidget


class ButtonWidget(QWidget):
    clicked = pyqtSignal()

    def __init__(self, icon: str = None):
        """Initialize button widget

        Args:
            icon (str): Icon path
        """
        super().__init__()
        self.setObjectName('widget_card')
        self.setFixedWidth(86)
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        # add icon
        label_icon = QLabel()
        pixmap = QPixmap(icon)
        label_icon.setFixedSize(30, 30)
        label_icon.setPixmap(pixmap.scaled(label_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(label_icon)       


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