import constants as const
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QMessageBox, QScrollArea,
                             QVBoxLayout, QWidget, QPushButton)


class MentalPage(QWidget):
    def __init__(self):
        """Initialize mental health page
        """
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Create buttons
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        
        # Create a horizontal layout for button1
        button1_layout = QHBoxLayout()
        button1_layout.addStretch()  # This pushes the button to the right
        button1_layout.addWidget(button1)
        
        # Add the horizontal layout and button2 to the main vertical layout
        layout.addLayout(button1_layout)
        layout.addWidget(button2)


        self.setLayout(layout)