#!/usr/bin/python3
"""
Fonction utilitaire pour obtenir une description d'objet sérialisable en JSON.
"""


def class_to_json(obj):
    """
    Retourne le dictionnaire des attributs de l'objet. 
    Ce dictionnaire ne contient que des types simples :
    listes, dicts, chaînes, entiers, booléens,
    donc il est directement sérialisable en JSON.
    """
    return obj.__dict__
