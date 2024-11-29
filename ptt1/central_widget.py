import os

import constants as const
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget


class CentralWidget(QWidget):
    def __init__(self, curr_dir: str):
        super().__init__()
        self.curr_dir = curr_dir
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # Create nav bar section
        self._create_nav_bar()
        self.layout.addLayout(self._layout_top_bar)
        self.layout.addStretch()


    def _create_nav_bar(self):
        self._layout_top_bar = QHBoxLayout()
        self._layout_top_bar.setContentsMargins(0, 0, 0, 0)
        self._layout_top_bar.addWidget(self._create_logo_widget(), alignment=Qt.AlignmentFlag.AlignLeft)


    def _create_logo_widget(self):
        widget_title = QWidget()
        layout_title = QHBoxLayout()
        widget_title.setLayout(layout_title)
        # Add icon
        label_icon = QLabel()
        label_icon.setPixmap(QPixmap(os.path.join(self.curr_dir, const.APP_LOGO)))
        layout_title.addWidget(label_icon)
        # Add title text
        layout_title.addWidget(QLabel(const.APP_NAME, objectName='label_title'))
        # Set layout margins and spacing for a cleaner look
        layout_title.setSpacing(0)
        layout_title.setContentsMargins(0, 0, 0, 0)
        return widget_title