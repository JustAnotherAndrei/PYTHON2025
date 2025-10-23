def loop(mapping):
    visited = set()
    result = []
    current = mapping['start']

    while current not in visited:
        if current not in mapping:  # in cazul in care cheia nu e in mapping
            break
        visited.add(current) #adaugam cheia curenta la setul de chei vazute
        result.append(current) #pastram
        current = mapping[current] #trecem la urmatoarea pereche (cred)

    return result

mapping = {
    'start': 'a',
    'b': 'a',
    'a': '6',
    '6': 'z',
    'x': '2',
    'z': '2',
    '2': '2',
    'y': 'start'
}

print(loop(mapping))