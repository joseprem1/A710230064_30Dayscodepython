import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QWidget

class Degree:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class DegreeManager:
    def __init__(self):
        self.degrees = []

    def add_degree(self, degree):
        self.degrees.append(degree)

    def get_degrees(self):
        return [degree.name for degree in self.degrees]

    def get_description(self, name):
        for degree in self.degrees:
            if degree.name == name:
                return degree.description
        return "Deskripsi tidak tersedia."

class DegreeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Daftar Gelar Sarjana")

        self.label = QLabel("Pilih Gelar Sarjana:")
        self.degree_combobox = QComboBox()

        self.select_button = QPushButton("Tampilkan Deskripsi")
        self.select_button.clicked.connect(self.display_description)

        self.result_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.degree_combobox)
        layout.addWidget(self.select_button)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.degree_manager = DegreeManager()
        self.load_degrees()

    def load_degrees(self):
        # Menambahkan beberapa gelar sarjana contoh
        self.degree_manager.add_degree(Degree("Sarjana Teknik (S.T.)", "Gelar yang diberikan kepada lulusan program studi teknik."))
        self.degree_manager.add_degree(Degree("Sarjana Hukum (S.H.)", "Gelar yang diberikan kepada lulusan program studi hukum."))
        self.degree_manager.add_degree(Degree("Sarjana Kedokteran (S.Ked.)", "Gelar yang diberikan kepada lulusan program studi kedokteran."))
        self.degree_manager.add_degree(Degree("Sarjana Ekonomi (S.E.)", "Gelar yang diberikan kepada lulusan program studi ekonomi."))
        self.degree_manager.add_degree(Degree("Sarjana Komputer (S.Kom.)", "Gelar yang diberikan kepada lulusan program studi komputer."))
        self.degree_manager.add_degree(Degree("Sarjana Pendidikan (S.Pd.)", "Gelar yang diberikan kepada lulusan program studi pendidikan."))
        self.degree_manager.add_degree(Degree("Sarjana Seni (S.Sn.)", "Gelar yang diberikan kepada lulusan program studi seni."))
        self.degree_manager.add_degree(Degree("Sarjana Pertanian (S.P.)", "Gelar yang diberikan kepada lulusan program studi pertanian."))
        self.degree_manager.add_degree(Degree("Sarjana Ilmu Sosial (S.Sos.)", "Gelar yang diberikan kepada lulusan program studi ilmu sosial."))
        self.degree_manager.add_degree(Degree("Sarjana Ilmu Politik (S.IP.)", "Gelar yang diberikan kepada lulusan program studi ilmu politik."))
        
        degrees = self.degree_manager.get_degrees()
        self.degree_combobox.addItems(degrees)

    def display_description(self):
        selected_degree = self.degree_combobox.currentText()
        description = self.degree_manager.get_description(selected_degree)
        self.result_label.setText(f"Deskripsi: {description}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DegreeApp()
    window.show()
    sys.exit(app.exec_())
