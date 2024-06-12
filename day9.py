def pangkat_empat(angka):
    hasil = angka ** 4
    return hasil

# Meminta pengguna untuk memasukkan angka
angka_input = float(input("Masukkan angka yang ingin dipangkatkan 4: "))

# Menghitung hasil pangkat 4
hasil = pangkat_empat(angka_input)

# Menampilkan hasil
print(f"Hasil dari {angka_input} dipangkatkan 4 adalah {hasil}")
