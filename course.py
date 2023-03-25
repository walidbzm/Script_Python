liste_courses = []

while True:
    # Affichage du menu
    print("\nMenu :")
    print("1. Ajouter un élément à la liste de courses")
    print("2. Retirer un élément de la liste de courses")
    print("3. Afficher les éléments de la liste de courses")
    print("4. Vider la liste de courses")
    print("5. Quitter le programme")

    # Demande à l'utilisateur de choisir une option
    choix = input("Entrez un nombre entre 1 et 5 pour choisir une option : ")

    # Vérification de la validité de l'entrée utilisateur
    if choix.isdigit() and 1 <= int(choix) <= 5:
        choix = int(choix)
    else:
        print("Veuillez entrer un nombre entre 1 et 5.")
        continue

    # Réalisation de l'action 
    if choix == 1:
        element = input("Entrez un élément à ajouter à la liste de courses : ")
        liste_courses.append(element)
    elif choix == 2:
        if not liste_courses:
            print("La liste de courses est vide.")
        else:
            element = input("Entrez l'élément à retirer de la liste de courses : ")
            if element in liste_courses:
                liste_courses.remove(element)
            else:
                print("Cet élément ne se trouve pas dans la liste de courses.")
    elif choix == 3:
        if not liste_courses:
            print("La liste de courses est vide.")
        else:
            print("Liste de courses :")
            for element in liste_courses:
                print("- " + element)
    elif choix == 4:
        if not liste_courses:
            print("La liste de courses est déjà vide.")
        else:
            liste_courses.clear()
            print("La liste de courses a été vidée.")
    elif choix == 5:
        print("Au revoir !")
        break