'''
    Nama : Muhammad Faiz Fahri
    NPM  : 140810220002
'''

import numpy as np

def huruf_ke_angka(huruf):
    return ord(huruf.upper()) - ord('A')

def angka_ke_huruf(angka):
    return chr(angka + ord('A'))

# Menghitung invers dari matriks modulo 26 (hanya untuk matriks 2x2)
def invers_modulo(kunci, mod):
    determinan = int(np.linalg.det(kunci))  
    determinan = determinan % mod  

    # Mencari invers dari determinan dengan modulo
    invers_determinan = None
    for i in range(1, mod):
        if (determinan * i) % mod == 1:
            invers_determinan = i
            break

    if invers_determinan is None:
        raise ValueError("Determinant tidak memiliki invers modulo.")

    # Menghitung adjugate dari matriks
    adjugate = np.array([[kunci[1][1], -kunci[0][1]], [-kunci[1][0], kunci[0][0]]])

    # Menghitung invers matriks kunci
    invers = (invers_determinan * adjugate) % mod
    return invers.astype(int)

def enkripsi_hill(pesan, kunci):
    n = kunci.shape[0]
    pesan = pesan.upper().replace(" ", "")
    
    # Menambakan padding 'X' jika panjang pesan tidak sesuai dengan ukuran matriks kunci
    while len(pesan) % n != 0:
        pesan += 'X'

    hasil = ""
    for i in range(0, len(pesan), n):
        blok = np.array([huruf_ke_angka(pesan[j]) for j in range(i, i + n)])
        blok_enkripsi = np.dot(kunci, blok) % 26
        hasil += ''.join([angka_ke_huruf(x) for x in blok_enkripsi])
    return hasil

def dekripsi_hill(pesan, kunci):
    n = kunci.shape[0]
    invers_kunci = invers_modulo(kunci, 26)

    hasil = ""
    for i in range(0, len(pesan), n):
        blok = np.array([huruf_ke_angka(pesan[j]) for j in range(i, i + n)])
        blok_dekripsi = np.dot(invers_kunci, blok) % 26
        hasil += ''.join([angka_ke_huruf(x) for x in blok_dekripsi])
    return hasil

def cari_kunci_dari_plainteks_dan_cipherteks(plainteks, cipherteks):
    if len(plainteks) != 4 or len(cipherteks) != 4:
        raise ValueError("Plainteks dan cipherteks harus memiliki panjang 4 huruf.")
    
    # Konversi plainteks dan cipherteks menjadi matriks 2x2
    plaintext_matrix = np.array([
        [huruf_ke_angka(plainteks[0]), huruf_ke_angka(plainteks[1])],
        [huruf_ke_angka(plainteks[2]), huruf_ke_angka(plainteks[3])]
    ])
    
    ciphertext_matrix = np.array([
        [huruf_ke_angka(cipherteks[0]), huruf_ke_angka(cipherteks[1])],
        [huruf_ke_angka(cipherteks[2]), huruf_ke_angka(cipherteks[3])]
    ])
    
    # Cari invers dari matriks plainteks
    try:
        invers_plaintext_matrix = invers_modulo(plaintext_matrix, 26)
    except ValueError as e:
        print(f"Error: {e}")
        return None

    # Hitung matriks kunci
    kunci = np.dot(ciphertext_matrix, invers_plaintext_matrix) % 26
    return kunci.astype(int)

def tampilkan_kunci(kunci):
    for baris in kunci:
        print(" ".join(map(str, baris)))

def menu():
    while True:
        print("\nMenu:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Cari Kunci Hill Cipher")
        print("4. Keluar")
        pilihan = int(input("Pilih opsi: "))

        if pilihan == 1:
            pesan = input("Masukkan pesan: ").strip()
            kunci = []
            print("Masukkan matriks kunci 2x2 (4 angka):")
            for i in range(2):
                baris = list(map(int, input().split()))
                kunci.append(baris)
            kunci = np.array(kunci)
            print(f"Pesan terenkripsi: {enkripsi_hill(pesan, kunci)}")

        elif pilihan == 2:
            pesan = input("Masukkan pesan terenkripsi: ").strip()
            kunci = []
            print("Masukkan matriks kunci 2x2 (4 angka):")
            for i in range(2):
                baris = list(map(int, input().split()))
                kunci.append(baris)
            kunci = np.array(kunci)
            try:
                print(f"Pesan terdekripsi: {dekripsi_hill(pesan, kunci)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif pilihan == 3:
            plainteks = input("Masukkan plainteks (4 huruf): ").strip()
            cipherteks = input("Masukkan cipherteks (4 huruf): ").strip()
            kunci = cari_kunci_dari_plainteks_dan_cipherteks(plainteks, cipherteks)
            if kunci is not None:
                print("Kunci Hill Cipher yang ditemukan:")
                tampilkan_kunci(kunci)

        elif pilihan == 4:
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()
