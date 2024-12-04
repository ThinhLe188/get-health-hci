import common.constants as const
from components.button_widget import ButtonWidget
from pages.mental_page import MentalPage
from pages.news_page import NewsPage
from pages.physical_page import PhysicalPage
from components.login_widget import LoginWidget
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QScrollArea, QStackedLayout,
                             QVBoxLayout, QWidget, QStyle)


class CentralWidget(QWidget):
    def __init__(self, parent):
        """Initialize central widget
        """
        super().__init__(parent)
        # init parameters
        self._current_page_btn = None
        self._user_logged_in = False
        # init layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        # create header section
        layout.addWidget(self._create_header_section())
        # add content section
        layout.addWidget(self._create_content_sections())
        # add footer section
        layout.addWidget(self._create_footer_section())


    def _create_header_section(self):
        self.widget_header = QWidget(objectName='widget_nav')
        self.widget_header.setFixedHeight(56)
        layout_header = QHBoxLayout()
        self.widget_header.setLayout(layout_header)
        layout_header.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout_header.setContentsMargins(0, 0, 0, 0)
        # create title widget
        widget_title = QWidget()
        layout_header.addWidget(widget_title)
        layout_title = QHBoxLayout()
        layout_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_title.setSpacing(0)
        layout_title.setContentsMargins(0, 0, 0, 0)
        widget_title.setLayout(layout_title)
        label_icon = QLabel()
        pixmap = QPixmap(const.APP_LOGO)
        label_icon.setPixmap(pixmap)
        layout_title.addWidget(label_icon)       
        layout_title.addWidget(QLabel(const.APP_NAME, objectName='label_title'))
        return self.widget_header


    def _create_footer_section(self):
        widget_footer = QWidget(objectName='widget_nav')
        widget_footer.setFixedHeight(56)
        layout_footer = QHBoxLayout()
        widget_footer.setLayout(layout_footer)
        layout_footer.setAlignment(Qt.AlignmentFlag.AlignJustify)
        layout_footer.setContentsMargins(0, 0, 0, 0)
        # create navbar items
        button_news = ButtonWidget(const.APP_NEWS)
        button_mental = ButtonWidget(const.APP_MENTAL)
        button_physical = ButtonWidget(const.APP_PHYSICAL)
        button_profile = ButtonWidget(const.APP_PROFILE)
        button_exit = ButtonWidget(const.APP_EXIT)
        # add items
        layout_footer.addWidget(button_exit)
        layout_footer.addWidget(button_news)
        layout_footer.addWidget(button_mental)
        layout_footer.addWidget(button_physical)
        layout_footer.addWidget(button_profile)
        # add signals
        button_exit.clicked.connect(self.exit_app)
        button_profile.clicked.connect(self.open_login)
        button_news.clicked.connect(lambda: self._switch_tab(0))
        button_mental.clicked.connect(lambda: self._switch_tab(1))
        button_physical.clicked.connect(lambda: self._switch_tab(2))
        # init state
        self._current_page_btn = button_news
        self._current_page_btn.setObjectName('widget_card_pressed')
        self.style().polish(self._current_page_btn)
        return widget_footer


    def _create_content_sections(self):
        widget_main = QWidget()
        self._layout_stack = QStackedLayout()
        self._layout_stack.setStackingMode(QStackedLayout.StackingMode.StackAll)
        widget_main.setLayout(self._layout_stack)
        # create content sections
        self._widget_news = NewsPage()
        self._widget_scroll_news = QScrollArea(objectName='n_page')
        self._widget_scroll_news.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self._widget_scroll_news.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll_news.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll_news.setWidgetResizable(True)
        self._widget_scroll_news.setWidget(self._widget_news)
        self._widget_mental = MentalPage()
        self._widget_scroll_mental = QScrollArea(objectName='m_page')
        self._widget_scroll_mental.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self._widget_scroll_mental.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll_mental.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll_mental.setWidgetResizable(True)
        self._widget_scroll_mental.setWidget(self._widget_mental)
        self._widget_physical = PhysicalPage()
        self._widget_scroll_physical = QScrollArea(objectName='h_page')
        self._widget_scroll_physical.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self._widget_scroll_physical.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll_physical.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_scroll_physical.setWidgetResizable(True)
        self._widget_scroll_physical.setWidget(self._widget_physical)
        self._widget_login = LoginWidget(self)
        # add sections
        self._layout_stack.addWidget(self._widget_scroll_news)
        self._layout_stack.addWidget(self._widget_scroll_mental)
        self._layout_stack.addWidget(self._widget_scroll_physical)
        self._layout_stack.addWidget(self._widget_login)
        self._layout_stack.setCurrentIndex(0)
        widget_main.style()
        return widget_main


    def user_logged_in(self):
        self._user_logged_in = True


##############################################################################
# Signal handlers
##############################################################################
    @pyqtSlot()
    def _switch_tab(self, index: int):
        if self._current_page_btn:
            self._current_page_btn.setObjectName('widget_card')
            self.style().polish(self._current_page_btn)
        self.sender().setObjectName('widget_card_pressed')
        self.style().polish(self.sender())
        self._current_page_btn = self.sender()
        self._layout_stack.setCurrentIndex(index)


    @pyqtSlot()
    def open_login(self):
        self._switch_tab(3)
        # TODO:


    @pyqtSlot()
    def exit_app(self):
        self.parent().close()


    def closeEvent(self, event):
        return super().closeEvent(event)