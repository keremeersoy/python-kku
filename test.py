def main():
  yemek = ["Pizza","Donut","Hamburger","Kebap","Kek","Makarna"]

  print("Yemekler: ",yemek)

  secilenYemek = input("Yemeklerden hangisini silmek istersiniz?")

  try:
    secilenYemekIndex = yemek.index(secilenYemek)

    yeniEklenenYemek = input("Yeni eklemek istediğiniz yemek: ")

    yemek[secilenYemekIndex] = yeniEklenenYemek

    print("Yeni yemekler: ",yemek)
  except ValueError:
    print("Yemek bulunamadı!")  

main()

