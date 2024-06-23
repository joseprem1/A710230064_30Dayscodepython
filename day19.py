# Fungsi untuk menghitung daya listrik
def hitung_daya(tegang, arus):
    return tegang * arus

# Meminta input dari pengguna
tegang = float(input("Masukkan tegangan (Volt): "))
arus = float(input("Masukkan arus (Ampere): "))

# Menghitung daya
daya = hitung_daya(tegang, arus)

# Menampilkan hasil
print(f"Daya listrik: {daya} Watt")