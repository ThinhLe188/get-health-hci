import os

import constants as const
from button_widget import ButtonWidget
from pages.home_page import HomePage
from pages.mental_page import MentalPage
from pages.news_page import NewsPage
from pages.physical_page import PhysicalPage
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (QHBoxLayout, QMessageBox, QScrollArea,
                             QVBoxLayout, QWidget, QDialog, QLabel, QLineEdit, QPushButton)


class CentralWidget(QWidget):
    def __init__(self, curr_dir: str):
        """Initialize central widget

        Args:
            curr_dir (str): Current working directory
        """
        super().__init__()
        self.curr_dir = curr_dir
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        # create content section
        self._current_page = 0
        self._list_pages: list[QScrollArea] = [QScrollArea(), QScrollArea(), 
                                               QScrollArea(), QScrollArea()]
        self._widget_home = HomePage()
        self._widget_news = NewsPage()
        self._widget_mental = MentalPage()
        self._widget_physical = PhysicalPage()
        self._list_pages[0].setWidget(self._widget_home)
        self._list_pages[1].setWidget(self._widget_news)
        self._list_pages[2].setWidget(self._widget_mental)
        self._list_pages[3].setWidget(self._widget_physical)
        # create nav bar section
        layout.addWidget(self._create_nav_bar())
        # add content section
        for page in self._list_pages:
            layout.addWidget(page)
            page.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            page.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
            page.hide() # hide all pages
        self._list_pages[0].show() # only show Home page on start


    def _create_nav_bar(self):
        widget_nav_bar = QWidget(objectName='widget_nav')
        layout_nav_bar = QHBoxLayout()
        widget_nav_bar.setLayout(layout_nav_bar)
        layout_nav_bar.setContentsMargins(0, 0, 0, 0)
        # create title widget
        layout_nav_bar.addWidget(self._create_logo_widget())
        layout_nav_bar.addStretch()
        # create menu items
        widget_home = ButtonWidget(text='HOME', 
                                   text_objectName='label_card', 
                                   objectName='widget_card', 
                                   width=160)
        widget_home.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget_news = ButtonWidget(text='NEWS', 
                                   text_objectName='label_card', 
                                   objectName='widget_card', 
                                   width=160)
        widget_news.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget_mental = ButtonWidget(text='MENTAL HEALTH', 
                                   text_objectName='label_card', 
                                   objectName='widget_card', 
                                   width=160)
        widget_mental.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget_physical = ButtonWidget(text='PHYSICAL HEALTH', 
                                   text_objectName='label_card', 
                                   objectName='widget_card', 
                                   width=160)
        widget_physical.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget_about = ButtonWidget(text='ABOUT US', 
                                   text_objectName='label_card', 
                                   objectName='widget_card', 
                                   width=160)
        widget_about.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        # add menu items
        layout_nav_bar.addWidget(widget_home)
        layout_nav_bar.addWidget(widget_news)
        layout_nav_bar.addWidget(widget_mental)
        layout_nav_bar.addWidget(widget_physical)
        layout_nav_bar.addWidget(widget_about)
        # connect signals
        widget_home.clicked.connect(lambda: self._switch_page(0))
        widget_news.clicked.connect(lambda: self._switch_page(1))
        widget_mental.clicked.connect(lambda: self._switch_page(2))
        widget_physical.clicked.connect(lambda: self._switch_page(3))
        widget_about.clicked.connect(self._handle_about_page)
        # create profile widget
        layout_nav_bar.addStretch()
        layout_nav_bar.addWidget(self._create_login_widget(), alignment=Qt.AlignmentFlag.AlignRight)
        return widget_nav_bar


    def _create_logo_widget(self):
        widget_title = ButtonWidget(text=const.APP_NAME, 
                                    text_objectName='label_title', 
                                    icon=os.path.join(self.curr_dir, const.APP_LOGO))
        widget_title.layout().setSpacing(0)
        widget_title.layout().setContentsMargins(0, 0, 0, 0)
        # connect signal
        widget_title.clicked.connect(lambda: self._switch_page(0))
        return widget_title


    def _create_login_widget(self):
        login_button = ButtonWidget(text='LOGIN', 
                                    text_objectName='label_card', 
                                    objectName='widget_card', 
                                    width=160)
        login_button.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        login_button.clicked.connect(self._show_login_dialog)

        return login_button


    def _create_profile_widget(self):
        widget_profile = ButtonWidget(text=const.USER_NAME, 
                                      text_objectName='label_card', 
                                      objectName='widget_card', 
                                      width=180,
                                      icon=os.path.join(self.curr_dir, const.USER_PFP), 
                                      size=(30, 30))
        # connect signal
        widget_profile.clicked.connect(self._handle_profile_page)
        return widget_profile
    

##############################################################################
# Signal handlers
##############################################################################
    @pyqtSlot()
    def _switch_page(self, next_page: int):
        self._list_pages[self._current_page].hide()
        self._list_pages[next_page].show()
        self._current_page = next_page

    @pyqtSlot()
    def _handle_about_page(self):
        QMessageBox.information(self, 'GET HEALTH Prototype', 'Apologies! The About Us page are not yet ready in this prototype.')


    @pyqtSlot()
    def _handle_profile_page(self):
        QMessageBox.information(self, 'GET HEALTH Prototype', 'Apologies! The Profile page are not yet ready in this prototype.')


    @pyqtSlot()
    def _show_login_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Login")
        dialog.setFixedHeight(170)
        dialog.setFixedWidth(250)
        layout = QVBoxLayout(dialog)

        # Account input
        account_label = QLabel("Account:", objectName='label_card')
        account_input = QLineEdit()
        layout.addWidget(account_label)
        layout.addWidget(account_input)

        # Password input
        password_label = QLabel("Password:", objectName='label_card')
        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(password_label)
        layout.addWidget(password_input)

        # Login button
        login_button = QPushButton("Login", objectName='btn_bold')
        login_button.setFixedWidth(120)
        login_button.setFixedHeight(30)
        login_button.clicked.connect(lambda: self._handle_login(account_input.text(), password_input.text(), dialog))
        layout.addStretch()
        layout.addWidget(login_button, alignment=Qt.AlignmentFlag.AlignCenter)

        dialog.exec_()


    @pyqtSlot()
    def _handle_login(self, account, password, dialog):
        # Handle login logic here
        if account == const.USER_ACCOUNT and password == const.USER_PASSWORD:
            QMessageBox.information(self, "Login Successful", "Welcome, Alex!")
            dialog.accept()
            # Remove the login button and add the profile widget
            widget_nav_bar = self.findChild(QWidget, 'widget_nav') # Find the widget first
            if widget_nav_bar:
                layout_nav_bar = widget_nav_bar.layout() # Get the layout from the widget
                login_button = self.findChild(ButtonWidget, 'login_button')
                if login_button:
                    layout_nav_bar.removeWidget(login_button)
                    login_button.deleteLater()
                layout_nav_bar.addWidget(self._create_profile_widget(), alignment=Qt.AlignmentFlag.AlignRight)
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid account or password.")