import login
import os
import time

list_pupuk = {
    1: {"nama": "Pupuk SP36 Subsidi 50 kg", "harga": 120000},
    2: {"nama": "Pupuk Urea Subsidi 50 kg", "harga": 112500},
    3: {"nama": "Pupuk ZA Subsidi 50 kg", "harga": 285000},
    4: {"nama": "Pupuk SP36 Non-Subsidi 50 kg", "harga": 250000},
    5: {"nama": "Pupuk Urea Non-Subsidi 50 kg ","harga": 248000},
    6: {"nama": "Pupuk KCL Non-Subsidi 50 kg","harga":850000},
    7: {"nama": "Pupuk ZA Non-Subsidi 50 kg","harga":300000},
    8: {"nama": "Pupuk Furadan Non-Subsidi 50 kg","harga":175000},
    9: {"nama": "Pupuk Phonska Non-Subsidi 50 kg","harga":250000},
}

daftar_pesanan = {}

def heading():
    print("P U P U K . G O".center(51))
    print("Petani Maju Petani Sejahtera".center(51))
    print("="*51)

def clear():
    os.system("cls")

def kembali():
    kembali = input("klik 'ENTER' untuk kembali")
    menu_tanaman()
    print(kembali)

def menu_utama():
    while True:
        heading()
        print("MENU".center(51))
        print("-"*51)
        print("1. Informasi Tumbuhan\n")
        print("2. Pesan Pupuk\n")
        print("3. Update Pemesanan\n")
        print("4. Delete Pemesanan\n")
        print("5. Daftar Pesanan\n")
        print("6. Struk Pembelian")
        print("-"*51)
        menu = input("Ketik angka untuk memilih\t:")
        if menu == "1":
            menu_tanaman()
        elif menu == "2":
            pesan()
        elif menu == "3":
            update_pesanan()
        elif menu == "4":
            delete_pesanan()
        elif menu == "5":
            print_total_pesanan()
        elif menu == "6":
            struk()
            break
        else:
            print("")

def menu_tanaman():
    clear()
    heading()
    print("Pilih Tanaman".center(51))
    print("-"*51)

    print("\n1. Padi\n")
    print("2. Jagung\n")
    print("3. Kembali")
    print("-"*51)

    pilih_1 = input("\nKetik angka untuk memilih Tanaman: ")
    if pilih_1 == "1":
        inform_1 = open("infotanaman.txt")
        inform_2 = inform_1.readlines()[1:56]
        for a in inform_2:
            print(a)
        print("Rekomendasi Pupuk".center(51))
        inform_3 = open("hargapupuk.txt")
        inform_4 = inform_3.readlines()[2:11]
        for b in inform_4:
            print(b)
        kembali()
    elif pilih_1 == "2":
        inform_5 = open("infotanaman.txt")
        inform_6 = inform_5.readlines()[56:121]
        for c in inform_6:
            print(c, end="")
        print("Rekomendasi Pupuk".center(51))
        inform_3 = open("hargapupuk.txt")
        inform_4 = inform_3.readlines()[15:27]
        for b in inform_4:
            print(b)
        kembali()
    elif pilih_1 == "3":
        menu_utama()
    else:
        print("Maaf Data tidak ditemukan")
        kembali()
 

def pesan():
    clear()
    heading()
    print_pupuk()
    pilihan_pupuk = int(input("Pilih pupuk: "))
 
    id = len(daftar_pesanan) + 1
    daftar_pesanan[id] = list_pupuk[pilihan_pupuk]
    print("Pesanan anda berhasil")
    time.sleep(2)
 
def update_pesanan():
    clear()
    heading()
    
    print_pesanan()
    pilihan_pesanan = int(input("Pilih nomor pesanan yang ingin diupdate: "))
    
    print("Pupuk".center(51))
    print("-"*51)
    for pupuk in list_pupuk:
        print(str(pupuk) + ". Nama: " + list_pupuk[pupuk]['nama'] + '. Harga: ' + str(list_pupuk[pupuk]['harga']))
    pilihan_pupuk = int(input("Pilih pupuk: "))
 
    daftar_pesanan[pilihan_pesanan] = list_pupuk[pilihan_pupuk]
    print("Pesanan Berhasil Diubah!")
    time.sleep(2)


def delete_pesanan():
    clear()
    
    print_pesanan()
    
    pilihan_pesanan = int(input("Pilih nomor pesanan yang ingin dihapus: "))
    del daftar_pesanan[pilihan_pesanan]
    print("Pesanan anda berhasil dihapus")
    print("\n\n")
    
def print_total_pesanan():
    print_pesanan()

    total = 0
    for pesanan in daftar_pesanan:
        total += daftar_pesanan[pesanan]['harga']
    print("Total: " + str(total))
    print("\n\n")
    
def print_pesanan():
    print("\n")
    print("Daftar Pesanan".center(51))
    print("-"*51)
    for pesanan in daftar_pesanan:
        print(str(pesanan) + ". Nama: " + daftar_pesanan[pesanan]['nama'] + '. Harga: ' + str(daftar_pesanan[pesanan]['harga']))
    print("\n\n")
    
def print_pupuk():
    print("\n")
    print("Pupuk".center(51))
    print("-"*51)
    for pupuk in list_pupuk:
        print(str(pupuk) + ". Nama: " + list_pupuk[pupuk]['nama'] + '. Harga: ' + str(list_pupuk[pupuk]['harga']))
    print("\n\n")

def struk():
    clear()
    heading()
    print("S T R U K".center(51))
    print("-"*51)
    nama   =     input("Masukan Nama             : ")
    no     = int(input("Masukan No.telp          : "))
    alamat =     input("Masukan Alamat           : ")
    clear()
    print             (f"Nama Pembeli            : {nama}\n")
    print             (f"No.Telp                 : {no}\n")
    print             (f"alamat                  : {alamat}")
    print_total_pesanan()
    print("\n"+"-"*51)
    print("Terima Kasih Telah Menggunakan Program Kami".center(51))


login
menu_utama()

