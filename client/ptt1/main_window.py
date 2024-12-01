import os

import constants as const
from central_widget import CentralWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, curr_dir: str):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysShowToolTips, True)
        # configure the window's title and icon
        self.setWindowIcon(QIcon(os.path.join(curr_dir, const.APP_LOGO)))
        self.setWindowTitle(const.APP_NAME)
        # create the central widget
        self.central_widget = CentralWidget(curr_dir)
        # set the central widget
        self.setCentralWidget(self.central_widget)