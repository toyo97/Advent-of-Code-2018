def reduce(pol):
    length = len(pol)
    i = 0
    while i < length - 1:
        if (pol[i].islower() and pol[i].upper() == pol[i + 1]) or (pol[i].isupper() and pol[i].lower() == pol[i + 1]):
            del pol[i:i+2]
            length -= 2
            i = 0
        else:
            i += 1

    return pol


file = open("input.txt", "r")
pol = list(file.read())

reduced_pol = reduce(pol)
print(len(reduced_pol))

alphabet = list("abcdefghijklmnopqrstuvwxyz")

sizes = []

for a in alphabet:
    correct_pol = pol.copy()
    while a in correct_pol:
        correct_pol.remove(a)
    while a.upper() in correct_pol:
        correct_pol.remove(a.upper())
    sizes.append(len(reduce(correct_pol)))

print(sizes)
print(min(sizes))



