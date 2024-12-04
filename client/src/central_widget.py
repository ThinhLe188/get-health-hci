import common.constants as const
from components.button.navbar_button_widget import NavBarButtonWidget
from components.modal.login_widget import LoginWidget
from components.modal.sidebar_widget import SideBarWidget
from pages.mental_page import MentalPage
from pages.news_page import NewsPage
from pages.physical_page import PhysicalPage
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QScrollArea, QStackedLayout,
                             QVBoxLayout, QWidget)


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
        # create title widget
        widget_title = QWidget()
        self._layout_header.addWidget(widget_title, alignment=Qt.AlignmentFlag.AlignLeft)
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
        button_news = NavBarButtonWidget(const.APP_NEWS)
        button_mental = NavBarButtonWidget(const.APP_MENTAL)
        button_physical = NavBarButtonWidget(const.APP_PHYSICAL)
        button_setting = NavBarButtonWidget(const.APP_SETTING)
        # add items
        layout_footer.addWidget(button_news)
        layout_footer.addWidget(button_mental)
        layout_footer.addWidget(button_physical)
        layout_footer.addWidget(button_setting)
        # add signals
        button_setting.clicked.connect(self._open_sidebar)
        button_news.clicked.connect(lambda: self._switch_page(const.APP_PAGE_NEWS_IDX))
        button_mental.clicked.connect(lambda: self._switch_page(const.APP_PAGE_MENTAL_IDX))
        button_physical.clicked.connect(lambda: self._switch_page(const.APP_PAGE_PHYSICAL_IDX))
        # init state
        self._current_nav_btn = button_news
        self._current_nav_btn.setObjectName('widget_button_pressed')
        self.style().polish(self._current_nav_btn)
        return widget_footer


    def _create_content_sections(self):
        widget_main = QWidget()
        self._layout_stack = QStackedLayout()
        self._layout_stack.setStackingMode(QStackedLayout.StackingMode.StackAll)
        widget_main.setLayout(self._layout_stack)
        # create content sections
        # news page
        self._widget_news = NewsPage(self)
        self._widget_scroll_news = QScrollArea()
        self._widget_scroll_news.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll_news.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll_news.setWidgetResizable(True)
        self._widget_scroll_news.setWidget(self._widget_news)
        # mental page
        self._widget_mental = MentalPage(self)
        self._widget_scroll_mental = QScrollArea()
        self._widget_scroll_mental.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll_mental.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll_mental.setWidgetResizable(True)
        self._widget_scroll_mental.setWidget(self._widget_mental)
        # physical page
        self._widget_physical = PhysicalPage(self)
        self._widget_scroll_physical = QScrollArea()
        self._widget_scroll_physical.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll_physical.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll_physical.setWidgetResizable(True)
        self._widget_scroll_physical.setWidget(self._widget_physical)
        # add sections
        self._layout_stack.addWidget(self._widget_scroll_news)
        self._layout_stack.addWidget(self._widget_scroll_mental)
        self._layout_stack.addWidget(self._widget_scroll_physical)
        self._layout_stack.setCurrentIndex(const.APP_PAGE_NEWS_IDX)
        widget_main.style()
        return widget_main


    def user_logged_in(self):
        self._user_logged_in = True


##############################################################################
# Signal handlers
##############################################################################
    @pyqtSlot()
    def _switch_page(self, index: int):
        self._switch_nav_tab(index)
        self._layout_stack.currentWidget().widget().display_page()


    def _switch_nav_tab(self, index: int):
        if self._current_nav_btn:
            self._current_nav_btn.setObjectName('widget_button')
            self.style().polish(self._current_nav_btn)
        self.sender().setObjectName('widget_button_pressed')
        self.style().polish(self.sender())
        self._current_nav_btn = self.sender()
        self._layout_stack.setCurrentIndex(index)


    @pyqtSlot()
    def _open_sidebar(self):
        self._layout_outer.setCurrentIndex(const.APP_SIDEBAR_IDX)


    @pyqtSlot()
    def open_login_modal(self):
        self.back_to_main_widget()
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