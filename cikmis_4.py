#kullanıcının kişiler için gireceği isim,kilo,boy bilgilerini sözlük bileşenleri olarak bilgiler.dat dosyasına pickle ile yazan,
#sonrasında da aynı program içinde bilgiler.dat dosyasından okuduğu tüm sözlük verilerini ekrana yazdıran programı yaz.

import pickle

def main():
    dosya = open("bilgiler.dat","wb")

    devam_mi = "e"

    while devam_mi.lower() == "e":
        kisi = {}

        kisi["isim"] = input("isim giriniz : ")
        kisi["kilo"] = int(input("kilo giriniz : "))
        kisi["boy"] = float(input("boy giriniz : "))

        pickle.dump(kisi,dosya)

        devam_mi = input("kisi girmeye devam edecek misiniz ? (e/h)")

    dosya.close()

    okuma_dosya = open("bilgiler.dat","rb")
    satir_sonu = False

    try:
        while satir_sonu == False:
            kisi = pickle.load(okuma_dosya)
            print("isim : ",kisi["isim"])
            print("kilo : ",kisi["kilo"])
            print("boy : ", kisi["boy"])
            print("\n")
    except EOFError:
        satir_sonu = True

    okuma_dosya.close()

main()

## HOCANIN ÇÖZÜMÜ


