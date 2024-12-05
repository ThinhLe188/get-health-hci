import os

import common.constants as const
from components.card.news_pinned_widget import NewsPinnedCardWidget
from components.card.news_widget import NewsCardWidget
from components.modal.news_content_widget import NewsContentWidget
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.QtWidgets import (QListWidget, QListWidgetItem, QScrollArea,
                             QSizePolicy, QStackedWidget, QTabWidget,
                             QVBoxLayout, QWidget)


class ContentWidget(QStackedWidget):
    def __init__(self, parent):
        super().__init__()
        from central_widget import CentralWidget
        self.parent: CentralWidget = parent
        self.setAutoFillBackground(True)
        self._widget_scroll = QScrollArea()
        self._widget_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.addWidget(self._widget_scroll)
        self.setCurrentIndex(0)


    def display_page(self):
        self.parent.button_back.clicked.connect(self._back_to_main)


    def _back_to_main(self):
        self.parent.button_back.hide()
        self.setCurrentIndex(0)