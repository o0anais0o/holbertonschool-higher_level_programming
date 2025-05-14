#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Retourne une nouvelle liste où toutes les occurrences de 'search'
    sont remplacées par 'replace'.
    """
    # Crée une nouvelle liste en remplaçant les éléments correspondants
    new_list = []
    for item in my_list:
        # Remplace si l'élément correspond à 'search'
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    # Retourne la nouvelle liste
    return new_list
