# Kamus untuk mengonversi ukuran sepatu
konversi_ukuran_sepatu = {
    "AS": {
        "Pria": {6: 39, 7: 40, 8: 41, 9: 42, 10: 43, 11: 44, 12: 45},
        "Wanita": {5: 35, 6: 36, 7: 37, 8: 38, 9: 39, 10: 40, 11: 41}
    },
    "UK": {
        "Pria": {5: 39, 6: 40, 7: 41, 8: 42, 9: 43, 10: 44, 11: 45},
        "Wanita": {3: 35, 4: 36, 5: 37, 6: 38, 7: 39, 8: 40, 9: 41}
    },
    "EU": {
        "Pria": {39: 39, 40: 40, 41: 41, 42: 42, 43: 43, 44: 44, 45: 45},
        "Wanita": {35: 35, 36: 36, 37: 37, 38: 38, 39: 39, 40: 40, 41: 41}
    }
}

def konversi_ukuran(size, negara, jenis_kelamin):
    try:
        if negara in konversi_ukuran_sepatu and jenis_kelamin in konversi_ukuran_sepatu[negara]:
            ukuran_indonesia = konversi_ukuran_sepatu[negara][jenis_kelamin][size]
            return ukuran_indonesia
        else:
            return "Konversi tidak tersedia untuk ukuran ini."
    except KeyError:
        return "Ukuran tidak ditemukan dalam data konversi."

# Input ukuran sepatu dan detail pembeli
ukuran = int(input("Masukkan ukuran sepatu (dalam satuan luar negeri): "))
negara = input("Masukkan negara (AS, UK, EU): ")
jenis_kelamin = input("Masukkan jenis kelamin (Pria/Wanita): ")

# Proses konversi dan tampilkan hasil
ukuran_indonesia = konversi_ukuran(ukuran, negara, jenis_kelamin)
print(f"Ukuran sepatu {ukuran} {negara} untuk {jenis_kelamin} setara dengan ukuran Indonesia {ukuran_indonesia}.")