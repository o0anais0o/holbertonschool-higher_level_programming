def safe_print_list(my_list=[], x=0):
    """
    Affiche x éléments d'une liste.
    Args:
        my_list: liste dont les éléments seront affichés
        x: nombre d'éléments à afficher
    Returns:
        Le nombre réel d'éléments affichés
    """
    count = 0
    try:
        # Parcourt les x premiers indices de la liste
        for i in range(x):
            # Affiche l'élément sans retour à la ligne
            print(my_list[i], end="")
            count += 1  # Incrémente le compteur d'éléments affichés
    except IndexError:
        # Arrête la boucle si l'indice dépasse la taille de la liste
        pass
    print()  # Ajoute un retour à la ligne après l'affichage
    return count  # Retourne le nombre d'éléments effectivement affichés
