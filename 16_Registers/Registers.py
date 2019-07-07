# Before: [0, 3, 0, 3]
# 9 0 0 1
# After:  [0, 0, 0, 3]
#
# Before: [1, 3, 3, 1]
# 0 3 1 0
# After:  [1, 3, 3, 1]
#
# OpCode first sec result
import re


file = open('input1.txt', 'r').readlines()

B = []
A = []
I = []
for i in range(0, len(file), 4):
    B.append(map(int, re.findall('\d', file[i][8:].strip())))
    I.append(map(int, file[i+1].split()))
    A.append(map(int, re.findall('\d', file[i+2][8:].strip())))
    print(A[-1])
