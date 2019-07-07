def count(v, items):
    c = 0
    for i in items:
        if v == i:
            c += 1
    return c


def best_distance(x, y, centers):
    ds = {}
    for cx, cy in centers:
        ds[cx, cy] = abs(cx-x) + abs(cy-y)
    best_key = min(ds.keys(), key=ds.get)
    best = ds[best_key]
    if count(best, ds.values()) > 1:
        return None, best  # pari distanza tra più centri
    else:
        return best_key, best


def centres_distance(x, y, centers):
    d = 0
    for cx, cy in centers:
        d += abs(cx-x) + abs(cy-y)
    return d


def border(mx, Mx, my, My):
    b = []
    for x in range(mx, Mx+1):
        for y in range(my, My+1):
            if x == mx or x == Mx or y == my or y == My:
                b.append((x, y))
    return b


file = open("input.txt", "r")

M = {}  # mappa con tutti i punti e relativa zona di appartenenza (id) e distanza

max_x, max_y = 0, 0
min_x, min_y = 10e5, 10e5
area_keys = set()
for line in file:
    coord = line.split(",")
    x, y = int(coord[0]), int(coord[1])
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y
    M[x, y] = (x, y), 0  # coordinate e distanza
    area_keys.add((x, y))

for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        if (x, y) not in area_keys:
            M[x, y] = best_distance(x, y, area_keys)

A = {(x, y): 0 for (x, y) in area_keys}  # mappa con area per ogni zona

for (x, y) in M.keys():
    center, d = M[x, y]
    if center is not None:
        A[center] += 1

for (x, y) in border(min_x, max_x, min_y, max_y):
    center, d = M[x, y]
    if center in A.keys():
        print(center)
        A.pop(center, None)

print(max(A.values()))

'''Parte 2'''

safe_area = 0

for x, y in M.keys():
    if centres_distance(x, y, area_keys) < 10000:
        safe_area += 1

print(safe_area)

