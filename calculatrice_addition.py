#walid le 05/03/23

#Dans ce projet, vous devez réaliser une calculatrice en ligne de commande qui vous
#permettra d'additionner deux nombres ensemble.

#Demande le nom du joueur
nom_Gamer= input("Hello gamer c'est quoi ton prénom : ")


while True:
    try:
        num1 = float(input( nom_Gamer + " entre un premier nombre : "))
        num2 = float(input( nom_Gamer + " entre un deuxième nombre : "))
        break
    except ValueError:
        print(nom_Gamer + " entrte deux nombres valides s'il te plaît")

resultat = num1 + num2
print(f"Le résultat de l'addition de {num1} avec {num2} est égal à {resultat}")
print("")

