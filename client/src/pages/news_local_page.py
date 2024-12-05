from pages.content_widget import *
from components.modal.news_filter_widget import RegionFilterWidget


class NewsLocalPage(ContentWidget):
    def __init__(self, parent):
        """Initialize health local news page
        """
        super().__init__(parent)
        self.widget_content = QTabWidget(self._widget_scroll)
        self.widget_content.setFixedSize(430, 820)
        self.widget_content.setContentsMargins(0, 0, 0, 0)
        list_news_local = QListWidget()
        list_news_local.setAutoScroll(False)
        list_news_local.setSpacing(5)
        list_news_local.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        list_news_local.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.widget_content.addTab(list_news_local, 'Toronto') # current location
        self.load_news(list_news_local, 'Toronto')
        # create filter widget
        self._widget_filter = RegionFilterWidget(self)
        self.addWidget(self._widget_filter)
        # add signals
        self.widget_content.currentChanged.connect(self.update_layout)
        list_news_local.itemDoubleClicked.connect(self._view_news_content)


    def display_page(self):
        super().display_page()
        self.parent.label_title.setText(const.APP_PAGE_LOCAL_NEWS)
        self.parent.button_filter.show()
        self.parent.button_filter.clicked.connect(self._open_filter_widget)


    def load_news(self, list_widget: QListWidget, filter_text: str):
        for news in const.NEWS_TOP:
            item = QListWidgetItem(list_widget)
            card_news = NewsCardWidget(self.parent, self.parent.curr_dir, *news)
            item.setSizeHint(QSize(400, 340))
            list_widget.setItemWidget(item, card_news)
            if filter_text.lower() not in card_news.location_str:
                item.setHidden(True)
        
        for news in const.NEWS:
            item = QListWidgetItem(list_widget)
            card_news = NewsCardWidget(self.parent, self.parent.curr_dir, *news)
            item.setSizeHint(QSize(400, 340))
            list_widget.setItemWidget(item, card_news)
            if filter_text.lower() not in card_news.location_str:
                item.setHidden(True)


    def update_layout(self, index: int):
        current_list_widget = self.widget_content.widget(index)
        if isinstance(current_list_widget, QListWidget):
            # force recalculation
            current_list_widget.setFixedWidth(self.widget_content.width())

            # adjust each item
            for i in range(current_list_widget.count()):
                item = current_list_widget.item(i)
                widget = current_list_widget.itemWidget(item)
                if widget:
                    widget.setFixedSize(current_list_widget.viewport().width() - 20, 330)
                    widget.updateGeometry()

            # repaint the viewport
            current_list_widget.viewport().update()


    def _open_filter_widget(self):
        self.parent.label_title.setText(const.APP_PAGE_REGION_FILTER)
        self.parent.button_back.show()
        self.setCurrentIndex(2)


    def remove_tab_by_region_name(self, region_name):
        """Remove a tab from QTabWidget by its text"""
        for index in range(self.widget_content.count()):
            if self.widget_content.tabText(index) == region_name:
                self.widget_content.removeTab(index)
                break  # Exit the loop after removing the tab