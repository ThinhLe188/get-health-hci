import common.constants as const
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class ModalWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        from central_widget import CentralWidget
        self.parent: CentralWidget = parent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        layout_outer = QVBoxLayout()
        layout_outer.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout_outer)
        self._widget_modal = None
        # install event filter
        self.installEventFilter(self)


    def paintEvent(self, event):
        """custom paint event to draw a semi-transparent background"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        color = QColor(0, 0, 0, 128)
        painter.fillRect(self.rect(), color)
        super().paintEvent(event)


    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            # convert sidebar geometry to global coordinates
            modal_global_rect = self._widget_modal.rect().translated(self._widget_modal.mapToGlobal(self._widget_modal.rect().topLeft()))
            # check if the click is outside the modal
            if not modal_global_rect.contains(event.globalPos()):
                self.parent.back_to_main_widget()
        return super().eventFilter(source, event)