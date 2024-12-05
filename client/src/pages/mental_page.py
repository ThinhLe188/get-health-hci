from pages.content_widget import *


class MentalPage(ContentWidget):
    def __init__(self, parent):
        """Initialize mental health page
        """
        super().__init__(parent)
        layout = self.layout()
        self._widget_content = QWidget()
        self._widget_content.setFixedHeight(1864)
        self._layout_content = QVBoxLayout()
        self._widget_content.setLayout(self._layout_content)
        self._widget_scroll.setWidget(self._widget_content)
        layout.addWidget(self._widget_scroll)


    def display_page(self):
        self.parent.label_title.setText(const.APP_PAGE_MENTAL)