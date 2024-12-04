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
    const.USER_PFP     = os.path.join(curr_dir, const.USER_PFP)
    const.APP_LOGO     = os.path.join(curr_dir, const.APP_LOGO)
    const.APP_LOGIN    = os.path.join(curr_dir, const.APP_LOGIN)
    const.APP_LOGOUT   = os.path.join(curr_dir, const.APP_LOGOUT)
    const.APP_NEWS     = os.path.join(curr_dir, const.APP_NEWS)
    const.APP_LOCAL    = os.path.join(curr_dir, const.APP_LOCAL)
    const.APP_MENTAL   = os.path.join(curr_dir, const.APP_MENTAL)
    const.APP_PHYSICAL = os.path.join(curr_dir, const.APP_PHYSICAL)
    const.APP_PROFILE  = os.path.join(curr_dir, const.APP_PROFILE)
    const.APP_SETTING  = os.path.join(curr_dir, const.APP_SETTING)
    const.APP_EXIT     = os.path.join(curr_dir, const.APP_EXIT)
    const.APP_FILTER   = os.path.join(curr_dir, const.APP_FILTER)
    const.APP_SEARCH   = os.path.join(curr_dir, const.APP_SEARCH)
    const.APP_BACK     = os.path.join(curr_dir, const.APP_BACK)
    const.APP_BOOKMARK = os.path.join(curr_dir, const.APP_BOOKMARK)
    const.APP_BOOKMARK_FILL = os.path.join(curr_dir, const.APP_BOOKMARK_FILL)
    const.APP_REMOVE = os.path.join(curr_dir, const.APP_REMOVE)


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
    window.show()  # ensure the window's size is set
    screen_geometry = app.screens()[0].geometry()
    window_geometry = window.frameGeometry()
    # calculate the center position
    center_point = screen_geometry.center()
    window_geometry.moveCenter(center_point)
    window.move(window_geometry.topLeft())
    # loading should be done before closing the splash screen
    if getattr(sys, 'frozen', False): pyi_splash.close()
    # run the main Qt loop
    sys.exit(app.exec())