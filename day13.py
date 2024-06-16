def main():
    # Daftar harga tiket berdasarkan kategori
    harga_tiket = {
        "VVIP": 1500000,
        "VIP": 1000000,
        "Utara": 750000,
        "Selatan": 750000
    }

    print("Selamat datang di sistem pemesanan tiket bola!")
    print("Kategori tiket yang tersedia:")
    for kategori in harga_tiket:
        print(f"- {kategori} (Rp{harga_tiket[kategori]:,})")

    total_biaya = 0

    while True:
        # Memilih kategori tiket
        kategori = input("Masukkan kategori tiket yang ingin Anda beli (VVIP, VIP, Utara, Selatan) atau 'selesai' untuk mengakhiri: ")
        if kategori.lower() == 'selesai':
            break

        if kategori not in harga_tiket:
            print("Kategori tiket tidak valid. Silakan coba lagi.")
            continue

        # Memasukkan jumlah tiket yang ingin dibeli
        try:
            jumlah_tiket = int(input(f"Masukkan jumlah tiket {kategori} yang ingin dibeli: "))
            if jumlah_tiket <= 0:
                print("Jumlah tiket harus lebih dari 0. Silakan coba lagi.")
                continue
        except ValueError:
            print("Jumlah tiket harus berupa angka. Silakan coba lagi.")
            continue

        # Menghitung biaya untuk tiket yang dipilih
        biaya = harga_tiket[kategori] * jumlah_tiket
        total_biaya += biaya

        print(f"Anda telah memilih {jumlah_tiket} tiket kategori {kategori}. Total sementara: Rp{total_biaya:,}")

    print(f"Total biaya keseluruhan: Rp{total_biaya:,}")
    print("Terima kasih telah menggunakan sistem pemesanan tiket kami!")

if __name__ == "__main__":
    main()
