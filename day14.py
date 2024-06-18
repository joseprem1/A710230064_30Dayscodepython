class Motor:
    def __init__(self, merk, model, harga):
        self.merk = merk
        self.model = model
        self.harga = harga

class NotaPenjualan:
    def __init__(self, nama_pembeli, motor, tanggal, jumlah):
        self.nama_pembeli = nama_pembeli
        self.motor = motor
        self.tanggal = tanggal
        self.jumlah = jumlah
        self.total_harga = self.hitung_total_harga()

    def hitung_total_harga(self):
        return self.motor.harga * self.jumlah

    def cetak_nota(self):
        print("=== Nota Penjualan ===")
        print(f"Nama Pembeli  : {self.nama_pembeli}")
        print(f"Motor         : {self.motor.merk} {self.motor.model}")
        print(f"Harga Satuan  : Rp{self.motor.harga:,.2f}")
        print(f"Jumlah        : {self.jumlah}")
        print(f"Tanggal       : {self.tanggal}")
        print("------------------------")
        print(f"Total Harga   : Rp{self.total_harga:,.2f}")
        print("========================")

# Data contoh
motor1 = Motor("Honda", "CBR 150R", 35000000)

# Input dari pengguna
nama_pembeli = input("Masukkan nama pembeli: ")
tanggal = input("Masukkan tanggal penjualan (dd-mm-yyyy): ")
jumlah = int(input("Masukkan jumlah motor yang dibeli: "))

# Membuat objek NotaPenjualan
nota = NotaPenjualan(nama_pembeli, motor1, tanggal, jumlah)

# Mencetak nota penjualan
nota.cetak_nota()