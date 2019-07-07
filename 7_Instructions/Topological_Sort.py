'''Parte 1'''


def free(x, V, E):
    E2 = set([(u, x) for u in V])  # archi entranti in x
    if len(E2.intersection(E)) == 0:
        return True
    else:
        return False


def topological_sort(V, E, result):
    while len(V) != 0:
        for x in sorted(V):
            if free(x, V, E):
                result.append(x)
                V.remove(x)
                E.difference_update(set([(x, v) for v in V]))
                break

        print(E)
    return result


file = open("input_try.txt", "r")

V = set()  # vertici
E = set()  # archi
for line in file:
    s = line.split()
    E.add((s[1], s[7]))
    V.add(s[1])
    V.add(s[7])


result = []

result = topological_sort(V, E, result)
print("".join(result))

