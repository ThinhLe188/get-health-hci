import common.constants as const
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QCheckBox, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QWidget)


class LoginWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(const.APP_NAME + ' Sign In')
        self.setWindowIcon(QIcon(const.APP_LOGO))
        self.setFixedSize(400, 410)
        font_underline = QFont()
        font_underline.setUnderline(True)
        # create main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)
        # create title
        label_icon = QLabel()
        pixmap = QPixmap(const.APP_LOGO)
        label_icon.setPixmap(pixmap)
        label_title = QLabel('Welcome to our platform')
        label_title.setStyleSheet('font-weight: bold; font-size: 20px; color: rgb(2, 102, 0);')
        layout.addWidget(label_icon, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(40)
        # create prompts
        label_username = QLabel('Username:', objectName='label_card')
        self._input_username = QLineEdit(objectName='input_prompt')
        self._input_username.setPlaceholderText('Enter your username')
        self._input_username.setText(const.USER_ACCOUNT)
        layout.addWidget(label_username)
        layout.addWidget(self._input_username)
        layout.addSpacing(10)
        label_password = QLabel('Password:', objectName='label_card')
        self._input_password = QLineEdit(objectName='input_prompt')
        self._input_password.setPlaceholderText('Enter your password')
        self._input_password.setEchoMode(QLineEdit.Password)
        self._input_password.setText(const.USER_PASSWORD)
        layout.addWidget(label_password)
        layout.addWidget(self._input_password)
        layout.addSpacing(5)
        # create forgot password
        label_rememberme = QLabel('Forgot password?')
        label_rememberme.setFont(font_underline)
        label_rememberme.setStyleSheet('font-weight: bold')
        layout.addWidget(label_rememberme, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addSpacing(10)
        self._label_status = QLabel('')
        self._label_status.setStyleSheet('font-weight: bold; color: red;')
        layout.addWidget(self._label_status, alignment=Qt.AlignmentFlag.AlignCenter)
        # create status label
        layout.addStretch()
        # login button
        button_login = QPushButton('Sign In', objectName='button_submit')
        button_login.setFixedWidth(160)
        button_login.clicked.connect(self._handle_login)
        layout.addWidget(button_login, alignment=Qt.AlignmentFlag.AlignCenter)
        label_rememberme = QLabel('Don\'t have account yet?')
        label_rememberme.setFont(font_underline)
        label_rememberme.setStyleSheet('font-weight: bold')
        layout.addWidget(label_rememberme, alignment=Qt.AlignmentFlag.AlignCenter)


    @pyqtSlot()
    def _handle_login(self):
        if self._input_username.text() == const.USER_ACCOUNT and self._input_password.text() == const.USER_PASSWORD:
            print('hello')
            self.parent.user_logged_in()
            self.close()
        else:
            self._label_status.setText('Incorrect username or password. Please try again')