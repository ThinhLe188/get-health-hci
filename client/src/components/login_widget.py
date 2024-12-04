import common.constants as const
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QColor, QFont, QPainter, QPixmap
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QWidget)


class LoginWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        layout_outer = QVBoxLayout()
        layout_outer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_outer.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout_outer)
        widget_login_card = QWidget(objectName='widget_login')
        widget_login_card.setFixedSize(400, 410)
        layout_outer.addWidget(widget_login_card)
        font_underline = QFont()
        font_underline.setUnderline(True)
        # create main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        widget_login_card.setLayout(layout)
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
        label_rememberme = QLabel('Forgot password?', objectName='label_button')
        label_rememberme.setFont(font_underline)
        layout.addWidget(label_rememberme, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addSpacing(10)
        self._label_status = QLabel('')
        self._label_status.setStyleSheet('font-size: 12px; font-weight: bold; color: red;')
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


    def paintEvent(self, event):
        """Custom paint event to draw a semi-transparent background"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        color = QColor(0, 0, 0, 85)
        painter.fillRect(self.rect(), color)
        super().paintEvent(event)


    @pyqtSlot()
    def _handle_login(self):
        if self._input_username.text() == const.USER_ACCOUNT and self._input_password.text() == const.USER_PASSWORD:
            self.parent.user_logged_in()
            self.close()
        else:
            self._label_status.setText('Incorrect username or password. Please try again')