from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QSpinBox, QFormLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Daftar Harga dan Pemesanan')

        # Daftar harga makanan dan minuman
        self.items = {
            "Nasi Goreng Spesial": 15000,
            "Mie Goreng": 8000,
            "Es Teh": 3000,
            "Kopi": 3000,
            "Ayam Goreng": 11000
        }

        # Layout utama
        main_layout = QVBoxLayout()

        # Layout untuk daftar harga
        price_layout = QFormLayout()
        self.order_widgets = {}
        for item, price in self.items.items():
            label = QLabel(f"{item}: Rp {price}")
            spin_box = QSpinBox()
            spin_box.setRange(0, 10)  # Set range dari 0 hingga 10
            self.order_widgets[item] = spin_box
            price_layout.addRow(label, spin_box)

        main_layout.addLayout(price_layout)

        # Tombol untuk menghitung total
        self.total_button = QPushButton('Hitung Total')
        self.total_button.clicked.connect(self.calculate_total)
        main_layout.addWidget(self.total_button)

        # Label untuk menampilkan total harga
        self.total_label = QLabel("Total: Rp 0")
        main_layout.addWidget(self.total_label)

        # Set layout utama
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def calculate_total(self):
        total = 0
        for item, spin_box in self.order_widgets.items():
            total += self.items[item] * spin_box.value()
        self.total_label.setText(f"Total: Rp {total}")

# Buat aplikasi PyQt5
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
