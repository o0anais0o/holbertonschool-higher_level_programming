#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
        Vérifie si un objet est une instance d'une classe donnée ou
        d'une de ses classes parentes.

        Args:
        obj: L'objet à vérifier.
        a_class: La classe à comparer.

        Returns:
        bool: True si obj est une instance de a_class ou
        d'une sous-classe de a_class, False sinon.
    """
    return isinstance(obj, a_class)
