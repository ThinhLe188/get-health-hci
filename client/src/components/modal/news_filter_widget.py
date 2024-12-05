import common.constants as const
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QListWidget,
                             QListWidgetItem, QPushButton, QVBoxLayout,
                             QWidget)


class RegionFilterWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.regions_set = set()
        self.setStyleSheet("font-size: 14px;")

        # Main Layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 20, 0, 20)
        main_layout.setSpacing(0)

        intro_label = QLabel('Add, remove your locations to get customized news and stories')
        intro_label.setWordWrap(True)
        intro_label.setStyleSheet('font-weight: bold;')
        intro_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(intro_label, Qt.AlignmentFlag.AlignCenter)
        main_layout.addSpacing(15)
        # Text Input for Adding Regions
        self.region_input = QLineEdit(self)
        self.region_input.setPlaceholderText("Type a region and press Enter")
        self.region_input.setStyleSheet("margin: 5px; padding: 10px;")
        self.region_input.returnPressed.connect(self.add_region)
        main_layout.addWidget(self.region_input)

        # Label
        label = QLabel('My Regions')
        label.setStyleSheet("background-color: rgb(255, 255, 102); font-weight: bold; padding: 15px; border-top: 1px solid grey; font-size: 16px;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(label)

        # List for My Regions
        self.region_list = QListWidget(self)
        self.region_list.setSpacing(2)
        main_layout.addWidget(self.region_list)
        # Create current region
        list_item = QListWidgetItem(self.region_list)
        # Create QWidget for item
        item_widget = QWidget(objectName='widget_region_list')
        layout = QHBoxLayout(item_widget)
        layout.setSpacing(10)
        # Region Name
        name_label = QLabel('Toronto', objectName='Toronto') # current location
        name_label.setStyleSheet("text-align: left; font-weight: bold;")
        name_label.setFixedHeight(25)
        layout.addWidget(name_label, Qt.AlignmentFlag.AlignLeft)
        status_label = QLabel('Current location') # current location
        status_label.setStyleSheet("text-align: left; font-style: italic; font-weight: bold;")
        layout.addStretch()
        layout.addWidget(status_label)
        # Set the item widget
        list_item.setSizeHint(item_widget.sizeHint())
        self.region_list.addItem(list_item)
        self.region_list.setItemWidget(list_item, item_widget)


    def add_region(self):
        """Add a new region to the list"""
        region_name = self.region_input.text().strip()
        if region_name and region_name not in self.regions_set:  # Ensure input is not empty
            self.add_region_item(region_name)
        self.region_input.clear()

        list_news_local = QListWidget()
        list_news_local.setAutoScroll(False)
        list_news_local.setSpacing(5)
        list_news_local.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        list_news_local.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.parent.widget_content.addTab(list_news_local, region_name)
        self.parent.load_news(list_news_local, region_name)


    def add_region_item(self, region_name):
        """Add an item with a delete button to the list"""
        self.regions_set.add(region_name)
        # Create QListWidgetItem
        list_item = QListWidgetItem(self.region_list)

        # Create QWidget for item
        item_widget = QWidget(objectName='widget_region_list')
        layout = QHBoxLayout(item_widget)
        layout.setSpacing(10)

        # Region Name
        name_label = QLabel(region_name, objectName=f'{region_name}')
        name_label.setStyleSheet("text-align: left;")
        layout.addWidget(name_label, Qt.AlignmentFlag.AlignLeft)

        # Delete Button
        delete_button = QPushButton()
        delete_button.setFlat(True)
        delete_button.setFixedSize(25, 25)
        delete_button.setIcon(QIcon(const.APP_REMOVE));
        delete_button.setIconSize(QSize(25, 25));
        delete_button.clicked.connect(lambda: self.delete_region_item(list_item))
        layout.addWidget(delete_button, Qt.AlignmentFlag.AlignRight)

        # Set the item widget
        list_item.setSizeHint(item_widget.sizeHint())
        self.region_list.addItem(list_item)
        self.region_list.setItemWidget(list_item, item_widget)

    def delete_region_item(self, item):
        """Remove an item from the list"""
        region_name = self.region_list.itemWidget(item).layout().itemAt(0).widget().objectName()
        row = self.region_list.row(item)
        self.region_list.takeItem(row)
        self.regions_set.remove(region_name)
        self.parent.remove_tab_by_region_name(region_name)