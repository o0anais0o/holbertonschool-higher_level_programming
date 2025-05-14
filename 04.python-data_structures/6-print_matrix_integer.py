#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Affiche une matrice d'entiers ligne par ligne.
    Les entiers sont affichés formatés sans conversion explicite en chaîne.
    """
    # Parcourt chaque ligne (sous-liste) de la matrice
    for row in matrix:
        # Crée une liste temporaire pour stocker les entiers formatés
        formatted_row = []
        # Convertit chaque entier avec str.format() et l'ajoute à la liste
        for element in row:
            formatted_row.append("{:d}".format(element))
        # Affiche la ligne en joignant les éléments par des espaces
        print(" ".join(formatted_row))
