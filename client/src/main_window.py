import os

import common.constants as const
from central_widget import CentralWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysShowToolTips, True)
        # configure the window's title and icon
        self.setWindowIcon(QIcon(const.APP_LOGO))
        self.setWindowTitle(const.APP_NAME)
        # create the central widget
        self._central_widget = CentralWidget()
        # set the central widget
        self.setCentralWidget(self._central_widget)


    def closeEvent(self, event):
        self._central_widget.close()
        return super().closeEvent(event)