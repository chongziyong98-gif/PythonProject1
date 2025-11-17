

set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set4)

set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# intersection (value that both set have)
print(set1 & set2)                      # {2, 4, 6}
# union (set 1 + set 2) but not use +, we use | symbol
print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# difference (take what set 1 have but set 2 don't have)
print(set1 - set2)                      # {1, 3, 5, 7}
# symmetric_difference (take value that is unique, not show up in common)
print(set1 ^ set2)                      # {1, 3, 5, 7, 8, 10}

#Important note: set is not for direct calculation, it is not list
#Set's  value is not arranged,