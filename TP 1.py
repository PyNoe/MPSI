"""TP n°1 - Noé Daniel"""

"""Exercice 0.0"""
from PIL import Image
from PIL import ImageDraw
"""
A_rouge = Image.new("RGB", (100, 50), (255, 0, 0))
A_rouge.show()

A_noire = Image.new("RGB", (100, 50), (0, 0, 0))
A_noire.show()
"""
"""Exercice 0.1"""

def drapeau_francais(n):
    drapeau = Image.new("RGB", (3*n, 2*n), (0, 0, 255))
    for j in range(n, 2*n +1):
        for k in range(2*n):
            drapeau.putpixel((j, k), (255, 255, 255))
    for j in range(2*n+1, 3*n):
        for k in range(2*n):
            drapeau.putpixel((j, k), (255, 0, 0))
    drapeau.save("France", "JPEG")
    drapeau.show()

def drapeau_japonais(n):
    drapeau = Image.new("RGB", (3*n, 2*n), (255, 255, 255))
    cercle = ImageDraw.Draw(drapeau)
    r = int(0.3*(2*n))
    cercle.ellipse((int(1.5*n)-r, n-r, int(1.5*n)+r, n+r), fill=(188, 0, 45))
    drapeau.show()

def distance(a, b):
    xA, xB = a[0], b[0]
    yA, yB = a[1], b[1]
    distance = ((xA-xB)**2 + (yA-yB)**2)**(1/2)
    return distance

def drapeau_japonais2(n):
    drapeau = Image.new("RGB", (3*n, 2*n), (255, 255, 255))
    r = int(0.3*(2*n))
    centre = (int(1.5*n), n)
    for i in range(3*n):
        for j in range(2*n):
            pixel = (i,j)
            if distance(pixel, centre) <= r:
                drapeau.putpixel(pixel, (188, 0, 45))
    drapeau.save("Japon", "JPEG")
    drapeau.show()

"""Exercice 1.2"""

im1 = Image.open("chihiro.jpg")
print(im1.mode, im1.size)
im2 = Image.open("chihiro032.jpg")
print(im2.mode, im2.size)
im3 = Image.open("Mars_Perseverance_ZL0_0175_0682476554_193EBY_N0061648ZCAM03205_1100LMJ.png")
print(im3.mode, im3.size)

"""Exercice 1.3"""

"""
def gris(image):
    dimension = image.size
    grisee = Image.new("P", dimension)
    for i in range(dimension[0]):
        for j in range(dimension[1]):
            couleur_rgb = image.getpixel((i,j))
            couleur_grise = int(0.2126*couleur_rgb[0] + 0.7152*couleur_rgb[1] + 0.0722*couleur_rgb[2])
            grisee.putpixel((i, j), couleur_grise)
    grisee.show()
"""

image = Image.open("chihiro032.jpg")


def gris(A):
    B = Image.new("P", A.size, 0)
    (colonnes, lignes) = A.size
    for x in range(colonnes):
        for y in range (lignes):
            Rouge, Vert, Bleu = A.getpixel((x, y))
            pixelgris = int(0.2126 * Rouge + 0.7152 * Vert + 0.0722 * Bleu)
            B.putpixel((x, y), pixelgris)
    return B

image_g = gris(image)
#image_g.show()

"""Exercice 1.14"""

def rotation(A):
    hauteur, longueur = A.size
    B = Image.new("RGB", (longueur, hauteur), (255, 255, 255))
    for i in range(hauteur):
        for j in range(longueur):
            couleur = A.getpixel((i, j))
            B.putpixel((j, i), couleur)
    B.show()

"""Exercice 2.5"""

def convolution(image, noyau):
    assert image.mode == "P", "L'image n'est pas en niveaux de gris"
    center = len(noyau)//2
    (hauteur, longueur) = image.size
    image_c = Image.new("P", image.size, 0)
    for x in range(center,hauteur - center):
        for y in range (center, longueur - center):
            pixel_gray = 0
            for x_2 in range(len(noyau)):
                for y_2 in range(len(noyau)):
                    pixel_gray = pixel_gray + image.getpixel((x- center+ x_2, y-center + y_2))* noyau[x_2][y_2]
                    image_c.putpixel((x,y), int(pixel_gray))
    image_c.show()

noyau = [[1,4,6,4,1],
         [4,16,24,16,4],
         [6,24,36,24,6],
         [4,16,24,16,4],
         [1,4,6,4,1]]

for i in range(len(noyau)):
    for j in range(len(noyau[0])):
        noyau[i][j] = noyau[i][j]/256 

image_finale = convolution(image_g, noyau)








