import numpy as np


# calculates rackID and power level
def power_level(x, y):
    global sn
    rackID = x + 10
    pl = int(((rackID * y + sn) * rackID) / 100) % 10 - 5

    return rackID, pl


sn = int(open('input.txt', 'r').readline())

# test serial number
# sn = 18

grid = np.zeros((300, 300, 2), dtype=int)

for x in range(300):
    for y in range(300):
        grid[x, y, :] = power_level(x, y)

max_tp = -10e5
X, Y, S = -1
for s in range(1, 301):
    print(s)
    for x in range(301-s):
        for y in range(301-s):
            tp = np.sum(grid[x:x+s, y:y+s, 1])
            if tp > max_tp:
                max_tp = tp
                X, Y, S = x, y, s

print('({}, {}, {}), tp = {}'.format(X, Y, S, max_tp))

# result = 231, 135, 8
