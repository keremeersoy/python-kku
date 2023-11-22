#kullanıcının dosya isimlerini gireceği iki farklı dosya içindeki sözcüklerden
#her iki dosyada yer alan benzersiz sözcükler
#her iki dosyada yer alan aynı sözcükler
#birinci dosyada olup ikinci dosyada olmayanlar
#ikinci dosyada olup birinci dosyada olmayanlar listeleyerek ekrana basan program


def main():
    kelimeler_1 = []
    kelimeler_2 = []

    dosya1_adi = input("1.dosya adını girin : ")
    dosya2_adi = input("2.dosya adını girin : ")

    dosya1 = open(dosya1_adi, "r")
    dosya2 = open(dosya2_adi, "r")

    ## dosyadan okuma ve diziye aktarma islemleri
    for line in dosya1:
        for word in line.split():
            kelimeler_1.append(word)

    for line in dosya2:
        for word in line.split():
            kelimeler_2.append(word)

    kume_1 = set(kelimeler_1)
    kume_2 = set(kelimeler_2)
    
    benzersiz_sozcukler = kume_1.union(kume_2)
    ayni_kelimeler = kume_1.intersection(kume_2)
    bir_diff_iki = kume_1.difference(kume_2)
    iki_diff_bir = kume_2.difference(kume_1)

    print("benzersiz_sozcukler", benzersiz_sozcukler)
    print("ayni_kelimeler", ayni_kelimeler)
    print("bir_diff_iki", bir_diff_iki)
    print("iki_diff_bir", iki_diff_bir)

main()

## HOCANIN ÇÖZÜMÜ

# def main():
#    name1=input("birinci dosyanın tam adını giriniz")
#    dosya1=open(name1,'r')
#    içerik1=dosya1.read()
#    dosya1.close()
#    kelimeler1=içerik1.split()

#    küme1=set(kelimeler1)

#    name2=input("ikinci dosyanın tam adını giriniz")
#    dosya2=open(name2,'r')
#    içerik2=dosya2.read()
#    dosya2.close()
#    kelimeler2=içerik2.split()

#    küme2=set(kelimeler2)

#    benzersiz = küme1.union(küme2)
#    print('benzersiz sözcükler')
#    for i in benzersiz:
#        print(i)

#    birleşim=küme1.intersection(küme2)
#    print ("birleşen sözcükler")
#    for i in birleşim:
#        print (i)

#    farkıa=küme1.difference(küme2)
#    print("a nın bden farkı")
#    for i in farkıa:
#        print(i)

#    farkıb=küme2.difference(küme1)
#    print("b nin a dan farkı")
#    for i in farkıb:
#        print(i)



# main()
