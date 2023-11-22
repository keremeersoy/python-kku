def get_splited_name(full_name):
    first_name = full_name.split()[0]
    last_name = full_name.split()[1]
    return first_name, last_name

def main():
    first_name,last_name = get_splited_name("John Doe")

    print("First name:", first_name)
    print("Last name:", last_name)


main()