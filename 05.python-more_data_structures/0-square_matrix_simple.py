#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Retourne une nouvelle matrice où chaque valeur est le carré
    de la valeur correspondante de la matrice d'origine.
    La matrice d'origine n'est pas modifiée.
    """
    # Crée une nouvelle matrice pour stocker les carrés
    new_matrix = []

    # Parcourt chaque ligne de la matrice d'origine
    for row in matrix:
        # Calcule le carré de chaque élément de la ligne
        new_row = [x ** 2 for x in row]
        # Ajoute la nouvelle ligne à la nouvelle matrice
        new_matrix.append(new_row)

    # Retourne la nouvelle matrice
    return new_matrix
