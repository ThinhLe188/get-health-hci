from components.modal.modal_widget import *
from components.button.sidebar_button_widget import SideBarButtonWidget
from PyQt5.QtWidgets import QFrame


class SideBarWidget(ModalWidget):
    def __init__(self, parent):
        super().__init__(parent)
        layout_outer = self.layout()
        layout_outer.setAlignment(Qt.AlignmentFlag.AlignRight)
        self._widget_modal = QWidget(objectName='widget_component')
        self._widget_modal.setFixedWidth(const.SIDEBAR_W)
        layout_outer.addWidget(self._widget_modal)
        layout_sidebar = QVBoxLayout()
        layout_sidebar.setContentsMargins(0, 30, 0, 0)
        layout_sidebar.setSpacing(0)
        self._widget_modal.setLayout(layout_sidebar)
        # create sidebar header
        self._label_pfp = QLabel()
        pixmap = QPixmap(const.APP_PROFILE)
        self._label_pfp.setFixedSize(50, 50)
        self._label_pfp.setPixmap(pixmap.scaled(self._label_pfp.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self._label_username = QLabel(const.USER_GUEST, objectName='label_username')
        layout_sidebar.addWidget(self._label_pfp, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_sidebar.addSpacing(15)
        layout_sidebar.addWidget(self._label_username, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_sidebar.addSpacing(30)
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        layout_sidebar.addWidget(line)
        # create sidebar items
        self._button_login = SideBarButtonWidget('Sign In', const.APP_LOGIN)
        layout_sidebar.addWidget(self._button_login)
        self._button_logout = SideBarButtonWidget('Sign Out', const.APP_LOGOUT)
        self._button_logout.hide()
        layout_sidebar.addWidget(self._button_logout)
        layout_sidebar.addStretch()
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        layout_sidebar.addWidget(line)
        button_exit = SideBarButtonWidget('Exit', const.APP_EXIT)
        layout_sidebar.addWidget(button_exit)
        # add signals
        self._button_login.clicked.connect(self.parent.open_login_modal)
        self._button_logout.clicked.connect(self.user_logged_out)
        button_exit.clicked.connect(self.parent.exit_app)


    def user_logged_in(self):
        # display persona user
        self._label_username.setText(const.USER_NAME)
        pixmap = QPixmap(const.USER_PFP)
        self._label_pfp.setFixedSize(50, 50)
        self._label_pfp.setPixmap(pixmap.scaled(self._label_pfp.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self._button_login.hide()
        self._button_logout.show()


    def user_logged_out(self):
        self._label_username.setText(const.USER_GUEST)
        pixmap = QPixmap(const.APP_PROFILE)
        self._label_pfp.setFixedSize(50, 50)
        self._label_pfp.setPixmap(pixmap.scaled(self._label_pfp.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self._button_login.show()
        self._button_logout.hide()
        self.parent.user_logged_out()