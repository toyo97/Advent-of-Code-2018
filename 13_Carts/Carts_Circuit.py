file = open('input.txt', 'r')

C = []
nc = 0

carts = []

# (row, col) coordinates!!! (to use sort on tuples)

# DEF
LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)


def change_vel(v, new_dir):
    if v == RIGHT:
        if new_dir == 'l':
            v = UP
        elif new_dir == 'r':
            v = DOWN
    elif v == LEFT:
        if new_dir == 'l':
            v = DOWN
        elif new_dir == 'r':
            v = UP
    elif v == DOWN:
        if new_dir == 'l':
            v = RIGHT
        elif new_dir == 'r':
            v = LEFT
    elif v == UP:
        if new_dir == 'l':
            v = LEFT
        elif new_dir == 'r':
            v = RIGHT

    return v, next_rot[new_dir]


def check_collision(pos):
    global carts
    if [k[0] for k in carts].count(pos) > 1:
        return True
    else:
        return False


def next_step(k):
    global C
    r, c = k[0]
    dr, dc = k[1]
    new_dir = k[2]

    r += dr
    c += dc
    vel = dr, dc
    # cases
    if C[r][c] == '/':
        if vel == LEFT:
            vel = DOWN
        elif vel == RIGHT:
            vel = UP
        elif vel == UP:
            vel = RIGHT
        elif vel == DOWN:
            vel = LEFT
    elif C[r][c] == '\\':
        if vel == LEFT:
            vel = UP
        elif vel == RIGHT:
            vel = DOWN
        elif vel == UP:
            vel = LEFT
        elif vel == DOWN:
            vel = RIGHT
    elif C[r][c] == '+':
        vel, new_dir = change_vel(vel, new_dir)
    new_k = [(r, c), vel, new_dir]
    return new_k


next_rot = {'l': 's',
          's': 'r',
          'r': 'l'
          }

# build circuit and take track of carts
for r, line in enumerate(file):
    row = []
    for c, e in enumerate(line.strip('\n')):
        if e == 'v':
            carts.append([(r, c), (1, 0), 'l'])
            row.append('|')
            nc += 1
        elif e == '^':
            carts.append([(r, c), (-1, 0), 'l'])
            row.append('|')
            nc += 1
        elif e == '>':
            carts.append([(r, c), (0, 1), 'l'])
            row.append('-')
            nc += 1
        elif e == '<':
            carts.append([(r, c), (0, -1), 'l'])
            row.append('-')
            nc += 1
        else:
            row.append(e)

    C.append(row)

print(nc)

collision = False
t = 0
while not collision:
    if nc == 1:
        r, c = carts[0][0]
        print('survivor (row,column): ({},{})'.format(r, c))
        print('survivor (X,Y): ({},{})'.format(c, r))
        collision = True

    t += 1
    # print(t)

    carts = sorted(carts)
    colliders = []

    for i in range(nc):
        if i not in colliders:
            carts[i] = next_step(carts[i])

            if check_collision(carts[i][0]):
                print(carts[i][0])
                colliders = colliders + [j for j, c in enumerate(carts) if c[0] == carts[i][0]]

    nc -= len(colliders)
    for j in sorted(colliders, reverse=True):
        print('collider: {}'.format(carts.pop(j)))


# carts = list(filter(lambda a: a[0] != carts[i][0], carts))
