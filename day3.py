import math

def hitung_luas_dan_diameter_persegi(sisi):
    # Menghitung luas persegi
    luas = sisi ** 2
    
    # Menghitung diameter (diagonal) persegi
    diameter = sisi * math.sqrt(2)
    
    return luas, diameter

# Contoh penggunaan
sisi = float(input("Masukkan panjang sisi persegi: "))
luas, diameter = hitung_luas_dan_diameter_persegi(sisi)

print(f"Luas persegi: {luas}")
print(f"Diameter (diagonal) persegi: {diameter}")