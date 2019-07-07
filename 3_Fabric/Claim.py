import numpy as np

dim = 1000

'''Estrae l'oggetto Claim con i parametri indicati nella stringa'''
def extract_claim(claim_string):

    clear_claim = claim_string
    for c in ["#", "@", ",", ":", "x"]:
        clear_claim = clear_claim.replace(c, " ")

    values = [int(char) for char in clear_claim.split()]
    return Claim(values)

'''Struttura dati del claim'''
class Claim:

    def __init__(self, values):
        self.id = values[0]
        self.x = values[1]
        self.y = values[2]
        self.width = values[3]
        self.height = values[4]
        self.values = values

    '''Metodo che restituisce una matrice composta da 0 e 1 indicante la posizione del claim nel fabric'''
    def overlap_matrix(self):
        mat = np.zeros(shape=(dim, dim), dtype=int)
        mat[self.x:self.x+self.width, self.y: self.y+self.height] = 1
        return mat


file = open("input.txt", "r")

claims = []

for line in file:
    claims.append(extract_claim(line))

fabric = np.zeros(shape=(dim, dim), dtype=int)
for c in claims:
    fabric += c.overlap_matrix()

count = 0
for square_inch in np.nditer(fabric):
    if square_inch > 1:
        count += 1

print(count)

## Soluzione lenta
#
# for c in claims:
#     mask_matrix = np.multiply(fabric, c.overlap_matrix())
#
#     checks = 0
#     for square_inch in np.nditer(mask_matrix):
#         if square_inch > 1:
#             break
#         else:
#             checks += 1
#
#     if checks == dim**2:
#         print(c.id)
#         break
#     else:
#         print(str(c.id) + "NO")

for c in claims:

    checks = 0
    mask = fabric[c.x:c.x+c.width, c.y:c.y+c.height]
    for square_inch in np.nditer(mask):
        if square_inch > 1:
            break
        else:
            checks += 1

    if checks == mask.size:
        print(c.id)
        break

