class Teh:
    def __init__(self, nama, asal, jenis_teh, profil_rasa):
        self.nama = nama
        self.asal = asal
        self.jenis_teh = jenis_teh
        self.profil_rasa = profil_rasa

    def menyeduh_teh(self, suhu, waktu):
        return f"Seduh {self.nama} pada suhu {suhu}°C selama {waktu} menit untuk rasa terbaik."

    def deskripsi_teh(self):
        return f"{self.nama} adalah teh {self.jenis_teh} dari {self.asal}. Rasanya {self.profil_rasa}."

# Contoh penggunaan
teh_hijau = Teh("Sencha", "Jepang", "Hijau", "seperti rumput dan manis")
teh_hitam = Teh("Assam", "India", "Hitam", "seperti malt dan kuat")

# Menyeduh teh
print(teh_hijau.menyeduh_teh(80, 2))
print(teh_hitam.menyeduh_teh(95, 4))

# Mendeskripsikan teh
print(teh_hijau.deskripsi_teh())
print(teh_hitam.deskripsi_teh())