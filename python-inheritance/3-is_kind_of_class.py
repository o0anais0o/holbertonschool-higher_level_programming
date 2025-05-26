#!/usr/bin/python3
"""
Fonction qui renvoie True si l'objet est une instance de,
ou si l'objet est une instance d'une classe héritée de, 
la classe spécifiée; sinon False.
"""
def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)
