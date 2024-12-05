from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QTextEdit


class NewsArticleWidget(QWidget):
    def __init__(self, image_path, title, last_update, author, content, parent=None):
        super().__init__(parent)

        # Create the layout
        layout = QVBoxLayout(self)

        # Image
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            pixmap = QPixmap(400, 200)  # Placeholder if image doesn't exist
            pixmap.fill(Qt.lightGray)
        self.image_label.setPixmap(pixmap.scaledToWidth(400, Qt.SmoothTransformation))
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        # Title
        self.title_label = QLabel(title, self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setWordWrap(True)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(self.title_label)

        # Metadata
        metadata = f"Last update: {last_update} | Author: {author}"
        self.metadata_label = QLabel(metadata, self)
        self.metadata_label.setAlignment(Qt.AlignLeft)  # Align metadata to the left
        self.metadata_label.setStyleSheet("color: gray; font-size: 14px;")
        layout.addWidget(self.metadata_label)

        # Content
        self.content_text = QTextEdit(self)
        self.content_text.setReadOnly(True)
        self.content_text.setText(content)
        self.content_text.setStyleSheet("""
            QTextEdit {
                font-size: 16px;
                border: none;
                background: transparent;
            }
            QTextEdit:focus {
                outline: none;
            }
        """)  # Remove borders and scrollbar
        self.content_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.content_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        layout.addWidget(self.content_text)

        # Set the layout and the overall widget appearance
        self.setLayout(layout)
        self.setStyleSheet("background-color: white; padding: 10px;")

    def set_image(self, image_path):
        """Update the image displayed at the top."""
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap.scaledToWidth(400, Qt.SmoothTransformation))


# Example usage
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    # Example data
    image_path = "example_image.jpg"  # Path to the top image
    title = "Breaking News: PyQt Makes UI Development Easier!"
    last_update = "1 hour ago"
    author = "John Doe"
    content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."""

    # Create and show the widget
    news_widget = NewsArticleWidget(image_path, title, last_update, author, content)
    news_widget.resize(450, 600)
    news_widget.show()

    sys.exit(app.exec_())
