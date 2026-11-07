import os

def ekrani_temizle():
 # Windows için 'cls', Mac/Linux için 'clear' komutunu çalıştırır
 os.system('cls' if os.name == 'nt' else 'clear')

while True:
 print("1 - Load Cheat")
 print("2 - Steps")
 
 secim = input("1/2? ")
 
 if secim == "1":
 ekrani_temizle() # Önceki menüyü temizler
 print("""
 @@@
 @@@@@
 @@@@@
 @@@@@
 @@@@@
 @@@@@
 @@@@@ @@@@@
 @@@@@@ @@@@@@
 @@@@@@ @@@@@""")
 # Şekil çıktıktan sonra kullanıcı bir şeye basıp Enter yapana kadar bekler
 input("\nMenüye dönmek için Enter'a basın...")
 ekrani_temizle() # Şekli siler ve döngü sayesinde kod en başa döner
 
 elif secim == "2":
 ekrani_temizle() # Önceki ekranı siler
 print("TT:kntQREST")
 print("instagram:Ahmet.cetin416")
 input("\nMenüye dönmek için Enter'a basın...")
 ekrani_temizle() # Bilgileri siler ve en başa döner
 
 else:
 ekrani_temizle()
 print("Geçersiz seçim! Lütfen 1 veya 2 yazın.\n")
Bunu github dan apk yapabilirmiyim
