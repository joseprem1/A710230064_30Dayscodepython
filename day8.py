def tanya_alamat():
    # Menanyakan nama
    nama = input("Siapa nama Anda? ")
    
    # Menanyakan alamat
    alamat = input(f"Halo {nama}, di mana alamat Anda? ")
    
    # Menampilkan alamat yang diberikan
    print(f"Terima kasih, {nama}. Alamat Anda adalah {alamat}.")

# Memanggil fungsi untuk menanyakan alamat
tanya_alamat()