from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QMouseEvent, QPainter, QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QStyle, QStyleOption, QWidget


class ButtonWidget(QWidget):
    clicked = pyqtSignal()

    def __init__(self, text: str = None, icon: str = None, size: tuple = None, is_title: bool = False):
        """Initialize button widget

        Args:
            text (str, optional): Display text string. Defaults to None.
            icon (str, optional): Icon path. Defaults to None.
            size (tuple, optional): Icon size. Defaults to None.
            is_title (bool, optional): If the widget is title widget. Defaults to None.
        """
        super().__init__()
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        if is_title:
            widget_style = ''
            text_style = 'label_title'
            layout.setSpacing(0)
            layout.setContentsMargins(0, 0, 0, 0)
        else:
            widget_style = 'widget_card'
            text_style = 'label_card'
        self.setObjectName(widget_style)
        self.setFixedWidth(160)
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
            layout.addWidget(QLabel(text, objectName=text_style))


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