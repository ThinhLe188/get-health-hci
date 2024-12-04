import common.constants as const
from PyQt5.QtWidgets import QVBoxLayout, QWidget


class ContentWidget(QWidget):
    def __init__(self, parent):
        """Initialize mental health page
        """
        super().__init__()
        from central_widget import CentralWidget
        self.parent: CentralWidget = parent
        self.setFixedHeight(1864)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)


    def display_page(self):
        pass