from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, pyqtSlot


class LoginCard(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Window settings
        self.setWindowTitle("Login Card")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #f4f4f4; border-radius: 10px;")

        # Create main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Title label
        title_label = QLabel("Welcome Back!")
        title_label.linkActivated.connect(self.link_handler)
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #333333;")

        # Username input
        username_label = QLabel("Username:")
        username_label.setStyleSheet("font-size: 14px; font-weight: bold")
        username_input = QLineEdit()
        username_input.setPlaceholderText("Enter your username")

        # Password input
        password_label = QLabel("Password:")
        password_label.setStyleSheet("font-size: 14px; font-weight: bold")
        password_input = QLineEdit()
        password_input.setPlaceholderText("Enter your password")
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setStyleSheet(
            """
            QLineEdit {
                padding: 4px;
                border: 1px solid #cccccc;
                border-radius: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #0078d7;
                outline: none;
            }
            """
        )

        # Login button
        login_button = QPushButton("Login")
        login_button.setStyleSheet(
            """
            QPushButton {
                background-color: #0078d7;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QPushButton:pressed {
                background-color: #004578;
            }
            """
        )

        # Arrange widgets in the layout
        main_layout.addWidget(title_label)
        main_layout.addWidget(username_label)
        main_layout.addWidget(username_input)
        main_layout.addWidget(password_label)
        main_layout.addWidget(password_input)
        main_layout.addSpacing(10)
        main_layout.addWidget(login_button, alignment=Qt.AlignCenter)

        # Set the main layout
        self.setLayout(main_layout)
    
    @pyqtSlot()
    def link_handler(self):
        print('hello')


if __name__ == "__main__":
    app = QApplication([])
    window = LoginCard()
    window.show()
    app.exec_()
