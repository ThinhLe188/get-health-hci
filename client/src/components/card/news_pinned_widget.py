import common.constants as const
from components.card.card_widget import *
from components.card.news_widget import NewsCardWidget


class NewsPinnedCardWidget(CardWidget):
    def __init__(self, parent, bookmark_items: NewsCardWidget, curr_dir: str, img: str, title: str, author: str, location: str, publish: str, content: str):
        super().__init__(curr_dir, img, title, author, location, publish, content)
        label_bookmark = ButtonLabel(const.APP_REMOVE, const.APP_REMOVE)
        label_bookmark.clicked.connect(bookmark_items.toggle_bookmark)
        self._layout_footer.addWidget(label_bookmark)