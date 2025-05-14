#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Retourne une nouvelle liste de booléens indiquant si chaque élément
    de la liste d'origine est un multiple de 2.
    """
    # Initialise la nouvelle liste qui contiendra les booléens
    result = []

    # Parcourt chaque élément de la liste d'origine
    for num in my_list:
        # Ajoute True si l'élément est divisible par 2, sinon False
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    # Retourne la nouvelle liste de booléens
    return result
