zduplikowane_dane = [
    {'id': 1, 'imie': 'Anna'},
    {'id': 2, 'imie': 'Piotr'},
    {'id': 1, 'imie': 'Anna'},
    {'id': 3, 'imie': 'Zofia'},
]

widziane_id = set()
unikalne_dane = [(d['id'], d['imie']) for d in zduplikowane_dane if d['id'] not in widziane_id and not widziane_id.add(d['id'])]

print(unikalne_dane)