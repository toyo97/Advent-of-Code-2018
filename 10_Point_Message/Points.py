import numpy as np  # per vettori posizione e velocità
import scipy.misc as smp  # per disegnare immagine
import matplotlib.pyplot as plt


def next_step(P):
    P[:, 0, :] = P[:, 0, :] + P[:, 1, :]


def scale(P, Pl):
    return P[:, 0, :] - Pl


s = []
for line in open('input.txt', 'r'):
    s.append(line.strip())
    for c in ['<', '>', ',', '=']:
        s[-1] = s[-1].replace(c, ' ')
    s[-1] = s[-1].split()

numP = len(s)
# print(s[0])
P = np.zeros((numP, 2, 2), dtype=int)  # punti: tensore di np punti con 2 coordinate pos e due componenti vel
j = 0
for l in s:
    P[j] = P[j] + np.array([[l[1], l[2]], [l[4], l[5]]], dtype=int)
    j += 1

# print(P[0, 0, 1])  # indica punto numero 0, valore di pos (0), coordinata 1 (y)
# print(P[3, 1, 0])  # indica punto 3, valore di vel, coordinata x
# print(P[0, 0, :])  # vettore posizione del punto 0
# print(P[0, 1, :])  # vettore velocità del punto 0

# print(np.amax(P, axis=0)[0])

screen = int(numP/2)

# test = np.zeros((5, 6), dtype=np.uint8)
# test[np.array([0, 1, 2, 3, 4, 4, 2]), np.array([4, 3, 2, 1, 0, 5, 4])] = 1
# print(test)

for i in range(20000):
    Ph = np.amax(P, axis=0)[0]  #coordinate più grandi
    Pl = np.amin(P, axis=0)[0]  # coordinate più piccole

    # guardo se i dx e dy sono abbastanza piccoli da avere i punti concentrati in un'area ragionevole
    # TODO: regolare i parametri 80 e 12 trovati empiricamente
    if (Ph-Pl)[0] < 80 and (Ph-Pl)[1] < 12:
        data = np.zeros((screen, screen), dtype=np.uint8)
        P_shift = scale(P, Pl)
        rows, cols = P_shift.transpose()
        data[cols, rows] = 255
        print(i)
        plt.figure()
        plt.imshow(smp.toimage(data))
        plt.show()

    next_step(P)
