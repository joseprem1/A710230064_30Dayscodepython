class Motor:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun

    def deskripsi(self):
        return f"Motor ini adalah {self.merk} {self.model} keluaran tahun {self.tahun}."

    def usia(self, tahun_sekarang):
        return tahun_sekarang - self.tahun

# Membuat objek dari class Motor
motor1 = Motor("Vario", "led old", 2017)
motor2 = Motor("Vario", "led new", 2020)

# Menggunakan method deskripsi untuk mendapatkan informasi motor
print(motor1.deskripsi())
print(motor2.deskripsi())

# Menghitung usia motor berdasarkan tahun sekarang
tahun_sekarang = 2024
print(f"Usia {motor1.merk} {motor1.model} adalah {motor1.usia(tahun_sekarang)} tahun.")
print(f"Usia {motor2.merk} {motor2.model} adalah {motor2.usia(tahun_sekarang)} tahun.")