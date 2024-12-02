import common.constants as const
from components.button_widget import ButtonWidget
from components.login_widget import LoginWidget
from pages.mental_page import MentalPage
from pages.news_page import NewsPage
from pages.physical_page import PhysicalPage
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QLabel, QLineEdit,
                             QMessageBox, QPushButton, QScrollArea,
                             QVBoxLayout, QWidget)


class CentralWidget(QWidget):
    def __init__(self):
        """Initialize central widget
        """
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        # create content section
        self._current_page = 0
        self._list_pages: list[QScrollArea] = [QScrollArea(), QScrollArea(), 
                                               QScrollArea(), QScrollArea()]
        self._widget_news = NewsPage()
        self._widget_mental = MentalPage()
        self._widget_physical = PhysicalPage()
        self._list_pages[0].setWidget(self._widget_news)
        self._list_pages[1].setWidget(self._widget_mental)
        self._list_pages[2].setWidget(self._widget_physical)
        # create nav bar section
        layout.addWidget(self._create_nav_bar())
        # add content section
        for page in self._list_pages:
            layout.addWidget(page)
            page.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            page.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
            page.setWidgetResizable(True)
            page.hide() # hide all pages
        self._list_pages[0].show() # only show Home page on start
        # init parameters
        self._user_logged_in = False


    def _create_nav_bar(self):
        widget_nav_bar = QWidget(objectName='widget_nav')
        layout_nav_bar = QHBoxLayout()
        widget_nav_bar.setLayout(layout_nav_bar)
        layout_nav_bar.setContentsMargins(0, 0, 0, 0)
        # create title widget
        widget_title = ButtonWidget(text=const.APP_NAME, 
                                    icon=const.APP_LOGO,
                                    is_title=True)
        # create menu items
        self._widget_news = ButtonWidget(text='News')
        self._widget_mental = ButtonWidget(text='Mental Health')
        self._widget_physical = ButtonWidget(text='Physical Health')
        widget_about = ButtonWidget(text='About Us')
        # create profile widget
        self._widget_profile = ButtonWidget(text=const.USER_NAME, 
                                            icon=const.USER_PFP, 
                                            size=(30, 30))
        # create login widget
        self._widget_login = ButtonWidget(text='Sign In', 
                                            icon=const.APP_LOGIN, 
                                            size=(20, 20))
        self._window_login = LoginWidget(self)
        # add navbar items
        layout_nav_bar.addWidget(widget_title)
        layout_nav_bar.addStretch()
        layout_nav_bar.addWidget(self._widget_news)
        layout_nav_bar.addWidget(self._widget_mental)
        layout_nav_bar.addWidget(self._widget_physical)
        layout_nav_bar.addWidget(widget_about)
        layout_nav_bar.addStretch()
        layout_nav_bar.addWidget(self._widget_login)
        layout_nav_bar.addWidget(self._widget_profile)
        # connect signals
        widget_title.clicked.connect(lambda: self._switch_page(0))
        self._widget_news.clicked.connect(lambda: self._switch_page(1))
        self._widget_mental.clicked.connect(lambda: self._switch_page(2))
        self._widget_physical.clicked.connect(lambda: self._switch_page(3))
        widget_about.clicked.connect(self._handle_about_page)
        self._widget_login.clicked.connect(self._handle_login)
        self._widget_profile.clicked.connect(self._handle_profile_page)
        # init states
        self._widget_profile.hide()
        return widget_nav_bar


    def user_logged_in(self):
        self._user_logged_in = True
        self._widget_login.hide()
        self._widget_profile.show()


##############################################################################
# Signal handlers
##############################################################################
    @pyqtSlot()
    def _switch_page(self, next_page: int):
        self._list_pages[self._current_page].hide()
        self._list_pages[next_page].show()
        self._current_page = next_page


    @pyqtSlot()
    def _handle_login(self):
        self._window_login.show()


    @pyqtSlot()
    def _handle_about_page(self):
        QMessageBox.information(self, 'GET HEALTH Prototype', 'Apologies! The About Us page are not yet ready in this prototype.')


    @pyqtSlot()
    def _handle_profile_page(self):
        QMessageBox.information(self, 'GET HEALTH Prototype', 'Apologies! The Profile page are not yet ready in this prototype.')
        self._user_logged_in = False
        self._widget_profile.hide()
        self._widget_login.show()


    def closeEvent(self, event):
        self._window_login.close()
        return super().closeEvent(event)