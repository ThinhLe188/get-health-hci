import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysShowToolTips, True)
        # configure the window's title and icon
        self.setWindowIcon(QIcon(os.path.join(sys._MEIPASS, 'logo.ico')))
        self.setWindowTitle('Get Health')