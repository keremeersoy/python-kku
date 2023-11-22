# Bu program, bilgi.dat dosyasından alınan pickled (serileştirilmiş) nesneleri unpickle (serileştirilmemiş) hale getirerek ekrana yazdıran bir programdır.

import pickle

def main():
    end_of_file = False
    
    input_file = open('info.dat', 'rb')

    while not end_of_file:
        try:
            person = pickle.load(input_file)
            
            display_data(person)
        except EOFError:
            end_of_file = True

    input_file.close()

def display_data(person):
    print('Ad:', person['ad'])
    print('Yaş:', person['yas'])
    print('Kilo:', person['kilo'])
    print()

if __name__ == '__main__':
    main()
