import common.constants as const
from components.button.header_button_widget import HeaderButtonWidget
from components.button.navbar_button_widget import NavBarButtonWidget
from components.modal.login_widget import LoginWidget
from components.modal.sidebar_widget import SideBarWidget
from pages.mental_page import MentalPage
from pages.news_local_page import NewsLocalPage
from pages.news_page import NewsPage
from pages.physical_page import PhysicalPage
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QStackedLayout,
                             QStackedWidget, QVBoxLayout, QWidget)


class CentralWidget(QWidget):
    def __init__(self, parent):
        """Initialize central widget
        """
        super().__init__(parent)
        # init parameters
        self._prev_stack_idx = None
        self._current_nav_btn = None
        self._user_logged_in = False
        # init outer layout
        self._layout_outer = QStackedLayout()
        self._layout_outer.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.setLayout(self._layout_outer)
        # init main layout
        widget_main = QWidget()
        self._layout_outer.addWidget(widget_main)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        widget_main.setLayout(layout)
        # create header section
        layout.addWidget(self._create_header_section())
        # add content section
        layout.addWidget(self._create_content_sections())
        # add footer section
        layout.addWidget(self._create_footer_section())
        # init sidebar widget
        widget_sidebar = SideBarWidget(self)
        self._layout_outer.addWidget(widget_sidebar)
        # init login widget
        widget_login = LoginWidget(self)
        self._layout_outer.addWidget(widget_login)
        # show main widget
        self._layout_outer.setCurrentIndex(0)


    def _create_header_section(self):
        widget_header = QWidget(objectName='widget_component')
        widget_header.setFixedHeight(const.BUTTON_H)
        self._layout_header = QHBoxLayout()
        widget_header.setLayout(self._layout_header)
        self._layout_header.setContentsMargins(0, 0, 0, 0)
        self._layout_header.setSpacing(0)
        # create title widget
        self.button_back = HeaderButtonWidget(const.APP_BACK)
        self.button_back.hide()
        self._layout_header.addWidget(self.button_back, alignment=Qt.AlignmentFlag.AlignLeft)
        widget_title = QWidget()
        self._layout_header.addWidget(widget_title, alignment=Qt.AlignmentFlag.AlignLeft)
        self._layout_header.addStretch()
        layout_title = QHBoxLayout()
        layout_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_title.setSpacing(0)
        layout_title.setContentsMargins(0, 0, 0, 0)
        widget_title.setLayout(layout_title)
        label_icon = QLabel()
        pixmap = QPixmap(const.APP_LOGO)
        label_icon.setPixmap(pixmap)
        layout_title.addWidget(label_icon)
        self.label_title = QLabel(const.APP_PAGE_NEWS, objectName='label_title')
        layout_title.addWidget(self.label_title)
        # create utility buttons
        self.button_search = HeaderButtonWidget(const.APP_SEARCH)
        self.button_filter = HeaderButtonWidget(const.APP_FILTER)
        self.button_filter.hide()
        self._layout_header.addWidget(self.button_search, alignment=Qt.AlignmentFlag.AlignRight)
        self._layout_header.addWidget(self.button_filter, alignment=Qt.AlignmentFlag.AlignRight)
        return widget_header


    def _create_footer_section(self):
        widget_footer = QWidget(objectName='widget_component')
        widget_footer.setFixedHeight(const.BUTTON_H)
        layout_footer = QHBoxLayout()
        widget_footer.setLayout(layout_footer)
        layout_footer.setAlignment(Qt.AlignmentFlag.AlignJustify)
        layout_footer.setContentsMargins(0, 0, 0, 0)
        layout_footer.setSpacing(0)
        # create navbar items
        button_news_global = NavBarButtonWidget('Global', const.APP_NEWS)
        button_news_local = NavBarButtonWidget('Local', const.APP_LOCAL)
        button_mental = NavBarButtonWidget('Mental', const.APP_MENTAL)
        button_physical = NavBarButtonWidget('Physical', const.APP_PHYSICAL)
        button_setting = NavBarButtonWidget('Settings', const.APP_SETTING)
        # add items
        layout_footer.addWidget(button_news_global)
        layout_footer.addWidget(button_news_local)
        layout_footer.addWidget(button_mental)
        layout_footer.addWidget(button_physical)
        layout_footer.addWidget(button_setting)
        # add signals
        button_setting.clicked.connect(self._open_sidebar)
        button_news_global.clicked.connect(lambda: self._switch_page(const.APP_PAGE_NEWS_IDX))
        button_news_local.clicked.connect(lambda: self._switch_page(const.APP_PAGE_NEWS_LOCAL_IDX))
        button_mental.clicked.connect(lambda: self._switch_page(const.APP_PAGE_MENTAL_IDX))
        button_physical.clicked.connect(lambda: self._switch_page(const.APP_PAGE_PHYSICAL_IDX))
        # init state
        self._current_nav_btn = button_news_global
        self._current_nav_btn.setObjectName('widget_button_pressed')
        self.style().polish(self._current_nav_btn)
        return widget_footer


    def _create_content_sections(self):
        self._widget_stack = QStackedWidget()
        # create content sections
        self._widget_news = NewsPage(self)
        self._widget_news_local = NewsLocalPage(self)
        self._widget_mental = MentalPage(self)
        self._widget_physical = PhysicalPage(self)
        # add sections
        self._widget_stack.addWidget(self._widget_news)
        self._widget_stack.addWidget(self._widget_news_local)
        self._widget_stack.addWidget(self._widget_mental)
        self._widget_stack.addWidget(self._widget_physical)
        self._widget_stack.setCurrentIndex(const.APP_PAGE_NEWS_IDX)
        return self._widget_stack


    def user_logged_in(self):
        self._user_logged_in = True


##############################################################################
# Signal handlers
##############################################################################
    @pyqtSlot()
    def _switch_page(self, index: int):
        self._switch_nav_tab(index)
        self._widget_stack.currentWidget().display_page()


    def _switch_nav_tab(self, index: int):
        if self._current_nav_btn:
            self._current_nav_btn.setObjectName('widget_button')
            self.style().polish(self._current_nav_btn)
        self.sender().setObjectName('widget_button_pressed')
        self.style().polish(self.sender())
        self._current_nav_btn = self.sender()
        self._widget_stack.setCurrentIndex(index)


    @pyqtSlot()
    def _open_sidebar(self):
        self._layout_outer.setCurrentIndex(const.APP_SIDEBAR_IDX)


    @pyqtSlot()
    def open_login_modal(self):
        self.back_to_main_widget()
        self._layout_outer.widget(const.APP_LOGIN_MODAL_IDX).reset_modal()
        self._layout_outer.setCurrentIndex(const.APP_LOGIN_MODAL_IDX)


    def back_to_main_widget(self):
        self._layout_outer.setCurrentIndex(const.APP_MAIN_WINDOW_IDX)


    def user_logged_in(self):
        self.back_to_main_widget()

        self._layout_outer.widget(const.APP_SIDEBAR_IDX).user_logged_in()
        self._layout_outer.setCurrentIndex(const.APP_SIDEBAR_IDX)
        self._user_logged_in = True


    def user_logged_out(self):
        self.back_to_main_widget()
        self._user_logged_in = False


    @pyqtSlot()
    def exit_app(self):
        self.parent().close()


    def closeEvent(self, event):
        return super().closeEvent(event)