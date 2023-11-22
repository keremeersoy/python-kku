import pickle 

def main():
    tekrar = "e"

    cikti_dosyasi = open("bilgi.dat","wb")

    while tekrar.lower() == "e":
        veri_kaydet(cikti_dosyasi)

        tekrar = input("Tekrar veri girmek ister misiniz? (e/h) : ")
    
    cikti_dosyasi.close()

    dosya_oku("bilgi.dat")

def veri_kaydet(dosya):
    kisi= {}

    kisi["ad"] = input("Adınızı girin : ")
    kisi["soyad"] = input("Soyadınızı girin : ")
    kisi["yas"] = int(input("Yaşınızı girin : "))


    pickle.dump(kisi,dosya)

def dosya_oku(dosya_adi):
    dosya = open(dosya_adi, "rb")

    users= []
    
    try:
        while True:
            loaded_data = pickle.load(dosya)

            users.append(loaded_data)
            print("Okunan data:", loaded_data)
    except EOFError:
        pass  # End of file reached

    print("Okunan veriler : ",users)
    dosya.close()


main()