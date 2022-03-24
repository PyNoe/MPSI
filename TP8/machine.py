"""TP 8 - Machine à  voter"""

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

"""Question 4 PB"""

def unvote(Lcandidats, Lvotes):
    affiche_candidats(Lcandidats)
    choix = input("Entrez le numero du candidat pour qui vous souhaitez voter :")
    if choix.isdecimal() == True:
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
    return ">> Vote effectuÈ."

#Les scores sont bien renvoyÈs dans le fichier CSV.


    
    