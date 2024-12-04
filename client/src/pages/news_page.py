from pages.content_widget import *


class NewsPage(ContentWidget):
    def __init__(self, parent):
        """Initialize health news page
        """
        super().__init__(parent)
        self.layout().addStretch()


    def display_page(self):
        self.parent.label_title.setText(const.APP_PAGE_NEWS)