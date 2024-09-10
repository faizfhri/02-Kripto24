/*
    Nama : Muhammad Faiz Fahri
    NPM  : 140810220002
*/

#include <iostream>
#include <string>
using namespace std;

string encrypt(string text, int shift) {
    string result = "";

    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        if (isupper(ch)) {
            result += char(int(ch + shift - 65) % 26 + 65);
        }
        else if (islower(ch)) {
            result += char(int(ch + shift - 97) % 26 + 97);
        }
        else {
            result += ch;
        }
    }

    return result;
}

string decrypt(string text, int shift) {
    return encrypt(text, 26 - shift); 
}

void program() {
    int pilih;
    cout << "============================" << endl;
    cout << "|    Program Shift Cipher   |" << endl;
    cout << "| 1. Enkripsi               |" << endl;
    cout << "| 2. Dekripsi               |" << endl;
    cout << "| 3. Exit                   |" << endl;
    cout << "============================" << endl;
    cout << "Pilih: ";
    cin >> pilih;

    string text;
    int shift;

    switch (pilih) {
        case 1:
            cout << "Masukkan teks yang ingin dienkripsi: ";
            cin.ignore(); 
            getline(cin, text);
            cout << "Masukkan pergeseran (shift): ";
            cin >> shift;
            cout << "Teks terenkripsi: " << encrypt(text, shift) << endl;
            break;
        case 2:
            cout << "Masukkan teks yang ingin didekripsi: ";
            cin.ignore(); 
            getline(cin, text);
            cout << "Masukkan pergeseran (shift): ";
            cin >> shift;
            cout << "Teks terdekripsi: " << decrypt(text, shift) << endl;
            break;
        case 3:
            cout << "Keluar dari program." << endl;
            exit(0);
        default:
            cout << "Pilihan tidak valid!" << endl;
    }
}

int main() {
    bool loop = true;
    while (loop) {
        program();
    }
    return 0;
}
