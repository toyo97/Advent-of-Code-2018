'''Part 1'''


def part_1(x):
    nr = x

    # test
    # nr = 9

    LB = [3, 7, 1, 0]

    # elves current recipe
    curr = [0, 1]

    while len(LB) < nr + 10:
        new_recipes = [int(c) for c in str(LB[curr[0]] + LB[curr[1]])]

        for r in new_recipes:
            LB.append(r)

        l = len(LB)
        for i in range(len(curr)):
            curr[i] = (1 + LB[curr[i]] + curr[i]) % l

    # assert '5158916779' == ''.join([str(s) for s in LB[nr:nr+11]])

    return ''.join([str(s) for s in LB[nr:nr+11]])


'''Part 2'''


def part_2(x):
    LB = [3, 7, 1, 0]

    # elves current recipe
    curr = [0, 1]

    target = [int(c) for c in str(x)]

    # test
    # target = [int(c) for c in '51589']

    match_found = False

    k = 0  # index of target scores
    nr = len(LB)
    result = 4
    round = 1
    while not match_found:
        round += 1
        if round % 1000000 == 0:
            print('Round: {}'.format(round))
        new_recipes = [int(c) for c in str(LB[curr[0]] + LB[curr[1]])]
        # print('new rec: {}'.format(new_recipes), end=', ')
        for r in new_recipes:
            LB.append(r)
            nr += 1
            if not match_found:
                if target[k] == r:
                    k += 1
                else:
                    result += k + 1
                    k = 0
                if k == len(target):
                    match_found = True
        # print('matches: {}'.format(k), end=', ')
        # print(LB)
        for i in range(len(curr)):
            curr[i] = (1 + LB[curr[i]] + curr[i]) % nr
        # print('*******')

    return result


x = 330121
ans1 = part_1(x)
print(ans1, end='\n*****\n')

ans2 = part_2(x)
print(ans2)

file = open('answers.txt', 'w')
file.write('First answer: ' + ans1 + '\n')
file.write('Second answer: {}'.format(ans2))
