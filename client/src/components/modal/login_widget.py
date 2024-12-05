import common.constants as const
from components.modal.modal_widget import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit, QPushButton


class LoginWidget(ModalWidget):
    def __init__(self, parent):
        super().__init__(parent)
        layout_outer = self.layout()
        layout_outer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._widget_modal = QWidget(objectName='widget_modal')
        self._widget_modal.setFixedSize(400, 420)
        layout_outer.addWidget(self._widget_modal)
        font_underline = QFont()
        font_underline.setUnderline(True)
        # create main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        self._widget_modal.setLayout(layout)
        # create title
        label_icon = QLabel()
        pixmap = QPixmap(const.APP_LOGO)
        label_icon.setPixmap(pixmap)
        label_title = QLabel('Welcome to Get Health', objectName='label_title')
        layout.addWidget(label_icon, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(40)
        # create prompts
        label_username = QLabel('Username:', objectName='label_prompt')
        self._input_username = QLineEdit(objectName='input_prompt')
        self._input_username.setPlaceholderText('Enter your username')
        self._input_username.setText(const.USER_ACCOUNT)
        layout.addWidget(label_username)
        layout.addWidget(self._input_username)
        layout.addSpacing(10)
        label_password = QLabel('Password:', objectName='label_prompt')
        self._input_password = QLineEdit(objectName='input_prompt')
        self._input_password.setPlaceholderText('Enter your password')
        self._input_password.setEchoMode(QLineEdit.Password)
        self._input_password.setText(const.USER_PASSWORD)
        layout.addWidget(label_password)
        layout.addWidget(self._input_password)
        layout.addSpacing(5)
        # create forgot password
        label_rememberme = QLabel('Forgot password?', objectName='label_button')
        label_rememberme.setFont(font_underline)
        layout.addWidget(label_rememberme, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addSpacing(10)
        self._label_status = QLabel('')
        self._label_status.setStyleSheet('font-size: 14px; font-weight: bold; color: red;')
        layout.addWidget(self._label_status, alignment=Qt.AlignmentFlag.AlignCenter)
        # create status label
        layout.addStretch()
        # login button
        button_login = QPushButton('Sign In', objectName='button_submit')
        button_login.setFixedWidth(160)
        button_login.clicked.connect(self._handle_login)
        layout.addWidget(button_login, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(10)
        label_register = QLabel('Don\'t have account yet?', objectName='label_button')
        label_register.setFont(font_underline)
        layout.addWidget(label_register, alignment=Qt.AlignmentFlag.AlignCenter)


    def reset_modal(self):
        self._label_status.clear()
        self._input_username.setText(const.USER_ACCOUNT)
        self._input_password.setText(const.USER_PASSWORD)


    @pyqtSlot()
    def _handle_login(self):
        if self._input_username.text() == const.USER_ACCOUNT and self._input_password.text() == const.USER_PASSWORD:
            self.parent.user_logged_in()
        else:
            self._label_status.setText('Incorrect username or password. Please try again')