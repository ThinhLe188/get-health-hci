import os
import sys

from app_style import STYLE_SHEET
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    # for splash screen
    if getattr(sys, 'frozen', False): import pyi_splash
    # create the Qt app
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = '0'
    app = QApplication(sys.argv)
    # configure the Qt app window
    app.setStyleSheet(STYLE_SHEET)
    # loading should be done before closing the splash screen
    if getattr(sys, 'frozen', False): pyi_splash.close()
    # run the main Qt loop
    sys.exit(app.exec())