def tambah(angka1, angka2):
    return angka1 + angka2

def bagi(angka1, angka2):
    if angka2 == 0:
        return "Tidak bisa membagi dengan nol!"
    else:
        return angka1 / angka2

def kalkulator():
    print("Pilih operasi:")
    print("1. Penambahan")
    print("2. Pembagian")
    
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan in ('1', '2'):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")

        elif pilihan == '2':
            hasil = bagi(angka1, angka2)
            if isinstance(hasil, str):
                print(hasil)
            else:
                print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Memanggil fungsi kalkulator
kalkulator()