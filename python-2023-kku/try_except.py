def main():
    try:
        file = open("dosya.txt","r")
        print(file.read())
    except Exception as e:
        print("Bir hata oluştu : ",e)
    finally:
        print("Finally bloğu çalıştı")

    # baska bir kullanim
    print("--------------------")

    try:
        file = open("dosya.txt","r")
        print(file.read())
    except ValueError:
        print("Bir hata oluştu : ")
    except FileNotFoundError:
        print("Dosya bulunamadı")
    except Exception as e:
        print("Bir hata oluştu : ",e)
    finally:
        print("Finally bloğu çalıştı")

main()