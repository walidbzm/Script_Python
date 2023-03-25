#WALID LE 05/03/2023

liste_courses = []
nom_Gamer= input("Hello, avant d'entrer dans le programme pour faire tes courses je veux savoir ton prénom : ")

while True:
    # Affichage du menu
    print("\nMenu :")
    print("1. Ajoute un élément à la liste de courses")
    print("2. Retire un élément de la liste de courses")
    print("3. Affiche les éléments de la liste de courses")
    print("4. Vide la liste de courses")
    print("5. Quitter le programme")

    # Demande à l'utilisateur de choisir une option
    print("")
    choix = input(nom_Gamer + " entre un nombre entre 1 et 5 pour choisir une option : ")
    print("")

    # Vérification de la validité de l'entrée utilisateur
    if choix.isdigit() and 1 <= int(choix) <= 5:
        choix = int(choix)
    else:
        print("")
        print(nom_Gamer + " entre un nombre entre 1 et 5.")
        continue

    # Réalisation de l'action 
    if choix == 1:
        print("")
        element = input("Entrez un élément à ajouter à la liste de courses : ")
        liste_courses.append(element)
    elif choix == 2:
        if not liste_courses:
            print("La liste de courses est vide.")
            print("")
        else:
            print("")
            element = input("Entrez l'élément à retirer de la liste de courses : ")
            if element in liste_courses:
                liste_courses.remove(element)
            else:
                print("")
                print("Cet élément ne se trouve pas dans la liste de courses.")
                print("")
    elif choix == 3:
        if not liste_courses:
            print("La liste de courses est vide.")
            print("")
        else:
            print("Liste de courses :")
            print("")
            for element in liste_courses:
                print("- " + element)
                print("")
    elif choix == 4:
        if not liste_courses:
            print("La liste de courses est déjà vide.")
            print("")
        else:
            liste_courses.clear()
            print("La liste de courses a été vidée.")
            print("")
    elif choix == 5:
        print("")
        print("")
        print("Au revoir !")
        break