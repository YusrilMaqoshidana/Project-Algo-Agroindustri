import hashlib
import os
import time

def heading():
    print("P U P U K . G O".center(51))
    print("Petani Maju Petani Sejahtera".center(51))
    print("="*51)

def clear():
    os.system("cls")

# Fungsi untuk meng-hash password menggunakan enkripsi MD5
def hash_password(password):
  return hashlib.md5(password.encode()).hexdigest()

# Fungsi untuk mendaftarkan user baru
def register():
  clear()
  heading()
  print('register'.center(51))
  print("-"*51)
  username = input("Masukkan username   : ")
  password = input("Masukkan password   : ")
  print("-"*51)

  enkripsi_password = hash_password(password)

  # Menambahkan data user baru ke file
  with open("users.txt", "a") as file:
    file.write(username + "," + enkripsi_password + "\n")

  print("Pendaftaran berhasil! Silakan login.")
  time.sleep(2)
  mulai()

# Fungsi untuk login
def login():
  clear()
  heading()
  print('login'.center(51))
  print("-"*51)
  username = input("Masukkan username   : ")
  password = input("Masukkan password   : ")
  print("-"*51)
  time.sleep(1)

  enkripsi_password = hash_password(password)

  # Membaca data user dari file
  with open("users.txt", "r") as file:
    for line in file:
      data = line.strip().split(",")

      if data[0] == username and data[1] == enkripsi_password:
        print("Login berhasil! Selamat datang, " + username + ".")
        time.sleep(2)
        return

  print("Username atau password salah. Silakan coba lagi.")
  kesempatan = 1
  while kesempatan < 3:
    password = input("Masukkan password   : ")
    enkripsi_password = hash_password(password)
    if data[1] == enkripsi_password:
      print("Login berhasil! Selamat datang, " + username + ".")
      time.sleep(2)
      return
    else:
      print("Username atau password salah. Silakan coba lagi.")
      kesempatan += 1


  print("Anda telah salah 3 kali. Silahkan anda registrasi")
  time.sleep(2)
  mulai()


def mulai():
    clear()
    heading()
    print("1. Register\n")
    print("2. Login")
    print("="*51)
    option = input("\nKetik angka untuk memilih   : ")
    if option == "1":
        register()
        time.sleep(1)
    elif option == "2":
        login()
        time.sleep(1)
    else:
        mulai()



mulai()

