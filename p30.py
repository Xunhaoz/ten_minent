def flatten(L):
    return [sub_element for element in L for sub_element in element]


print(flatten([[1, 2, 3], [4, 5, 6]]))
