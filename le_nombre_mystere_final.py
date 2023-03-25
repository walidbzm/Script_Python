#le nombre 05/03/23

#Le but de ce projet est de permettre à un joueur d'essayer de deviner un nombre mystère
#généré aléatoirement par l'ordinateur, en 5 essais ou moins.
#il va falloir deviner un nombre de 0 à 100 

import random

# Générer un nombre aléatoire entre 0 et 100
nombre_secret = random.randint(0, 100)

# Initialiser le nombre d'essais restants à 5
essais_restants = 5

#Demande le nom du joueur
nom_Gamer= input("Hello gamer c'est quoi ton prénom : ")

# Boucle pour demander à l'utilisateur de deviner le nombre mystère
while essais_restants > 0:
    # Demander à l'utilisateur de deviner un nombre
    nombre_devine = int(input(nom_Gamer + " ! Devine le nombre mystère entre 0 et 100 : "))

    # Vérifier si le nombre deviné est égal au nombre mystère
    if nombre_devine == nombre_secret:
        print("YESSSSSS, " + nom_Gamer + " tu as trouvé le nombre mystère en", 6 - essais_restants, "essai(s) !")
        print("")
        break
    # Si le nombre deviné est plus grand que le nombre mystère
    elif nombre_devine > nombre_secret:
        print("Le nombre mystère est plus petit que", nombre_devine)
        print("")
    # Si le nombre deviné est plus petit que le nombre mystère
    else:
        print("Le nombre mystère est plus grand que", nombre_devine)
        print("")

    # Diminuer le nombre d'essais restants
    essais_restants -= 1

# Si le joueur n'a pas trouvé le nombre mystère après 5 essais, afficher le nombre mystère
if essais_restants == 0:
    print("C'est fini " + nom_Gamer + ", tu as épuisé tes 5 essais. Le nombre mystère était", nombre_secret)
