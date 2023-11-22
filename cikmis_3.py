#içinde her bir satırda kelimeler bulunan ve program çalışmadan önce var olan kaynak.txt dosyasında yer alan her bir kelimeyi ve
#kaynak.txt dosyası içinde bulunduğu satır numaralarını program çalışması sonucu oluşacak analiz.txt dosyasına alt alta yazdıran program,
#sözlükler(dictionary) kullanarak yazınız. program çalıştıktan sonra ekrandaa çıktı göstermeyecektir.

# kaynak.txt su sekilde olacak:
# nesne yönelimli programlama
# bu sinav bir ara sinav
# bu soru guzel bir soru
# sinav suresi bir saat otuz dakika
# bu soru dikkatli cozulmeli

# analiz.txt su sekilde olacak:
# nesne 1
# yönelimli 1
# programlama 1
# bu 2 3 5
# sinav 2 4
# bir 2 3 4
# ara 2
# soru 3 5
# guzel 3
# sinav 4
# saat 4
# otuz 4
# dakika 4
# dikkatli 5
# cozulmeli 5

def main():
    kaynak_dosya = open("kaynak.txt", "r")
    analiz_dosya = open("analiz.txt", "w")

    kelimeler_ve_satirlar = {}

    satir_no = 1
    for line in kaynak_dosya:
        for word in line.split():
            if word in kelimeler_ve_satirlar:
                kelimeler_ve_satirlar[word].append(satir_no)
            else:
                kelimeler_ve_satirlar[word] = [satir_no]
        satir_no += 1

    for kelime in kelimeler_ve_satirlar:
        satir_bilgisi = ""
        for satir in kelimeler_ve_satirlar[kelime]:
            satir_bilgisi += str(satir) + " "

        analiz_dosya.write(kelime + " " + satir_bilgisi + "\n")

    kaynak_dosya.close()
    analiz_dosya.close()

main()

## HOCANIN ÇÖZÜMÜ

# def main():
#     dosyaoku = open("kaynak.txt", "r")

#     sozluk = {}

#     okunan_satir = dosyaoku.readline()

#     satir_sayisi = 0

#     while okunan_satir != "":
#         okunan_satir = okunan_satir.rstrip("\n")

#         kelimeler = okunan_satir.split()

#         satir_sayisi += 1

#         for kelime in kelimeler:
#             if kelime in sozluk:
#                 sozluk[kelime] = sozluk[kelime] + str(satir_sayisi) + " "
#             else:
#                 sozluk[kelime] = str(satir_sayisi) + " "

#         okunan_satir = dosyaoku.readline()

#     dosyaoku.close()

#     dosyayaz = open("analiz.txt", "w")
#     for kelime, satirlar in sozluk.items():
#         dosyayaz.write(f"{kelime}: {satirlar}\n")

#     dosyayaz.close()

# if __name__ == "__main__":
#     main()