from pages.content_widget import *


class MentalPage(ContentWidget):
    def __init__(self, parent):
        """Initialize mental health page
        """
        super().__init__(parent)
        self.layout().addStretch()


    def display_page(self):
        self.parent.label_title.setText(const.APP_PAGE_MENTAL)