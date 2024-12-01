from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QMouseEvent, QPainter, QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QStyle, QStyleOption, QWidget


class ButtonWidget(QWidget):
    clicked = pyqtSignal()

    def __init__(self, objectName: str = None, width: int = None, text: str = None, text_objectName: str = None, icon: str = None, size: tuple = None):
        """Initialize button widget

        Args:
            objectName (str, optional): Object ID tag for styling. Defaults to None.
            width (int, optional): Widget's width. Defaults to None.
            text (str, optional): Display text string. Defaults to None.
            text_objectName (str, optional): Object ID tag for text styling. Defaults to None.
            icon (str, optional): Icon path. Defaults to None.
            size (tuple, optional): Icon size. Defaults to None.
        """
        super().__init__()
        self.setObjectName(objectName)
        if width:
            self.setFixedWidth(width)
        layout = QHBoxLayout()
        self.setLayout(layout)
        # add icon
        if icon:
            label_icon = QLabel()
            pixmap = QPixmap(icon)
            if size:
                label_icon.setFixedSize(*size)
                label_icon.setPixmap(pixmap.scaled(label_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            else:
                label_icon.setPixmap(pixmap)
            layout.addWidget(label_icon)
        # add title text
        if text:
            layout.addWidget(QLabel(text, objectName=text_objectName))


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