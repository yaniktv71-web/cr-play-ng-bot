import os
import time

def ekrani_temizle():
    # Android'de çökme yapmaması için kontrol ekledik
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass

while True:
    print("1 - Load Cheat")
    print("2 - Steps")
    
    secim = input("1/2? ")
    
    if secim == "1":
        ekrani_temizle()
        print("""
      @@@
     @@@@@
     @@@@@
     @@@@@
     @@@@@
     @@@@@
  @@@@@ @@@@@
 @@@@@@  @@@@@@
  @@@@@ @@@@@""")
        input("\nMenüye dönmek için Enter'a basın...")
        ekrani_temizle()
        
    elif secim == "2":
        ekrani_temizle()
        print("TT:kntQREST")
        print("instagram:Ahmet.cetin416")
        input("\nMenüye dönmek için Enter'a basın...")
        ekrani_temizle()
        
    else:
        ekrani_temizle()
        print("Geçersiz seçim! Lütfen 1 veya 2 yazın.\n")
