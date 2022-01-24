def dic_diff(dica, dicb):
    allkeys = set(dica.keys()) | set(dicb.keys())
    dicc = {}
    for key in allkeys:
        dicc[key] = [dica.get(key), dicb.get(key)]
    return dicc


dica = {'a': 1, 'b': 2, 'c': 3, 'd': 5}
dicb = {'a': 1, 'b': 2, 'c': 4, 'e': 6}
print(dic_diff(dica, dicb))