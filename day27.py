import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QComboBox

class Lesson:
    def __init__(self, subject, day, start_time, end_time):
        self.subject = subject
        self.day = day
        self.start_time = start_time
        self.end_time = end_time

class ScheduleManager:
    def __init__(self):
        self.schedule = []

    def add_lesson(self, lesson):
        self.schedule.append(lesson)

    def get_schedule(self):
        return self.schedule

class ScheduleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jadwal Pelajaran Mingguan")

        # Widgets untuk input pelajaran
        self.day_label = QLabel("Pilih Hari:")
        self.day_combobox = QComboBox()
        self.day_combobox.addItems(["Senin", "Selasa", "Rabu", "Kamis", "Jumat"])

        self.start_time_label = QLabel("Waktu Mulai:")
        self.start_time_input = QLineEdit()

        self.end_time_label = QLabel("Waktu Selesai:")
        self.end_time_input = QLineEdit()

        self.subject_label = QLabel("Nama Pelajaran:")
        self.subject_input = QLineEdit()

        self.add_button = QPushButton("Tambah Pelajaran")
        self.add_button.clicked.connect(self.add_lesson)

        self.schedule_label = QLabel("Jadwal Pelajaran:")
        self.schedule_display = QLabel()

        # Layouts
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.day_label)
        input_layout.addWidget(self.day_combobox)
        input_layout.addWidget(self.start_time_label)
        input_layout.addWidget(self.start_time_input)
        input_layout.addWidget(self.end_time_label)
        input_layout.addWidget(self.end_time_input)
        input_layout.addWidget(self.subject_label)
        input_layout.addWidget(self.subject_input)
        input_layout.addWidget(self.add_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.schedule_label)
        main_layout.addWidget(self.schedule_display)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Manager untuk jadwal
        self.schedule_manager = ScheduleManager()
        self.load_default_schedule()
        self.update_schedule_display()

    def load_default_schedule(self):
        # Jadwal pelajaran yang sudah terisi sebelumnya
        default_lessons = [
            Lesson("Matematika", "Senin", "08:00", "09:30"),
            Lesson("Fisika", "Senin", "10:00", "11:30"),
            Lesson("Kimia", "Senin", "13:00", "14:30"),
            Lesson("Biologi", "Senin", "14:45", "16:00"),
            Lesson("Bahasa Indonesia", "Selasa", "08:00", "09:30"),
            Lesson("Sejarah", "Selasa", "10:00", "11:30"),
            Lesson("Geografi", "Selasa", "13:00", "14:30"),
            Lesson("Seni", "Selasa", "14:45", "16:00"),
            Lesson("Kimia", "Rabu", "08:00", "09:30"),
            Lesson("Biologi", "Rabu", "10:00", "11:30"),
            Lesson("Ekonomi", "Rabu", "13:00", "14:30"),
            Lesson("Matematika", "Rabu", "14:45", "16:00"),
            Lesson("Geografi", "Kamis", "08:00", "09:30"),
            Lesson("Ekonomi", "Kamis", "10:00", "11:30"),
            Lesson("Matematika", "Kamis", "13:00", "14:30"),
            Lesson("Seni", "Kamis", "14:45", "16:00"),
            Lesson("Pendidikan Jasmani", "Jumat", "08:00", "09:30"),
            Lesson("Sejarah", "Jumat", "10:00", "11:30"),
            Lesson("Fisika", "Jumat", "12:00", "13:30")
        ]
        for lesson in default_lessons:
            self.schedule_manager.add_lesson(lesson)

    def add_lesson(self):
        day = self.day_combobox.currentText()
        start_time = self.start_time_input.text()
        end_time = self.end_time_input.text()
        subject = self.subject_input.text()

        # Validasi agar Jumat hanya sampai jam 14:00
        if day == "Jumat" and end_time > "14:00":
            self.result_label.setText("Pelajaran hari Jumat hanya sampai jam 14:00")
            return

        if day and start_time and end_time and subject:
            lesson = Lesson(subject, day, start_time, end_time)
            self.schedule_manager.add_lesson(lesson)
            self.update_schedule_display()

    def update_schedule_display(self):
        schedule = self.schedule_manager.get_schedule()
        display_text = "\n".join([f"{lesson.day} {lesson.start_time} - {lesson.end_time} : {lesson.subject}" for lesson in schedule])
        self.schedule_display.setText(display_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScheduleApp()
    window.show()
    sys.exit(app.exec_())
