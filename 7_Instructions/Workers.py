'''Parte 2'''


def free(x, E1):
    global V
    E2 = set([(u, x) for u in V])  # archi entranti in x
    if len(E1 & E2) == 0:
        return True
    else:
        return False


def assign_task(V1, E1, T):
    for x in sorted(V1):
        if free(x, E1):
            V1.remove(x)
            return x, T[x]
    return None


file = open("input.txt", "r")

V = set()  # vertici
E = set()  # archi
for line in file:
    s = line.split()
    E.add((s[1], s[7]))
    V.add(s[1])
    V.add(s[7])

print(V)

V1, E1 = V.copy(), E.copy()

T = {}
c = 61
for v in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    T[v] = c
    c += 1

workers = [None for i in range(5)]
t = 0
while len(V1) > 0:  # ogni iterazione corrisponde ad un secondo passato
    for i in range(5):
        if workers[i] is None:
            workers[i] = assign_task(V1, E1, T)
        else:
            v, rem = workers[i]
            rem -= 1
            if rem == 0:
                E1.difference_update([(v, u) for u in V])
                workers[i] = assign_task(V1, E1, T)
                for j in range(0, i):  # assegna eventualmente a quelli prima
                    if workers[j] is None:
                        workers[j] = assign_task(V1, E1, T)
            else:
                workers[i] = v, rem

    print(str(t)+str(workers))
    t += 1

for w in workers:
    if w is not None:
        v, rem = w
        t += rem


print(t-1)
