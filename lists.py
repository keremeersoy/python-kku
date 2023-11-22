def main():
    # List
    list = ["John", "Doe", 1990, 1.80, True]
    print("List: ", list)

    # List length -> len( list )
    print("List length: ", len(list))

    # List index -> list[ index ]
    print("List index 0: ", list[0])
    print("List index 1: ", list[1])
    print("List index 2: ", list[2])
    print("List index 3: ", list[3])
    print("List index 4: ", list[4])

    # List index out of range
    # print("List index 5: ", list[5])

    # List index negative
    print("List index -1: ", list[-1])
    print("List index -2: ", list[-2])
    print("List index -3: ", list[-3])
    print("List index -4: ", list[-4])
    print("List index -5: ", list[-5])

    # List index negative out of range
    # print("List index -6: ", list[-6])

    # List index range -> list[ start : end ]
    print("List index range 0:2: ", list[0:2])
    print("List index range 2:4: ", list[2:4])
    print("List index range 0:4: ", list[0:4])
    print("List index range 0:5: ", list[0:5])
    print("List index range 0:6: ", list[0:6])


    # List index range negative -> list[ start : end ]
    print("List index range -2:-1: ", list[-2:-1])
    print("List index range -3:-1: ", list[-3:-1])
    print("List index range -4:-1: ", list[-4:-1])
    print("List index range -5:-1: ", list[-5:-1])
    print("List index range -6:-1: ", list[-6:-1])

    # ------------------------------
    list1 = ["Ford", "BMW", "Volvo"]
    list2 = ["Toyota", "Renault", "Fiat"]

    # concat list
    list3 = list1 + list2
    print("List concat: ", list3)

    # List append -> list.append( item )
    list1.append("Honda")
    print("List append: ", list1)

    # List insert -> list.insert( index, item )
    list1.insert(1, "Honda")
    print("List insert: ", list1)

    # List remove -> list.remove( item )
    list1.remove("Honda")
    print("List remove: ", list1)

    # List pop -> list.pop( index )
    list1.pop(1)
    print("List pop: ", list1)

    # List clear -> list.clear()
    list1.clear()
    print("List clear: ", list1)

    # List copy -> list.copy()
    list1 = list2.copy()
    print("List copy: ", list1)

    # List count -> list.count( item )
    list_count = list1.count("Toyota")
    print("List count: ", list_count)

    # List index -> list.index( item )
    list_index = list1.index("Toyota")
    print("List index: ", list_index)

    # List reverse -> list.reverse()
    list1.reverse()
    print("List reverse: ", list1)

    # List sort -> list.sort()
    list1.sort()     
    print("List sort: ", list1)

    # List sort reverse -> list.sort( reverse=True )
    list1.sort(reverse=True)
    print("List sort reverse: ", list1)

    


main()