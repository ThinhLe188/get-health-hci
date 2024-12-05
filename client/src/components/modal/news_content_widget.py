from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QLabel, QTextEdit, QVBoxLayout,
                             QWidget)


class NewsContentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Image
        self.image_label = QLabel()
        pixmap = QPixmap()
        if pixmap.isNull():
            pixmap = QPixmap(430, 300) # placeholder if image doesn't exist
            pixmap.fill(Qt.lightGray)
        self.image_label.setPixmap(pixmap.scaledToWidth(400, Qt.SmoothTransformation))
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)
        # Title
        self.title_label = QLabel()
        self.title_label.setWordWrap(True)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(self.title_label)
        # Metadata
        self.metadata_label = QLabel()
        self.metadata_label.setAlignment(Qt.AlignLeft)
        self.metadata_label.setStyleSheet("color: gray; font-size: 14px;")
        layout.addWidget(self.metadata_label)
        layout.addSpacing(10)
        # Content
        self.content_text = QTextEdit()
        self.content_text.setReadOnly(True)
        self.content_text.setStyleSheet("""
            QTextEdit {
                font-size: 16px;
                border: none;
                background: transparent;
            }
            QTextEdit:focus {
                outline: none;
            }
        """)
        self.content_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.content_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        layout.addWidget(self.content_text)
        # Set the layout and the overall widget appearance
        self.setLayout(layout)


    def display_content(self, image_path, title, author, location, last_update, content):
        self._set_image(image_path)
        self.title_label.setText(title)
        metadata = f"Last update: {last_update} | Author: {author}"
        self.metadata_label.setText(metadata)
        self.content_text.setText(content)


    def _set_image(self, image_path):
        """Update the image displayed at the top."""
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap.scaledToWidth(400, Qt.SmoothTransformation))