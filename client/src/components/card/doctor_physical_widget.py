import common.constants as const
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget


class DoctorPhysicalInfoWidget(QWidget):
    def __init__(self, gender, name, specialization, years_of_experience, clinic_name, appointment_type, distance, parent=None):
        super(DoctorPhysicalInfoWidget, self).__init__(parent)

        # Choose avatar based on gender
        avatar_path = const.APP_MALE if gender.lower() == "male" else const.APP_FEMALE

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(15, 15, 15, 15)

        # Image section
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap(avatar_path).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.image_label.setFixedSize(100, 100)
        self.image_label.setStyleSheet("border-radius: 50px; border: 2px solid #3498DB;")  # Circular profile picture

        # Info section
        info_layout = QVBoxLayout()
        info_layout.setSpacing(8)

        # Name
        self.name_label = QLabel(f"<b>{name}</b>")
        self.name_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.name_label.setStyleSheet("color: #2C3E50;")

        # Specialization
        self.specialization_label = QLabel(f"🔬 Specialization: {specialization}")
        self.specialization_label.setStyleSheet("color: #34495E; font-size: 12px;")

        # Years of experience
        self.years_label = QLabel(f"📅 Experience: {years_of_experience}")
        self.years_label.setStyleSheet("color: #34495E; font-size: 12px;")

        # Clinic name
        self.clinic_label = QLabel(f"🏥 Clinic: {clinic_name}")
        self.clinic_label.setStyleSheet("color: #34495E; font-size: 12px;")

        # Appointment type
        self.appointment_label = QLabel(f"📞 Appointments: {appointment_type}")
        self.appointment_label.setStyleSheet("color: #34495E; font-size: 12px;")

        # Distance
        self.distance_label = QLabel(f"📍 Distance: {distance}")
        self.distance_label.setStyleSheet("color: #34495E; font-size: 12px;")

        # Add info widgets to the info layout
        info_layout.addWidget(self.name_label)
        info_layout.addWidget(self.specialization_label)
        info_layout.addWidget(self.years_label)
        info_layout.addWidget(self.clinic_label)
        info_layout.addWidget(self.appointment_label)
        info_layout.addWidget(self.distance_label)

        # Add widgets to the main layout
        main_layout.addWidget(self.image_label)
        main_layout.addLayout(info_layout)

        # Styling the main frame
        self.setLayout(main_layout)
        self.setStyleSheet("""
            QWidget {
                background-color: #ECF0F1;
                border: 2px solid #BDC3C7;
                border-radius: 10px;
            }
        """)