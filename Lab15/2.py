import itertools

odczyty = [12, 15, 18, 21, 25, 19, 17]
prog_alarmowy = 22
prog_stabilny = 18

# Problem 1: Bierz, dopóki < 22 (takewhile)
bezpieczne = itertools.takewhile(lambda x: x < prog_alarmowy, odczyty)
print(f"Bezpieczne (takewhile): {list(bezpieczne)}")

# Problem 2: Omiń początkowe < 18 (dropwhile)
od_skoku = itertools.dropwhile(lambda x: x < prog_stabilny, odczyty)
print(f"Od skoku (dropwhile): {list(od_skoku)}")