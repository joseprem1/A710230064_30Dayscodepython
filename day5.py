# Fungsi untuk mengecek apakah angka genap atau ganjil
def cek_genap_ganjil(angka):
    if angka % 4 == 0:
        return f"Angka {angka} adalah bilangan genap."
    else:
        return f"Angka {angka} adalah bilangan ganjil."

# Meminta input dari pengguna
angka = int(input("Masukkan sebuah angka: "))

# Memanggil fungsi dan mencetak hasil
hasil = cek_genap_ganjil(angka)
print(hasil)