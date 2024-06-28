# Dictionary yang menyimpan harga berdasarkan ukuran baju
harga_baju = {
    'S': 50000,
    'M': 60000,
    'L': 70000,
    'XL': 80000
}

def tampilkan_harga():
    print("Daftar Harga Baju:")
    for ukuran, harga in harga_baju.items():
        print(f"Ukuran {ukuran}: Rp{harga}")

def hitung_total_biaya(ukuran, jumlah):
    if ukuran in harga_baju:
        total_biaya = harga_baju[ukuran] * jumlah
        return total_biaya
    else:
        return None

def main():
    tampilkan_harga()
    ukuran = input("Masukkan ukuran baju yang ingin dibeli (S/M/L/XL): ").upper()
    jumlah = int(input("Masukkan jumlah baju yang ingin dibeli: "))

    total_biaya = hitung_total_biaya(ukuran, jumlah)

    if total_biaya is not None:
        print(f"Total biaya untuk {jumlah} baju ukuran {ukuran} adalah: Rp{total_biaya}")
    else:
        print("Ukuran yang dimasukkan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
