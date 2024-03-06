# saisie d'un nom + affichage bienvenue

"""nom = input("insérer le nom de l'utilisateur afin de le saluer: ")

print(f"Bienvenue {nom}")"""

# saisie de a et b et affichage de leur somme

"""a = input("saisie la valeur de a: ") # input renvoie toujours un string
b = input("saisie la valeur de b: ")
somme = int(a) + int(b) # ça concatene si on spécifie pas le type de a et b du coup on les convertit
print(f"valeur de a: {a} et la valeur de b: {b} et leur somme: {somme}")"""

# saisie d'un nombre puis check si pair ou impair

"""a = input("saisie d'un nombre a: ")
entier_de_a = int(a)
if entier_de_a % 2 == 0:
    print(f"l'entier a: {entier_de_a} saisi est pair.")
else:
    print(f"l'entier a: {entier_de_a} est impair")"""

# affichage des 100 premiers nombres

"""taille = 1
while taille <= 100:
    print(taille)
    taille += 1"""

"""for i in range(1, 101, 1):
    print(i)
    
    liste = [i for i in range(1, 101, 1)] # création d'une liste avec les valeurs de 1 à 100"""

# modification des valeurs d'une liste à condition

"""liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"liste originale: {liste}")
liste_filtre = [500 if element == 2 else element for element in liste]
print(f"liste modifiée: {liste_filtre}")"""

# saisie d'un nombre n et faire la somme de 1 à n

"""nombre = input("saisisser le nombre choisi: ")
entier_nombre = int(nombre)
somme = 0

for i in range(entier_nombre):
    somme += i
    print(i, somme)"""


