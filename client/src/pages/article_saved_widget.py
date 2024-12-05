from pages.content_widget import *


class SavedArticlesPage(ContentWidget):
    def __init__(self, parent):
        """Initialize health news page
        """
        super().__init__(parent)
        self._widget_content = QTabWidget(self._widget_scroll)
        self._widget_content.tabBar().setDocumentMode(True)
        self._widget_content.setFixedSize(430, 820)
        self._widget_content.setContentsMargins(0, 0, 0, 0)
        self.list_news = QListWidget()
        self.list_news.setAutoScroll(False)
        self.list_news.setSpacing(5)
        self.list_news.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_news.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_jours = QListWidget()
        self.list_jours.setAutoScroll(False)
        self.list_jours.setSpacing(5)
        self.list_jours.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_jours.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_content.addTab(self.list_news, 'News')
        self._widget_content.addTab(self.list_jours, 'Journals')
        # connect signals
        self._widget_content.currentChanged.connect(self.update_layout)


    def display_page(self):
        self.parent.button_search.show()
        self.parent.label_title.setText(const.APP_PAGE_NEWS)


    def update_layout(self, index: int):
        current_list_widget = self._widget_content.widget(index)
        if isinstance(current_list_widget, QListWidget):
            # force recalculation
            current_list_widget.setFixedWidth(self._widget_content.width())

            # adjust each item
            for i in range(current_list_widget.count()):
                item = current_list_widget.item(i)
                widget = current_list_widget.itemWidget(item)
                if widget:
                    widget.setFixedSize(current_list_widget.viewport().width() - 20, 330)
                    widget.updateGeometry()

            # repaint the viewport
            current_list_widget.viewport().update()