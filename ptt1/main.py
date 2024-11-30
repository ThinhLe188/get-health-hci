import os
import sys

from app_style import STYLE_SHEET
from main_window import MainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    # for splash screen
    if getattr(sys, 'frozen', False): import pyi_splash # type: ignore
    # create the Qt app
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = '0'
    app = QApplication(sys.argv)
    # configure the Qt app window
    app.setStyle('Fusion')
    app.setFont(QFont('Open Sans', 12))
    app.setStyleSheet(STYLE_SHEET)
    # get resource path
    try:
        curr_dir = sys._MEIPASS
    except:
        curr_dir = os.getcwd()
    # create Qt window
    window = MainWindow(curr_dir)
    window.showMaximized()
    # loading should be done before closing the splash screen
    if getattr(sys, 'frozen', False): pyi_splash.close()
    # run the main Qt loop
    sys.exit(app.exec())