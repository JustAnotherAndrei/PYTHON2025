def are_equal(a, b):
    if type(a) != type(b):
        return False

    # handler pt dictionar
    if isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        # verif recursiv fiecare cheie
        return all(are_equal(a[key], b[key]) for key in a)

    # handler pt liste, tupluri si seturi
    if isinstance(a, (list, tuple, set)):
        if len(a) != len(b):
            return False
        # il convertim la lista si comparam rezultatele
        return all(are_equal(x, y) for x, y in zip(a, b))

    # pentru restul tipurilor, comparam trivial
    return a == b


dict1 = {'a': 1, 'b': [1, 2, {'x': 5, 'y': 7}], 'c': 'hello'}
dict2 = {'a': 1, 'b': [1, 2, {'x': 5, 'y': 7}], 'c': 'hello'}
dict3 = {'a': 1, 'b': [1, 2, {'x': 5, 'y': 8}], 'c': 'hello'}

print(are_equal(dict1, dict2))  # prawda
print(are_equal(dict1, dict3))  # fałsz
print(are_equal(dict2, dict3))  # fałsz