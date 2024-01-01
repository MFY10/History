# -*- coding: utf-8 -*-
"""5_UTPSDA_D

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/180DXSJwgoZB2x70h1WNBcCvHSePQlMV1
"""

class data_Karyawan:
    def __init__(self, nama, jabatan, gaji, umur, alamat):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji
        self.umur = umur
        self.alamat = alamat
    
    def tampilkan_data(self):
        print("Nama    :", self.nama)
        print("Jabatan :", self.jabatan)
        print("Gaji    :", self.gaji)
        print("Umur    :",self.umur)
        print("alamat  :",self.alamat)

username = ["Atna", "Aldo", "Dafreeze"]
password = ["a", "aturlahbang", "dinging"]
log = False
daftar_karyawan = []

def menu():
  print(" Selamat datang di Program Kita")
  print("================================")
  print("Pilihlah menu di bawah ini!")
  print("1. Login")
  print("2. Register")
  tmp_temp = int(input("Pilihan anda : "))
  if tmp_temp == 1:
    print()
    login()
  elif tmp_temp == 2 :
    print()
    register()
  else :
    print("Anda keluar dari Program!")
    exit()

def login():
  coba = True
  c_coba = 0
  while coba != False :
    username_temp = input("Username   : ")
    password_temp = input("Password   : ")
    if username_temp in username and password_temp == password[username.index(username_temp)] :
      print("Login Berhasil!")
      print("Selamat datang {}!".format(username_temp))
      print()
      log = True
      coba = True
      main_menu()
      break
    else :
      c_coba += 1
      if c_coba == 3:
        print("Anda sudah mencoba 3 kali!")
        coba = False
        print()
        menu()
        break
      elif username_temp not in username :
        print("Username Tidak ditemukan!")
        print()
      elif password_temp != password[username.index(username_temp)] :
        print("Password salah!")
        print()

def register():
  done = False
  d_done = 0
  while done != True :
    username_temp_2 = input("Username                 : ")
    password_temp_2 = input("Password                 : ")
    password_cek_temp = input("Konfirmasi Password      : ")
    if username_temp_2 in username :
      print("Username  {} Sudah terdaftar!".format(username_temp_2))
      d_done+=1
      print()
    elif password_cek_temp != password_temp_2 :
      d_done+=1
      print("Password tidak sama!")
      print()
    else :
      print("Selamat {} Telah Terdaftar!".format(username_temp_2))
      print()
      done = True
      username.append(username_temp_2)
      password.append(password_temp_2)
      menu()
      break

def main_menu():
  jumlah_karyawan = int(input("Masukkan jumlah karyawan  : "))
  for i in range(jumlah_karyawan):
     print("==========================================")
     nama = input("Masukkan nama karyawan    : ")
     jabatan = input("Masukkan jabatan karyawan : ")
     gaji = int(input("Masukkan gaji karyawan    : "))
     umur = int(input("Masukkan umur karyawan    : "))
     alamat = input("Masukkan alamat karyawan  : ")

     karyawan = data_Karyawan(nama, jabatan, gaji, umur, alamat)
     daftar_karyawan.append(karyawan)

  print("Daftar Karyawan")
  for karyawan in daftar_karyawan:
     print("==========================================")
     karyawan.tampilkan_data()
     print("==========================================")


menu()