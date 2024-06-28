import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QWidget, QLineEdit

class ProgramStudi:
    def __init__(self, nama, fakultas):
        self.nama = nama
        self.fakultas = fakultas

class ProgramStudiManager:
    def __init__(self):
        self.programs = []

    def tambah_program(self, program):
        self.programs.append(program)

    def get_fakultas(self):
        fakultas = set(program.fakultas for program in self.programs)
        return list(fakultas)

    def get_programs_by_fakultas(self, fakultas):
        return [program.nama for program in self.programs if program.fakultas == fakultas]

class ProgramStudiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Pemilihan Program Studi dan Fakultas")
        
        self.nama_label = QLabel("Masukkan Nama Anda:")
        self.nama_input = QLineEdit()
        
        self.fakultas_label = QLabel("Pilih Fakultas:")
        self.fakultas_combobox = QComboBox()
        self.fakultas_combobox.currentIndexChanged.connect(self.update_programs)
        
        self.program_label = QLabel("Pilih Program Studi:")
        self.program_combobox = QComboBox()
        
        self.pilih_button = QPushButton("Pilih")
        self.pilih_button.clicked.connect(self.pilih_program)
        
        self.hasil_label = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(self.nama_label)
        layout.addWidget(self.nama_input)
        layout.addWidget(self.fakultas_label)
        layout.addWidget(self.fakultas_combobox)
        layout.addWidget(self.program_label)
        layout.addWidget(self.program_combobox)
        layout.addWidget(self.pilih_button)
        layout.addWidget(self.hasil_label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.program_manager = ProgramStudiManager()
        self.load_programs()
        
    def load_programs(self):
        # Menambahkan contoh program dengan fakultasnya
        self.program_manager.tambah_program(ProgramStudi("Teknik Informatika", "Teknik"))
        self.program_manager.tambah_program(ProgramStudi("Sistem Informasi", "Teknik"))
        self.program_manager.tambah_program(ProgramStudi("Teknik Elektro", "Teknik"))
        self.program_manager.tambah_program(ProgramStudi("Teknik Mesin", "Teknik"))
        self.program_manager.tambah_program(ProgramStudi("Teknik Industri", "Teknik"))
        self.program_manager.tambah_program(ProgramStudi("Manajemen", "Ekonomi"))
        self.program_manager.tambah_program(ProgramStudi("Akuntansi", "Ekonomi"))
        self.program_manager.tambah_program(ProgramStudi("Hukum", "Hukum"))
        self.program_manager.tambah_program(ProgramStudi("Pendidikan Teknik Informatika", "Keguruan dan ILmu Pendidikan"))
        self.program_manager.tambah_program(ProgramStudi("Pendidikan Matematika", "Keguruan dan ILmu Pendidikan"))
        self.program_manager.tambah_program(ProgramStudi("Pendidikan Guru Sekolah Dasar", "Keguruan dan ILmu Pendidikan"))
        self.program_manager.tambah_program(ProgramStudi("Pendidikan Bahasa Indonesia", "Keguruan dan ILmu Pendidikan"))
        self.program_manager.tambah_program(ProgramStudi("Pendidikan Olahraga", "Keguruan dan ILmu Pendidikan"))
        
        fakultas = self.program_manager.get_fakultas()
        self.fakultas_combobox.addItems(fakultas)
    
    def update_programs(self):
        fakultas = self.fakultas_combobox.currentText()
        programs = self.program_manager.get_programs_by_fakultas(fakultas)
        self.program_combobox.clear()
        self.program_combobox.addItems(programs)
    
    def pilih_program(self):
        nama = self.nama_input.text()
        fakultas_terpilih = self.fakultas_combobox.currentText()
        program_terpilih = self.program_combobox.currentText()
        self.hasil_label.setText(f"Nama: {nama}, Fakultas: {fakultas_terpilih}, Program Studi: {program_terpilih}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProgramStudiApp()
    window.show()
    sys.exit(app.exec_())
