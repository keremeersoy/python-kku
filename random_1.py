import random 

def get_random_number(start, end):
    return random.randint(start, end)

def main():
    randomNumber = get_random_number(1, 10)
    print("Random number: ", randomNumber)


main()