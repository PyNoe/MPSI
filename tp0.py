import PIL.ImageCms


def somme(a, b):
    return a+b

assert somme(3, 4) == 7, "Erreur"

"""Exo 4.7"""

from math import cos
#print(cos(18))

"""Exo 4.8"""

import random as rdm

def lancer_des():
    return rdm.randrange(1, 7) + rdm.randrange(1, 7)

"""Exo 5.9"""

def Rampe(x):
    if x < 0:
        return 0
    else:
        return x

assert Rampe(-1) == 0, "erreur"
assert Rampe(0) == 0, "erreur"
assert Rampe(2) == 2, "erreur"

"""Exo 5.10"""

def estpair(n):
    if n%2 == 0:
        return n
    else:
        return n-1

def signe(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return x

"""Exo 5.11"""

assert signe(0) == 0, "erreur"
assert signe(3) == 1, "erreur"
assert signe(-4) == -1, "erreur"

assert estpair(3) == 2, "erreur"
assert estpair(2) == 2, "erreur"

"""Exo 5.12"""

def carré(x):
    return x**2

"""Exo 6.13"""

def parite(n):
    return n%2 == 0

def parite_bis(n, m):
    return parite(n) == parite(m)

"""Exo 7.15"""

"""
for i in range(10):
    print("bonjour")

for j in range(20):
    print(2**j)
"""

"""Exo 7.16"""

"""
i = 0
while i != 10:
    print("bonjour")
    i += 1

k = 0
while k != 20:
    print(2**k)
    k += 1
"""

"""Exo 7.17"""

def bonjour(k):
    if k == 0:
        return
    print("bonjour")
    return bonjour(k-1)

def puissances(k):
    if k == 0:
        return
    print(2**k)
    return puissances(k-1)

"""Exo 7.18"""

def onze(n):
    if n%11 == 0:
        print(n)
    if n == 0:
        return
    return onze(n-1)

def div_bis(n):
    if n%5 != 0 and n%7 != 0 and n%16 != 0:
        print(n)
    if n == 0:
        return
    return div_bis(n-1)

"""Exo 7.19"""

def nb_bits(n):
    k = 0
    while n >= 2**k:
        k += 1
    return k

"""Exo 7.20"""

def simul_des(n):
    somme = 0
    for i in range(n):
        somme += rdm.randrange(1, 7)
    return somme

"""Exo 7.21"""

def pile_face():
    n = 0
    while rdm.random() < 0.5:   # 1 chance sur 2
        n += 1
    return n

"""
somme = 0
for i in range(100000):
    somme += pile_face()

print("En moyenne : {}".format(somme/100000))
"""

"""Exo 7.22"""

def jeu(k):
    position_pion = 0
    while position_pion < (k):
        position_pion += rdm.randrange(1, 7)
    print(position_pion)
    if position_pion == (k):
        return True
    return False

"""Exo 8.23"""

S = "tortue"

"""Exo 8.25"""

def zeros(n):
    return [0 for i in range(n)]

"""Exo 8.27"""

def somme(L):
    som = 0
    for elt in L:
        som += elt
    return som

"""Exo 8.28"""

def mon_max(L):
    max = L[0]
    for i in range(1, len(L)):
        if L[i] > max:
            max = L[i]
    return max

"""Exo 8.29"""

def indice_max(L):
    return L.index(mon_max(L))

def indice_max2(L):
    ind, max = 0, L[0]
    for i in range(1, len(L)):
        if L[i] > max:
            max = L[i]
            ind = i
    return i

"""Exo 8.30"""

def compter(S, v):
    return v.count(S)

global alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

def minuscule(s):
    for lettre in s:
        if s not in alphabet:
            return "Erreur"
    return "Verif passed"

def trier(s):
    L = []
    for i in range(len(s)):
        L.append(s[i])
    print(L)
    L.sort()
    s_tri = ""
    for i in range(len(L)):
        s_tri += L[i]
    return s_tri

"""Exo 9.31"""

def premieres_puissances(n):
    L = []
    for k in range(n):
        L.append(2**k)
    return L

"""Exo 9.32"""

def positiver(L):
    for i in range(len(L)):
        if L[i] < 0:
            L[i] = 0
    return L

"""Exo 10.33"""

def premieres_puissances_comprehension(n):
    return [2**k for k in range(n)]

"""Exo 10.34"""

def affiche_un_par_un(L):
    for elt in L:
        print(elt)

def cherche(S, v):
    if v in S:
        return True
    return False

#On a déjà utilisé l'itération pour somme.

"""Exo 11.35"""

aliments = {"pizza":5, "ananas": 2}

"""Exo 11.36"""

D = dict()
def list_to_dict(L):
    for i in range(len(L)):
        if L[i] in D.keys():
            D[L[i]] = D[L[i]] + 1
        else:
            D[L[i]] = 1
    return D

L = ["a", "b", "c", "d", "a"]

"""Exo 11.37"""

def antecedent(v, D):
    cles = []
    for clef, valeur in D.items():
        if valeur == v:
            cles.append(clef)
    return cles

"""Exo 12.38"""

def lignes_file():
    texte = open("../../VocabulaireFr.txt")
    L = []
    ligne = "ok"
    while ligne != "":
        ligne = texte.readline()
        L.append(ligne)
    return L

def lignes_best():
    lignes = open("../../VocabulaireFr.txt").read().splitlines()
    return lignes

"""Exo 12.39"""

def ligne_file2():
    texte = open("../../VocabulaireFr.txt")
    return texte.readlines()

n = 0
for mot in lignes_best():
    if mot.count("e") == 4:
        n += 1
print(n)

"""Exo 12.40"""

def alea_mot():
    return rdm.choice(lignes_best())

