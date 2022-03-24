import sys

nom = sys.argv[0]
print("Nom du fichier source >>", nom)

f = open(nom, 'r')
f.writelines("for k in range(10):\n")
f.writelines('   print("RIP")')
f.close()

