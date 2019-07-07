import matplotlib.pyplot as plt

file = open('input.txt', 'r')

s = list(file.readline().strip().split()[2])

file.readline()  # blank line

R = {}
for l in file:
    line = l.strip().split()
    a = line[0]
    b = line[2]
    R[a] = b

print(R)
dot = [e for e in R.keys() if R[e] == '.']
hashtag = [h for h in R.keys() if R[h] == '#']

x = []
y = []

start = 0
gen = 140
print('0 r=x ' + ''.join(s))

for i in range(gen):
    new_s = []

    while s[0] == '.':
        s = s[1:]
        start -= 1

    if '....'+s[0] in hashtag:
        for _ in range(4):
            s.insert(0, '.')
        start += 2
    elif '...'+''.join(s[0:2]) in hashtag:
        for _ in range(3):
            s.insert(0, '.')
        start += 1
    else:
        for _ in range(2):
            s.insert(0, '.')

    if s[-1]+'....' in hashtag:
        for _ in range(4):
            s.append('.')
    elif ''.join([s[-2], s[-1]])+'...' in hashtag:
        for _ in range(3):
            s.append('.')
    else:
        for _ in range(2):
            s.append('.')

    for j in range(2, len(s) - 2):
        new_s.append(R[''.join(s[j - 2:j + 3])])

    s = new_s

    result = 0
    for j in range(len(s)):
        if s[j] == '#':
            result += j - start

    print(('{} r={} ' + ''.join(s)).format(i+1, result))

    x.append(i+1)
    y.append(result)

print('start: {}'.format(start))

plt.plot(x, y)
plt.show()

print(y[-1] + (50000000000 - gen)*58)