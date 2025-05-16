#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divise les éléments de deux listes indice par indice.
    Args:
        my_list_1: première liste de numérateurs
        my_list_2: deuxième liste de dénominateurs
        list_length: nombre d'éléments à traiter
    Returns:
        Une nouvelle liste contenant les résultats des divisions.
    """
    res = []  # Initialise la liste des résultats
    for i in range(list_length):
        try:
            # Tente de diviser les éléments aux indices i des deux listes
            res += [my_list_1[i] / my_list_2[i]]
        except ZeroDivisionError:
            # Si division par zéro, ajoute 0 au résultat et affiche un message
            res += [0]
            print("division by 0")
        except TypeError:
            # Si un des éléments n'est pas du bon type,
            # ajoute 0 et affiche un message
            res += [0]
            print("wrong type")
        except IndexError:
            # Si l'indice dépasse la taille d'une des listes,
            # ajoute 0 et affiche un message
            res += [0]
            print("out of range")
        finally:
            # Passe à l'itération suivante (continue n'est pas obligatoire ici)
            continue
    return res  # Retourne la liste des résultats
