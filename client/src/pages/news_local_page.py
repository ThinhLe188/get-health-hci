from pages.content_widget import *


class NewsLocalPage(ContentWidget):
    def __init__(self, parent):
        """Initialize health local news page
        """
        super().__init__(parent)
        self._widget_content = QTabWidget(self._widget_scroll)
        self._widget_content.tabBar().setMovable(True)
        self._widget_content.setFixedSize(430, 820)
        self._widget_content.setContentsMargins(0, 0, 0, 0)
        self.list_news_local = QListWidget()
        self.list_news_local.setAutoScroll(False)
        self.list_news_local.setSpacing(5)
        self.list_news_local.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_news_local.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_content.addTab(self.list_news_local, 'Toronto') # current location


    def display_page(self):
        super().display_page()
        self.parent.label_title.setText(const.APP_PAGE_LOCAL_NEWS)
        self.parent.button_filter.show()