def splaszcz_liste(elementy):
    splaszczona = []
    for elem in elementy:
        if isinstance(elem, list):
            splaszczona.extend(splaszcz_liste(elem))
        else:
            splaszczona.append(elem)
    return splaszczona

zagniezdzona_lista = [1, [2, 3], 4, [5, [6, 7]]]
wynik = splaszcz_liste(zagniezdzona_lista)
print(f"Lista zagnieżdżona: {zagniezdzona_lista}")
print(f"Lista spłaszczona: {wynik}")