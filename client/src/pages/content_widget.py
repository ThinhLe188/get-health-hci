import os
import sys

import common.constants as const
from components.card.news_pinned_widget import NewsPinnedCardWidget
from components.card.news_widget import NewsCardWidget
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.QtWidgets import (QListWidget, QListWidgetItem, QScrollArea,
                             QSizePolicy, QTabWidget, QVBoxLayout, QWidget)


class ContentWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        from central_widget import CentralWidget
        self.parent: CentralWidget = parent
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        self._widget_scroll = QScrollArea()
        self._widget_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        layout.addWidget(self._widget_scroll)
        try:
            self._curr_dir = sys._MEIPASS
        except:
            self._curr_dir = os.getcwd()


    def display_page(self):
        pass