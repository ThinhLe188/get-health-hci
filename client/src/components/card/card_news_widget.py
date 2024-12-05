import os

import common.constants as const
from components.button.button_label import ButtonLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QFrame, QHBoxLayout, QLabel, QListWidgetItem,
                             QVBoxLayout, QWidget)


class CardNewsWidget(QWidget):
    def __init__(self, curr_dir: str, img: str, title: str, author: str, location: str, publish: str, content: str):
        super().__init__()
        self._data = (img, title, author, location, publish, content)
        layout = QVBoxLayout()
        layout.setSpacing(0)
        self.setLayout(layout)
        # create title
        label_icon = QLabel()
        pixmap = QPixmap(os.path.join(curr_dir, img))
        label_icon.setFixedSize(400, 230)
        label_icon.setPixmap(pixmap.scaled(label_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        label_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_title = QLabel(title, objectName='label_news_title')
        label_title.setWordWrap(True)
        layout.addWidget(label_icon, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_title)
        layout.addStretch()
        self._layout_footer = QHBoxLayout()
        self._layout_footer.setContentsMargins(0, 0, 0, 0)
        self._layout_footer.setSpacing(10)
        layout.addLayout(self._layout_footer)
        self._layout_footer.addWidget(QLabel(publish, objectName='label_news_footer'))
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        self._layout_footer.addWidget(line)
        self._layout_footer.addWidget(QLabel(location, objectName='label_news_footer'))
        self._layout_footer.addStretch()


    def get_data(self):
        return self._data
