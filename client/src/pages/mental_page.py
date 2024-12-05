from pages.content_widget import *
from components.card.doctor_mental_widget import DoctorMentalInfoWidget


class MentalPage(ContentWidget):
    def __init__(self, parent):
        """Initialize mental health page
        """
        super().__init__(parent)
        self._widget_content = QTabWidget(self._widget_scroll)
        self._widget_content.tabBar().setDocumentMode(True)
        self._widget_content.setFixedSize(430, 820)
        self._widget_content.setContentsMargins(0, 0, 0, 0)
        self._widget_services = QScrollArea(objectName='scroll_content')
        self._widget_services.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_services.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._list_journals = QListWidget()
        self._list_journals.setAutoScroll(False)
        self._list_journals.setSpacing(5)
        self._list_journals.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._list_journals.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._list_appoinments = QListWidget()
        self._list_appoinments.setAutoScroll(False)
        self._list_appoinments.setSpacing(5)
        self._list_appoinments.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._list_appoinments.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._widget_content.addTab(self._widget_services, 'Supports')
        self._widget_content.addTab(self._list_appoinments, 'Appoinments')
        self._widget_content.addTab(self._list_journals, 'Journals')
        # init content section
        self._init_content_section()
        self._load_journals()
        self._load_doctor()


    def _init_content_section(self):
        section_content = QWidget(self._widget_services)
        section_content.setFixedWidth(430)
        layout_content = QVBoxLayout()
        layout_content.setContentsMargins(0, 15, 0, 0)
        layout_content.setSpacing(0)
        section_content.setLayout(layout_content)
        button_chatbot = QPushButton('Quick Diagnosis AI Chatbot', objectName='button_chatbot')
        button_chatbot.setIcon(QIcon(const.APP_CHATBOT))
        button_chatbot.setIconSize(QSize(35, 35))
        layout_content.addWidget(button_chatbot, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_content.addSpacing(15)
        label_professionals = QLabel('Connect with mental health specialists')
        label_professionals.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_professionals.setStyleSheet("background-color: rgb(255, 255, 102); font-weight: bold; margin: 0px; padding: 15px; border-top: 1px solid grey; font-size: 16px;")
        layout_content.addWidget(label_professionals)
        self._list_specialists = QListWidget()
        self._list_specialists.setAutoScroll(False)
        self._list_specialists.setSpacing(5)
        self._list_specialists.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._list_specialists.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        layout_content.addWidget(self._list_specialists)


    def display_page(self):
        super().display_page()
        self.parent.label_title.setText(const.APP_PAGE_MENTAL)


    def _load_doctor(self):
        for data in const.MENTAL_DOC:
            item = QListWidgetItem()
            widget = DoctorMentalInfoWidget(*data)
            item.setSizeHint(widget.sizeHint())
            self._list_specialists.addItem(item)
            self._list_specialists.setItemWidget(item, widget)


    def _load_journals(self):
        pass