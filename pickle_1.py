import pickle

# Veriyi oluşturalım
user_data = {'name': 'John', 'age': 25}

# Veriyi bir dat dosyasına yazalım
file = open('user_data.dat', 'wb')
pickle.dump(user_data, file)
file.close()

# Dat dosyasından veriyi okuyalım
file = open('user_data.dat', 'rb')
loaded_user_data = pickle.load(file)
file.close()

# Okunan veriyi ekrana yazdıralım
print("Loaded User Data:", loaded_user_data)