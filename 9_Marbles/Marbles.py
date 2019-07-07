from collections import deque

l = open('input.txt', 'r').read().strip().split()

np = int(l[0])
nm = int(l[6]) * 100  # <-- parte 2

current_p = 1  # si parte dal player 2 (1 in notazione 0:np) per avere una coda con già 2 elementi

d = deque()
d.append(1)  # turno 0
d.append(0)  # turno 1

scores = [0] * np

for i in range(2, nm+1):
    if i % 23 != 0:
        d.insert(2, i)
        d.rotate(-2)
    else:
        d.rotate(7)
        scores[current_p] += i + d.popleft()
    current_p = (current_p + 1) % np

print(max(scores))

