# Daftar mahasiswa sebagai list of dictionaries
mahasiswa = [
    {
        "nama": "Jose",
        "usia": 20,
        "jurusan": "Pendidikan Teknik Informatika"
    },
    {
        "nama": "Aji",
        "usia": 19,
        "jurusan": "Pendidikan Teknik Informatika"
    },
    {
        "nama": "Budi",
        "usia": 19,
        "jurusan": "Teknik Elektro"
    }
]

# Fungsi untuk mencetak informasi mahasiswa
def cetak_informasi(mahasiswa_list):
    for mhs in mahasiswa_list:
        print(f"Nama: {mhs['nama']}")
        print(f"Usia: {mhs['usia']}")
        print(f"Jurusan: {mhs['jurusan']}")
        print("-" * 20)

# Memanggil fungsi untuk mencetak informasi mahasiswa
cetak_informasi(mahasiswa)