import os

import constants as const
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QSizePolicy,
                             QVBoxLayout, QWidget)


class CentralWidget(QWidget):
    def __init__(self, curr_dir: str):
        super().__init__()
        self.curr_dir = curr_dir
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # create nav bar section
        self._create_nav_bar()
        self.layout.addLayout(self._layout_top_bar)
        self.layout.addStretch()


    def _create_nav_bar(self):
        self._layout_top_bar = QHBoxLayout()
        self._layout_top_bar.setContentsMargins(0, 0, 0, 0)
        # create title widget
        self._layout_top_bar.addWidget(self._create_logo_widget(), alignment=Qt.AlignmentFlag.AlignLeft)
        # create profile widget
        self._layout_top_bar.addWidget(self._create_profile_widget(), alignment=Qt.AlignmentFlag.AlignRight)


    def _create_logo_widget(self):
        widget_title = QWidget()
        layout_title = QHBoxLayout()
        widget_title.setLayout(layout_title)
        # add icon
        label_icon = QLabel()
        label_icon.setPixmap(QPixmap(os.path.join(self.curr_dir, const.APP_LOGO)))
        layout_title.addWidget(label_icon)
        # add title text
        layout_title.addWidget(QLabel(const.APP_NAME, objectName='label_title'))
        # set layout margins and spacing for a cleaner look
        layout_title.setSpacing(0)
        layout_title.setContentsMargins(0, 0, 0, 0)
        return widget_title


    def _create_profile_widget(self):
        button_profile = QPushButton(const.USER_NAME, objectName='button_card')
        button_profile.setFixedWidth(180)
        button_profile.setLayoutDirection(Qt.LeftToRight)
        button_profile.setFlat(True) # removes button border for a clean look
        # add profile picture
        button_profile.setIconSize(QSize(30, 30))
        button_profile.setIcon(QIcon(os.path.join(self.curr_dir, const.USER_PFP)))
        return button_profile