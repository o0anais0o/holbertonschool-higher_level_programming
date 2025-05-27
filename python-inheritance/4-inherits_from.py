#!/usr/bin/python3
"""
Fonction qui renvoie True si l'objet est une instance d'une classe héritée
(directement ou indirectement) de la classe spécifiée ; sinon False.
"""


def inherits_from(obj, a_class):
    """
    Retourne True si l'objet est une instance d'une classe qui hérite
    (directement ou indirectement) de la classe a_class, mais n'est
    pas une instance directe de a_class elle-même.
    """
    # Vérifie si obj est une instance de a_class ou d'une sous-classe de
    # a_class et s'assure que le type exact de obj n'est pas a_class
    # (donc obj hérite bien de a_class).
    return isinstance(obj, a_class) and type(obj) is not a_class
