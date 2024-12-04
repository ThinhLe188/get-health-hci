from pages.content_widget import *


class NewsLocalPage(ContentWidget):
    def __init__(self, parent):
        """Initialize health local news page
        """
        super().__init__(parent)
        self._widget_content = QTabWidget(self._widget_scroll)
        self._widget_content.setFixedSize(430, 820)
        self._widget_content.setContentsMargins(0, 0, 0, 0)
        self._list_saved = QListWidget()
        self._widget_content.addTab(self._list_saved, 'Saved')


    def display_page(self):
        self.parent.label_title.setText(const.APP_PAGE_LOCAL_NEWS)