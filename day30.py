import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QWidget

class MerekSepatu:
    def __init__(self, nama, deskripsi):
        self.nama = nama
        self.deskripsi = deskripsi

class PengelolaMerekSepatu:
    def __init__(self):
        self.merek = []

    def tambah_merek(self, merek):
        self.merek.append(merek)

    def dapatkan_merek(self):
        return [merek.nama for merek in self.merek]

    def dapatkan_deskripsi(self, nama):
        for merek in self.merek:
            if merek.nama == nama:
                return merek.deskripsi
        return "Deskripsi tidak tersedia."

class AplikasiMerekSepatu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Daftar Merek Sepatu")

        self.label = QLabel("Pilih Merek Sepatu:")
        self.merek_combobox = QComboBox()

        self.pilih_tombol = QPushButton("Tampilkan Deskripsi")
        self.pilih_tombol.clicked.connect(self.tampilkan_deskripsi)

        self.hasil_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.merek_combobox)
        layout.addWidget(self.pilih_tombol)
        layout.addWidget(self.hasil_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.pengelola_merek = PengelolaMerekSepatu()
        self.muati_merek()

    def muati_merek(self):
        # Menambahkan beberapa merek sepatu contoh
        self.pengelola_merek.tambah_merek(MerekSepatu("Nike", "Merek sepatu terkenal dengan desain yang inovatif dan nyaman."))
        self.pengelola_merek.tambah_merek(MerekSepatu("Adidas", "Merek sepatu populer dengan fokus pada kinerja olahraga."))
        self.pengelola_merek.tambah_merek(MerekSepatu("Puma", "Merek sepatu terkenal dengan gaya yang sporty dan elegan."))
        self.pengelola_merek.tambah_merek(MerekSepatu("Reebok", "Merek sepatu terkenal dengan sepatu olahraga berkualitas tinggi."))
        self.pengelola_merek.tambah_merek(MerekSepatu("New Balance", "Merek sepatu terkenal dengan kenyamanan dan daya tahan tinggi."))
        self.pengelola_merek.tambah_merek(MerekSepatu("Converse", "Merek sepatu terkenal dengan desain klasik yang ikonik."))
        self.pengelola_merek.tambah_merek(MerekSepatu("Vans", "Merek sepatu terkenal dengan desain kasual dan streetwear."))
        self.pengelola_merek.tambah_merek(MerekSepatu("Under Armour", "Merek sepatu terkenal dengan kinerja olahraga dan teknologi inovatif."))
        self.pengelola_merek.tambah_merek(MerekSepatu("ASICS", "Merek sepatu terkenal dengan fokus pada kenyamanan dan dukungan untuk pelari."))
        self.pengelola_merek.tambah_merek(MerekSepatu("Skechers", "Merek sepatu terkenal dengan desain yang nyaman dan trendi."))
        
        merek = self.pengelola_merek.dapatkan_merek()
        self.merek_combobox.addItems(merek)

    def tampilkan_deskripsi(self):
        merek_terpilih = self.merek_combobox.currentText()
        deskripsi = self.pengelola_merek.dapatkan_deskripsi(merek_terpilih)
        self.hasil_label.setText(f"Deskripsi: {deskripsi}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AplikasiMerekSepatu()
    window.show()
    sys.exit(app.exec_())
