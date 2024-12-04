from pages.content_widget import *


class NewsPage(ContentWidget):
    def __init__(self, parent):
        """Initialize health news page
        """
        super().__init__(parent)
        self._widget_content = QTabWidget(self._widget_scroll)
        self._widget_content.tabBar().setDocumentMode(True)
        self._widget_content.setFixedSize(430, 820)
        self._widget_content.setContentsMargins(0, 0, 0, 0)
        self._list_all = QListWidget()
        self._list_all.setAutoScroll(False)
        self._list_all.setSpacing(5)
        self._list_all.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._list_all.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._list_top = QListWidget()
        self._list_top.setAutoScroll(False)
        self._list_top.setSpacing(5)
        self._list_top.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._list_top.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._list_saved = QListWidget()
        self._list_saved.setAutoScroll(False)
        self._list_saved.setSpacing(5)
        self._list_saved.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._list_saved.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_content.addTab(self._list_all, 'All')
        self._widget_content.addTab(self._list_top, 'Top News')
        self._widget_content.addTab(self._list_saved, 'Saved')
        self._load_news()
        # connect signals
        self._widget_content.currentChanged.connect(self.update_layout)


    def display_page(self):
        self.parent.button_search.show()
        self.parent.label_title.setText(const.APP_PAGE_NEWS)


    def _load_news(self):
        for news in const.NEWS:
            item = QListWidgetItem(self._list_all)
            card_news = NewsCardWidget(self, self._curr_dir, *news)
            item.setSizeHint(QSize(400, 340))
            self._list_all.setItemWidget(item, card_news)

        for news in const.NEWS_TOP:
            item = QListWidgetItem(self._list_top)
            card_news = NewsCardWidget(self, self._curr_dir, *news)
            item.setSizeHint(QSize(400, 340))
            self._list_top.setItemWidget(item, card_news)


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


    @pyqtSlot()
    def bookmark_news(self, news_item: NewsCardWidget, news: tuple):
        item = QListWidgetItem(self._list_saved)
        card_news = NewsPinnedCardWidget(self, news_item, self._curr_dir, *news)
        item.setSizeHint(QSize(400, 340))
        self._list_saved.setItemWidget(item, card_news)
        news_item.set_bookmark(item)


    @pyqtSlot()
    def remove_bookmark_news(self, item: QListWidgetItem):
        self._list_saved.removeItemWidget(item)
        self._list_saved.takeItem(self._list_saved.row(item))