import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QWidget

class DistanceCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Penghitung Sisa Jarak Antar Kota")

        # Membuat widget
        self.label = QLabel("Pilih Kota:")
        self.city1_combobox = QComboBox()
        self.city2_combobox = QComboBox()

        self.calculate_button = QPushButton("Hitung Sisa Jarak")
        self.calculate_button.clicked.connect(self.calculate_distance)

        self.result_label = QLabel()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.city1_combobox)
        layout.addWidget(self.city2_combobox)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.city_distances = {
            "Jakarta": {"Bandung": 150, "Surabaya": 780, "Yogyakarta": 560},
            "Bandung": {"Jakarta": 150, "Surabaya": 690, "Yogyakarta": 400},
            "Surabaya": {"Jakarta": 780, "Bandung": 690, "Yogyakarta": 330},
            "Yogyakarta": {"Jakarta": 560, "Bandung": 400, "Surabaya": 330}
        }

        self.cities = list(self.city_distances.keys())
        self.city1_combobox.addItems(self.cities)
        self.city2_combobox.addItems(self.cities)

    def calculate_distance(self):
        city1 = self.city1_combobox.currentText()
        city2 = self.city2_combobox.currentText()

        if city1 == city2:
            self.result_label.setText("Kota yang dipilih sama. Silakan pilih kota yang berbeda.")
        else:
            distance = self.city_distances.get(city1, {}).get(city2, None)
            if distance is not None:
                self.result_label.setText(f"Sisa jarak antara {city1} dan {city2} adalah {distance} km.")
            else:
                self.result_label.setText(f"Tidak ada data jarak antara {city1} dan {city2}.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DistanceCalculator()
    window.show()
    sys.exit(app.exec_())
