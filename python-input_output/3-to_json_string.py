#!/usr/bin/python3
"""
Ce module fournit une fonction pour convertir un objet
Python en une chaîne JSON.

Fonction :
    to_json_string(my_obj):
        Retourne la représentation JSON d'un objet Python
        (sous forme de chaîne de caractères).
"""


import json  # Importe le module json pour sérialisation et désérialisation


def to_json_string(my_obj):
    """
    Convertit un objet Python en une chaîne JSON.

    Args:
        my_obj (object): L'objet Python à convertir
        (ex : dictionnaire, liste, etc.).

    Returns:
        str: La représentation JSON de l'objet,
        sous forme de chaîne de caractères.

    Raises:
        TypeError: Si l'objet n'est pas sérialisable en JSON.
    """
    # Convertit l'objet Python en une chaîne JSON
    json_str = json.dumps(my_obj)
    # Retourne la chaîne JSON résultante
    return json_str
