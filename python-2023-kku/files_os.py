def write_to_file(name,content):
    file = open(f"{name}.txt", "w")
    file.write(content)
    file.close()

    return file

def read_from_file(file):
    file = open(file, "r")
    content = file.readline()
    print("Content'in tamamı budur : ",content)
    file.close()


def main():

    file_name = input("Dosya adı girin : ")
    content = input("Dosyaya yazılacak içerik: ")
    
    file = write_to_file(file_name,content)
    read_from_file(file.name)    



main()