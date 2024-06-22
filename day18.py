# Daftar buah-buahan
daftar_buah = ['apel', 'jeruk', 'mangga', 'pisang', 'anggur', 'nanas', 'semangka', 'pepaya', 'melon']

def cari_buah(nama_buah, daftar):
    if nama_buah in daftar:
        return f'{nama_buah} ditemukan dalam daftar.'
    else:
        return f'{nama_buah} tidak ditemukan dalam daftar.'

# Input dari pengguna
nama_buah_dicari = input('Masukkan nama buah yang ingin dicari: ').lower()

# Pencarian buah
hasil = cari_buah(nama_buah_dicari, daftar_buah)
print(hasil)