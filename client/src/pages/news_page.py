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
        self.list_news_all = QListWidget()
        self.list_news_all.setAutoScroll(False)
        self.list_news_all.setSpacing(5)
        self.list_news_all.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_news_all.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_news_top = QListWidget()
        self.list_news_top.setAutoScroll(False)
        self.list_news_top.setSpacing(5)
        self.list_news_top.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_news_top.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_content.addTab(self.list_news_all, 'All')
        self._widget_content.addTab(self.list_news_top, 'Top News')
        self._load_news()
        # init news content widget
        self._widget_news_content = NewsContentWidget()
        self.addWidget(self._widget_news_content)
        # connect signals
        self._widget_content.currentChanged.connect(self.update_layout)
        self.list_news_all.itemClicked.connect(self._view_news_content)
        self.list_news_top.itemClicked.connect(self._view_news_content)


    def display_page(self):
        super().display_page()
        self.parent.button_search.show()
        self.parent.label_title.setText(const.APP_PAGE_NEWS)


    def _load_news(self):
        for news in const.NEWS:
            item = QListWidgetItem(self.list_news_all)
            card_news = NewsCardWidget(self.parent, self.parent.curr_dir, *news)
            item.setSizeHint(QSize(400, 340))
            self.list_news_all.setItemWidget(item, card_news)

        for news in const.NEWS_TOP:
            item = QListWidgetItem(self.list_news_top)
            card_news = NewsCardWidget(self.parent, self.parent.curr_dir, *news)
            item.setSizeHint(QSize(400, 340))
            self.list_news_top.setItemWidget(item, card_news)


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


    def _view_news_content(self, item: QListWidgetItem):
        self._widget_news_content.display_content(*item.listWidget().itemWidget(item).get_data())
        self.parent.button_back.show()
        self.setCurrentIndex(1)