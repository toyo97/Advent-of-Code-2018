def compareBoxes(box1, box2):
    if len(box1) != len(box2):
        return -1
    different = 0  # numero di differenze
    d = -1
    c = 0  # indice di scorrimento
    while different < 2 and c < len(box1):
        if box1[c] != box2[c]:
            different += 1
            d = c  # salva indice del carattere diverso
        c += 1

    if different == 1:
        return d
    else:
        return -1


file = open("input.txt", "r")

IDs = [line for line in file]

check2 = 0
check3 = 0
for id in IDs:
    twoFound = False
    threeFound = False
    charMap = {}
    for char in id:
        if char not in charMap:
            charMap[char] = 1
        elif charMap[char] == 1:
            charMap[char] += 1
        else:
            charMap[char] += 1
    for key in charMap.keys():
        if charMap[key] == 2:
            twoFound = True
        elif charMap[key] == 3:
            threeFound = True
    if twoFound:
        check2 += 1
    if threeFound:
        check3 += 1

checksum = check2*check3

print(checksum)

for i in range(len(IDs)):
    for j in range(i+1, len(IDs)):
        box1 = IDs[i]
        box2 = IDs[j]
        d = compareBoxes(box1, box2)

        if d != -1:
            print(box1[:d]+box1[d+1:])
            break





