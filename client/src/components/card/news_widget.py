import common.constants as const
from components.card.card_widget import *
from PyQt5.QtCore import pyqtSlot


class NewsCardWidget(CardWidget):
    def __init__(self, central_widget, curr_dir: str, img: str, title: str, author: str, location: str, publish: str, content: str):
        super().__init__(curr_dir, img, title, author, location, publish, content)
        self.central_widget = central_widget
        self._data = (img, title, author, location, publish, content)
        self.pinned_item = None
        self._label_bookmark = ButtonLabel(const.APP_BOOKMARK, const.APP_BOOKMARK_FILL)
        self._label_bookmark.clicked.connect(self._handle_bookmark)
        self._layout_footer.addWidget(self._label_bookmark)


    def set_bookmark(self, item: QListWidgetItem):
        self.pinned_item = item


    @pyqtSlot(bool)
    def _handle_bookmark(self, is_toggled: bool):
        if is_toggled:
            self.central_widget.bookmark_news(self, self._data)
        else:
            self.central_widget.remove_bookmark_news(self.pinned_item)


    def toggle_bookmark(self):
        self._label_bookmark.click()