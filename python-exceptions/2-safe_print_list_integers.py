#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Affiche les x premiers entiers d'une liste.
    Args:
        my_list: liste à parcourir
        x: nombre d'éléments à traiter
    Returns:
        Le nombre d'entiers effectivement affichés.
    """
    printed = 0  # Initialise le compteur d'entiers affichés
    for i in range(x):
        try:
            # Tente d'afficher l'élément à l'indice i comme un entier
            print("{:d}".format(my_list[i]), end="")
            printed += 1  # Incrémente le compteur si l'affichage réussit
        except (ValueError, TypeError):
            # Ignore l'élément si ce n'est pas un entier
            continue
    print("")  # Ajoute un retour à la ligne après l'affichage
    return printed  # Retourne le nombre d'entiers affichés
