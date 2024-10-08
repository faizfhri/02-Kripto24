'''
    Nama : Muhammad Faiz Fahri
    NPM  : 140810220002
'''

def enkripsi_vigenere(pesan, kunci):
    cipherteks = ""
    kunci = perluas_kunci(pesan, kunci)  

    for i in range(len(pesan)):
        huruf_pesan = pesan[i]
        huruf_kunci = kunci[i]
        if huruf_pesan.isalpha():
            base = 'A' if huruf_pesan.isupper() else 'a'
            cipherteks += chr((ord(huruf_pesan) + ord(huruf_kunci) - 2 * ord(base)) % 26 + ord(base))
        else:
            cipherteks += huruf_pesan  
            
    return cipherteks

def dekripsi_vigenere(cipherteks, kunci):
    plainteks = ""
    kunci = perluas_kunci(cipherteks, kunci)

    for i in range(len(cipherteks)):
        huruf_cipher = cipherteks[i]
        huruf_kunci = kunci[i]
        if huruf_cipher.isalpha():
            base = 'A' if huruf_cipher.isupper() else 'a'
            plainteks += chr((ord(huruf_cipher) - ord(huruf_kunci) + 26) % 26 + ord(base))
        else:
            plainteks += huruf_cipher  
            
    return plainteks
def perluas_kunci(pesan, kunci):
    pesan_len = len(pesan)
    kunci_len = len(kunci)

    kunci_baru = kunci
    for i in range(pesan_len - kunci_len):
        kunci_baru += kunci[i % kunci_len]
    
    return kunci_baru

def main():
    while True:
        print("Menu:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        pilihan = int(input("Pilih opsi: "))

        if pilihan == 1:
            pesan = input("Masukkan pesan: ")
            kunci = input("Masukkan kunci: ")
            cipherteks = enkripsi_vigenere(pesan, kunci)
            print("Hasil enkripsi:", cipherteks)
        elif pilihan == 2:
            cipherteks = input("Masukkan cipherteks: ")
            kunci = input("Masukkan kunci: ")
            plainteks = dekripsi_vigenere(cipherteks, kunci)
            print("Hasil dekripsi:", plainteks)
        elif pilihan == 3:
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()