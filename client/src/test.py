from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QWidget, QLabel, QVBoxLayout

app = QApplication([])

list_widget = QListWidget()

# Create a custom widget
class CustomWidget(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        label = QLabel(text)
        label.setStyleSheet("color: red; font-size: 14px;")
        layout.addWidget(label)
        layout.setContentsMargins(0, 0, 0, 0)

# Add custom widgets to the QListWidget
for i in range(5):
    item = QListWidgetItem(list_widget)
    custom_widget = CustomWidget(f"Custom Item {i + 1}")
    item.setSizeHint(custom_widget.sizeHint())
    list_widget.setItemWidget(item, custom_widget)

list_widget.show()
app.exec_()