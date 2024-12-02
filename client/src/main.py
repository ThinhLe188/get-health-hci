import os
import sys

import common.constants as const
from common.app_style import STYLE_SHEET
from main_window import MainWindow
from PyQt5.QtWidgets import QApplication


def update_global_constants():
    try:
        curr_dir = sys._MEIPASS
    except:
        curr_dir = os.getcwd()
    const.APP_LOGO = os.path.join(curr_dir, const.APP_LOGO)
    const.APP_LOGIN = os.path.join(curr_dir, const.APP_LOGIN)
    const.USER_PFP = os.path.join(curr_dir, const.USER_PFP)


if __name__ == '__main__':
    # for splash screen
    if getattr(sys, 'frozen', False): import pyi_splash # type: ignore
    # create the Qt app
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = '0'
    app = QApplication(sys.argv)
    # configure the Qt app window
    app.setStyle('Fusion')
    app.setStyleSheet(STYLE_SHEET)
    # update asset paths
    update_global_constants()
    # create Qt window
    window = MainWindow()
    window.showMaximized()
    # loading should be done before closing the splash screen
    if getattr(sys, 'frozen', False): pyi_splash.close()
    # run the main Qt loop
    sys.exit(app.exec())