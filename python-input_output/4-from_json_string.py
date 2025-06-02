#!/usr/bin/python3
"""
Ce module fournit une fonction pour convertir une chaîne JSON en objet Python.

Fonction :
    from_json_string(my_str) :
        Convertit une chaîne de caractères JSON en structure de données Python
        (dictionnaire, liste, etc.).
"""


import json  # Importe le module json pour la désérialisation


def from_json_string(my_str):
    """
    Convertit une chaîne JSON en objet Python correspondant.

    Args:
        my_str (str): La chaîne JSON à convertir.

    Returns:
        object: L'objet Python représenté par la chaîne JSON.
    """
    # Utilise json.loads pour transformer la chaîne JSON en objet Python
    return json.loads(my_str)
