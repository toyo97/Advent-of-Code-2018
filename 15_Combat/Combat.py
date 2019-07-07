from collections import deque
import time
import copy

e_pwr = 4


def cls():
    print ('\n' * 25)


def d(A, B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1])


class Field:
    def __init__(self):
        self.units = []
        self.area = []

    def copy(self):
        return copy.deepcopy(self)

    def pop(self, unit):
        self.area[unit.pos[0]][unit.pos[1]] = '.'

    def build_field(self, input):
        global e_pwr
        for r, line in enumerate(input):
            row = []
            for c, point in enumerate(line):
                if point == 'E':
                    self.units.append(Unit(self, 0, r, c, e_pwr))
                if point == 'G':
                    self.units.append(Unit(self, 1, r, c))

                row.append(point)
            self.area.append(row)

    def swap_unit(self, old, new):
        self.area[old[0]][old[1]], self.area[new[0]][new[1]] = self.area[new[0]][new[1]], self.area[old[0]][old[1]]
        # swap unit indicator (E or G) with open cave indicator (.)

    def check_end(self):
        u = None
        for unit in [u for u in self.units if u.alive]:
            if u is None:
                u = unit.type
            elif unit.type != u:
                return False
        return True

    def adjacent(self, pos):
        r, c = pos
        adj = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

        for rr, cc in adj:
            if self.area[rr][cc] == '.':
                yield (rr, cc)

    def bfs_path(self, unit):
        targets = [e for e in self.units if e.type != unit.type and e.alive]
        goals = set()
        for t in sorted(targets, key=lambda a: (a.hp, a.pos)):
            goals.update(set(g for g in field.adjacent(t.pos)))
            if unit.in_range(t):
                return t, None

        grid = {unit.pos: (0, None)}  # dist, parent
        seen = set()
        visiting = deque([(unit.pos, 0)])

        while visiting:
            pos, dist = visiting.popleft()
            for next in self.adjacent(pos):
                if next in seen:
                    continue
                if next not in grid or grid[next] > (dist+1, pos):
                    grid[next] = (dist + 1, pos)
                if next not in [v[0] for v in visiting]:
                    visiting.append((next, dist+1))
            seen.add(pos)

        try:
            min_dist, closest = min((dist, pos) for pos, (dist, parent) in grid.items() if pos in goals)
        except ValueError:
            return None, None

        for e in sorted(targets, key=lambda e: e.pos):
            if closest in field.adjacent(e.pos):
                enemy = e
                break

        while grid[closest][0] > 1:
            closest = grid[closest][1]

        return enemy, closest

    def show(self, hp=False):
        for l in self.area:
            print(''.join(l))
        if hp:
            for u in sorted([u for u in self.units if u.alive], key=lambda a: a.pos):
                print('{}({})'.format('G' if u.type==1 else 'E', u.hp), end=' ')


class Unit:
    def __init__(self, f, t, r, c, pwr=3):
        self.field = f
        self.type = t  # 0 for elf, 1 for goblin
        self.pos = (r, c)
        self.hp = 200
        self.alive = True
        self.power = pwr

    def defend_from(self, attacker):
        self.hp -= attacker.power
        if self.hp <= 0:
            self.alive = False
            self.field.pop(self)

    def attack(self, enemy):
        enemy.defend_from(self)

    def in_range(self, enemy):
        if d(self.pos, enemy.pos) == 1:
            return True
        else:
            return False

    def move(self, closest):
        self.field.swap_unit(self.pos, closest)
        self.pos = closest


input_area = []

with open('input.txt', 'r') as file:
    for line in file:
        input_area.append(line.strip())

original_field = Field()
original_field.build_field(input_area)

ne = len([e for e in original_field.units if e.type == 0 and e.alive])

e_total_win = False

while not e_total_win:
    field = Field()
    field.build_field(input_area)
    t = 0
    end = False
    # field.show(hp=True)
    while not end:
        # input()
        for unit in sorted(field.units, key=lambda u: u.pos):
            if unit.alive:
                enemy, closest = field.bfs_path(unit)
                if enemy is not None:
                    if unit.in_range(enemy):
                        unit.attack(enemy)
                    else:
                        unit.move(closest)
                        if unit.in_range(enemy):
                            enemy, _ = field.bfs_path(unit)
                            unit.attack(enemy)

        if field.check_end():
            end = True
        else:
            t += 1

        # field.show(hp=True)

        # time.sleep(1)
    e_deaths = ne - len([e for e in field.units if e.type == 0 and e.alive])
    if e_deaths == 0:
        e_total_win = True
        hps = [u.hp for u in field.units if u.alive]
        print(hps)
        score = sum(hps)
        print(t, score, t * score, e_pwr)
    else:
        e_pwr += 1
