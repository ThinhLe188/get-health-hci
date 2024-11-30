import os

import constants as const
from button_widget import ButtonWidget
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QMessageBox, QVBoxLayout,
                             QWidget)


class CentralWidget(QWidget):
    def __init__(self, curr_dir: str):
        super().__init__()
        self.curr_dir = curr_dir
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        # create nav bar section
        layout.addWidget(self._create_nav_bar())
        layout.addStretch()


    def _create_nav_bar(self):
        widget_nav_bar = QWidget(objectName='widget_nav')
        layout_nav_bar = QHBoxLayout()
        widget_nav_bar.setLayout(layout_nav_bar)
        layout_nav_bar.setContentsMargins(0, 0, 0, 0)
        # create title widget
        layout_nav_bar.addWidget(self._create_logo_widget())
        layout_nav_bar.addStretch()
        # create menu items
        widget_news = ButtonWidget(text='NEWS', 
                                   text_objectName='label_card', 
                                   objectName='widget_card', 
                                   width=160)
        widget_news.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_nav_bar.addWidget(widget_news)
        widget_mental = ButtonWidget(text='MENTAL HEALTH', 
                                   text_objectName='label_card', 
                                   objectName='widget_card', 
                                   width=160)
        widget_mental.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_nav_bar.addWidget(widget_mental)
        widget_physical = ButtonWidget(text='PHYSICAL HEALTH', 
                                   text_objectName='label_card', 
                                   objectName='widget_card', 
                                   width=160)
        widget_physical.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_nav_bar.addWidget(widget_physical)
        widget_about = ButtonWidget(text='ABOUT US', 
                                   text_objectName='label_card', 
                                   objectName='widget_card', 
                                   width=160)
        widget_about.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_nav_bar.addWidget(widget_about)
        # create profile widget
        layout_nav_bar.addStretch()
        layout_nav_bar.addWidget(self._create_profile_widget(), alignment=Qt.AlignmentFlag.AlignRight)
        return widget_nav_bar


    def _create_logo_widget(self):
        widget_title = ButtonWidget(text=const.APP_NAME, 
                                    text_objectName='label_title', 
                                    icon=os.path.join(self.curr_dir, const.APP_LOGO))
        widget_title.layout().setSpacing(0)
        widget_title.layout().setContentsMargins(0, 0, 0, 0)
        # connect signal
        widget_title.clicked.connect(self._handle_home_page)
        return widget_title


    def _create_profile_widget(self):
        widget_profile = ButtonWidget(text=const.USER_NAME, 
                                      text_objectName='label_card', 
                                      objectName='widget_card', 
                                      width=180,
                                      icon=os.path.join(self.curr_dir, const.USER_PFP), 
                                      size=(30, 30))
        # connect signal
        widget_profile.clicked.connect(self._handle_profile_page)
        return widget_profile


##############################################################################
# Signal handlers
##############################################################################
    @pyqtSlot()
    def _handle_home_page(self):
        # TODO
        pass


    @pyqtSlot()
    def _handle_profile_page(self):
        QMessageBox.information(self, 'GET HEALTH Prototype', 'Apologies! The user authentication and profile features are not yet ready in this prototype.')