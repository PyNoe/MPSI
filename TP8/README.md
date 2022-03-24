# TP 8. Machine à voter.

##### Noé DANIEL MPSI2

[Projet Github](https://github.com/PyNoe/MPSI/tree/main/TP8) avec les programmes.

### Question 1.

```python
fichier = open("candidats.txt", 'r')

def lire_candidats():
    Lcandidats = fichier.readlines()
    for i in range(len(Lcandidats)-1):
        Lcandidats[i] = Lcandidats[i][:-1]
    return Lcandidats

Lcandidats = lire_candidats()
```

### Question 2.

```python
Lvotes = [321, 5000, 4657, 748, 478, 1748, 264, 45769, 48589, 37859, 10348]

def resultats(Lcandidats, Lvotes):
    f = open("resultats.csv", "w")
    for k in range(len(Lcandidats)):
        f.write(Lcandidats[k] +" ; "+ str(Lvotes[k])+"\n")
    f.close()    
```

### Question 3.

```python
def affiche_candidats(Lcandidats):
    for k in range(len(Lcandidats)):
        print(str(k) + " : " + Lcandidats[k])
```

### Question 4.

```python
def unvote(Lcandidats, Lvotes):
    affiche_candidats(Lcandidats)
    choix = input("Entrez le numero du candidat pour qui vous souhaitez voter :")
    if choix.isdecimal() == True:
        if int(choix) <= 10 and int(choix) >= 0:
            print("+1")
            Lvotes[int(choix)] += 1
            return True
    return False
```

### Question 5.

```python
def votez(Lcandidats):
    Lvotes = [0 for k in Lcandidats]
    FIN = True
    while FIN == True:
        FIN = unvote(Lcandidats, Lvotes)
        print(FIN)
    return Lvotes
```

### Question 6.

```python
def machine_a_voter():
    scores = votez(Lcandidats)
    resultats(Lcandidats, scores)
    return ">> Vote effectué."

#Les scores sont bien renvoyés dans le fichier CSV.
```

### Question 7 et 8.

```python
"""Question 7 et 8"""

def guerrier_glorieux(nom_fichier):
    f = open(nom_fichier, 'w')
    f.writelines("for k in range(10):\n")
    f.writelines('   print("RIP")')
    f.close()
```

### Question 9.

`sys.argv` a pour type `list`.

```python
import sys 

print(sys.argv[0])
```

### Question 10.

```python
import sys

nom = sys.argv[0]
print("Nom du fichier source >>", nom)

f = open(nom, 'r')
f.writelines("for k in range(10):\n")
f.writelines('   print("RIP")')
f.close()
```

### Question 11.

cf. Console.

### Question 12 et 13.

```python
from random import random

"""Question 1"""

fichier = open("candidats.txt", 'r')

def lire_candidats():
    Lcandidats = fichier.readlines()
    for i in range(len(Lcandidats)-1):
        Lcandidats[i] = Lcandidats[i][:-1]
    return Lcandidats

Lcandidats = lire_candidats()

"""Question 2"""
    
Lvotes = [321, 5000, 4657, 748, 478, 1748, 264, 45769, 48589, 37859, 10348]

def resultats(Lcandidats, Lvotes):
    f = open("resultats.csv", "w")
    for k in range(len(Lcandidats)):
        f.write(Lcandidats[k] +" ; "+ str(Lvotes[k])+"\n")
    f.close()    

"""Question 3"""

def affiche_candidats(Lcandidats):
    for k in range(len(Lcandidats)):
        print(str(k) + " : " + Lcandidats[k])
        
        
"""Fonction de trucage"""

def trucage(choix):
    if random() < 0.2:
        return 0
    return choix


"""Question 4 PB"""

def unvote(Lcandidats, Lvotes):
    affiche_candidats(Lcandidats)
    choix = input("Entrez le numero du candidat pour qui vous souhaitez voter :")
    if choix.isdecimal() == True:
        choix = trucage(choix)
        print(choix)
        if int(choix) <= 10 and int(choix) >= 0:
            print("+1")
            Lvotes[int(choix)] += 1
            return True
    return False

    
"""Question 5"""

def votez(Lcandidats):
    Lvotes = [0 for k in Lcandidats]
    FIN = True
    while FIN == True:
        FIN = unvote(Lcandidats, Lvotes)
        print(FIN)
    return Lvotes
        

"""Question 6"""

def machine_a_voter():
    scores = votez(Lcandidats)
    resultats(Lcandidats, scores)
    return ">> Vote effectué."

#Les scores sont bien renvoyés dans le fichier CSV.


"""Auto destruction"""

nom = sys.argv[0]
vrai = open("machine.py", 'r')
inject = vrai.read()
vrai.close()
faux = open(nom, "w")
print("Destruction du fichier truqué")
faux.write(inject)
faux.close()
```

### Question 14.

Les exigences ne sont donc pas respectées par le programme.

