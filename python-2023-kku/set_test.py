set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

if 1 in set1:
    print("1 in set1")

# Set union -> set1.union( set2 ) ---- set1 | set2 ----- KÜME BİRLEŞİMİ
# output -> Set union:  {1, 2, 3, 4, 5, 6, 7, 8}
print("Set union: ", set1.union(set2))
print("Set union: ", set1 | set2)

# Set intersection -> set1.intersection( set2 ) ---- set1 & set2 ----- KÜME KESİŞİMİ
# output -> Set intersection:  {4, 5}
print("Set intersection: ", set1.intersection(set2))
print("Set intersection: ", set1 & set2)

# Set difference -> set1.difference( set2 ) ---- set1 - set2 ----- KÜME FARKI
# output -> Set difference:  {1, 2, 3}
print("Set difference: ", set1.difference(set2)) # set1 kümesinde olup set2 kümesinde olmayan elemanlar
print("Set difference: ", set1 - set2)

# Set symmetric_difference -> set1.symmetric_difference( set2 ) ---- set1 ^ set2 ----- KÜME FARKI
# output -> Set symmetric_difference:  {1, 2, 3, 6, 7, 8}
print("Set symmetric_difference: ", set1.symmetric_difference(set2))
print("Set symmetric_difference: ", set1 ^ set2)

# Set issubset -> set1.issubset( set2 ) ---- set1 <= set2 ----- KÜME ALT KÜMESİ
# output -> Set issubset:  False
print("Set issubset: ", set1.issubset(set2)) # set1 kümesi set2 kümesinin alt kümesi mi?
print("Set issubset: ", set1 <= set2)
