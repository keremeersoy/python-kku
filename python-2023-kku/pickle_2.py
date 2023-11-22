import pickle

veri1 = {'ad': 'Ahmet', 'yaş': 25, 'şehir': 'İstanbul'} #SÖZLÜK
veri2 = [1, 2, 3, 4, 5] #LİSTE
veri3_kume = {10, 20, 30, 40, 50} #KÜME

# Dosyayı ikili yazma modunda açma
dosyamAç = open('kaydedilmis_veriler.dat', 'wb')

# Verileri pickle etmek ve dosyaya yazmak
pickle.dump(veri1, dosyamAç)
pickle.dump(veri2, dosyamAç)
pickle.dump(veri3_kume, dosyamAç)

# Dosyayı kapatma
dosyamAç.close()

# Dosyayı ikili okuma modunda açma
dosyam_okuma = open('kaydedilmis_veriler.dat', 'rb')

# Verileri dosyadan yükleme
oku_veri1 = pickle.load(dosyam_okuma)
oku_veri2 = pickle.load(dosyam_okuma)
oku_veri3_kume = pickle.load(dosyam_okuma)

# Dosyayı kapatma
dosyam_okuma.close()

# Okunan verileri ekrana yazdırma
print("Veri 1:", oku_veri1)
print("Veri 2:", oku_veri2)
print("Veri 3 (küme):", oku_veri3_kume)
