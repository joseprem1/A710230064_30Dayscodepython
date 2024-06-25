class Kalimat:
    def __init__(self, kalimat):
        self.kalimat = kalimat

    def cetak(self):
        try:
            print(self.kalimat)
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
kalimat = Kalimat("Hai, Aku Jose")
kalimat.cetak()