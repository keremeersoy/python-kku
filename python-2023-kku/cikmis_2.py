#öğrenciler için girilecek isim ,öğrenci numarası.not ortalaması verilerini sözlük bileşenleri olarak veriler dat dosyasına pickle ile yazan
#sonra aynı program içinde bu dosyadan okuduğu tüm sözlük verileini ekranayazdıran kod.Girilecek öğrenci sayısı belirsizdir.
import pickle

def main():
    veri_yaz()
    veri_oku()

def veri_yaz():
    devam_mi = "e"
    dosya = open("veriler.dat","wb")

    while devam_mi == "e":
        ogrenci = {}

        ogrenci["isim"] = input("ögrenci adini girin : ")
        ogrenci["ogr_no"] = int(input("ogr no girin : "))
        ogrenci["ortalama"] = int(input("ortalama girin : "))

        pickle.dump(ogrenci,dosya)

        devam_mi = input("ogrenci girmeye devam edecek misiniz ? (e/h)")
    
    dosya.close()

def veri_oku():
    dosya = open("veriler.dat","rb")
    
    try:
        while True:
            ogrenci = pickle.load(dosya)
            print("ogrenci bilgileri burada! \n",ogrenci)
    except EOFError:
        pass

    dosya.close()

main()

## HOCANIN ÇÖZDÜĞÜ

# import pickle

# def main():
#     tekrar = 'e'

#     try:

#         cikti_dosyasi = open('veriler.dat', 'wb')    
#         while tekrar.lower() == 'e':
#             veri_kaydet(cikti_dosyasi)
#             tekrar = input("Başka veri? (e/h): ")

#         cikti_dosyasi.close() #
#         print('Girilen veriler dosyaya yazıldı.\n')

#         print("Dosyadan okunan veriler aşağıda:")
#         okumadosyası = open("veriler.dat", "rb")  
#         dosyanin_sonu = False
#         while not dosyanin_sonu: 
#             try:
#                 ogrenci = pickle.load(okumadosyası) 

#                 veriyi_goster(ogrenci)   
#             except EOFError:             
#                 dosyanin_sonu = True

#         okumadosyası.close()

#     except FileNotFoundError:
#         print("Dosya bulunamadı.")

# def veri_kaydet(dosya):
#     ogrenci = {}
#     ogrenci['isim'] = input("İsim: ")
#     ogrenci['no'] = int(input("Öğrenci Numarası: "))
#     ogrenci['ortalama'] = float(input("Not Ortalaması: "))
#     pickle.dump(ogrenci, dosya)

# def veriyi_goster(ogrenci):
#     print("\nÖğrenci Bilgileri:")
#     print("İsim:", ogrenci['isim'])
#     print("Öğrenci Numarası:", ogrenci['no'])
#     print("Not Ortalaması:", ogrenci['ortalama'])

# if __name__ == "__main__":
#     main()